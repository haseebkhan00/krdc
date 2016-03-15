Summary:	KDE Remote Desktop Client
Name:		krdc
Version:	15.12.3
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
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		krdc-4.11.0-desktop.patch
BuildRequires:	kdelibs-devel
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
%{_bindir}/krdc
%{_datadir}/apps/krdc
%{_datadir}/applications/kde4/krdc.desktop
%{_datadir}/config.kcfg/krdc.kcfg
%{_libdir}/kde4/kcm_krdc_rdpplugin.so
%{_libdir}/kde4/kcm_krdc_vncplugin.so
%{_libdir}/kde4/krdc_rdpplugin.so
%{_libdir}/kde4/krdc_testplugin.so
%{_libdir}/kde4/krdc_vncplugin.so
%{_datadir}/kde4/services/rdp.protocol
%{_datadir}/kde4/services/vnc.protocol
%{_datadir}/kde4/services/krdc_rdp.desktop
%{_datadir}/kde4/services/krdc_rdp_config.desktop
%{_datadir}/kde4/services/krdc_test.desktop
%{_datadir}/kde4/services/krdc_vnc.desktop
%{_datadir}/kde4/services/krdc_vnc_config.desktop
%{_datadir}/kde4/services/ServiceMenus/smb2rdc.desktop
%{_datadir}/kde4/servicetypes/krdc_plugin.desktop
%doc %{_docdir}/HTML/*/krdc
#### Telepathy-Qt4-based optional feature ####
%{_bindir}/krdc_rfb_approver
%{_datadir}/apps/krdc_rfb_approver
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
%{_libdir}/libkrdccore.so.%{krdccore_major}*

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
%{_includedir}/krdc
%{_libdir}/libkrdccore.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
