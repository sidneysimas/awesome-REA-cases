# Hasselblad X2D series: Codex-assisted CIM research, Doom and bounded autofocus extensions

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-29
Stage: In progress

At 10:31:00 Beijing time on October 29, 2026, hongseyanqiu relays Radium Wang (@iamRadiumWang) using Codex to analyze Hasselblad CIM firmware and explore X2D-series extensions. The post describes Doom on the first-generation X2D 100C, connecting an ARM64 engine, C and Qt/QML to rendering, touch, shutter-triggered firing and audio. It also claims X2D II demonstrations of CarPlay and GPT-controlled focus/shutter, plus investigation of retained first-generation continuous-focus, face/eye and three-speed paths. Demonstrations and AI attribution are secondhand, not device observations by this collection.

Supplementary reading of README at commit 3dd59bbe1643397eede926b034c75df795f71006 in radium-wang/Hasselblad-X-System-CIM-Firmware-Research-Feature-Extensions identifies a document dated October 28 at 09:21:18 Beijing time, before the candidate. It explicitly reports limited first-generation device feedback for Doom's engine, shutter, audio and swipe controls, while the public tree has no deployment backend. Reaching stock AF-C state is not autofocus-performance acceptance. AFT/eye coexistence and the three-speed selector have separate, bounded feedback; multipliers are not end-to-end speed gains. A temporary parameter change from 80 to 100 reduced hunting but caused frequent false focus and was retired.

The same README marks second-generation LiDAR/AF paths and 39 still-encrypted models as offline research without second-generation hardware acceptance. No independent CarPlay/GPT validation was found; first-generation evidence cannot certify second-generation demonstrations. It also separates pixel-shift capture, offline processing and unquantified optical benefit, and records three UI-response trials failing to confirm improvement before stock restoration. Public source, tests and sanitized findings exclude vendor firmware, models, libraries and deployment backends. The experimental Mac/Windows one-click toolkit is a separate repository; its first-generation firmware-4.2.0 scope must not be generalized.

The project credits prior x2d-cim-notes and derrickyau9's extraction research. Most original code is MIT, with GPL-2.0-or-later for Doom and GPL-3.0-or-later for Shimeji; none grants rights to vendor material. This collection statically read the README only, without running its offline suite, installing tools, flashing a camera or measuring optical results. Included as in-progress firmware research, with REA unspecified and no claim that all hidden features are unlocked or modifications are safe.

Candidate snapshot: 0 likes, 45 views, 0 reposts. The supplementary repository commit is from October 28, not a new candidate in this window.
AI use and second-generation CarPlay/GPT are secondhand. The pinned README supports limited first-generation feedback, not complete-feature, all-model or safety validation.

## Sources

- [hongseyanqiu relays Radium Wang's Codex/Hasselblad research, October 29, 2026](https://x.com/i/status/2115632462437171618)
- [Supplementary pinned October 28 README: hardware, offline and unverified boundaries](https://github.com/radium-wang/Hasselblad-X-System-CIM-Firmware-Research-Feature-Extensions/blob/3dd59bbe1643397eede926b034c75df795f71006/README.md)

[中文](../radium-hasselblad-cim-codex-feature-research.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
