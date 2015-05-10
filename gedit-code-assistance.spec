Summary:	GEdit plugin providing code assistance support
Summary(pl.UTF-8):	Wtyczka GEdita udostępniająca wsparcie pracy z kodem
Name:		gedit-code-assistance
Version:	3.16.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gedit-code-assistance/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	3b34529e1851fd2c705a9f754386dcce
URL:		https://wiki.gnome.org/Projects/CodeAssistance
BuildRequires:	gedit-devel >= 3.8
BuildRequires:	gtksourceview3-devel >= 3.13.90
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GEdit plugin providing code assistance support from
gnome-code-assistance services.

%description -l pl.UTF-8
Wtyczka GEdita udostępniająca wsparcie pracy z kodem, zapewnianym
przez usługi gnome-code-assistance.

%package devel
Summary:	Header file for GEdit Code Assistance
Summary(pl.UTF-8):	Plik nagłówkowy funkcji GEdit Code Assistance
Group:		Development/Libraries
# doesn't require base
Requires:	gedit-devel >= 3.8

%description devel
Header file for GEdit Code Assistance.

%description devel -l pl.UTF-8
Plik nagłówkowy funkcji GEdit Code Assistance.

%package -n vala-gedit-code-assistance
Summary:	Vala API for GEdit Code Assistance
Summary(pl.UTF-8):	API języka Vala do funkcji GEdit Code Assistance
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n vala-gedit-code-assistance
Vala API for GEdit Code Assistance.

%description -n vala-gedit-code-assistance -l pl.UTF-8
API języka Vala do funkcji GEdit Code Assistance.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/gca/indent-backends/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/gedit/plugins/codeassistance.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/libcodeassistance.so
%dir %{_libdir}/gedit/plugins/gca
%dir %{_libdir}/gedit/plugins/gca/indent-backends
%{_libdir}/gedit/plugins/gca/indent-backends/gcaindentbackendc.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/gca/indent-backends/libgcaindentbackendc.so
%{_datadir}/appdata/gedit-code-assistance.metainfo.xml
%{_datadir}/gedit/plugins/codeassistance

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/gedit-3.0
%{_includedir}/gedit-3.0/gca

%files -n vala-gedit-code-assistance
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gca.vapi
