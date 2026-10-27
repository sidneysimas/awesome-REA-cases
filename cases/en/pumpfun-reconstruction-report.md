# Pump.fun: parallel-agent investigation of a token-launch platform

Category: Applications and clients · REA
Record date: 2026-10-27
Stage: Needs verification

Pump.fun is a token-launch platform on Solana. 8Bit reports clawddevs using Codex and another agent in parallel within Muse. The development post being replied to describes testing migration to a Raydium liquidity pool after the launch curve completes, LP-token burning and swaps. Early reports disclose no reversing steps or proof of full reconstruction, and REA use was initially unconfirmed.

On October 13, 8Bit (0rdlibrary) said a project forked from REA autonomously researched Pump.fun for about 24 hours; another post mentioned clawddevs and Muse. In the 04:00–08:00 window, clawddevs personally reported 24 hours of work at the ultra high setting and three Codex quota resets. This is ongoing-work narration without code or behavioral comparisons. clawddevs did not explicitly mention REA; 8Bit's fork account is by another author and does not establish a shared implementation or recovered server/contract source. An earlier unidentified quote claimed real depth-two tests passed, REA traced two creation paths, and an opening-settlement rounding shortfall was fixed and tested, while source/build verification remained ongoing and production readiness unproven. This is not original-developer confirmation or an independent retest.

At 18:04:28 Beijing time on October 25, FeiXiaoHao (@feixiaohaocom) recounted Shaw Walters (@shawmakesmagic) claiming approximately 90% completion of Pump contract reversing, expecting completion that night and announcing a GitHub repository. Its PumpFun tag and background on the platform's 2024 token-launch/bonding-curve introduction identify the target; October 26 lookup confirmed the reporting account. The 90% is secondhand progress, not a byte-match rate; expected completion is not completion. At 22:53:53 Beijing time on October 25, 8Bit named the Pump Source/REA-derived platform Musebook and announced a same-night Solana mainnet plan. The account 0rdlibrary matches the earlier author, so it is retained under this target rather than counted as a new product or attributed as Shaw's deployment. No checkable program address, deployment transaction, security audit or mainnet launch evidence was obtained. Pump Source behind that short URL remains unidentified.

In the candidate posted at 11:31:14 Beijing time on October 26, Shaw personally identifies lalalune/pumpfun-source and asks contributors to use ChatGPT or another agent to disassemble, reconstruct and submit PRs until the result is byte-identical to the original binaries, not merely functionally similar. He recommends REA but explicitly says he is not using it: Shaw's implementation must not be credited to REA. This record's REA classification retains 8Bit's and the earlier quotation's reports, not a claim that every author used it. The $200 subscription and GLM-5.3/Kimi K3.1/older Opus choices are author recommendations, not full-cost or capability benchmarks. Token rewards, security-platform launch plans and contract-loss figures at the end are not technical validation. A recruitment goal is not a completed match.

Supplementary static reading of the lalalune/pumpfun-source README is pinned to f359ab9b7de3c9bbac05ba3c5157af20d5580dc9, committed at 22:06:29 Beijing time on October 26, after this window's 12:00 end. It is later cross-checking, not evidence of the exact candidate-time state. The document explicitly retains 0/4 whole-file byte-identical core programs. Bounded reconstruction covers 140/150 identified instruction handlers, with five partial and five unrecovered. It lists 9,269 Pump, 17,462 AMM, 17,461 Fees and 9,595 Mayhem comparisons, plus 1,024 signed Pump Surfpool comparisons and ten Fees sequence steps. Counts overlap and repeat inputs; they cannot be summed as independent tests or converted into an overall completion percentage. Raw compiler output and retained allocation images are distinguished, without padding or editing bytes to manufacture identity. Security audit, SDK/deployment acceptance and broader behavior remain incomplete; the document claims no on-chain deployment. This collection only read repository documentation. It did not execute target code, compile, rerun comparisons, connect a wallet or trade, and does not turn project-generated evidence into independent reproduction or a security guarantee.

Posted: 2026-10-12T10:01:06+08:00 (Beijing time)
Engagement snapshot (2026-10-12): 1 like | 44 views | 0 reposts
Follow-up posted: 2026-10-13T05:43:27+08:00 (Beijing time)
Additional evidence: xreach confirmed the posting account as clawddevs; author report, not independent verification.
New evidence in this batch: a quote/secondhand account claims real depth-two tests passed, creation paths were traced, and an opening-settlement rounding shortfall was fixed and tested; production readiness remains unproven and author identity is unconfirmed.
The October 25 Shaw 90% figure is FeiXiaoHao's secondhand account, not a byte-match rate. Shaw identifies the repository on October 26; runtime validation remains absent.
The October 25, 22:53 Musebook report names 8Bit's derivative of the same target; same-night mainnet launch is only planned, and Pump Source identity and on-chain deployment are unverified.
Shaw explicitly says he is not using REA. New candidate snapshot on October 26, 2026: 105 likes, 4,354 views and 9 reposts; evening lookup growth is not substituted.
Documentation at the post-window 22:06:29 pinned commit still reports 0/4 whole-file core matches. The 140/150 figure is bounded handler coverage, comparison counts overlap, and security/deployment were not independently tested.
At 22:36:58 Beijing time on October 27, 8Bit (@0rdlibrary) says that when REA went viral two weeks earlier, he had AI also search X for problems and develop a solution called fair launch, linking Musebook. Lookup confirms the same author. October 28 static reading of launch.musebook.trade identifies a Launchpad page describing Solana assets and paired tokens, user review and wallet signing; the fairlaunch subpath returns 503. This checks the product entry only, without connecting a wallet or certifying deployment, transactions, safety or a relationship to Shaw's code. Candidate snapshot: 4 likes, 242 views, 4 reposts.

## Sources

- [Public source from this review](https://x.com/0rdlibrary/status/2109464346103263523)
- [Development post being replied to (background)](https://x.com/clawddevs/status/2109461838144458936)
- [This window: REA fork and autonomous-run report](https://x.com/i/status/2109730115152216125)
- [This window: developer's own work-in-progress report](https://x.com/i/status/2109761893808365700)
- [X post from this batch (quote/secondhand; author identity unconfirmed, not original-developer confirmation)](https://x.com/i/status/2110080570612941090)
- [FeiXiaoHao recounts Shaw's 90%-complete Pump contract research, October 25, 2026](https://x.com/i/status/2114297028620763266)
- [8Bit names Musebook and announces a mainnet plan, October 25, 2026 at 22:53:53](https://x.com/i/status/2114369864265515048)
- [Candidate: Shaw identifies pumpfun-source, its byte-identical goal and non-use of REA, October 26, 2026 at 11:31 Beijing time](https://x.com/i/status/2114560456891445597)
- [Same-window secondhand explanation: distinct 140/150 and 0/4 measurements](https://x.com/i/status/2114537509862740203)
- [Post-window supplementary README at pinned commit f359ab9, October 26, 2026 at 22:06:29 Beijing time](https://github.com/lalalune/pumpfun-source/blob/f359ab9b7de3c9bbac05ba3c5157af20d5580dc9/README.md)
- [8Bit adds a REA/social-research-to-Fair Launch workflow, October 27, 2026](https://x.com/i/status/2115090382015066319)
- [Supplementary: public Musebook Launch entry, statically read October 28](https://launch.musebook.trade/)

[中文](../pumpfun-reconstruction-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
