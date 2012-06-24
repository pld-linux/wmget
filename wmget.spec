Summary:	wmget - Background download manager in a Window Maker dock app
Summary(pl):	wmget - pracuj�cy w tle program do �ci�gania plik�w w postaci doku w Window Makerze
Name:		wmget
Version:	0.4.4
Release:	1
Group:		Applications/Networking
License:	MIT
Vendor:		Aaron Trickey
URL:		http://amtrickey.net/wmget/index.html
Source0:	http://amtrickey.net/download/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-CFLAGS.patch
Icon:		wmget.xpm
BuildArch:	i686
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xbindir	/usr/X11R6/bin
%define		_xmandir	/usr/X11R6/man

%description
Wmget is a dock app for the GNU Window Maker window manager (or one of
the many other WM's which support dockapps) which makes it more
convenient to perform long downloads in the backgound. It uses the
excellent libcurl library, part of the cURL automated-download


%description -l pl
Wmget jest aplikacj� - dokiem dla mened�era okien GNU Window Maker
(lub innych mened�er�w obs�uguj�cych aplikacje - doki). Wmget sprawia
�e �ci�ganie plik�w w tle jest bardziej wygodne. Korzysta on z
doskona�ej biblioteki libcurl, kt�ra jest cz�ci� programu cURL.


%prep
%setup -qn %{name}
%patch0 -p1


%build
%{__make} OPTFLAGS="${rpmcflags}"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xbindir},%{_xmandir}/man1}
install -s wmget $RPM_BUILD_ROOT%{_xbindir}/wmget
install wmget.1 $RPM_BUILD_ROOT%{_xmandir}/man1/wmget.1
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install wmget.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/wmget.xpm
install dockapp/unittest.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/unittest.xpm
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/share/applnk/Network
install %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/X11R6/share/applnk/Network


%clean
rm -fr $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root)%{_xbindir}/*
%{_xmandir}/man1/*
%{_applnkdir}/Network/wmget.desktop
%{_pixmapsdir}/*.xpm
