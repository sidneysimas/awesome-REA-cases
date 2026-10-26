# A7C II Tools 3.0: AI reversing reports and the limits of QAQLeonard's single-camera verification

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-26
Stage: Needs verification

A candidate published at 15:09 Beijing time on October 26, 2026 says developers used AI to study Sony A7C II firmware and enable FL2/FL3 and custom LUTs, seeking newer image looks without replacing the camera. A 15:41 candidate identifies QAQLeonard, A7C II Tools 3.0 and firmware 2.01, warning about third-party battery recognition, boot and warranty risks. Both concern one camera-tool effort, not separate cases for each feature. AI participation remains attributed to secondhand reports: no original developer disclosure of the model, reversing steps or scope of AI contributions was obtained, and REA is not explicitly named.

Searching the precise tool name and author identified QAQLeonard/a7c2-fl23-research. Static README reading corresponds to commit ef7db116e13e37be91e9af20360dc9bba8d64a9b, dated October 25 at 19:23:19 Beijing time, used as supplementary project documentation predating the candidates. It supports only the A7C II (ILCE-7CM2) on firmware 2.01 and refuses other models. Version 3.0 introduces a proper GUI and modifies programs and settings in the camera firmware. The README describes FL2/FL3, custom Creative Looks, offline DCP/CUBE conversion to .a7look, 15 paired DCP/A7Look profiles (11 Fujifilm and 4 Ricoh) and an optional Lightroom RAW-profile plugin that does not alter RAW data. This is not arbitrary Log LUT execution in the camera: CUBE input must be Sony ST/sRGB, S-Log3 cannot be used directly, and built-in colors are fitted approximations, not guaranteed exact matches to the source DCPs.

The project verification table reports writing, readback and post-restart checks for FL2/FL3, six-look installation and restoration on the author's single Windows/A7C II setup; custom-look previews/photos and temporary sound audition were tested on the same camera. Persistent custom shutter sound has offline and packaged self-tests only, with long-term camera testing ongoing. Vertical Display including menu frames is being rewritten with camera acceptance pending; macOS packages build but real USB operation is unverified. These features are not collectively described as complete or supported on every platform, and this collection has not independently run tests or examined sample photos.

The README credits prior A7CR/A7R V ports, Sony-PMCA-RE and other research rather than independently discovering every protocol. Current original project code uses PolyForm Noncommercial 1.0.0; third-party material and older versions have separate terms, so this is not broadly called MIT open source. The documentation explicitly says successful writes and identical readback do not establish boot safety. Boot failure, reboot loops, data loss and effects on updates, warranty and repairs remain possible, with no guaranteed recovery. Third-party battery effects are mentioned only by the candidate and are unverified here. The baseline original Sony alpha7 idea is a different model and retains its own ID. No firmware was downloaded, dependencies installed, camera connected or flashing performed. This remains unverified with clear AI-attribution and independent-reproduction limits.

AI reversing attribution comes from candidate reports; the model and contribution scope remain unconfirmed. The project reports verification on one Windows/A7C II/2.01 setup only; no independent flashing was done.
macOS USB is unverified, long-term persistent shutter-sound tests are ongoing and portrait-menu rewriting awaits acceptance. Colors are fitted approximations; readback does not guarantee boot or recovery.

## Sources

- [Candidate report of AI firmware research, FL2/FL3 and LUTs on the A7C II, October 26, 2026](https://x.com/i/status/2114615282480423016)
- [Candidate adds QAQLeonard, version 3.0, firmware 2.01 and risks, October 26, 2026](https://x.com/i/status/2114623475587698902)
- [Supplementary project README at pinned commit ef7db116, October 25, 2026 at 19:23:19 Beijing time](https://github.com/QAQLeonard/a7c2-fl23-research/blob/ef7db116e13e37be91e9af20360dc9bba8d64a9b/README.md)

[中文](../sony-a7cii-ai-fl2-fl3-lut-firmware-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
