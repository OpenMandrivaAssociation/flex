Summary:	A tool for creating scanners (text pattern recognizers)
Name:		flex
Version:	2.5.33
Release:	%mkrel 2
License:	GPL
Group:		Development/Other
URL: 		http://flex.sourceforge.net/
Source:		ftp.gnu.org:/non-gnu/flex/flex-%version.tar.bz2
Patch0:		flex-2.5.4a-skel.patch
BuildRequires:	byacc autoconf2.1
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
%patch0 -p1
# Force regeneration of skel.c with Patch2 changes
rm -f skel.c
# Force regeneration of configure script with --libdir= support
autoconf

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

cd $RPM_BUILD_ROOT%{_bindir}
ln -sf flex lex

cd $RPM_BUILD_ROOT%{_mandir}/
cd man1
ln -s flex.1 lex.1
ln -s flex.1 flex++.1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root,755)
%doc COPYING NEWS README
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/libfl.a
%{_includedir}/FlexLexer.h
%{_infodir}/*


