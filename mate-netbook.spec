%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Desktop window management tool
Name:		mate-netbook
Version:	1.20.0
Release:	1
License:	GPLv3
Group:		Graphical desktop/Other
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libfakekey)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	yelp-tools

Requires:	mate-panel

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides a simple window management tool which provides the
following functionality:
 * Allow to set basic rules for window types;
 * Allow exceptions to the rules based on string matching for window
   name and window class;
 * Allows reversing of rules when the user manually changes something;
 * Re-decorates windows on un-maximize

%files -f %{name}.lang
%doc ChangeLog README COPYING NEWS
%config %{_sysconfdir}/xdg/autostart/mate-maximus-autostart.desktop
%{_bindir}/mate-maximus
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mate-window-picker-applet
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/mate-panel/
%{_mandir}/man1/mate-maximus.1*

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--libexecdir=%{_libexecdir}/%{name} \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/mate-maximus-autostart.desktop
