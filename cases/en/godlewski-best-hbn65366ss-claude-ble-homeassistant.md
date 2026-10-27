# BEST HBN65366SS hood: Claude-assisted BLE tracing corrects a GATT-cache mistake for Home Assistant

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-27
Stage: In progress

At 02:50:08 Beijing time on October 27, 2026, Steve Godlewski (@stevegodlewski) reports using AI to research a BEST hood and connect it to Home Assistant. His thread credits prior work and says findings were sent upstream. The public godlewski/esphome-best-hood-hbn65366ss README explicitly describes researching, writing configuration and documenting together with Claude Code, testing each step on his own hood. Supplementary code and logs describe October 24-25 research, not newly collected posts in this run.

The target is a Best by Broan HBN65366SS, firmware 4.2.2 / 1.1.20, with an ESP-WROOM-32 running ESPHome for local BLE control instead of the vendor cloud route. It reuses WheapLabs' wake advertisement and encrypted pairing without bonding; these earlier discoveries are not credited as new. The ESP32 initially could not see light-level and delay-off characteristics, leading to an incorrect conclusion that the model lacked them. Static string searches of the BEST Kitchen Android app's Hermes bundle did not complete decompiled mappings. An Android 12 phone with network access disabled and exclusive device access then captured Bluetooth HCI; ATT parsing revealed 54 characteristics and app writes to 21026/21050. ESP-IDF cached only 40 by default. Setting CONFIG_BT_GATTC_MAX_CACHE_CHAR to 100 exposed the missing characteristics, and the log explicitly preserves and corrects the earlier mistake.

The project reports four fan speeds, four light levels, SmartSense, delay-off and two-way synchronization with physical buttons. Writing 0 to 21050 stops the fan immediately rather than cancelling the timer while leaving it running; natural delayed-stop duration still needs checking. Only one HBN65366SS was tested. While the ESP32 holds BLE, the phone app uses the cloud, not a simultaneous second BLE link. The original capture is withheld because it contains a network name; a parser and redacted logs are public, not independent reproduction.

Supplementary lookup confirms godlewski's cache fix in WheapLabs PR #5 was merged at 00:53:33 UTC on October 25. The PR reports ESPHome 2026.10.0 config validation and operation on his hood, without testing the unmodified files on HBN1306SS/WCS1306SS. README and logs are traceable to commit 28e1e1d772c55d9f94bb485854cb75e9608c2b0e. No configuration, capture or device was run here. REA is not mentioned. Retained as an in-progress, author-tested implementation, not general safety certification.

Candidate snapshot: 4 likes, 101 views, 0 reposts. Supplementary GitHub material predates this window.
54 is this device's characteristic count, 40 the default cache limit and 100 the corrected setting, not 100 features or tested devices.

## Sources

- [Current candidate: Steve reports BEST/Home Assistant integration, October 27 Beijing time](https://x.com/i/status/2114791707011379640)
- [Supplementary author thread: credits prior work and upstream contribution, October 27 Beijing time](https://x.com/i/status/2114791712199729238)
- [Supplementary public README: Claude participation and one-device limits, October 24 commit](https://github.com/godlewski/esphome-best-hood-hbn65366ss/blob/28e1e1d772c55d9f94bb485854cb75e9608c2b0e/README.md)
- [Supplementary build log: GATT mistake, HCI capture and correction, October 24](https://github.com/godlewski/esphome-best-hood-hbn65366ss/blob/28e1e1d772c55d9f94bb485854cb75e9608c2b0e/docs/LOG.md)
- [Supplementary upstream PR #5: cache fix and project tests, merged October 25](https://github.com/WheapLabs/ESPHome-Best-Hood/pull/5)

[中文](../godlewski-best-hbn65366ss-claude-ble-homeassistant.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
