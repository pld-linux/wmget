Summary:	wmget - Background download manager in a Window Maker dock app
Summary(pl):	wmget - pracuj±cy w tle program do ¶ci±gania plików w postaci doku w Window Makerze
Name:		wmget
Version:	0.4.4
Release:	1
Group:		Applications/Network
######		Unknown group!
License:	MIT
Vendor:		Aaron Trickey
URL:		http://amtrickey.net/wmget/index.html
Source0:	http://amtrickey.net/download/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop
Icon:		wmget.xpm
BuildArch:	i686
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xbindir	/usr/X11R6/bin
%define		_xmandir	/usr/X11R6/man
%description
%description -l pl
Wmget jest aplikacj± - dokiem dla mened¿era okien GNU Window Maker
(lub innych mened¿erów obs³uguj±cych aplikacje - doki). Wmget sprawia
¿e ¶ci±ganie plików w tle jest bardziej wygodne. Korzysta on z
doskona³ej biblioteki libcurl, która jest czê¶ci± programu cURL.
%prep
%setup -qn %{name}
%build
%{__make}
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xbindir},%{_xmandir}/man1}

install -s wmget $RPM_BUILD_ROOT%{_xbindir}/wmget
install wmget.1 $RPM_BUILD_ROOT%{_xmandir}/man1/wmget.1
%__install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install wmget.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/wmget.xpm
install dockapp/unittest.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/unittest.xpm
gzip -9nf $RPM_BUILD_ROOT%{_xmandir}/man1/* \
	  README wmget.pod
%__install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/share/applnk/Network
install %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/X11R6/share/applnk/Network
%clean
rm -fr $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_xbindir}/*
%{_xmandir}/man1/*
%{_applnkdir}/Network/wmget.desktop
%{_pixmapsdir}/*.xpm
%doc *.gz
%verify (not md5 size mtime)
