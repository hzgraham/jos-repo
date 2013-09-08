Name:		jos-repo
Version:	1.0.0
Release:	1%{?dist}
Summary:	package repository rpm

Group:		System Environment/Base
License:	GPLv2
URL:		https://github.com/hzgraham/jos-repo
Source0:	%{name}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	httpd, createrepo


%description
Creates and configures two package repositories for the JOS environment


%prep
%setup -q -c -n %{name}-src-base-%{version}


%build
echo "Build OK"

%install


%post
mkdir -p /var/www/html/JOS/stable/6.4
mkdir -p /var/www/html/JOS/unstable/6.4
service httpd start
chkconfig httpd on
createrepo /var/www/html/JOS/stable/6.4
createrepo /var/www/html/JOS/unstable/6.4

clear
echo "Reboot for the changes to take effect"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/var/www/html/JOS

%changelog
*  Sat Sep 07 2013 - hgraham@redhat.com
 - initial build
