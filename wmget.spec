Summary:	wmget - Background download manager in a Window Maker dock app
Summary(pl):	wmget - pracuj±cy w tle program do ¶ci±gania plików dla doku Window Makera
Name:		wmget
Version:	0.4.4
Release:	1
License:	MIT
Vendor:		Aaron Trickey
Group:		X11/Applications/Networking
Source0:	http://amtrickey.net/download/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-CFLAGS.patch
Icon:		wmget.xpm
URL:		http://amtrickey.net/wmget/
BuildRequires:	XFree86-devel
BuildRequires:	curl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Wmget is a dock app for the GNU Window Maker window manager (or one of
the many other WM's which support dockapps) which makes it more
convenient to perform long downloads in the backgound. It uses the
excellent libcurl library, part of the cURL automated-download

%description -l pl
Wmget jest dokowaln± aplikacj± dla mened¿era okien GNU Window Maker
(lub innych mened¿erów obs³uguj±cych aplikacje - doki). Wmget sprawia
¿e ¶ci±ganie plików w tle jest bardziej wygodne. Korzysta on z
doskona³ej biblioteki libcurl, która jest czê¶ci± programu cURL.

%prep
%setup -qn %{name}
%patch0 -p1

%build
%{__make} OPTFLAGS="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_pixmapsdir},%{_applnkdir}/Network}

install wmget $RPM_BUILD_ROOT%{_bindir}/wmget
install wmget.1 $RPM_BUILD_ROOT%{_mandir}/man1/wmget.1
install wmget.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/wmget.xpm
install dockapp/unittest.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/unittest.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/Network/wmget.desktop
%{_pixmapsdir}/*.xpm
