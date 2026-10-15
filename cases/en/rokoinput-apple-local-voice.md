# Roko Input: Apple on-device dictation after Typeless research

Category: Applications and clients · REA
Record date: 2026-10-15
Stage: In progress

Concerned about input methods collecting personal information, @slashui used REA to study a foreign voice-input tool, compared it with Typeless in the thread and published bassnova42/rokoinput. Unlike the existing whisper.cpp/Ollama-based REATypeless, this project uses Apple's Speech framework and InputMethodKit, without third-party ASR or large models. Reading the README on October 15 showed that only version 0.4.0 mandates on-device recognition, stopping rather than falling back to the cloud when unavailable. System language-resource preparation may access the network, and device/language support is conditional, so the post's broad suggestion of unrestricted Mac-model compatibility is not retained. Documentation also explicitly says text history is enabled by default, stored in plaintext and never automatically expires. It can be disabled but old records are not automatically deleted. Only source and local build scripts are provided. Real microphone use, global shortcuts and network traffic were not independently verified. A custom license restricts use to personal noncommercial purposes; this is not described as MIT or freely usable commercially.

Candidate snapshot: 3 likes | 432 views; reading public documentation is not physical-device acceptance.

## Sources

- [Author report and replies](https://x.com/i/status/2110610758212145408)
- [Public source and privacy/version boundaries](https://github.com/bassnova42/rokoinput)

[中文](../rokoinput-apple-local-voice.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
