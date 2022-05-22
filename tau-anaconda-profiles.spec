%define dist_version 36

Summary:        tauOS Anaconda Profiles
Name:           tau-anaconda-profiles
Version:        1.1
Release:        2
License:        GPLv3
URL:            https://tauos.co
Source0:        README.md
Source1:        LICENSE
Source2:        tau-home.conf
Source3:        tau-core.conf
BuildArch:      noarch
Provides:       tau-anaconda-profiles(%{version}) = %{release}

%description
Provides tauOS Anaconda profiles for installation.

%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/anaconda/profile.d/
install -m 644 %SOURCE2 %{buildroot}%{_sysconfdir}/anaconda/profile.d/
install -m 644 %SOURCE3 %{buildroot}%{_sysconfdir}/anaconda/profile.d/

# Install licenses and documentation
mkdir -p licenses
install -pm 0644 %SOURCE1 licenses/LICENSE

install -pm 0644 %SOURCE0 README.md

%files
%doc README.md
%license licenses/LICENSE
%dir %{_sysconfdir}/anaconda/profile.d/
%{_sysconfdir}/anaconda/profile.d/tau-home.conf
%{_sysconfdir}/anaconda/profile.d/tau-core.conf

%changelog
* Sat May 21 2022 Lleyton Gray <lleyton@fyralabs.com> - 1.1-2
- Fix and add core

* Sat Apr 23 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Update CI

* Wed Mar 23 2022 Jamie Lee <jamie@innatical.com> - 1.1-0
- Update for Fedora 36

* Sun Feb 27 2022 Jamie Lee <hello@jamiethalacker.dev> - 1.0.0-1
- Initial Release
