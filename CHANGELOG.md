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
