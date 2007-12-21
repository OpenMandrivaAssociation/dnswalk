Summary:	The dnswalk DNS database debugger
Name:		dnswalk
Version:	2.0.2
Release:	%mkrel 5
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


