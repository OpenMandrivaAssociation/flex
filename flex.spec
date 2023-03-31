# dont want lto on a static lib
%define _disable_lto 1

Summary:	A tool for creating scanners (text pattern recognizers)
Name:		flex
Version:	2.6.4
Release:	8
License:	BSD
Group:		Development/Other
Url:		https://github.com/westes/flex
Source0:	https://github.com/westes/flex/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Pull in changes from post-v2.6.4 tag in the flex git repository
# Fixes, among other things, doxygen build failures
Patch0:		flex-2.6.4-changes-from-git.patch
# -Wmaybe-uninitialized is gcc specific. Don't inject it
# when using clang.
Patch1:		flex-2.6.4-no-Wmaybe-uninitialized-in-clang.patch
BuildRequires:	bison
BuildRequires:	indent
BuildRequires:	gettext-devel
BuildRequires:	help2man
BuildRequires:	texinfo
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

%package devel
Summary:	Static libraries for flex scanner generator
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Conflicts:	flex < 2.5.37-2

%description devel
This package contains the static libraries and headers for %{name}.

%prep
%autosetup -p1

%build
CFLAGS="-fPIC %{optflags}" %configure --disable-shared --enable-static

%make_build

%check
#(tpg) these tests used features removed in bison-2.6
sed -i -e '/test-bison-yylloc/d' -e '/test-bison-yylval/d' tests/Makefile.in

make check ||:
cat tests/test-suite.log

%install
%make_install

%find_lang %{name}

pushd %{buildroot}
ln -sf flex .%{_bindir}/lex
ln -s flex.1 .%{_mandir}/man1/lex.1
ln -s flex.1 .%{_mandir}/man1/flex++.1
popd

rm -rf %{buildroot}%{_docdir}/%{name}

%files -f %{name}.lang
%doc NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*

%files devel
%{_includedir}/FlexLexer.h
%{_libdir}/libfl*.a
%{_libdir}/pkgconfig/libfl.pc
