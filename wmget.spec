Summary:	wmget - Background download manager in a Window Maker dock app
Summary(pl):	wmget - pracuj±cy w tle program do ¶ci±gania plików dla doku Window Makera
Name:		wmget
Version:	0.6.0
Release:	4
License:	MIT
Group:		X11/Window Managers/Tools
Source0:	http://amtrickey.net/download/%{name}-%{version}-src.tar.gz
# Source0-md5:	f4f196f3cf1c427e1f8321b4063c4917
Source1:	%{name}.desktop
Patch0:		%{name}-CFLAGS.patch
URL:		http://amtrickey.net/wmget/
BuildRequires:	XFree86-devel
BuildRequires:	curl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Wmget is a dock app for the GNU Window Maker window manager (or one of
the many other WM's which support dockapps) which makes it more
convenient to perform long downloads in the backgound. It uses the
excellent libcurl library, part of the cURL automated-download

%description -l pl
Wmget jest dokowaln± aplikacj± dla zarz±dcy okien GNU Window Maker
(lub innych zarz±dców obs³uguj±cych aplikacje - doki). Wmget sprawia,
¿e ¶ci±ganie plików w tle jest wygodniejsze. Korzysta on z doskona³ej
biblioteki libcurl, która jest czê¶ci± programu cURL.

%prep
%setup -qn %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="-L/usr/X11R6/%{_lib} -lXpm -lXext -lX11 -lm -lcurl"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_pixmapsdir}}

install wmget $RPM_BUILD_ROOT%{_bindir}/wmget
install wmget.1 $RPM_BUILD_ROOT%{_mandir}/man1/wmget.1
install wmget.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/wmget.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/wmget.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/*.xpm
