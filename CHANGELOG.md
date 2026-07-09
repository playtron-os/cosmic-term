## [1.2.4](https://github.com/playtron-os/cosmic-term/compare/v1.2.3...v1.2.4) (2026-07-09)


### Bug Fixes

* address issues with color mode setting ([121596c](https://github.com/playtron-os/cosmic-term/commit/121596c72a2c407494cb76c60412a49d55755ebd))

## [1.2.3](https://github.com/playtron-os/cosmic-term/compare/v1.2.2...v1.2.3) (2026-07-02)


### Bug Fixes

* update app icon ([9fecc77](https://github.com/playtron-os/cosmic-term/commit/9fecc770ee1a2e6771c5d7632ca475ea9c3a1682))

## [1.2.2](https://github.com/playtron-os/cosmic-term/compare/v1.2.1...v1.2.2) (2026-06-29)


### Bug Fixes

* lighten requirements on rpm spec ([4c9d9cf](https://github.com/playtron-os/cosmic-term/commit/4c9d9cf01018a50c9e77b14af5952464cdbe5e8f))

## [1.2.1](https://github.com/playtron-os/cosmic-term/compare/v1.2.0...v1.2.1) (2026-06-26)


### Bug Fixes

* make release CI pass ([f913c2a](https://github.com/playtron-os/cosmic-term/commit/f913c2a99beff4f7313fa870d8d78c6bfa70e1a7))

# [1.2.0](https://github.com/playtron-os/cosmic-term/compare/v1.1.3...v1.2.0) (2026-06-25)


### Bug Fixes

* avoid re-reading system theme from disk on every menu bar render ([18b4450](https://github.com/playtron-os/cosmic-term/commit/18b4450c0f3fbe3a35ca7ad3230cda7e7091712e))
* avoid unnecessary shape-until-cursor at start-up ([6793881](https://github.com/playtron-os/cosmic-term/commit/67938814b6c46d3a6b871d154891747b3f949cb0))
* change zoom reset scope to active tab ([f689040](https://github.com/playtron-os/cosmic-term/commit/f689040c9c74944ac54c00a58ee76846baa1cff8))
* clippy lint ([d413fdb](https://github.com/playtron-os/cosmic-term/commit/d413fdb593cd2e3bb26c6177a944e7a4c26fcea8))
* context menu by disabling IME when the widget has context menu ([1963929](https://github.com/playtron-os/cosmic-term/commit/1963929e052a84e3812f7ea5bbcea8faeace6e89))
* dismiss context menu when clicking in any pane ([133c526](https://github.com/playtron-os/cosmic-term/commit/133c526acd12e50f4ff53228986c7011f931455f))
* do not drop scrolling events from smooth scrolling mice ([124931f](https://github.com/playtron-os/cosmic-term/commit/124931faff8e136f5f639229e8af62063ed09e40))
* don't capture all mouse events ([e37f73d](https://github.com/playtron-os/cosmic-term/commit/e37f73dcbb75cdf282981580c8d006177d6cdb2a))
* fix the one pixel wide gap between panes ([8ae5918](https://github.com/playtron-os/cosmic-term/commit/8ae5918ccd15844a822eb63c091625b8ac798b2b))
* gate wayland features and add inline popover fallback ([8b95675](https://github.com/playtron-os/cosmic-term/commit/8b95675c9b6ffe0eb28910c097c129af4b1689e1))
* increase menu width to prevent cutting off toggle maximized ([260bb79](https://github.com/playtron-os/cosmic-term/commit/260bb7972861612f62486154c1d82d8e904890ca))
* keep the url in state for menu actions and underline ([1d86974](https://github.com/playtron-os/cosmic-term/commit/1d869746827c877ac665b7ceba7f93db9719596a))
* libcosmic updates ([512cc0d](https://github.com/playtron-os/cosmic-term/commit/512cc0d2509e59c4d961c0194741eddbb74193ee))
* **libcosmic:** fix item highlight in wayland context menu ([f5cbed0](https://github.com/playtron-os/cosmic-term/commit/f5cbed08d68c60874923797733c768f5b1ab8bc3))
* menu doesn't show by unfocusing when clicking outside of the terminal_box ([c22d1cc](https://github.com/playtron-os/cosmic-term/commit/c22d1ccc28b6e9ecc68f688e311abefedab7352f))
* **menu:** icetron context-menu styling + smaller toggle ([7bf3435](https://github.com/playtron-os/cosmic-term/commit/7bf34351c2ed6b660385ca474f8f4e9eed99f9b3))
* merge profile and startup options ([75cfa52](https://github.com/playtron-os/cosmic-term/commit/75cfa526730dddb361161e724fdc8e2db67208e3))
* only send "space" to the focused pane ([1428345](https://github.com/playtron-os/cosmic-term/commit/1428345cad272f4fd2a7c52cc434ecc8d10546c3))
* prevent crash when splits are resized too small ([9ed56eb](https://github.com/playtron-os/cosmic-term/commit/9ed56eb2db29e6d31948f1b1c908acbb44972a30))
* send the correct up/down code in APP_CURSOR mode ([02d977a](https://github.com/playtron-os/cosmic-term/commit/02d977ac4d1127174f4c77b25bfada14edcce3aa))
* **style:** add the background color to that tab bar ([8203b1e](https://github.com/playtron-os/cosmic-term/commit/8203b1e23322eda28432c2154e2c57a7eef53f87))
* **theme:** respect light mode in context-menu chrome ([f404ecc](https://github.com/playtron-os/cosmic-term/commit/f404ecc8799a2060baad791203c919931b0d08ed))
* use window-absolute coordinates for context menu position in split panes ([0b1490e](https://github.com/playtron-os/cosmic-term/commit/0b1490e7ffae687ea29a1cd2c45d9051c3833a28))


### Features

* add `--working-directory` arg ([5fedabd](https://github.com/playtron-os/cosmic-term/commit/5fedabd9f59d1d3825ee597d378d9f2fc20f210a))
* Convert context menu from widget::popover to Wayland popup surface ([0575680](https://github.com/playtron-os/cosmic-term/commit/057568086009c6971933fc11899e7cf6a833ce0c))
* option to open new windows in the current directory ([91fd140](https://github.com/playtron-os/cosmic-term/commit/91fd140ae371498bd2cd3fa86e5a9acd02a02f16))
* rebase libcosmic onto iced 0.14 ([f62abce](https://github.com/playtron-os/cosmic-term/commit/f62abcea4efbcd824297b269279826699c47d335))
* tab dnd ([54b9974](https://github.com/playtron-os/cosmic-term/commit/54b99741e8911e382b4e5e7ae22709319b928310))

## [1.1.3](https://github.com/playtron-os/cosmic-term/compare/v1.1.2...v1.1.3) (2026-06-02)


### Bug Fixes

* update dependencies ([ba1c6bb](https://github.com/playtron-os/cosmic-term/commit/ba1c6bb10f57d77732653b682b7c8201f7c18139))

## [1.1.2](https://github.com/playtron-os/cosmic-term/compare/v1.1.1...v1.1.2) (2026-04-24)


### Bug Fixes

* update libcosmic ([9c441b7](https://github.com/playtron-os/cosmic-term/commit/9c441b734498b204a0c9f95d8b0ef5756c6785c6))

## [1.1.1](https://github.com/playtron-os/cosmic-term/compare/v1.1.0...v1.1.1) (2026-04-09)


### Bug Fixes

* update app icon ([6920ca8](https://github.com/playtron-os/cosmic-term/commit/6920ca844df2e57ae68b4702bfed6e76ee2b415d))

# [1.1.0](https://github.com/playtron-os/cosmic-term/compare/v1.0.1...v1.1.0) (2026-03-27)


### Features

* remove cosmic from app name ([8bc5d3e](https://github.com/playtron-os/cosmic-term/commit/8bc5d3ebf0c6b74443ec57f58fd418721a07ea63))
* use playtronos libcosmic and replace cosmic-files for xdg file picker ([a9e2a32](https://github.com/playtron-os/cosmic-term/commit/a9e2a327b620eb2b18fa7ca0bcecb25b21aacc36))

## [1.0.1](https://github.com/playtron-os/cosmic-term/compare/v1.0.0...v1.0.1) (2026-02-04)


### Bug Fixes

* add missing release CI permission for PR/issues ([094794d](https://github.com/playtron-os/cosmic-term/commit/094794db9ddd2d9c474ac6d0c6c02ef936f81b8f))

# 1.0.0 (2026-02-04)


### Bug Fixes

* add dep to debian control ([63b807a](https://github.com/playtron-os/cosmic-term/commit/63b807a44397335b0df2440826be35ef6edede01))
* center go-up and go-down icons ([6d63530](https://github.com/playtron-os/cosmic-term/commit/6d635305adb635d958af7c018aa269427454ff46))
* **context menu:** use radius from theme ([a432f71](https://github.com/playtron-os/cosmic-term/commit/a432f714debf5e4ab30e198121d7dac800447b15))
* dead keys support ([aa1824d](https://github.com/playtron-os/cosmic-term/commit/aa1824d3096fda2dfbe47837a476949b66314d6f))
* disable terminal box when context page is active ([56f1ea3](https://github.com/playtron-os/cosmic-term/commit/56f1ea3eed64b2a900dd8d0db74a7e1771945bbc))
* downgrade `home` to 0.5.9 to fix build ([8b4f2a8](https://github.com/playtron-os/cosmic-term/commit/8b4f2a8d36197bd631bec8c07e2151cfb5ddea52))
* downgrade `home` to 0.5.9 to fix build ([0cc5c3d](https://github.com/playtron-os/cosmic-term/commit/0cc5c3d0d2b79e3e8f52777ab3b2d2caa2b9d797))
* downgrade home@0.5.11 to 0.5.9 for Rust 1.80 ([0c60100](https://github.com/playtron-os/cosmic-term/commit/0c601005c8cf6e0700c14f873f5a9d684fdadcd3))
* **header:** fixed new tab button padding ([98df257](https://github.com/playtron-os/cosmic-term/commit/98df25736a6520816c77b3f11da0a5e564063bee))
* hide cursor when scrolled in unfocused terminal ([1db6692](https://github.com/playtron-os/cosmic-term/commit/1db66929259674c4f141d9b2fdb655aeb52699ae))
* hoverable paginated tab buttons, and alignment fix ([39ac4ae](https://github.com/playtron-os/cosmic-term/commit/39ac4ae05c404ec4634fe0cd000521ee8beacaa8))
* improve font rendering on light theme w/ iced web-colors feature ([#147](https://github.com/playtron-os/cosmic-term/issues/147)) ([c500ef8](https://github.com/playtron-os/cosmic-term/commit/c500ef814ca79e65247134c8323533d20db48802))
* in CI upload rpms and add concurrency config ([edd6040](https://github.com/playtron-os/cosmic-term/commit/edd6040e7193e48daef48261e0b012f9dccfa2ae))
* **input:** update libcosmic ([6330ceb](https://github.com/playtron-os/cosmic-term/commit/6330ceb75640ab81110c5434674f5302f5cf11ae))
* keep shell program opt when checking ([69c5dff](https://github.com/playtron-os/cosmic-term/commit/69c5dff3bbd39b10f31d4ce7deff867db3bc8068))
* Launch with invalid default profile fails ([397b527](https://github.com/playtron-os/cosmic-term/commit/397b527fbd64e65fc0c1676ef2bab41ff2e1581f)), closes [#274](https://github.com/playtron-os/cosmic-term/issues/274)
* **libcosmic:** add x11 wgpu device detection to fix crash on NVIDIA desktops ([0f0601b](https://github.com/playtron-os/cosmic-term/commit/0f0601b3e52e560b35577337f58ff416d30153a2))
* **libcosmic:** double-click to maximize ([ed002ae](https://github.com/playtron-os/cosmic-term/commit/ed002ae57d234c01033861f31d34ef5763410bb8))
* **libcosmic:** input focus lost on click of header bar ([0652001](https://github.com/playtron-os/cosmic-term/commit/06520014ec94914ebdf43b113f28ecf0d617c420))
* **libcosmic:** theme subscription ([d8c417f](https://github.com/playtron-os/cosmic-term/commit/d8c417fcce5b2bd2427f8dd5dbc22336eabd7a54))
* next tab button misalignment in split panes ([7b5c128](https://github.com/playtron-os/cosmic-term/commit/7b5c128f55a98f49b75bab5ed2648aae2179aacd))
* opacity ([e40b955](https://github.com/playtron-os/cosmic-term/commit/e40b955f33a8537d4c9e7155b217ca9ab7ddf9e5))
* pin cosmic-text to `b017d7c` to fix cut text ([0b97944](https://github.com/playtron-os/cosmic-term/commit/0b9794414c4c12228405fbb2633e2626112763bc))
* text input copy paste ([06fcae2](https://github.com/playtron-os/cosmic-term/commit/06fcae2c705d436a8d90f6abd0c4538c7e56fb4f))
* update deps ([e6aecbe](https://github.com/playtron-os/cosmic-term/commit/e6aecbe8405de95af0710b0b6769d88c88628009))
* update libcosmic and use load configured theme instead of defaults ([61a5960](https://github.com/playtron-os/cosmic-term/commit/61a5960c706db4272fa182e382bd95ba7dd40475))
* use sed in CI version replacement and exit early if no release generated ([70b8e5e](https://github.com/playtron-os/cosmic-term/commit/70b8e5eaba7ec15929ccfd15c60405d7e444c6e3))
* **window:** round corners based on header ([20d5290](https://github.com/playtron-os/cosmic-term/commit/20d5290145553fbc0adaef203b14eb6436398525))


### Features

* add support for --no-headerbar flag ([6ed69bc](https://github.com/playtron-os/cosmic-term/commit/6ed69bc498ceb03b1703db90ead283cd4a4587c6))
* bind copy/paste keycodes to copy/paste actions. ([aa9d693](https://github.com/playtron-os/cosmic-term/commit/aa9d693dade93970308a43069269707b0c1c7bdb))
* **color-schemes:** add Seashells color-scheme ([be8309f](https://github.com/playtron-os/cosmic-term/commit/be8309fea5812bed291b6783521f0c8bfe38a5d5))
* implemnt --maximize flag and add rpm packaging script ([abdb289](https://github.com/playtron-os/cosmic-term/commit/abdb289d2bb9ee5c4d1a78f09e80f05b17377f18))
* menubar popups ([cce8f8c](https://github.com/playtron-os/cosmic-term/commit/cce8f8c3eaf5987cf2ae174c0d46254c58f2498f))
* responsive menu bar ([97f8780](https://github.com/playtron-os/cosmic-term/commit/97f87809b99a8545022a97672d5e71bcb99b27c9))
* tab pagination and text overlap fix ([41e95fc](https://github.com/playtron-os/cosmic-term/commit/41e95fc188cbd7862dca0f11405f7ff38cf633d2))


### Performance Improvements

* update libcosmic to improve window resize performance ([a2e3617](https://github.com/playtron-os/cosmic-term/commit/a2e3617fe45e92d0eb9a14ca3c34842d333cfec4))
