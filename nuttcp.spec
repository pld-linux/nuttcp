Summary:	Network bandwidth measurement tool
Summary(pl.UTF-8):   Narzędzie do monitorowania przepustowości sieci
Name:		nuttcp
Version:	5.3.1
Release:	1
License:	GPL
Group:		Networking
Source0:	ftp://ftp.lcp.nrl.navy.mil/pub/nuttcp/%{name}-%{version}.tar.bz2
# Source0-md5:	8fae45f7211b68e0657b472cce8eb108
URL:		ftp://ftp.lcp.nrl.navy.mil/pub/nuttcp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nuttcp is a benchmarking tool for determining TCP and UDP performance
between 2 systems.

%description -l pl.UTF-8
nuttcp jest narzędziem sprawdzającym wydajność połączeń TCP i UDP
pomiędzy dwoma systemami.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install nuttcp-%{version} $RPM_BUILD_ROOT%{_bindir}
install nuttcp.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
