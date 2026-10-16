# Typeless: a reported local voice-input alternative built with REA

Category: Applications and clients · REA
Record date: 2026-10-13
Stage: Needs verification

A Mac user reports that after Typeless reduced its free allowance, they used Claude Code with REA to analyze the Electron voice-input app and made a local alternative named REATypeless. The author says analysis showed the original client handles shortcuts, recording and pasting while speech recognition and text processing depend on servers. The replacement instead uses a quantized whisper.cpp large-v3-turbo model and Ollama/Qwen2.5 3B, adding polishing, translation and selected-text rewriting. The post reports about 2.9 GB of resident memory and roughly two to three seconds to produce text from five seconds of speech, but supplies no code or independent functional/performance tests. These remain author claims and do not establish a complete Typeless replica.

Another poster reports using Claude Code over half a day to build Saydra, a Windows voice-input alternative. Claimed features include local offline SenseVoice recognition (about 0.3 seconds), optional Groq Whisper large-v3, Qwen text polishing, translation, and selected-text rewriting. The poster says Chris used REA to reverse engineer Typeless; this is a retelling, not evidence that the poster personally used REA, nor independent confirmation of Chris's identity or original project details. Saydra's features and performance are unverified.

Author reports completing a local app on a personal Mac; no public code or independent functional/performance verification.
Original post specifies personal learning and technical research only, without distribution or sale.
2026-10-14: Another developer reports building Windows alternative Saydra with Claude Code; REA use is attributed to @Chris62771610 and is not independently verified.

## Sources

- [Author's REA analysis and local-alternative report](https://x.com/i/status/2109971905336037671)
- [Saydra author's report and retelling of Chris's REA work](https://x.com/i/status/2110386418929594439)

[中文](../rea-typeless-local.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
