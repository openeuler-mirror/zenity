Name:          zenity
Version:       3.41.0
Release:       1
Summary:       Display GTK dialog boxes in commandline and shell scripts

License:       LGPLv2+
URL:           https://wiki.gnome.org/Projects/Zenity
Source:        https://download-fallback.gnome.org/sources/zenity/3.41/%{name}-%{version}.tar.xz


BuildRequires: gcc pkgconfig(gtk+-3.0) >= 3.0.0 which gettext intltool itstool meson

%description
Zenity is a tool that allows you to display GTK dialog boxes in commandline and shell scripts.

%package_help

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang zenity --with-gnome

%files -f zenity.lang
%exclude %{_bindir}/gdialog
%license COPYING
%doc AUTHORS NEWS THANKS README
%{_bindir}/zenity
%{_datadir}/zenity

%files help
%{_mandir}/man1/zenity.1*

%changelog
* Sat Dec 04 2021 wangkerong <wangkerong@huawei.com> - 3.41.0-1
- update to 3.41.0

* Mon Sep 7 2020 zhanzhimin <zhanzhimin@huawei.com> - 3.32.0-2
- update source0

* Mon July 20 2020 chnegguipeng<chnegguipeng1@huawei.com> - 3.32.0-1
- Upgrade to 3.32.0-1

* Thu Sep 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.30.0-2
- Package init
