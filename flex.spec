Summary:	A tool for creating scanners (text pattern recognizers)
Name:		flex
Version:	2.5.37
Release:	1
License:	BSD
Group:		Development/Other
URL:		http://flex.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/flex/%{name}-%{version}.tar.bz2
Patch0:		flex-2.5.4a-skel.patch
BuildRequires:	bison
BuildRequires:	texinfo
Requires:	m4
Conflicts:	flex-reentrant

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

%prep
%setup -q
%patch0 -p0 -b .skel~

# Force regeneration of skel.c with Patch2 changes
rm -f skel.c
# Force regeneration of configure script with --libdir= support
autoconf

%build
CFLAGS="-fPIC %{optflags}" %configure2_5x \
	--disable-rpath
%make

%check
make check

%install
%makeinstall_std

%find_lang %{name}

#cd %{buildroot}%{_bindir}
#ln -sf flex lex

#cd %{buildroot}%{_mandir}/
#cd man1
#ln -s flex.1 lex.1
#ln -s flex.1 flex++.1

pushd %{buildroot}
ln -sf flex .%{_bindir}/lex
#ln -sf flex .%{_bindir}/flex++
ln -s flex.1 .%{_mandir}/man1/lex.1
ln -s flex.1 .%{_mandir}/man1/flex++.1
popd

%files -f %{name}.lang
%doc NEWS README
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/libfl*.a
%{_includedir}/FlexLexer.h
%{_infodir}/*
