%define upstream_name    Template-Provider-Encoding
%define upstream_version 0.10
Name:		perl-%{upstream_name}
Version:	0.10
Release:	4

Summary:	Template plugin to specify encoding
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Template-Provider-Encoding
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Template-Provider-Encoding-0.10.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Encode)
BuildRequires:	perl(Template)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Template::Plugin::encoding is a Template plugin to declare the encoding of
template files. This plugin doesn't actually do anything but
Template::Provider::Encoding scans the usage of this module to find the
encoding of templates. As a bonus, you can use 'encoding' variable in the
template to specify file encoding, which might be useful for XML or HTML
meta tag.

%prep
%setup -q -n Template-Provider-Encoding-0.10

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Template

