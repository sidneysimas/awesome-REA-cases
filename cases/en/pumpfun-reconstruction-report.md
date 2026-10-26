# Pump.fun: parallel-agent investigation of a token-launch platform

Category: Applications and clients · REA
Record date: 2026-10-25
Stage: Needs verification

Pump.fun is a token-launch platform on Solana. 8Bit reports clawddevs using Codex and another agent in parallel within Muse. The development post being replied to describes testing migration to a Raydium liquidity pool after the launch curve completes, LP-token burning and swaps. The early report disclosed no reversing steps or proof of full reconstruction, and REA use was initially unconfirmed.

In the October 13 window, 8Bit (0rdlibrary) said a project forked from the REA repository had autonomously researched Pump.fun for about 24 hours; another post mentioned clawddevs and Muse. In the October 13 04:00–08:00 window, clawddevs personally reported 24 hours of work at the ultra high setting and three Codex quota resets. This is an ongoing-work report without code or behavioral comparisons. clawddevs did not explicitly mention REA; 8Bit's fork report is by a different author and does not establish one shared implementation or recovered server/contract source.

An earlier captured quote from an unidentified author additionally claimed that real depth-two tests passed, REA traced two creation paths, and an opening-settlement rounding shortfall was fixed and tested. The same quotation said source/build verification was ongoing and production readiness unproven. This is neither confirmation from Pump.fun's original developers nor a retest by this collection.

At 18:04:28 Beijing time on October 25, 2026, FeiXiaoHao (@feixiaohaocom) separately recounted Shaw Walters (@shawmakesmagic) claiming approximately 90% completion of Pump contract reversing, expecting completion that night and announcing a GitHub repository. The post identifies the target through its PumpFun tag and 2024 token-launch/bonding-curve background, framing the work as AI-assisted reverse engineering. Supplementary lookup on October 26 confirmed the posting account. This is another author's research on the same platform, not confirmation of a shared codebase with 8Bit/clawddevs. No inspectable Shaw model log, repository identity or build result was obtained. The 90% figure is reported progress, not a byte-match rate; expected completion is not completed work. Protocol revenue and commercial commentary are not technical evidence. The target was not run and production usability was not verified.

At 22:53:53 Beijing time on October 25, 8Bit personally named the derived token-launch platform Musebook launchpad, explicitly described it as reverse engineered from Pump Source and REA, and announced a Solana mainnet launch for that night. Supplementary lookup confirmed 0rdlibrary as the same author as the earlier Pump investigation. It is therefore appended to that target's record rather than counted as a separate new case, and is not attributed as Shaw's own deployment. The post adds an artifact name and release plan but no checkable program address, deployment transaction, source, behavioral comparison or security audit. The identity of Pump Source behind its short link is unconfirmed. Mainnet launch remains future tense, not a completed deployment, safe token issuance or verified custody. No wallet was connected and no trade executed.

Posted: 2026-10-12T10:01:06+08:00 (Beijing time)
Engagement snapshot (2026-10-12): 1 like | 44 views | 0 reposts
Follow-up posted: 2026-10-13T05:43:27+08:00 (Beijing time)
Additional evidence: xreach confirmed the posting account as clawddevs; author report, not independent verification.
New evidence in this batch: a quote/secondhand account claims real depth-two tests passed, creation paths were traced, and an opening-settlement rounding shortfall was fixed and tested; production readiness remains unproven and author identity is unconfirmed.
October 25 adds FeiXiaoHao's secondhand Shaw/Pump contract report, not a confirmed shared codebase; 90% is not a byte-match rate, and no repository or runtime validation was obtained.
The October 25, 22:53 Musebook report names 8Bit's derivative of the same target; same-night mainnet launch is only planned, and Pump Source identity and on-chain deployment are unverified.

## Sources

- [Public source from this review](https://x.com/0rdlibrary/status/2109464346103263523)
- [Development post being replied to (background)](https://x.com/clawddevs/status/2109461838144458936)
- [This window: REA fork and autonomous-run report](https://x.com/i/status/2109730115152216125)
- [This window: developer's own work-in-progress report](https://x.com/i/status/2109761893808365700)
- [X post from this batch (quote/secondhand; author identity unconfirmed, not original-developer confirmation)](https://x.com/i/status/2110080570612941090)
- [FeiXiaoHao recounts Shaw's 90%-complete Pump contract research, October 25, 2026](https://x.com/i/status/2114297028620763266)
- [8Bit names Musebook and announces a mainnet plan, October 25, 2026 at 22:53:53](https://x.com/i/status/2114369864265515048)

[中文](../pumpfun-reconstruction-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
