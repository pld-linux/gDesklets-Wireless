%define	pname	Wireless
Summary:	A sensor and a display for wireless LAN control
Summary(pl):	Czujnik i wy¶wietlacz do kontroli bezprzewodowej sieci LAN
Name:		gDesklets-%{pname}
Version:	1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/%{pname}.tar.bz2
# Source0-md5:	efdcff274b6b913dbfbe0865f85fdea6
URL:		http://www.pycage.de/software_gdesklets.html
Buildrequires:	python >= 2.3
Requires:	gDesklets
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A sensor and a display for keeping an eye on the connection quality to
your wireless LAN.

%description -l pl
Czujnik i wy¶wietlacz do kontrolowania jako¶ci po³±czeñ do
bezprzewodowej sieci LAN.

%prep
%setup -q -n %{pname}
tail -c 10240 Install_Wireless_Sensor.bin 2>&1 | tar -xz 2>&1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gdesklets/{Sensors,Displays/%{pname}}

cp -R Wireless $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors
cp -R gfx *.display $RPM_BUILD_ROOT%{_datadir}/gdesklets/Displays/%{pname}

%py_comp $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors

rm -f $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors/*/*.py
rm -rf $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors/*/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/gdesklets/Sensors/*
%{_datadir}/gdesklets/Displays/*
