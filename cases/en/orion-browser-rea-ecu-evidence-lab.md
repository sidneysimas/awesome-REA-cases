# Orion's browser lab: REA, Ghidra and Claude explain an ECU function with content-linked evidence

Category: Hardware and interoperability · REA
Record date: 2026-10-23
Stage: Needs verification

At 00:20:00 Beijing time on October 23, 2026, Orion (@0xOrionVega) says he built a four-device reverse-engineering lab that runs in a browser without installation. An automotive ECU is an electronic control unit. His example follows a firmware function named read_rpm: give a binary to REA, inspect vehicle and ECU structure, decompile with Ghidra, then ask Claude for a plain-language explanation. The aim is to expose the material behind an explanation rather than simply accept a model's conclusion.

He says every answer has an evidence record, expressed as evidence_id = hash(content), with the identifier changing when the material changes. Content binding can help identify cited material, but a hash alone cannot establish that Claude's interpretation is correct, the firmware came from a real vehicle, or the behavior was tested. The post supplies no vehicle or ECU model, firmware version, actual decompiled excerpt, hash algorithm or inspectable tests.

A supplementary thread reply at 00:20:01 supplies a shortened lab link and suggests choosing Tour and then an item. At 00:31:14 the author explicitly says he has not tried a router, so expected ARM support is not treated as a tested device. These replies provide context, not additional candidates. A video is attached but was not verified by playback here. This collection operated no device, executed no target code and submitted no data to the lab. It remains an unverified demonstration project, not evidence of understanding arbitrary cars or an independent reproduction.

Candidate originally posted 2026-10-23T00:20:00+08:00; supplementary replies at 00:20:01 and 00:31:14 the same day. Four devices and zero installation are author claims, not independently validated.

## Sources

- [Orion: four-device browser lab and ECU evidence-hash workflow](https://x.com/i/status/2113304372905955722)
- [Supplementary author reply: lab entry and Tour](https://x.com/i/status/2113304375896440975)
- [Supplementary author reply: routers not yet tested](https://x.com/i/status/2113307199443243181)

[中文](../orion-browser-rea-ecu-evidence-lab.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
