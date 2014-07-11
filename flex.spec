Summary:	A tool for creating scanners (text pattern recognizers)
Name:		flex
Version:	2.5.39
Release:	3
License:	BSD
Group:		Development/Other
Url:		http://flex.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/flex/%{name}-%{version}.tar.bz2
Patch0:		flex-2.5.4a-skel.patch
Patch1:		flex-2.5.37-libtool.patch
BuildRequires:	bison
BuildRequires:	indent
BuildRequires:	texinfo
BuildRequires:	texlive
BuildRequires:	gettext-devel
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
%patch0 -p0 -b .skel~
%patch1 -p1 -R

# Force regeneration of skel.c with Patch2 changes
rm -f skel.c

# Force regeneration of configure script with --libdir= support
autoreconf -fi

%build
CFLAGS="-fPIC %{optflags}" %configure2_5x

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

