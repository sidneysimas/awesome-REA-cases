# Feishu: a dual-account Mac client after Codex/REA research

Category: Applications and clients · REA
Record date: 2026-10-15
Stage: Needs verification

To avoid constant account switching in Feishu on Mac, the author had Codex install REA and analyze Feishu 8.1.17, claiming the first installation and report took 4 minutes 34 seconds. The report lists a hybrid shell, multiprocess web components, 25 ASARs, a clipboard bridge and request routing, while acknowledging that Codex traced key paths mainly by reading code directly; package identifiers alone do not establish standard Electron. The author then claims a Feishu 2 copy was made in six minutes: changing the app identifier, replacing data-directory markers with equal-length names at 18 locations across 15 native files, isolating the single-instance lock, disabling updates for the copy and re-signing it. The author reports two-account login, separate locks/directories, and unchanged original signatures and main-executable hash. feishu-clone informed the approach, but the agent rewrote the script. All timings and acceptance checks are author-reported, without independent execution. The copy is local-only and not distributed. Local signing and disabled updates carry maintenance and licensing risks, with no guarantee for future versions.

Full article obtained this review; local acceptance and timing are all author reports.

## Sources

- [Author's long article from this review](https://x.com/i/status/2110601137707729071)
- [Author's original blog and experiment version](https://benx.ai/blog/posts/rea-reverse-engineer-feishu-dual-instance/)

[中文](../feishu-dual-instance-codex-rea.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
