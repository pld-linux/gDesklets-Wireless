%define		pname	Wireless
Summary:	A sensor and a display for wireless LAN control
Summary(pl):	Czujnik i wy¶wietlacz do kontroli bezprzewodowej sieci LAN
Name:		gDesklets-%{pname}
Version:	0.1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/wireless-desklet-%{version}.tar.bz2
# Source0-md5:	5fb527f3473f3142e4ed5a0058e112f3
URL:		http://www.pycage.de/software_gdesklets.html
BuildRequires:	python >= 2.3
Requires:	gDesklets
Provides:	gDesklets-display
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sensorsdir	%{_datadir}/gdesklets/Sensors
%define		_displaysdir	%{_datadir}/gdesklets/Displays

%description
A sensor and a display for keeping an eye on the connection quality to
your wireless LAN.

%description -l pl
Czujnik i wy¶wietlacz do kontrolowania jako¶ci po³±czeñ do
bezprzewodowej sieci LAN.

%prep
%setup -q -n wireless-desklet-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir},%{_displaysdir}/%{pname}}

./Install_%{pname}_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

cp -R gfx *.display $RPM_BUILD_ROOT%{_displaysdir}/%{pname}

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -rf $RPM_BUILD_ROOT%{_sensorsdir}/*/{CVS,*.py}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_sensorsdir}/*
%{_displaysdir}/*
