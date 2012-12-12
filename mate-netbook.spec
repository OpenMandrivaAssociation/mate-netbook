#
# spec file for mate-netbook
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Nelson Marques <nmarques@mate-desktop.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           mate-netbook
Version:        1.5.0
Release:        1.2
License:        GPL-3.0
Summary:        MATE Desktop window management tool
Url:            http://mate-desktop.org
Group:          System/GUI/Other
Source:         http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       mate-panel >= 1.5.0
%glib2_gsettings_schema_requires

BuildRequires:  mate-common
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libmatewnck)
BuildRequires:  pkgconfig(libmatepanelapplet-4.0)
BuildRequires:  pkgconfig(libfakekey)
BuildRequires:  pkgconfig(mate-doc-utils)
BuildRequires:  pkgconfig(unique-1.0)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  xz

%description
This package provides a simple window management tool which provides the
following functionality:
 * Allow to set basic rules for window types;
 * Allow exceptions to the rules based on string matching for window
   name and window class;
 * Allows reversing of rules when the user manually changes something;
 * Re-decorates windows on un-maximize

%lang_package

%prep
%setup -q

%build
export LDFLAGS="$LDFLAGS -lm"
NOCONFIGURE=1 ./autogen.sh
%configure --libexecdir=%{_libexecdir}/%{name}
make %{?_smp_mflags}

%install
%makeinstall
%find_lang %{name} %{?no_lang_C}

%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun

%files
%defattr(-,root,root,-)
%doc ChangeLog README COPYING
%dir %{_libexecdir}/%{name}
%config %{_sysconfdir}/xdg/autostart/mate-maximus-autostart.desktop
%{_bindir}/mate-maximus
%{_libexecdir}/%{name}/mate-window-picker-applet
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/mate-panel/

%files lang -f %{name}.lang
%defattr(-,root,root,-)

%changelog
* Sat Dec  1 2012 nmo.marques@gmail.com
- Initial package
