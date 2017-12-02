%define _prefix /usr
%define cvs rc1


Summary: The Open Vulnerability Assessment (OpenVAS) suite
Name:    openvas
Version: 1.0
Release: RELEASE-AUTO%{?dist}.art
Source0: %{name}-setup
Source1: http://svn.wald.intevation.org/svn/openvas/trunk/tools/openvas-check-setup
Source2: openvas-scap-sync-cronjob
Source3: openvas-cert-sync-cronjob
Source4: openvas-nvt-sync-cronjob
License: AGPL
URL: http://www.openvas.org
Group: System Environment/Libraries
Vendor: OpenVAS Development Team, http://www.openvas.org
Packager: Scott R. Shinn <scott@atomicorp.com>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}
BuildArch:      noarch

Requires: openvas-scanner
Requires: openvas-cli

%if 0%{?fedora} >= 24
Requires: gvm-tools
%endif
Requires: openvas-manager
Requires: greenbone-security-assistant
Requires: redis
Requires: psmisc
Requires: OSPd-nmap

# Support packages:
Requires: nmap

Requires: nikto
Requires: ncrack
Requires: wapiti

# Tmp, need to sort out alien and w3af for el6, and w3af for el7
#if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
#Requires: w3af
Requires: alien
#%endif

Requires: dirb
Requires: haveged

# not supported on fc27 now
#Requires: ovaldi
Requires: gnutls-utils
Requires: rng-tools

Requires: bzip2


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
openvas is a meta-package encompassing all of the components from OpenVAS.

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m0700 %{SOURCE0} %{buildroot}/usr/bin/openvas-setup
install -m0700 %{SOURCE1} %{buildroot}/usr/bin/openvas-check-setup
install -Dp -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/cron.d/openvas-sync-scap
install -Dp -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/cron.d/openvas-sync-cert
install -Dp -m 644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/cron.d/openvas-sync-nvt


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/openvas-setup
/usr/bin/openvas-check-setup
/etc/cron.d/openvas-sync-scap
/etc/cron.d/openvas-sync-cert
/etc/cron.d/openvas-sync-nvt


%changelog
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
