%define upstream_name    Template-Provider-Encoding
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Template plugin to specify encoding
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Template

%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 405537
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.10-2mdv2009.0
+ Revision: 268729
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.0
+ Revision: 210858
- import perl-Template-Provider-Encoding


* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.0
- first mdv release
