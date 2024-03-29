%define _prefix /usr


Summary: The Greenbone Vulnerability Management (GVM) suite
Name:    gvm
Version: 22.04
Release: RELEASE-AUTO%{?dist}.art
Source0: gvm.tar.gz
License: AGPL
URL: http://www.openvas.org
Vendor: Greenbone https://www.greenbone.net
Packager: https://www.atomicorp.com
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}
BuildArch:      noarch
Obsoletes: openvas
Provides: openvas
Obsoletes: greenbone-vulnerability-manager
Provides: greenbone-vulnerability-manager
Provides: greenbone-vulnerability-management


Requires: mosquitto
Requires: pg-gvm
Requires:  texlive-collection-fontsrecommended texlive-collection-latexrecommended texlive-changepage texlive-titlesec
Requires: postgresql-server postgresql-contrib
Requires: python3
Requires: openvas-scanner
# Manual building now
#Requires: OSPd
Requires: OSPd-openvas
Requires: gvmd
Requires: greenbone-security-assistant
Requires: redis
Requires: psmisc
Requires: nmap
# move to script, this is from epel 
#Requires: haveged
Requires: gnutls-utils
Requires: rng-tools
Requires: bzip2
Requires: openvas-smb
# possibly fixes something
Requires: perl-XML-Twig

%if  0%{!?rhel} >= 6
# PDF reports
Requires: texlive-texconfig texlive-metafont-bin  
%else
Requires: texlive-texmf-latex
#Requires: texlive-collection-latexextra
%endif

%if 0%{?fedora} >= 21
Requires: texlive-comment
Requires: texlive-collection-latexextra
%endif

 

%description
Greenbone Vulnerability Management (GVM) is a meta-package encompassing all of the components from GVM including OpenVAS.

%prep

%autosetup  -n gvm

%build

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/licenses/greenbone-vulnerability-management/
mkdir -p %{buildroot}/etc/sudoers.d/
mkdir -p %{buildroot}/etc/cron.daily/
mkdir -p %{buildroot}/usr/share/texlive/texmf-local/tex/latex/comment
install -m0700 openvas-setup %{buildroot}/usr/bin/openvas-setup
install -m0700 openvas-setup %{buildroot}/usr/bin/gvm-setup
install -m0600 gvm.sudo %{buildroot}/etc/sudoers.d/gvm
install -m0644 LICENSE %{buildroot}/usr/share/licenses/greenbone-vulnerability-management/
install -m700 gvm.cron %{buildroot}/etc/cron.daily/gvm
install -m0644 comment.sty %{buildroot}/usr/share/texlive/texmf-local/tex/latex/comment/comment.sty


%post
/usr/bin/texhash >/dev/null 2>&1 ||: 


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%license LICENSE
/usr/bin/openvas-setup
/usr/bin/gvm-setup
/etc/sudoers.d/gvm
/etc/cron.daily/gvm
/usr/share/licenses/greenbone-vulnerability-management/LICENSE
/usr/share/texlive/texmf-local/tex/latex/comment/comment.sty



%changelog
* Sat Sep 12 2020 Scott R. Shinn <scott@atomicorp.com> - 20.08.0-RELEASE-AUTO
- Add fixes for pdf generation

* Sat Aug 1 2020 Scott R. Shinn <scott@atomicorp.com> - 11.0.0-RELEASE-AUTO
- Update loader for GVM/Openvas 11.0.0

* Mon Apr 8 2019 Scott R. Shinn <scott@atomicorp.com> - 10.0.0-RELEASE-AUTO
- Update loader for Openvas 10.0.0

* Thu Dec 22 2016 Scott R. Shinn <scott@atomicorp.com> - 1.0-24
- Add PATH to cron jobs (Credit: Edwin Eefting)

* Tue Dec 13 2016 Scott R. Shinn <scott@atomicorp.com> - 1.0-23
- Update openvas-check-setup to 2.3.7

* Mon Aug 3 2015 Scott R. Shinn <scott@atomicorp.com> - 1.0-21
- Add redis setup step

* Fri May 29 2015 Scott R. Shinn <scott@atomicorp.com> - 1.0-20
- Add redis dependency
- Add systemctl logic to openvas-setup
- Add wget/curl/rsync dialog to openvas-setup

* Fri May 29 2015 Scott R. Shinn <scott@atomicorp.com> - 1.0-17
- Update openvas-setup to 2.3.0

* Thu Apr 23 2015 Scott R. Shinn <scott@atomicorp.com> - 1.0-16
- Openvas 8 support

* Thu Jun 19 2014 Scott R. Shinn <scott@atomicorp.com> - 1.0-11
- Drop openvas-administrator requires

* Tue Jun 10 2014 Scott R. Shinn <scott@atomicorp.com> - 1.0-10
- Updates for Openvas 7

* Tue Sep 17 2013 Scott R. Shinn <scott@atomicorp.com> - 1.0-9
- Add havegd dependency
- Add openvas-certdata-sync to setup and cron

* Thu Apr 18 2013 Scott R. Shinn <scott@atomicorp.com> - 1.0-8
- Drop gsd dependency
- Update openvas-check-setup

* Wed Feb 13 2013 Scott R. Shinn <scott@atomicorp.com> - 1.0-6
- Add dirb dependency
- Update openvas-setup to return output on the lengthy nvt update

* Wed Jan 16 2013 Scott R. Shinn <scott@atomicorp.com> - 1.0-5
- Exit 1 if download fails on either NVT or SCAP data during setup

* Fri Nov 23 2012 Scott R. Shinn <scott@atomicorp.com> - 1.0-3
- Disable output suppression in openvas-scapdata cron by request (Devin Walsh)

* Thu Jun 21 2012 Scott R. Shinn <scott@atomicorp.com> - 1.0-2
- Add openvas-sync-scap routine to setup
- Add openvas-sync-scap cron job

* Wed Jun 6 2012 Scott R. Shinn <scott@atomicorp.com> - 1.0-1
- Add wapiti dependency 
- Update openvas-check-setup
- Add administrator password validation dialog to setup
- Fixes for openvasmd db creation


* Tue Mar 20 2012 Scott R. Shinn <scott@atomicorp.com> - 1.0-0.8
- Bugfix for initializing the openvas manager database correctly. Routine duplicated from openvas-manager package
- Add startup routine for openvas-administrator 

* Thu Feb 17 2011 Scott R. Shinn <scott@atomicorp.com> - 1.0-0.2
- Dropped requires on openvas-administrator
