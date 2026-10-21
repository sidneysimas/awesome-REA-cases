# LayerFS: reported storage savings for multi-agent Unity reverse-engineering workspaces

Category: Applications and clients · REA use unconfirmed
Record date: 2026-10-21
Stage: Related project

At 21:26 Beijing time on October 21, 2026, Chasen (@chasen_liao) introduces LayerFS v1.0.0 as an AI-agent filesystem: separate workspaces for Bash calls, rejection of same-file conflicts, forks without full file copies and access to previous steps. The post repeats another user's claim that Unity game reverse-engineering artifacts shrank from 400G to 33G. A 22:39 post adds that the material came from eight days of work. Neither provides the game, original storage measurements or that user's logs; these are not two independent experiments.

The later post also relays the author's Rust database-engine task: 30 branches representing 2.5TB of snapshots reportedly occupied 4.66GB, versus 8.23GB for main alone. The earlier post separately claims ten copies occupying 0.31 copies' space and a 0.05-second mount. These source figures have different denominators and are not combined into a compression rate or an improvement in reversing speed or accuracy. Deduplication and copy-free branches are the sources' explanations; the later author explicitly learned its mechanism from Grok, not source-code inspection. MIT licensing, open-source availability, rollback and conflict guarantees remain promotional claims without an inspected implementation or executed tests here. This is a related tool for multi-agent reversing workspaces, with REA involvement unconfirmed and no downloaded code executed.

First candidate snapshot: 32 likes, 3,720 views, 2 reposts; later post: 7 likes, 471 views, 1 repost; neither is performance verification.

## Sources

- [Chasen on LayerFS workspaces and the Unity 400G-to-33G claim](https://x.com/i/status/2112898320997781948)
- [22:39 follow-up: eight days of Unity artifacts and database-branch storage figures](https://x.com/i/status/2112916736693490097)

[中文](../layerfs-unity-agent-workspaces.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
