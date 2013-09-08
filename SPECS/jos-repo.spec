Name:		jos-repo
Version:	1.0.1
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
mkdir -p $RPM_BUILD_ROOT/var/www/html/JOS/stable/6.4
mkdir -p $RPM_BUILD_ROOT/var/www/html/JOS/unstable/6.4
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
install -p -m 0755 RPM-GPG-KEY-JOS-STABLE $RPM_BUILD_ROOT/var/www/html/JOS/stable/6.4
install -p -m 0755 RPM-GPG-KEY-JOS-UNSTABLE $RPM_BUILD_ROOT/var/www/html/JOS/unstable/6.4
install -p -m 0600 iptables $RPM_BUILD_ROOT/etc/sysconfig

%post
mkdir -p /var/www/html/JOS/stable/6.4
mkdir -p /var/www/html/JOS/unstable/6.4
service httpd start
chkconfig httpd on
createrepo /var/www/html/JOS/stable/6.4
createrepo /var/www/html/JOS/unstable/6.4

/sbin/iptables -F
/sbin/iptables-restore < /etc/sysconfig/iptables
/sbin/service iptables save
/sbin/service iptables restart

clear
echo "Reboot for the changes to take effect"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/var/www/html/JOS/stable/6.4/RPM-GPG-KEY-JOS-STABLE
/var/www/html/JOS/unstable/6.4/RPM-GPG-KEY-JOS-UNSTABLE
/etc/sysconfig/iptables

%changelog
*  Sun Sep 08 2013 - hgraham@redhat.com
 - added iptables configurations

*  Sat Sep 07 2013 - hgraham@redhat.com
 - initial build
