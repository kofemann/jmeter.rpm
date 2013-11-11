#
# build as:
#     rpmbuild -ba jmeter.spec
#

Name:       jmeter
Summary:    JMeter loag generator
Version:    2.10
Release:    1
License:    http://www.apache.org/licenses/LICENSE-2.0
Packager:   dCache.ORG
Group:      Development/Tools
BuildArch:  noarch
Requires:   java-1.7.0-openjdk >= 1.7 
Source0:    http://archive.apache.org/dist/jmeter/binaries/apache-jmeter-%{version}.tgz
Source1:    jmeter
Source2:    jmeter.sysconfig

%define target_dir /usr/share/jmeter

%description
Apache JMeterâ„¢ is a 100% pure Java desktop application
designed to load test functional behavior and measure
performance. It was originally designed for testing
Web Applications but has since expanded to other test
functions.

%prep
%{__mkdir_p} %{buildroot}
%setup -q -n apache-jmeter-%{version}

%install
%{__mkdir_p} %{buildroot}/%{target_dir}
%{__mv} * %{buildroot}/%{target_dir}

%{__mkdir_p} %{buildroot}/etc/init.d
cp %{SOURCE1} %{buildroot}/etc/init.d/jmeter

%{__mkdir_p} %{buildroot}/etc/sysconfig
cp %{SOURCE2} %{buildroot}/etc/sysconfig/jmeter


%files
%defattr(-,root,root,-)
%{target_dir}
/etc/init.d/jmeter
%config(noreplace) /etc/sysconfig/jmeter

%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%changelog
* Mon Nov 11 2013 Tigran Mkrtchyan <tigran.mkrtchyan@desy.de>
- initial version of package
