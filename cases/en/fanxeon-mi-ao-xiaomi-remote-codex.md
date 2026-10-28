# MI-AO: Codex-assisted BLE remote research turns push-to-talk into Mac task input

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-28
Stage: In progress

The candidate at 18:29 Beijing time on October 28, 2026 distinguishes MI-AO, SayAll and OpenRemoteAssistant. MI-AO connects a Xiaomi Bluetooth Voice Remote 2 Pro to a Mac: hold the voice button, release to transcribe locally with Whisper, then submit to the current Codex task. Firmware 2671 end-to-end validation is explicitly a project report, not a model running on the remote. The three implementations have separate records and cannot borrow each other's compatibility or tests.

Supplementary reading of fanxeon/mi-ao's public README credits FanXeon@Poemcoder with direction and Codex as an AI collaborator on code, tests, documentation and debugging. Protocol work builds on Google ATV Voice over BLE research, not a claimed first discovery of a proprietary protocol. The path is BLE ATVV v0.4/v1.0, IMA/DVI ADPCM, 16kHz PCM/WAV, local whisper.cpp and the Codex Accessibility tree. Automatic submission requires one uniquely available input field; otherwise text is copied. The document reports Xiaomi 2 Pro firmware 2671, ATVV 1.0, 16kHz/120B validation, not other remotes.

The documentation read describes V2/0.2.2, macOS 14+, source-first beta, without Windows/Linux support and with a locally built ad-hoc signed app. It also retains pending installed-build hardware acceptance for the 0.2.2 menu bar and connection strategies, plus prolonged use, multiple displays, login startup and some button stress tests. A working voice path does not validate every feature. Local recordings/transcripts are still stored data, and local transcription does not change subsequent Codex processing of submitted text. Source is MIT; REA is unspecified. This collection installed nothing, paired no hardware, read no BLE and submitted no Codex task. Hardware tests are project reports.

Shared candidate snapshot: 1 like, 18 views, 0 reposts, not separate project engagement.
Reported hardware is 2 Pro firmware 2671; some 0.2.2 installed-build acceptance remains pending.

## Sources

- [Candidate comparison of three Xiaomi-remote AI-input projects, October 28, 2026](https://x.com/i/status/2115390370095800483)
- [Supplementary MI-AO README, Codex credit and hardware limits, read October 28](https://github.com/fanxeon/mi-ao)

[中文](../fanxeon-mi-ao-xiaomi-remote-codex.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
