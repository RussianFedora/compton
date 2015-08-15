Name:           compton
Version:        0.1
Release:        0.2.beta2%{?dist}
Summary:        A compositor for X11
 
License:        MIT
URL:            https://github.com/chjj/compton
Source0:        https://github.com/chjj/compton/archive/v0.1_beta2.tar.gz
 
BuildRequires:  gcc-c++
BuildRequires:  asciidoc
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
# check
BuildRequires:  /usr/bin/desktop-file-validate
Requires:       xorg-x11-utils
 
%description
Compton is a X compositing window manager, fork of xcompmgr-dana.
 
%prep
%setup -q -n %{name}-0.1_beta2
echo '#!/bin/bash' > configure
chmod +x configure
 
%build
%configure
export COMPTON_VERSION=%{version}
make %{?_smp_mflags}
 
%install
%make_install
 
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
 
%files
%doc README.md 
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-trans
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-trans.1.*
 
%changelog
* Sat Aug 15 2015 Maxim Orlov <murmansksity@gmail.com> - 0.1-0.2.beta2
- Add desktop file

* Fri Aug 07 2015 Maxim Orlov <murmansksity@gmail.com> - 0.1-0.1.beta2
- Initial package.
