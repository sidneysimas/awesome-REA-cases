# Plustek 8200i / ThinkPad MIPI: improve Linux drivers using Windows reference behavior

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-16
Stage: In progress

Christian F. K. Schaller bought a Plustek OpticFilm 8200i to scan family negatives, then found that the newer batch used a Genesys GL128 controller (USB 07b3:1825), unlike the already-supported GL845 model. Initial Claude research stalled for a long time. After adopting Windows-VM control and host-side usbmon capture, he reports a recognizable first scan within hours and infrared scanning a few days later. His SANE backend lists color, gray, infrared and color-plus-infrared modes, 300–7200 dpi, 8 or 16 bits per channel, infrared dust removal and an exposure multiplier; he tested mainly with his Negative Vibes app. Upstream SANE independently added support in September 2026, so the original support gap must not be described as still current. His single-device, single-frame comparison reports 34.6 versus 54.4 seconds at full resolution, while upstream offers more resolution steps. He presents his backend as a proof of concept and expects to switch to upstream once it reaches feature parity.

He then used Claude to investigate the Sony IMX471 / Intel IPU7 MIPI camera in a ThinkPad X1 Carbon Gen 14 Aura Edition. With no equivalent USB bus to capture, evidence came mainly from Windows INF files, registry, ACPI and configuration data, with a USB webcam as an image reference. The public page documents five defects: kernel crop-rectangle handling, test-pattern register width and analogue-gain limits, plus missing lens-shading correction and black-level bit-depth handling in libcamera white balance. Color and shading data came from studying the layout of CPFF configuration containers in the Windows driver package. His controlled low-light test raises brightness from 31.1 to 90.9, but blue remains about 17% short, the exposure/frame-rate tradeoff is unfixed, no color-chart validation was performed, and testing covers one room and the GPU processing path only. His October 15 article says kernel patches were sent to Kate Hsuan and libcamera patches were being reviewed by Wim Taymans for submission; upstream merging is not confirmed.

Two October 16 candidate reports led to supplemental reading of the October 15 original article, hw-harness README and camera-measurement page. An older October 15 Phoronix candidate was also resolved separately. hw-harness generalizes bespoke scripts after the investigations; the author explicitly says he did not use the current generic form for the original work. All hardware outcomes remain author and project reports, not device tests by this collection. No evidence of REA use was found.

October 16 candidate snapshots: long post 4 likes, 493 views; Joshua_WD post 4 likes, 134 views.
Supplementary-source dates: the original article and Phoronix news are October 15; project pages were read this round, not independently reproduced.

## Sources

- [Current-window long report on the scanner and MIPI camera](https://x.com/i/status/2110852184988385570)
- [Joshua_WD's report on known-good-reference comparison](https://x.com/i/status/2110869080555082144)
- [Previously unresolved Phoronix post](https://x.com/i/status/2110740084387672274)
- [Schaller's October 15 original article](https://blogs.gnome.org/uraeus/2026/10/15/aiandreverseengineerhardware/)
- [Phoronix's October 15 news article](https://www.phoronix.com/news/AI-Reverse-Engineer-Linux-HW)
- [hw-harness project and observational boundaries](https://github.com/cschalle/hw-harness)
- [Five MIPI fixes, measurements and unresolved issues](https://cschalle.github.io/mipi-fixes-x1-aura/)

[中文](../schaller-opticfilm-thinkpad-linux.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
