%define upstream_name    Template-Provider-Encoding
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Template plugin to specify encoding
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl(Template)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/Template
