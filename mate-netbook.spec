%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Desktop window management tool
Name:           mate-netbook
Version:	1.8.1
Release:	1
License:	GPLv3
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libfakekey)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(unique-1.0)
Requires:	mate-panel

%description
This package provides a simple window management tool which provides the
following functionality:
 * Allow to set basic rules for window types;
 * Allow exceptions to the rules based on string matching for window
   name and window class;
 * Allows reversing of rules when the user manually changes something;
 * Re-decorates windows on un-maximize

%prep
%setup -q
%apply_patches
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
	--libexecdir=%{_libexecdir}/%{name}

%make

%install
%makeinstall_std

# remove unneeded converter
rm -fr %{buildroot}%{_datadir}/MateConf

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc ChangeLog README COPYING
%config %{_sysconfdir}/xdg/autostart/mate-maximus-autostart.desktop
%{_bindir}/mate-maximus
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mate-window-picker-applet
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/mate-panel/
%{_mandir}/man1/mate-maximus.1*

