%include	/usr/lib/rpm/macros.perl
%define	pdir	IPC
%define	pnam	SharedCache
Summary:	%{pdir}::%{pnam} perl module
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Name:		perl-%{pdir}-%{pnam}
Version:	1.3
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d5d159a6b41d42918b7c1fceafb43ae
BuildRequires:	perl-devel >= 5.005
BuildRequires:	perl-Carp
BuildRequires:	perl-IPC-ShareLite >= 0.06
BuildRequires:	perl-IPC-SysV
BuildRequires:	perl-Storable
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a shared memory cache accessed as a tied hash.

%description -l pl
Ten modu³ udostêpnia cache pamiêci dzielonej, dostêpny jako
dowi±zany hash.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes ANNOUNCE
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*.3pm*
