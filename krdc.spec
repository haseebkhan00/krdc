Summary:	KDE Remote Desktop Client
Name:		krdc
Version:	4.12.3
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		krdc-4.11.0-desktop.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libvncserver)
BuildRequires:	pkgconfig(TelepathyQt4)
BuildRequires:	freerdp >= 1.0.2
Requires:	freerdp >= 1.0.2
Conflicts:	kde4-filesharing < 3:4.8.0

%description
KDE Remote Desktop Client is a client application that allows you to view
or even control the desktop session on another machine that is running a
compatible server. VNC and RDP are supported.

%files
%{_kde_bindir}/krdc
%{_kde_appsdir}/krdc
%{_kde_applicationsdir}/krdc.desktop
%{_kde_datadir}/config.kcfg/krdc.kcfg
%{_kde_libdir}/kde4/kcm_krdc_rdpplugin.so
%{_kde_libdir}/kde4/kcm_krdc_vncplugin.so
%{_kde_libdir}/kde4/krdc_rdpplugin.so
%{_kde_libdir}/kde4/krdc_testplugin.so
%{_kde_libdir}/kde4/krdc_vncplugin.so
%{_kde_services}/rdp.protocol
%{_kde_services}/vnc.protocol
%{_kde_services}/krdc_rdp.desktop
%{_kde_services}/krdc_rdp_config.desktop
%{_kde_services}/krdc_test.desktop
%{_kde_services}/krdc_vnc.desktop
%{_kde_services}/krdc_vnc_config.desktop
%{_kde_services}/ServiceMenus/smb2rdc.desktop
%{_kde_servicetypes}/krdc_plugin.desktop
%{_kde_docdir}/HTML/*/krdc
#### Telepathy-Qt4-based optional feature ####
%{_kde_bindir}/krdc_rfb_approver
%{_kde_appsdir}/krdc_rfb_approver
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.krdc_rfb*.service
%{_datadir}/telepathy/clients/krdc_rfb*.client

#----------------------------------------------------------------------------

%define krdccore_major 4
%define libkrdccore %mklibname krdccore %{krdccore_major}

%package -n %{libkrdccore}
Summary:	Shared library for KRDC
Group:		System/Libraries
Obsoletes:	%{_lib}krdccore1 < 3:4.10.1

%description -n %{libkrdccore}
Shared library for KRDC.

%files -n %{libkrdccore}
%{_kde_libdir}/libkrdccore.so.%{krdccore_major}*

#----------------------------------------------------------------------------

%define devkrdccore %mklibname krdccore -d

%package -n %{devkrdccore}
Summary:	Development for KRDC
Group:		Development/KDE and Qt
Requires:	%{libkrdccore} = %{EVRD}
Conflicts:	kdenetwork4-devel < 3:4.11.0
Provides:	%{name}-devel = %{EVRD}

%description -n %{devkrdccore}
This package contains header files needed if you want to build applications
based on KRDC.

%files -n %{devkrdccore}
%{_kde_includedir}/krdc
%{_kde_libdir}/libkrdccore.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.3-1
- New version 4.11.3

* Thu Oct 31 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.2-2
- Add freerdp to BuildRequires and Requires

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0
- Split from kdenetwork4 package as upstream did
