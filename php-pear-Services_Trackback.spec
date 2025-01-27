%define		_class		Services
%define		_subclass	Trackback
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.7.1
Release:	2
Summary:	A generic class for sending and receiving trackbacks
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Services_Trackback/
Source0:	http://download.pear.php.net/package/Services_Trackback-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
A generic class for sending and receiving trackbacks.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-10mdv2012.0
+ Revision: 742275
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-9
+ Revision: 679579
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-8mdv2011.0
+ Revision: 613772
- the mass rebuild of 2010.1 packages

* Tue Nov 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-7mdv2010.1
+ Revision: 467081
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.6.1-6mdv2010.0
+ Revision: 441569
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-5mdv2009.1
+ Revision: 322661
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-4mdv2009.0
+ Revision: 237066
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-3mdv2008.0
+ Revision: 15501
- rule out the PHPUnit.php dep


* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-2mdv2007.1
+ Revision: 140455
- add a bunch of missing files

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-1mdv2007.1
+ Revision: 82633
- Import php-pear-Services_Trackback

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-1mdk
- 0.6.1

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-1mdk
- 0.5.1
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdk
- initial Mandriva package (PLD import)


