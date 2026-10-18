# Hupu and Coolapk APKs: REA/LLM ad-logic investigation with integrity and re-signing blockers

Category: Applications and clients · REA
Record date: 2026-10-18
Stage: In progress

At 17:46 Beijing time on October 18, @ADLXBT proposes recovering Java with JADX, asking an LLM to abstract ad-API calls into patterns, changing related methods and re-signing. Reading the 17:15 parent identifies @xulijian1994 (Kxians) reporting investigation of Hupu and Coolapk APKs with REA Skill, an AI agent, JADX and Ghidra to locate ad logic. The parent is supplementary evidence for the original reply, not a replacement candidate from outside the supplied array.

The author says both use NetEase protection: the first visible code is the wrapper, and real business DEX is needed before tracing splash and feed-ad entry points. For Coolapk he names EntityAdHelper and SplashAdLoader. He distinguishes static localization and DEX edits from usable applications: Hupu startup-integrity checks and possible Coolapk API 403 responses after re-signing remain obstacles. Editing DEX does not prove the app runs. The reply's claim of directly replacing DEX methods through Ghidra was not verified and is not treated as a tool-capability guarantee.

No APK versions, lawful fixtures, patches, complete logs or before/after tests are supplied. Progress and blockers remain author reports, without confirmation of successful ad removal, repaired signing, preserved full functionality or compliance with service terms. No target was downloaded, software modified or API accessed.

October 18 original candidate snapshot: 0 likes, 29 views; the parent supplies context, not independent execution or proof of ad-removal success.

## Sources

- [ADL's LLM ad-API pattern proposal](https://x.com/i/status/2111755690108985465)
- [17:15 supplementary parent: Hupu/Coolapk investigation and re-signing blockers](https://x.com/i/status/2111748065749307658)

[中文](../hupu-coolapk-rea-ad-removal-investigation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
