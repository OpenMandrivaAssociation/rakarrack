Summary:	Guitar FX processor emulator
Name:		rakarrack
Version:	0.5.8
Release:	%mkrel 1
License:	GPLv2
Group:		Sound
URL:		http://rakarrack.sourceforge.net/
Source0:	http://dfn.dl.sourceforge.net/sourceforge/rakarrack/%{name}-%{version}_Equinox.tar.bz2
Patch0:		rakarrack-0.4.2-new-fltk.patch
Patch1:		rakarrack-0.4.2-string-format.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	alsa-utils
BuildRequires:	desktop-file-utils
BuildRequires:	fltk-devel
BuildRequires:	libjack-devel
BuildRequires:	libpng-devel
BuildRequires:	libxau-devel
BuildRequires:	libxdmcp-devel
BuildRequires:	libxpm-devel
BuildRequires:	xcb-devel
BuildRequires:	xft2-devel
BuildRequires:	libsamplerate-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n %{name}-%{version}_Equinox
%patch0 -p0
%patch1 -p0 -b .format

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_desktop_database

%postun
%clean_desktop_database
%endif

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

