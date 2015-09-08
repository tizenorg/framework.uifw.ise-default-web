Name: ise-default-web
Version: 1.0.2
Release: 1
Summary: Default web keyboard for Tizen Wearable SDK
Source: %{name}-%{version}.tar.gz
License: Apache-2.0

BuildRequires: cmake
BuildRequires: zip
BuildRequires: wrt-installer

Requires: wrt-installer
Requires: wrt-plugins-common
Requires: wrt-plugins-tizen
Requires: unzip
Requires: pkgmgr
Requires: pkgmgr-server
Requires: pkgmgr-client
Requires: pkgmgr-installer
Requires: pkgmgr-info-parser
Requires: pkgmgr-info

%description
Default web keyboard for Tizen Wearable SDK

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
mkdir -p %{buildroot}/opt/usr/media/Downloads/.preinstallWidgets
cp %{_builddir}/%{name}-%{version}/DefaultWebKeyboard.wgt %{buildroot}/opt/usr/media/Downloads/.preinstallWidgets/
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}

%post
#/usr/bin/wrt-installer -ip /opt/usr/media/Downloads/.preinstallWidgets/DefaultWebKeyboard.wgt

%postun
PKG_ID=yc3pRFwQHH
wrt-installer -un ${PKG_ID}

%posttrans
wrt-installer -ip /opt/usr/media/Downloads/.preinstallWidgets/DefaultWebKeyboard.wgt

%files
/opt/usr/media/Downloads/.preinstallWidgets/*
/usr/share/license/%{name}

