%include	/usr/lib/rpm/macros.perl
%define	pdir	IPC
%define	pnam	SharedCache
Summary:	%{pdir}::%{pnam} perl module
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Name:		perl-%{pdir}-%{pnam}
Version:	1.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005
BuildRequires:	perl(IPC::ShareLite) >= 0.06 perl(Storable) perl(Carp) perl(IPC::SysV)
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
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes ANNOUNCE
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*.3pm.gz
