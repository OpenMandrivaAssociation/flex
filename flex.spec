# dont want lto on a static lib
%define _disable_lto 1

Summary:	A tool for creating scanners (text pattern recognizers)
Name:		flex
Version:	2.6.1
Release:	1
License:	BSD
Group:		Development/Other
Url:		https://github.com/westes/flex
Source0:	https://github.com/westes/flex/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:	bison
BuildRequires:	indent
BuildRequires:	gettext-devel
BuildRequires:	help2man
Requires:	m4

%description
The flex program generates scanners. Scanners are
programs which can recognize lexical patterns in text.

Flex takes pairs of regular expressions and C code as input and
generates a C source file as output. The output file is compiled and
linked with a library to produce an executable.

The executable searches through its input for occurrences of the
regular expressions. When a match is found, it executes the
corresponding C code.

Flex was designed to work with both Yacc and Bison, and is used by
many programs as part of their build process.

You should install flex if you are going to use your system for
application development.

%package	devel
Summary:	Static libraries for flex scanner generator
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Conflicts:	flex < 2.5.37-2

%description	devel
This package contains the static libraries and headers for %{name}.

%prep
%setup -q

%build
CFLAGS="-fPIC %{optflags}" %configure --disable-shared --enable-static

%make

%check
#(tpg) these tests used features removed in bison-2.6
sed -i -e '/test-bison-yylloc/d' -e '/test-bison-yylval/d' tests/Makefile.in

make check

%install
%makeinstall_std

%find_lang %{name}

pushd %{buildroot}
ln -sf flex .%{_bindir}/lex
ln -s flex.1 .%{_mandir}/man1/lex.1
ln -s flex.1 .%{_mandir}/man1/flex++.1
popd

%files -f %{name}.lang
%doc NEWS README
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*

%files devel
%{_includedir}/FlexLexer.h
%{_libdir}/libfl*.a

