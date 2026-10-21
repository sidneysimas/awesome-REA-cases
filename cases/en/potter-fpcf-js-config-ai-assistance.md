# Potter fire-alarm configuration: human fpcf recovery with AI-assisted browser checks, audio and ZIP handling

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-21
Stage: In progress

At 10:44 Beijing time on October 21, 2026, joe (mrjoebert) describes organizing Potter fire-alarm control-panel config-datetime.fpcf files. He first extracted plaintext location and serial-number information from the binaries and organized them by location with PHP, then investigated the format in JavaScript. He wants to integrate this into an existing PWA/ESP32 field tool so coworkers can back up and update using remotely queued files, reducing laptop trips.

He reports mostly parsing IPA, AFC and PFC configurations, including IPA/AFC voice evacuation. Dropping a file in a browser flags technically valid settings the official software may not warn about: sounder-base zones without their power circuit activating, PAD100-DIM dual inputs with identical functions causing ambiguous signals, conflicting floor descriptions between points and their first zone, notification circuits absent from drill zones, and apparent elevator-recall relays incorrectly included in drill zones. He finds it useful in hotels/apartments with hundreds of devices and reports under two seconds for 80 files in ZIPs and nested directories. That performance was not rerun here.

New conventional voice-system software zones, recent logic points and reference points remain incomplete; network checks are limited by missing reference support. He explicitly says AI struggled with fpcf reversing: humans inferred most of the format, while AI implemented observations, wrote WAV parsing and browser-preview audio conversion, handled ZIP processing and improved HTML/CSS. No repository, model, samples, detection accuracy or field-validation record is provided; REA is not stated. File checks are not fire-system safety certification or a replacement for on-site testing.

## Sources

- [joe's full Potter fpcf, browser-checking and AI-contribution account](https://x.com/i/status/2112736717727756546)

[中文](../potter-fpcf-js-config-ai-assistance.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
