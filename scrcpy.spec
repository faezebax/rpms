%global         debug_package       %{nil}
Name:           scrcpy
Version:        1.10
Release:        1%{?dist}
Summary:        Display and control your Android device 

License:        ASL 2.0
URL:            https://github.com/Genymobile/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-server-v%{version}.jar

BuildRequires:  android-tools
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  java-devel
Requires:       android-tools

%description
This application provides display and control of Android devices connected on 
USB (or over TCP/IP). It does not require any root access.

%prep
%autosetup -n %{name}
cp %{SOURCE1} %{_builddir}/%{name}/

%build
%meson --strip -Db_lto=true -Dprebuilt_server=%{name}-server-v%{version}.jar


%install
%meson_install



%files
%license LICENSE
%doc README.md
%{_bindir}/scrcpy
%{_datadir}/scrcpy/scrcpy-server.jar
%{_mandir}/man1/scrcpy.1.gz


%changelog
* Mon Nov 11 2019 Faeze Bax <faezebax@riseup.net> - 1.10-1
- First rpm release