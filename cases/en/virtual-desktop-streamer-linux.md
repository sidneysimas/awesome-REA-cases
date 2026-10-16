# Virtual Desktop Streamer: a Linux platform-layer port

Category: Applications and clients · REA
Record date: 2026-10-13
Stage: In progress

Reading cudanexus's six-post thread established the target: bringing Virtual Desktop Streamer's desktop, audio and input streaming to Linux. The author says the Windows installer route was blocked by .NET Framework/drivers, so they studied the macOS .NET 8 version, located platform calls and replaced them with PipeWire/X11, GStreamer, PulseAudio and uinput. The public vd-streamer-linux README explicitly credits Claude Code and REA and reuses official macOS protocol libraries, rather than recovering all source from scratch. Users must obtain the official libraries themselves; packages containing them cannot be redistributed. The thread also reports fixes for accumulating latency, scrolling and network switching following Ubuntu use. The project does not support the SteamVR/OpenXR games available in the Windows version. Although the thread describes feedback as 'real use,' the README's 'Not verified yet' section explicitly says all tests used simulated headsets, without a real headset, Wi-Fi or GPU encoder, and Ubuntu testing occurred in a container. The scrolling fix was not directly observed delivering events to an X11 app either. This review did not build it or independently verify interoperability.

Posted: 2026-10-13T06:06:16+08:00 (Beijing time)
Evidence boundary: in progress; not independently run or verified
The thread's 'real use' does not establish physical-device acceptance: the repository explicitly describes only simulated-headset/container tests.

## Sources

- [Original post from this window (author report)](https://x.com/i/status/2109767636452265990)
- [Public project README](https://github.com/cudanexus/vd-streamer-linux)

[中文](../virtual-desktop-streamer-linux.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
