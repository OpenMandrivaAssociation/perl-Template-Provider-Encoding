%define module   Template-Provider-Encoding
%define version    0.10
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Template plugin to specify encoding
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Template/%{module}-%{version}.tar.gz
BuildRequires: perl(Encode)
BuildRequires: perl(Template)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Template::Plugin::encoding is a Template plugin to declare the encoding of
template files. This plugin doesn't actually do anything but
Template::Provider::Encoding scans the usage of this module to find the
encoding of templates. As a bonus, you can use 'encoding' variable in the
template to specify file encoding, which might be useful for XML or HTML
meta tag.

%prep
%setup -q -n %{module}-%{version} 

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

