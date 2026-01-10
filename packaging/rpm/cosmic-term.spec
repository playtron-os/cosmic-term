Name:           cosmic-term
Epoch:          1
Version:        %{getenv:COSMIC_TERM_VERSION}
Release:        1%{?dist}
Summary:        COSMIC Terminal Emulator (Playtron fork)

License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-term

# No BuildRequires - binary is pre-built

# cosmic-icon-theme is the only explicit dependency (like upstream)
Requires:       (cosmic-icon-theme >= 1.0.0 with cosmic-icon-theme < 1.1.0)

%description
Terminal emulator for the COSMIC desktop environment.
A libcosmic-based terminal emulator with GPU acceleration.

%prep
%build

%install
# COSMIC_TERM_SOURCE is set by the build script
install -Dm0755 "%{getenv:COSMIC_TERM_SOURCE}/target/release/cosmic-term" "%{buildroot}%{_bindir}/cosmic-term"
install -Dm0644 "%{getenv:COSMIC_TERM_SOURCE}/res/com.system76.CosmicTerm.desktop" "%{buildroot}%{_datadir}/applications/com.system76.CosmicTerm.desktop"
install -Dm0644 "%{getenv:COSMIC_TERM_SOURCE}/res/com.system76.CosmicTerm.metainfo.xml" "%{buildroot}%{_datadir}/metainfo/com.system76.CosmicTerm.metainfo.xml"
install -Dm0644 "%{getenv:COSMIC_TERM_SOURCE}/LICENSE" "%{buildroot}%{_datadir}/licenses/cosmic-term/LICENSE"

# Install icons
for size in 16x16 24x24 32x32 48x48 64x64 128x128 256x256; do
    install -Dm0644 "%{getenv:COSMIC_TERM_SOURCE}/res/icons/hicolor/${size}/apps/com.system76.CosmicTerm.svg" \
        "%{buildroot}%{_datadir}/icons/hicolor/${size}/apps/com.system76.CosmicTerm.svg"
done

%files
%license %{_datadir}/licenses/cosmic-term/LICENSE
%{_bindir}/cosmic-term
%{_datadir}/applications/com.system76.CosmicTerm.desktop
%{_datadir}/metainfo/com.system76.CosmicTerm.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/com.system76.CosmicTerm.svg

%changelog
* Fri Jan 10 2026 Playtron <dev@playtron.one> - 0.1.0-1
- Initial RPM package with --maximize flag support
