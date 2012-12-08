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
BuildRequires:	texlive
BuildRequires:	gettext-devel
BuildRequires:	indent
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

%build
# Force regeneration of configure script with --libdir= support
autoreconf -fi

CFLAGS="-fPIC %{optflags}" %configure2_5x \
	--disable-rpath
%make

%check
#(tpg) these tests used features removed in bison-2.6
sed -i -e '/test-bison-yylloc/d' -e '/test-bison-yylval/d' tests/Makefile.in

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


%changelog
* Tue Aug 21 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5.37-1
+ Revision: 815556
- add buildrequires on texlive and indent
- disable checks for bison, because these features are no longer in bison-2.6
- add missing buildrequires
- update to new version 2.5.37

  + Bernhard Rosenkraenzer <bero@bero.eu>
    - Adjust BuildRequires
    - Update to 2.5.36

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.35-8
+ Revision: 664312
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.35-7mdv2011.0
+ Revision: 605151
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.35-6mdv2010.1
+ Revision: 518999
- rebuild

* Wed Oct 21 2009 Frederik Himpe <fhimpe@mandriva.org> 2.5.35-5mdv2010.0
+ Revision: 458597
- Add Requires: m4 to make sure lex can work (bug #54782)

* Sun May 03 2009 Frederik Himpe <fhimpe@mandriva.org> 2.5.35-4mdv2010.0
+ Revision: 371154
- Build with -fPIC, needed to build ipsec-tools on x86_64
- Add Fedora patches fixing build warnings

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5.35-3mdv2009.1
+ Revision: 316579
- rediffed one fuzzy patch

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 2.5.35-2mdv2009.0
+ Revision: 264465
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5.35-1mdv2009.0
+ Revision: 195398
- new version
- license is BSD not a GPL
- nuke rpath
- spec file clean
- enable checks

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.5.33-3mdv2008.1
+ Revision: 149727
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sat Jan 13 2007 Götz Waschk <waschk@mandriva.org> 2.5.33-2mdv2007.0
+ Revision: 108195
- use find-lang

* Tue Oct 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.5.33-1mdv2007.1
+ Revision: 71736
- New version of flex.
  Remove obsolete patches, and add info pages and localized messages.

  + Oden Eriksson <oeriksson@mandriva.com>
    - bzip2 cleanup
    - bunzip patches
    - Import flex

* Mon Jul 03 2006 Oden Eriksson <oeriksson@mandriva.com> 2.5.4a-25mdv2007.0
- make it conflict with flex-reentrant

* Mon May 15 2006 Stefan van der Eijk <stefan@eijk.nu> 2.5.4a-24mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.5.4a-23mdk
- Rebuild

* Wed Jun 09 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.5.4a-22mdk
- fix buildrequires
- wipe out buildroot in %%install, not %%prep

