Summary:	A tool for creating scanners (text pattern recognizers)
Name:		flex
Version:	2.5.35
Release:	%mkrel 3
License:	BSD
Group:		Development/Other
URL: 		http://flex.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/flex/%{name}-%{version}.tar.bz2
Patch0:		flex-2.5.4a-skel.patch
BuildRequires:	bison
Conflicts:	flex-reentrant
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p0
# Force regeneration of skel.c with Patch2 changes
rm -f skel.c
# Force regeneration of configure script with --libdir= support
autoconf

%build
%configure2_5x \
	--disable-rpath
%make

%check
make check

%install
rm -rf %{buildroot}

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

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS README
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/libfl*.a
%{_includedir}/FlexLexer.h
%{_infodir}/*
