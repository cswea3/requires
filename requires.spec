%global _el_version rtcs_el6
%global _el_sub .buildsys

Name:       cswearingen-requires-test
Summary:    Test RPM
Version:    1
Release:    12
License:    GPL
Group:      Development/Buildsystem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
BuildRequires: chainbuild-test
Requires:   chainbuild-test
%description
Just a test

%prep

%build

%install

%clean


%changelog
* Thu Oct 31 2019 Craig Swearingen <craig.swearingen@forcepoint.com>
- Initial variables for koji mock build of ttc packages
