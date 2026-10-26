# daos.fun: wei relays Shaw's AI-assisted Anchor reconstruction and matching-binary claim

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-25
Stage: Needs verification

At 13:02:23 Beijing time on October 25, 2026, wei (@8853wei) relayed Shaw's (@shawmakesmagic) October 24 research on daos.fun. The target is a closed-source program deployed on Solana: obtain the program from the chain, then use AI to rebuild Anchor source. The post claims the recompiled 1,120,784-byte binary matches the deployed program byte for byte with the same SHA-256 and says source and an audit are on GitHub.

The same retelling lists one critical, four medium and one low finding. The critical concerns a missing DAO-to-pool binding, allegedly allowing migration fees to be redirected and another DAO's state corrupted. The claim that new launches, rather than already-bonded ones, are affected is attributed to Shaw. This entry summarizes the reported issue class without invocation or exploitation steps. Private security bounties and Umia are subsequent suggestions in the post, not separate reversing projects or evidence that findings were confirmed or fixed.

Supplementary reading on October 26 confirmed the retelling's author. Public-repository searches did not locate a verifiable original reconstruction/audit commit, so no repository or contract address is guessed. AI involvement, byte count, hash identity and audit ratings remain wei's account of Shaw's claims. No on-chain target was obtained, no binary rebuilt or hash recomputed, and no funds-related operation tested here. This is not automatically merged with unspecified pump.fun or OpenSolana summaries, and readable source does not establish safe reconstruction of every contract.

Secondary account; the 1,120,784-byte size, matching hash and 1 critical/4 medium/1 low findings were not independently verified.
Original reconstruction repository, audit commit and on-chain address remain unconfirmed; no on-chain operations performed.

## Sources

- [wei relaying Shaw's daos.fun reconstruction and audit, October 25, 2026](https://x.com/i/status/2114221010853781864)

[中文](../shaw-daosfun-ai-anchor-reconstruction-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
