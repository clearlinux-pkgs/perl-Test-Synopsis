#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-Synopsis
Version  : 0.17
Release  : 35
URL      : https://cpan.metacpan.org/authors/id/Z/ZO/ZOFFIX/Test-Synopsis-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZO/ZOFFIX/Test-Synopsis-0.17.tar.gz
Summary  : 'Test your SYNOPSIS code'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Synopsis-license = %{version}-%{release}
Requires: perl-Test-Synopsis-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Test-Synopsis,
version 0.17:
Test your SYNOPSIS code

%package dev
Summary: dev components for the perl-Test-Synopsis package.
Group: Development
Provides: perl-Test-Synopsis-devel = %{version}-%{release}
Requires: perl-Test-Synopsis = %{version}-%{release}

%description dev
dev components for the perl-Test-Synopsis package.


%package license
Summary: license components for the perl-Test-Synopsis package.
Group: Default

%description license
license components for the perl-Test-Synopsis package.


%package perl
Summary: perl components for the perl-Test-Synopsis package.
Group: Default
Requires: perl-Test-Synopsis = %{version}-%{release}

%description perl
perl components for the perl-Test-Synopsis package.


%prep
%setup -q -n Test-Synopsis-0.17
cd %{_builddir}/Test-Synopsis-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Synopsis
cp %{_builddir}/Test-Synopsis-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Synopsis/f6380ad8ac244fd8ea6e66d87726ad51820174c9 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Synopsis.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Synopsis/f6380ad8ac244fd8ea6e66d87726ad51820174c9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
