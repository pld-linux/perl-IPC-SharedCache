#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IPC
%define		pnam	SharedCache
Summary:	IPC::SharedCache - manage a cache in SysV IPC shared memory
Summary(pl):	IPC::SharedCache - zarz�dzanie pami�ci� podr�czn� w pami�ci dzielonej SysV
Name:		perl-IPC-SharedCache
Version:	1.3
Release:	6
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d5d159a6b41d42918b7c1fceafb43ae
BuildRequires:	perl-Carp-Assert
BuildRequires:	perl-IPC-ShareLite >= 0.06
BuildRequires:	perl-IPC-SysV
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a shared memory cache accessed as a tied hash.

%description -l pl
Ten modu� udost�pnia cache pami�ci dzielonej, dost�pny jako
dowi�zany hash.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes ANNOUNCE
%{perl_vendorlib}/IPC/SharedCache.pm
%{_mandir}/man3/*.3pm*
