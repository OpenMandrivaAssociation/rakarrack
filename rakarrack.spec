Summary:    Guitar FX processor emulator
Name:       rakarrack
Version:    0.6.1
Release:    3
License:    GPLv2
Group:      Sound
URL:        http://rakarrack.sourceforge.net/
Source0:    http://dfn.dl.sourceforge.net/sourceforge/rakarrack/%{name}-%{version}.tar.bz2
Patch0:     rakarrack-0.6.1-strfmt.patch
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  alsa-utils
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  jackit-devel
BuildRequires:  libpng-devel
BuildRequires:  libxau-devel
BuildRequires:  libxdmcp-devel
BuildRequires:  libxpm-devel
BuildRequires:  xcb-devel
BuildRequires:  libxft-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  sndfile-devel

%description
Rakarrack is a FX processor emulator for guitar and other purposes. It provides
many effects: tcompressor, expander, noise gate, graphic equalizer, parametric
equalizer, exciter, shuffle, convolotron, valve, flanger, dual flange, chorus,
musicaldelay, arpie, echo with reverse playback, musical delay, reverb,
digital phaser, analogic phaser, synthfilter, varyband, ring, wah-wah,
alien-wah, mutromojo, harmonizer, looper and four flexible distortion modules
including sub-octave modulation and dirty octave up. It features real time
processing, JACK support, an online tuner, bank and preset managment, and a
monophonic MIDI converter. Patch files from previous versions can be converted
using the provided rakconvert script.

%prep
%setup -q
%patch0 -p1
sed -ie 's/<Fl\//<FL\//g' src/global.h src/process.C

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root,0755)
%doc %{_docdir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/rakconvert
%attr(0755,root,root) %{_bindir}/rakgit2new
%attr(0755,root,root) %{_bindir}/rakverb
%attr(0755,root,root) %{_bindir}/rakverb2
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*.1*



%changelog
* Sun Dec 25 2011 Frank Kober <emuse@mandriva.org> 0.6.1-2
+ Revision: 745140
- rebuild with fltk 1.3

* Sun Nov 28 2010 Frank Kober <emuse@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 602431
- new version 0.6.1
  o rediff patch1, replace patch0 by script

* Sat Jul 17 2010 Frank Kober <emuse@mandriva.org> 0.5.8-1mdv2011.0
+ Revision: 554542
- add another missing BR
- add missing BR
- new version 0.5.8 (Equinox)
- update description
- adjust file list
- old patches still functional

* Mon Apr 05 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.2-1mdv2010.1
+ Revision: 531497
- new upstream release 0.4.2
- rediff patch0
- add patch to fix string format

* Mon Jan 18 2010 Jérôme Brenier <incubusss@mandriva.org> 0.3.0-4mdv2010.1
+ Revision: 493155
- rebuild for new fltk

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.0-3mdv2010.0
+ Revision: 442668
- rebuild

* Sun Dec 14 2008 Funda Wang <fwang@mandriva.org> 0.3.0-2mdv2009.1
+ Revision: 314174
- build with new fltk

* Tue Nov 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-1mdv2009.1
+ Revision: 306679
- fix deps (alsa-utils)
- import rakarrack


* Tue Nov 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-1mdv2009.0
- initial Mandriva package
