# libfl intentionally leaves yylex undefined because that will be defined
# by the application using it (through the code generator included here)
%define _disable_ld_no_undefined 1

%define libname %mklibname fl

Summary:	A tool for creating scanners (text pattern recognizers)
Name:		flex
Version:	2.6.11
Release:	1
License:	BSD
Group:		Development/Other
Url:		https://github.com/westes/flex
Source0:	https://github.com/westes/flex/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Bison's generated parser asks Clang to ignore -Wmaybe-uninitialized.
# Clang 23 rejects that warning group.
Patch0:		flex-2.6.5-clang-no-Wmaybe-uninitialized.patch
BuildRequires:	gnu-config
BuildRequires:	make
BuildRequires:	slibtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	indent
BuildRequires:	gettext-devel >= 0.23
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

%package -n %{libname}
Summary:	Shared library for the flex scanner generator
Group:		System/Libraries

%description -n %{libname}
Shared library for the flex scanner generator

%package devel
Summary:	Static libraries for flex scanner generator
Group:		Development/Other
Requires:	%{name} = %{EVRD}
Requires:	%{libname} = %{EVRD}
Conflicts:	flex < 2.5.37-2

%description devel
This package contains the static libraries and headers for %{name}.

%prep
%autosetup -p1

%conf
CFLAGS="-fPIC %{optflags}" %configure --enable-shared --enable-static

%build
%make_build

%check
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

%files -n %{libname}
%{_libdir}/libfl.so.*

%files devel
%{_includedir}/FlexLexer.h
%{_libdir}/libfl*.a
%{_libdir}/libfl.so
%{_libdir}/pkgconfig/libfl.pc
