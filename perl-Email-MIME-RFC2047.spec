#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Email
%define		pnam	MIME-RFC2047
Summary:	Email::MIME::RFC2047 - Correct handling of non-ASCII MIME headers
Summary(pl.UTF-8):	Email::MIME::RFC2047 - właściwa obsługa nagłówkow MIME ze znakami nie ASCII
Name:		perl-Email-MIME-RFC2047
Version:	0.97
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	33642e5bb20c90fa86d8370877e14153
URL:		http://search.cpan.org/dist/Email-MIME-RFC2047/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution tries to provide a correct and usable implementation
of RFC 2047 "MIME Part Three: Message Header Extensions for Non-ASCII
Text". The Encode::MIME::Header module also provides RFC 2047 encoding
and decoding but a useful API should handle the different situations
where RFC 2047 encoded headers are used.

%description -l pl.UTF-8
Ten moduł dostarcza właściwą i użyteczną implementację
RFC 2047 "MIME Part Three: Message Header Extensions for Non-ASCII
Text". Moduł Encode::MIME::Header również dostarcza implementację
kodowania i dekodowania zgodnego z RFC 2047, ale użyteczne API
pozwala na obsługę różnych sytuacji, w których jest
wykorzystywane kodowanie nagłówków wg RFC 2047.

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
%doc Changes
%dir %{perl_vendorlib}/Email/MIME
%{perl_vendorlib}/Email/MIME/*.pm
%dir %{perl_vendorlib}/Email/MIME/RFC2047
%{perl_vendorlib}/Email/MIME/RFC2047/*.pm
%{_mandir}/man3/*
