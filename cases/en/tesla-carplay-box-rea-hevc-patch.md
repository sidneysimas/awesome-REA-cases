# Tesla CarPlay box: a reported JPEG-to-HEVC firmware patch using Claude, Codex and REA

Category: Hardware and interoperability · REA
Record date: 2026-10-24
Stage: Needs verification

At 21:37:14 Beijing time on October 23, 2026, vibelatte says Claude, Codex and REA analyzed and patched his Tesla CarPlay box firmware, which he had not previously investigated. The reported bottleneck was a blurry, compressed JPEG path at 30 fps. The replacement reportedly accepts native HEVC directly from the phone at full resolution, about 60 fps and 2 ms decode time.

The author says the work is fully open source and installable through the box's web UI; a reply supplies only a short link. This review checked the thread but did not obtain a fixed, inspectable patch repository, device model, firmware version, frame-time measurements or latency definition. The 2 ms figure is therefore only reported decode time, not end-to-end latency. Compatibility with every Tesla, CarPlay box or firmware is not inferred. No firmware was installed or executed, nor image quality or frame rate independently tested. This is an unverified modification report with a specific use case.

Source: October 23, 2026, 21:37:14 Beijing time; supplementary reply at 21:37:44.
30 fps, about 60 fps and 2 ms are author reports, not independent measurements; 2 ms is not full-path latency.

## Sources

- [vibelatte original: CarPlay box HEVC firmware modification, October 23, 2026](https://x.com/i/status/2113625799744016497)
- [Same-author supplementary link reply, October 23, 2026](https://x.com/i/status/2113625923589214307)

[中文](../tesla-carplay-box-rea-hevc-patch.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
