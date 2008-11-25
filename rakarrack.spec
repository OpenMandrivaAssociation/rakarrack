Summary:	Guitar FX processor emulator
Name:		rakarrack
Version:	0.3.0
Release:	%mkrel 1
License:	GPLv2
Group:		Sound
URL:		http://rakarrack.sourceforge.net/
Source0:        http://dfn.dl.sourceforge.net/sourceforge/rakarrack/%{name}-%{version}.tar.gz
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Rakarrack is a FX processor emulator for guitar and other purposes. It provides
many effects: two EQ (multiband and parametric), distortion, overdrive, echo,
chorus, flanger, phaser, compressor, reverb, harmonizer, delay, autopan,
wahwah, cabinet emulation, and alienwah. It features real time processing, JACK
support, an online tuner, bank and preset managment, and a monophonic MIDI
converter. 

%prep

%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%post
%update_desktop_database

%postun
%clean_desktop_database

%files
%defattr(-,root,root,0755)
%doc %{_docdir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*.1*

