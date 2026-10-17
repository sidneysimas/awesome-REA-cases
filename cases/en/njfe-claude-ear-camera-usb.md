# NJFE: Claude builds on prior protocol research to turn an ear camera into a PC inspection scope

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-17

The 08:29 Beijing-time candidate on October 17 opens a seven-build AI thread; a supplementary reply at 08:29:51 identifies NJFE, Not Just For Ears. A name search found WildweaselMS/NJFE. Reading its README and commit metadata showed implementation and English documentation already existed on October 10, before this window; these are supplementary sources, not newly collected candidate posts. An ESP32-C3 joins a Soulear ear camera's Wi-Fi, receives JPEG over i4season UDP and forwards it over USB serial to a Python PC interface for electronics and mechanical inspection, without the vendor phone app.

The project says research, protocol implementation, bridge firmware, PC tools, tests and documentation were developed in Claude Code conversations; the human supplied the idea, hardware, real-device testing and decisions. However, the README explicitly credits rbeilvert/otoscope's existing protocol implementation as the blueprint. The circulating shorthand about reversing the phone app must not become a claim that Claude independently discovered the protocol first. The project reports a single Hopefox Find T/HKV41B device, Windows testing, 480×480 JPEG at about 17 fps, and photos, recording, rotation and LED controls.

These are project reports, not execution by this collection: no dependencies were installed, bridge flashed or camera connected. The camera's Wi-Fi remains open and its protocol unauthenticated; bridge isolation does not remove nearby wireless access risk. Compatibility with other cameras is an expectation. The tool is not a medical device and its PC image should not be treated as diagnosis or treatment.

Project reports testing only one Hopefox Find T; no independent reproduction by this collection.
GPL-3.0-or-later; protocol implementation derives from GPL otoscope; REA use unconfirmed.

## Sources

- [In-window candidate: AI-build roundup opening](https://x.com/i/status/2111253121204994318)
- [Supplementary same-thread reply identifying NJFE](https://x.com/i/status/2111253320170164278)
- [NJFE README: Claude involvement, prior-work attribution and limits](https://github.com/WildweaselMS/NJFE)
- [October 10 documentation commit, predating the candidate window](https://github.com/WildweaselMS/NJFE/commit/992866c6609f8c813f459ff79840cf04d5883f8e)

[中文](../njfe-claude-ear-camera-usb.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
