%define dist_version 35

Summary:        tauOS Anaconda Profiles
Name:           tau-anaconda-profiles
Version:        1
Release:        1
License:        GPLv3
URL:            https://tauos.co
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Provides:       tau-anaconda-profiles(%{version}) = %{release}

# Requires:       anaconda-core(%{dist_version})

%description
Provides tauOS Anaconda profiles for installation.

%prep
%setup -q
%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/anaconda/profile.d/
install -m 644 tauos-home.conf %{buildroot}%{_sysconfdir}/anaconda/profile.d/

%files
%dir %{_sysconfdir}/anaconda/profile.d/
%{_sysconfdir}/anaconda/profile.d/tauos-home.conf

%changelog
* Sun Feb 27 2022 Jamie Lee <hello@jamiethalacker.dev> - 1.0.0-1
- Initial Release
