# SayAll: a related project bridging Xiaomi Bluetooth remotes to computer voice input

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-28
Stage: Related project

The same comparison at 18:29 Beijing time on October 28, 2026 describes SayAll as Mac-focused, with a first Windows preview supporting Xiaomi Remote 2 and 2 Pro and voice input restricted to WeChat's input method. Unlike MI-AO's local Whisper-to-Codex path, it makes the remote a computer voice-input device. With no author reversing log in the candidate, this is retained as a related interoperability/AI-development project.

Supplementary reading of HD838A/remote-mic-app's public README describes a SwiftUI Mac app turning BLE voice remotes into wireless microphones. A compatible virtual microphone or loopback device such as BlackHole is required, with recognition performed by the selected input software; the Windows preview remains basic. AI-tool token costs fund ongoing development, but that does not establish AI discovery of the protocol or participation in every implementation. The project began as a nijez/open-voice-bridge fork, references MiRemoteVoice's microphone naming and USB-transport compatibility approach, and derives its driver from BlackHole source; prior work is credited. Mac code/drivers are GPL-3.0-only, branding has separate terms, and iOS is maintained privately.

The document identifies multi-step actions, per-app profiles and expression-history/read-only MCP as candidates or still needing real-environment acceptance, not fully validated capabilities merely because configuration exists. History is off by default and stores no audio; third-party AI clients may upload text they read. The current README also distinguishes platform/chip requirements and membership-only features, so universal free access is not inferred. Performance, notarization, device breadth and Windows speech routing were not independently validated here. No driver was installed or remote paired; REA is unspecified.

Shared candidate snapshot: 1 like, 18 views, 0 reposts. AI-assisted development is not proof of AI-assisted protocol reversing.

## Sources

- [Candidate comparing SayAll and two other remote-input paths, October 28, 2026](https://x.com/i/status/2115390370095800483)
- [Supplementary SayAll README, provenance and testing limits, read October 28](https://github.com/HD838A/remote-mic-app)

[中文](../sayall-xiaomi-remote-voice-bridge.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
