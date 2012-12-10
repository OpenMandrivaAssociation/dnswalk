Summary:	The dnswalk DNS database debugger
Name:		dnswalk
Version:	2.0.2
Release:	%mkrel 9
Group:		Networking/Other
URL:		http://www.visi.com/~barr/dnswalk/
License:	Artistic
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-perlpath.patch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
dnswalk is a DNS debugger. It performs zone transfers of specified
domains, and checks the database in numerous ways for internal
consistency, as well as accuracy. 

%prep

%setup -q -c -a0
%patch0 -p1

%build

# fix attr
chmod 644 *

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1
install -m755 %{name} %{buildroot}%{_sbindir}/
install -m755 %{name}.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README TODO makereports sendreports rfc1912.txt do-dnswalk
%attr(0755,root,root) %{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-9mdv2011.0
+ Revision: 617864
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 2.0.2-8mdv2010.0
+ Revision: 428306
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.0.2-7mdv2009.0
+ Revision: 244443
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.0.2-5mdv2008.1
+ Revision: 136369
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-5mdv2007.0
+ Revision: 101689
- Import dnswalk

* Sat Jul 15 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-5mdv2007.0
- rebuild

* Sat Jun 04 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-4mdk
- rebuild
- fix autodeps

* Mon May 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.2-3mdk
- build release

