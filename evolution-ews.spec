Summary:	Exchange Web Services for Evolution
Name:		evolution-ews
Version:	3.12.0
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-ews/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	817cf396d43b8fd3cbab1698d3081c91
URL:		http://projects.gnome.org/evolution/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-devel >= 3.12.0
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libical-devel
BuildRequires:	libmspack-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
Requires:	evolution >= 3.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows Evolution to interact with Microsoft Exchange
servers, versions 2007 and later, through its Exchange Web Services
(EWS) interface.

%package devel
Summary:	Development files for ews library
Group:		Development/Libraries

%description devel
This package provides development files for ews library.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*/{,*/,*/*/}*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/evolution-data-server/addressbook-backends/libebookbackendews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/calendar-backends/libecalbackendews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/camel-providers/libcamelews.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.urls
%attr(755,root,root) %{_libdir}/evolution-data-server/libeews-1.2.so*
%attr(755,root,root) %{_libdir}/evolution-data-server/libewsutils.so*
%attr(755,root,root) %{_libdir}/evolution-data-server/registry-modules/module-ews-backend.so
%attr(755,root,root) %{_libdir}/evolution/*/modules/module-ews-configuration.so
%{_datadir}/evolution-data-server/ews
%{_datadir}/evolution/*/errors/module-ews-configuration.error

%files devel
%defattr(644,root,root,755)
%{_includedir}/evolution-data-server/ews

