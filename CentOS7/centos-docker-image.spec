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
Spec file for packaging docker centos7 image as RPM

%prep
%setup -q -n %{name}-%{version} -c


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_datadir}/%{name}-%{version}
cp %{_builddir}/%{name}-%{version}/centos.tar %{buildroot}/%{_datadir}/%{name}-%{version}

%postun
if [ $1 -eq 0 ] ; then
    docker rmi centos
fi

%post
docker load < %{_datadir}/%{name}-%{version}/centos.tar

%files
%{_datadir}/%{name}-%{version}/centos.tar
%doc centos-7.ks README.md


%changelog
* Mon Sep  7 2015 Lalatendu Mohanty<lmohanty@redhat.com>
- Initial commit
- 
