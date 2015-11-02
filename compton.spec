%global commit d7f95b56b176281bfb252c54defef48c9cd1f4e1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20150920

Name:           compton
Version:        0.1
Release:        1.%{date}git%{shortcommit}%{?dist}
Summary:        A compositor for X11

License:        MIT
URL:            https://github.com/chjj/compton
Source0:        https://github.com/chjj/%{name}/tarball/%{commit}

BuildRequires:  gcc-c++
BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(dbus-1)

%description
Compton is a X compositing window manager, fork of xcompmgr-dana.

%prep
%setup -q -n chjj-%{name}-%{shortcommit}

echo '#!/bin/bash' > configure
chmod +x configure

%build
%configure
export COMPTON_VERSION=%{version}
make %{?_smp_mflags}

%install
%make_install

install -Dm644 %{name}.sample.conf %{buildroot}%{_sysconfdir}/xdg/%{name}.sample.conf

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/xdg/%{name}.sample.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-trans
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-trans.1.*

%changelog
* Mon Nov 02 2015 Maxim Orlov <murmansksity@gmail.com> - 0.1-1.20150920gitd7f95b5
- Update to the latest git snapshot

* Sat Aug 15 2015 Maxim Orlov <murmansksity@gmail.com> - 0.1-0.2.beta2
- Add desktop file

* Fri Aug 07 2015 Maxim Orlov <murmansksity@gmail.com> - 0.1-0.1.beta2
- Initial package.
