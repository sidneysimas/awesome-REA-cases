# OpenRemoteAssistant: a preview bridging the RC003-MS microphone to Mac and Windows

Category: Hardware and interoperability · REA use unconfirmed
Record date: 2026-10-28
Stage: Related project

The comparison at 18:29 Beijing time on October 28, 2026 distinguishes OpenRemoteAssistant from MI-AO and SayAll: RC003-MS only, Mac/Windows development previews, Windows 10 developer-machine records but no Windows 11 testing, with VB-CABLE and transcription by the input app. Retained as a separate interoperability-related project in the same candidate, without transferring the other projects' Codex or Whisper methods to it.

Supplementary reading of ru-gong/OpenRemoteAssistant's public README describes connecting Xiaomi Bluetooth Remote 2 Pro buttons and microphone to a computer for voice input, voice programming and web coding; the app does not perform speech recognition. Mac 0.2.10 targets Apple Silicon/macOS 26 with Swift/SwiftUI, CoreBluetooth/CoreAudio and an OpenRemoteAudio virtual microphone. Windows 0.3.1 x64 uses C#/.NET 9, WinRT BLE and NAudio, with optional separately licensed VB-CABLE. Windows 10 build 19045 developer testing is not clean-system or all-device acceptance. Platform releases are independent; the Windows release does not replace the Mac release.

RC003-MS self-identifies as RC003; other remotes are not claimed compatible. The helper must keep running: Windows exits when closed, whereas Mac can remain in the menu bar. Mac saves no recordings; Windows defaults to no recording but offers local WAV. Source is GPL-3.0-only with separate third-party terms. Neither candidate nor README identifies a model in protocol investigation: AI is usage context, not proof of AI-assisted reversing. No installation, recording, pairing or OS-compatibility test was performed here. REA and model involvement are unknown.

Shared candidate snapshot: 1 like, 18 views, 0 reposts. Windows 10 developer records are not Windows 11 or full-platform acceptance; AI reversing involvement is unknown.

## Sources

- [Candidate: OpenRemoteAssistant preview scope and input-app boundary, October 28, 2026](https://x.com/i/status/2115390370095800483)
- [Supplementary public OpenRemoteAssistant README, read October 28](https://github.com/ru-gong/OpenRemoteAssistant)

[中文](../openremoteassistant-rc003-computer-microphone.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
