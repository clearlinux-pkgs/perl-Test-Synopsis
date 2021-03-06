#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Synopsis
Version  : 0.16
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/Z/ZO/ZOFFIX/Test-Synopsis-0.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZO/ZOFFIX/Test-Synopsis-0.16.tar.gz
Summary  : 'Test your SYNOPSIS code'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Synopsis-license = %{version}-%{release}
Requires: perl-Test-Synopsis-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Test-Synopsis,
version 0.16:
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
%setup -q -n Test-Synopsis-0.16
cd %{_builddir}/Test-Synopsis-0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
cp %{_builddir}/Test-Synopsis-0.16/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Synopsis/5406f6b1a7d020f7ed2e9a9d221d915973971e84
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
/usr/share/package-licenses/perl-Test-Synopsis/5406f6b1a7d020f7ed2e9a9d221d915973971e84

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Test/Synopsis.pm
