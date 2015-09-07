Name:        	centos-docker-image 
Version:        1.0
Release:        1%{?dist}
Summary:        RPM containing docker container of centos

License:        GPLV2
URL:            http://www.projectatomic.io
Source0:        %{name}-%{version}.tar.gz 

#BuildRequires:  
Requires:       docker

%description


%prep
%setup -q -n %{name}-%{version} -c


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_datadir}/%{name}-%{version}
cp %{_builddir}/%{name}-%{version}/centos.tar %{buildroot}/%{_datadir}/%{name}-%{version}

%post
docker load < %{_datadir}/%{name}-%{version}/centos.tar

%files
%{_datadir}/%{name}-%{version}/centos.tar
%doc centos-7.ks README.md


%changelog
* Thu Sep  3 2015 lmohanty
- 
