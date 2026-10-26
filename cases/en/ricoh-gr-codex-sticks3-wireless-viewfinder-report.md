# Ricoh GR wireless viewfinder: Codex-assisted StickS3 firmware with generation-specific protocols

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-22
Stage: Needs verification

October 21–22, 2026 community posts describe a Codex-assisted Ricoh GR wireless viewfinder and shutter remote: a hot-shoe-mounted M5Stack StickS3, landscape preview, portrait Bluetooth shutter and M5Burner installation. One post says the developer gave real-device serial logs to Codex to diagnose reconnection. The purpose is a separate small-screen preview and camera remote, distinct from the Ricoh GXR color-recipe port idea. A reader's description of hot-shoe interface reversing does not establish that video travels through that interface.

Supplementary lookup on October 26 found sky18Dragon/RICOH-GR-Live-View-Shooting with matching characteristics and statically examined README at October 19 commit 8c4fc0f. The project credits collaboration between the author and Codex, identifies its M5Burner author as TinkerZhang, and supplies hot-shoe mounting parts. The documentation describes images traveling over Wi-Fi through HTTP MJPEG LiveView. GR III/IV use BLE for pairing, WLAN control and shutter release; the Bluetooth-free GR II requires manually enabled Wi-Fi and uses the official GR Remote HTTP interface. This is not a complete camera-firmware rewrite, and hot-shoe mounting must not be described as an image bus.

That commit's documentation reports real-camera validation for GR IIIx, GR IV, GR IV HDF and GR II. GR III still needs complete independent regression, while GR III HDF/IIIx HDF support is experimental without separate real-device evidence. It reports 93/93 Native tests passing, a successful StickS3 build, RAM usage of 66,444/327,680 bytes (20.3%) and Flash usage of 1,455,789/3,342,336 bytes (43.6%). Only the documentation was checked here; no tests, build, flashing or camera connection were performed. Automated tests do not replace regression on each model and firmware. The entry remains unverified, distinguishing community serial-debugging accounts, project-reported tests and this collection's static reading. The older commit is supplementary evidence, not a new release in the candidate window.

Public project and Codex collaboration statement located; static reading only, with per-model support and 93/93 tests attributed to the project.
GR II has no BLE and uses official HTTP interfaces; GR III/IV have a separate BLE control path. Hot-shoe mounting is not image transport.

## Sources

- [Reported Ricoh GR interface research, October 21, 2026](https://x.com/i/status/2112892660251795697)
- [Reported StickS3 and flashing method, October 22, 2026](https://x.com/i/status/2113242014242287678)
- [Reported Wi-Fi/Bluetooth and serial-log debugging workflow, October 21, 2026](https://x.com/i/status/2112738503222349881)
- [README at an October 19 commit: Codex attribution, transport and test scope; read on October 26](https://github.com/sky18Dragon/RICOH-GR-Live-View-Shooting/blob/8c4fc0f768b8a14369b9b2a426d90177d7405efb/README.md)

[中文](../ricoh-gr-codex-sticks3-wireless-viewfinder-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
