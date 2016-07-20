%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1

Summary: Sugar toolkit GTK+ 3
Name:    sugar-toolkit-gtk3
Version: 0.108.1
Release: 1
URL:     http://wiki.laptop.org/go/Sugar
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Source1: macros.sugar
Source100: %{name}.rpmlintrc
License: LGPLv2+
Group:   System/Libraries

BuildRequires: pkgconfig(alsa)
BuildRequires: gettext-devel
BuildRequires: gtk+3.0-devel
BuildRequires: gobject-introspection-devel
BuildRequires: intltool
BuildRequires: librsvg2-devel
BuildRequires: pkgconfig(sm)
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: python2-devel
BuildRequires: pkgconfig(pygtk-2.0)
BuildRequires: python2-gobject-devel

Requires: python2-dbus
Requires: gettext
Requires: python2-gi
Requires: python2-simplejson
Requires: python2-dateutil
Requires: sugar-datastore
Requires: unzip

%description
Sugar is the core of the OLPC Human Interface. The toolkit provides
a set of widgets to build HIG compliant applications and interfaces
to interact with system services like presence and the datastore.
This is the toolkit depending on GTK3.

%package devel
Summary: Invokation information for accessing SugarExt-1.0
Group: Development/GNOME and GTK+
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the invocation information for accessing
the SugarExt-1.0 library through gobject-introspection.

%prep
%setup -q

%build
%configure
make V=1

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_sysconfdir}/rpm/
install -p %{SOURCE1} %{buildroot}/%{_sysconfdir}/rpm/macros.sugar

%find_lang %name

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README
%{python2_sitelib}/*
%{_sysconfdir}/rpm/macros.sugar
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/lib*.so.*
%{_bindir}/sugar-activity
%{_bindir}/sugar-activity-web

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir

