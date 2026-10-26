# A treadmill with broken buttons: ShaneX reports AI-assisted Nautilus Bluetooth research and an ESP32 phone-control bridge

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-25
Stage: Needs verification

At 00:35:36 Beijing time on October 25, 2026, ShaneX (@purgane) describes a treadmill whose button pad had been broken for a year, possibly because of a ribbon cable. Instead of replacing parts, he reports working with OpenClaw, a multimeter and a Pi to access the main chip's firmware and investigate another control path. Rereading the original confirmed the author and full text. The Nautilus channel name is not treated as a confirmed treadmill brand or model.

The author describes two Bluetooth connections: one provides read-only app telemetry without commanding the main chip, while a second Nautilus channel communicates with it. They focus on the latter and build an ESP32 bridge that connects to the treadmill over Bluetooth and hosts a local web app. A phone on the same local network can reportedly control it. He reports four days of safety refusals from Claude and ChatGPT and repeated firmware flashing before phone control worked. Four days describes his process, not independently measured labor or a model-speed comparison. Internal use of the second channel is his speculation, not a confirmed fact.

No model, firmware version, protocol records, source, controllable parameter list, complete tests or emergency-stop behavior are supplied. The post attaches a video, which this collection did not watch, and no device was operated. Safe speed/incline control, preservation of all safety interlocks, compatibility with other models and discovery of a new vulnerability are not established. REA is not mentioned. This unverified entry preserves the specific repair purpose and author-reported result; no device was connected, firmware executed or dependencies installed.

Candidate at 00:35:36 Beijing time. Four days, repeated flashing, two Bluetooth channels and successful control are author statements.
Model, code, protocol and motion-equipment safety tests are not supplied; the video was not watched and the treadmill was not operated here.

## Sources

- [ShaneX: AI-assisted treadmill Bluetooth research and an ESP32 local control web app, October 25, 2026 Beijing time](https://x.com/i/status/2114033074212073559)

[中文](../purgane-treadmill-nautilus-esp32-control.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
