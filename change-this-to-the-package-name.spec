%define name libdb4-utils
%define version 1.0
%define release 1
Summary: This is what libdb4-utils does.
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source: %{name}-%{version}.tar.gz
License: GNU GPL version 2
Group: SMEserver/addon
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 10.0
AutoReqProv: no

%description
3rd Party (Maintained by Koozali) git repo for libdb4-utils smeserver

%changelog
* Day MMMM DD YYYY <brianr@koozali.org> 1.0-1.sme
- Initial code - create RPM [SME:99999]

%prep

%setup -q

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
> %{name}-%{version}-filelist
#echo "%doc COPYING"  >> %{name}-%{version}-filelist
#--dir <dir> 'attr(755,user,grp)' \
#--file <file> 'attr(755,root,root)' \

%clean
cd ..
rm -rf %{name}-%{version}

%pre

%preun

%post

%postun
#uninstall
%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
