# OtterSec's GoonFi V2 research: AI-recovered Rust, whole-program recompilation constraints and a disclosed accounting bug

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-27
Stage: Needs verification

The historical source is pashov's general account at 20:08 Beijing time on October 16, 2026, of @osec_io's AI-assisted Rust recovery, hash-perfect recompilation and Critical findings, without a named target. This window's October 27, 15:19 candidate by r1cksec names GoonFi V2. Supplementary reading covers OtterSec's Breaking open a propAMM, by Renato Marziano and Robert Chen, dated October 15, plus README and VERIFY.sh at renato-osec/goonfi-v2-decompiled commit 381cc31945474ba6b5b56b32a8cad5266602d612, timestamped October 15 at 22:35:39 Beijing time. These pre-window supplements are not new releases in this window. The existing research ID and pashov source are retained, without assuming his earlier general statement referred only to this target.

The target is the closed-source GoonFi V2 Solana market-making program, recovered into auditable Rust. The authors describe Opus 5.5 coordinating Astra subagents on smaller reversing tasks, using Binary Ninja, Solana tooling, the IDL and on-chain transactions. Function-level recompiled instructions are compared, with deterministic checks and agent review controlling merges. Similarity-only optimization overfits, so unnatural compiler tricks are restricted and library code should be reproduced through dependencies. Even after 100% per-function matching, the article says about 93k bytes still differed in a 243k-byte binary; function ordering, pointer tables and panic paths/line numbers had to be addressed for the claimed hash-perfect result. Local zero-score matches are not whole-program identity or recovery of a unique original source.

The public README targets original deployment slot 448984043 and says an October 6, 2026 upgrade fixed the reported bugs. VERIFY.sh comments identify the old deployment as September 21 and a 243,080-byte ELF. Its flow requires archival RPC data to reconstruct the old deployment, then builds and compares with cmp; a current on-chain dump is not the old target. The README separately describes matching 'beyond padding'; this collection neither independently reran verification nor resolved that wording difference. Readable verification material is not a matching hash established here.

The authors report that auditing the reconstruction revealed a vault-live-balance accounting/pricing flaw potentially exposing $6.1 million, responsibly disclosed. That is reported risk, not actual loss. Remediation is a project statement; no current contract inspection or exploitation was performed. The original article, public source and scripts materially strengthen the earlier secondhand evidence, but this collection did not compile, access archival credentials, execute targets or reproduce the financial risk. Status remains unverified, REA use unconfirmed, and the result does not establish recovery of arbitrary Rust programs or universal failure of closed source.

Historical October 16 snapshot: 120 likes, 4,339 views, 11 reposts. Current-window candidate: 1 like, 29 views, 0 reposts; engagement is not validation.
$6.1 million is author-reported exposure, not loss. Original deployment: September 21; README reports an October 6 upgrade.
100% function-level matching is not whole-program byte identity. Public source and verification scripts were read, without compilation, archival reconstruction or current on-chain inspection.

## Sources

- [Historical: pashov's account of osec_io Rust research, October 16, 2026](https://x.com/i/status/2111066785890054605)
- [Current-window candidate: r1cksec on GoonFi V2 AI reversing, October 27, 2026](https://x.com/i/status/2114980383414722716)
- [Supplement: signed OtterSec article, dated October 15, 2026](https://osec.io/blog/goonfi-decompilation/)
- [Supplement: pinned October 15 README, original deployment and upgrade scope](https://github.com/renato-osec/goonfi-v2-decompiled/blob/381cc31945474ba6b5b56b32a8cad5266602d612/README.md)
- [Supplement: same-commit VERIFY.sh, archival reconstruction and cmp flow, not executed](https://github.com/renato-osec/goonfi-v2-decompiled/blob/381cc31945474ba6b5b56b32a8cad5266602d612/VERIFY.sh)

[中文](../osec-ai-rust-hash-recompilation-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
