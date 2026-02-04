Name:           cosmic-term
Epoch:          1
Version: 1.0.0
Release:        1%{?dist}
Summary:        COSMIC Terminal Emulator (Playtron fork)

License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-term
Source0:        %{name}-%{_arch}.tar.gz

# No BuildRequires - binary is pre-built

# cosmic-icon-theme is the only explicit dependency (like upstream)
Requires:       (cosmic-icon-theme >= 1.0.0 with cosmic-icon-theme < 1.1.0)

%description
Terminal emulator for the COSMIC desktop environment.
A libcosmic-based terminal emulator with GPU acceleration.

%prep
%autosetup -n %{name} -p1

%build

%install
install -Dm0755 "usr/bin/cosmic-term" "%{buildroot}%{_bindir}/cosmic-term"
install -Dm0644 "usr/share/applications/com.system76.CosmicTerm.desktop" "%{buildroot}%{_datadir}/applications/com.system76.CosmicTerm.desktop"
install -Dm0644 "usr/share/metainfo/com.system76.CosmicTerm.metainfo.xml" "%{buildroot}%{_datadir}/metainfo/com.system76.CosmicTerm.metainfo.xml"
install -Dm0644 "usr/share/licenses/cosmic-term/LICENSE" "%{buildroot}%{_datadir}/licenses/cosmic-term/LICENSE"

# Install icons
install -Dm0644 "usr/share/icons/hicolor/16x16/apps/com.system76.CosmicTerm.svg" "%{buildroot}%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicTerm.svg"
install -Dm0644 "usr/share/icons/hicolor/24x24/apps/com.system76.CosmicTerm.svg" "%{buildroot}%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicTerm.svg"
install -Dm0644 "usr/share/icons/hicolor/32x32/apps/com.system76.CosmicTerm.svg" "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicTerm.svg"
install -Dm0644 "usr/share/icons/hicolor/48x48/apps/com.system76.CosmicTerm.svg" "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicTerm.svg"
install -Dm0644 "usr/share/icons/hicolor/64x64/apps/com.system76.CosmicTerm.svg" "%{buildroot}%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicTerm.svg"
install -Dm0644 "usr/share/icons/hicolor/128x128/apps/com.system76.CosmicTerm.svg" "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicTerm.svg"
install -Dm0644 "usr/share/icons/hicolor/256x256/apps/com.system76.CosmicTerm.svg" "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicTerm.svg"

%files
%license %{_datadir}/licenses/cosmic-term/LICENSE
%{_bindir}/cosmic-term
%{_datadir}/applications/com.system76.CosmicTerm.desktop
%{_datadir}/metainfo/com.system76.CosmicTerm.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/com.system76.CosmicTerm.svg

%changelog
* Tue Feb 03 2026 Playtron <dev@playtron.one> - 1.0.5-1
- Initial RPM package with --maximize flag support
