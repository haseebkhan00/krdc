Summary:	KDE Remote Desktop Client
Name:		krdc
Version:	16.04.0
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
BuildRequires:	pkgconfig(libvncserver)
BuildRequires:	pkgconfig(TelepathyQt4)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5DNSSD)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	freerdp >= 1.0.2
Requires:	freerdp >= 1.0.2
Conflicts:	kde4-filesharing < 3:4.8.0

%description
KDE Remote Desktop Client is a client application that allows you to view
or even control the desktop session on another machine that is running a
compatible server. VNC and RDP are supported.

%files
%{_bindir}/krdc
%{_datadir}/applications/org.kde.krdc.desktop
%{_datadir}/config.kcfg/krdc.kcfg
%{_datadir}/krdc
%{_datadir}/kservices5/ServiceMenus/smb2rdc.desktop
%{_datadir}/kservices5/krdc_rdp_config.desktop
%{_datadir}/kservices5/krdc_vnc_config.desktop
%{_datadir}/kservices5/rdp.protocol
%{_datadir}/kservices5/vnc.protocol
%{_libdir}/plugins/krdc
%{_datadir}/kxmlgui5/krdc/krdcui.rc
%doc %{_docdir}/HTML/*/krdc

#----------------------------------------------------------------------------

%define krdccore_major 5
%define libkrdccore %mklibname krdccore %{krdccore_major}

%package -n %{libkrdccore}
Summary:	Shared library for KRDC
Group:		System/Libraries
Obsoletes:	%{_lib}krdccore1 < 3:4.10.1

%description -n %{libkrdccore}
Shared library for KRDC.

%files -n %{libkrdccore}
%{_libdir}/libkrdccore.so.%{krdccore_major}*
%{_libdir}/libkrdccore.so.%{version}

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
%{_includedir}/krdccore_export.h
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
