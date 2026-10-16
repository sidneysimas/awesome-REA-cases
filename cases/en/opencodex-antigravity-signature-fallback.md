# OpenCodex / Antigravity: REA investigation of missing multi-turn tool-call signatures

Category: Applications and clients · REA
Record date: 2026-10-16
Stage: Needs verification

An October 16 author report says complex multi-turn sessions proxying Gemini/Antigravity through OpenCodex still encountered 400 errors for missing thought_signature values despite caching and replaying historical signatures. The author used REA to inspect local antigravity_tools (Rust) and Google's language_server (Go) binary, claiming the client uses a skip_thought_signature_validator placeholder when caches and fallbacks find no real signature. They describe adding that fallback at the end of OpenCodex's Antigravity request pipeline while allowing later real signatures to replace it. The author says the errors stopped but gives no patch, versions, request logs or test matrix. The explanation of a hard-coded Google gateway exemption remains the author's attribution: client-side static observations cannot directly prove the server implementation or compatibility with arbitrary models or sessions. This collection did not send requests or reproduce it.

October 16 candidate snapshot: 1 like, 108 views; neither results nor the server-side explanation are independently verified.

## Sources

- [OpenCodex signature error and REA investigation report](https://x.com/i/status/2110921946418602001)

[中文](../opencodex-antigravity-signature-fallback.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
