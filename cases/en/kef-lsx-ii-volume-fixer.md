# KEF LSX II: finer Mac volume control

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-15

KEF LSX II are desktop wireless speakers. Frustrated by roughly six Mac USB volume steps of 6 dB each, the author says Claude helped create LSX II Volume Fixer: a virtual audio output passes samples unchanged to USB, while volume keys control the speakers' existing LAN volume interface from 0 to 100 rather than modifying signed firmware. The author reports 192 kHz audio, about 2 ms of added latency and 16 default steps spaced 3.4 dB apart, and measured the volume curve, claiming manufacturer-table deviations of up to 20 dB at the low end. The public repository was checked on October 15; documentation explains driver and network-control design. Measurements and compatibility remain project reports; this collection did not run the driver. Only Mac and LSX II were tested by the author; Windows is merely a possible direction in the documentation.

Candidate snapshot: 0 likes | 18 views; performance is author-measured, not independently reproduced.

## Sources

- [Author report](https://x.com/i/status/2110581933533184501)
- [Public implementation and measurement notes](https://github.com/roberdorfer/kef-lsx-volume)

[中文](../kef-lsx-ii-volume-fixer.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
