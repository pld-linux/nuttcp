Summary:	Network bandwidth measurement tool
Summary(pl):	Narzêdzie do monitorowania przepustowo¶ci sieci
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

%description -l pl
nuttcp jest narzêdziem sprawdzaj±cym wydajno¶æ po³±czeñ TCP i UDP
pomiêdzy dwoma systemami.

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
