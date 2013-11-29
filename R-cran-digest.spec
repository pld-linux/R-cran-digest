%define		fversion	%(echo %{version} |tr r -)
%define		modulename	digest
Summary:	Create cryptographic hash digests of R objects
Name:		R-cran-%{modulename}
Version:	0.6.3
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	d7913e8091a31885ee2ab798badd7958
URL:		http://cran.fhcrc.org/web/packages/digest/index.html
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The digest package provides a function 'digest()' for the creation of
hash digests of arbitrary R objects (using the md5, sha-1, sha-256 and
crc32 algorithms) permitting easy comparison of R language objects,
as well as a function 'hmac()' to create hash-based message
authentication code.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
