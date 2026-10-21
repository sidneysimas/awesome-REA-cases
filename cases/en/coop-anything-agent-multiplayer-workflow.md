# Co-op Anything: agent playbooks for adding multiplayer and reviving old co-op mods

Category: Games and preservation · REA
Record date: 2026-10-21
Stage: Related project

At 12:10 Beijing time on October 19, @Bing_Bryan_BRN introduces Co-op Anything as a workflow for Claude Code/Codex to investigate engines, write synchronization, test with bots driving game clients and package Steam-relay multiplayer. The public cranebeaker/coop-anything README confirms an MCP server and engineering playbooks. MCP tools identify engines from installation folders, search a directory of over 230 co-op mods and read the workflow; REA can provide binary analysis. This is not one model that independently performs all reversing.

Its two paths are auditing and repairing existing abandoned mods, or researching state, hooks, player/enemy/world synchronization, level transitions and saves from scratch. The README links a Deus Ex HX mod fix package, Dungeon Keeper/KeeperFX, Fallout: New Vegas and Ocarina of Time projects, distinguishing untested, player-report, automated-client-test and verified-playthrough quality levels. These are documented examples and labels, not separately added, unreviewed candidate cases.

The project describes real-client bot tests, Steam relay and distribution without port forwarding. Each participant must own the game; anti-cheat and other people's online services are out of scope. Adaptation, stability and release maturity vary by game. The README's claim that any game is possible is not a verified compatibility guarantee. No dependencies were installed, MCP server run, game launched or two-client synchronization tested here. This is a public workflow project, not proof of unattended multiplayer success. The repository is supplementary background, not a candidate post.

The October 21 candidate at 22:17 Beijing time says Deus Ex builds on Sebastian Kaufel's (Hanfling's) HX 0.9.89.4, reportedly last released in June 2019. A separate HXFix package addresses map-change crashes, ending conversations and lost door-code notes without modifying or redistributing HX. It reports over 40 real-client tests and Beta status. Public README material read on October 22 confirms the project's separate-package, Steam-relay and real-client-testing descriptions, but neither the historical test count nor test execution was verified. The documentation still lists stub ending credits and conversation warnings; campaign co-op does not mean no known defects.
The same candidate attributes Dungeon Keeper work to KeeperFX, STALKER work to patches for Shadow of COOP, and Ocarina of Time work to Ship of Harkinian and its multiplayer fork, while calling Fallout New Vegas an approximately 35%-complete developer preview. These are the October 21 secondary report's figures, not individually verified or separately added cases. Legally owned games/ROMs are required. Steam's Spacewar AppID 480 supplies a test relay path, not certification for commercial release. The reported 499 stars explicitly date to the morning of October 19, not current engagement; this candidate has 1 like, 125 views and 0 reposts.

## Sources

- [Candidate: introduction to Co-op Anything multiplayer adaptation](https://x.com/i/status/2112033640419045529)
- [Public project: MCP, two workflow paths and QA levels](https://github.com/cranebeaker/coop-anything)
- [October 21 secondary report: HXFix, Beta and other game stages](https://x.com/i/status/2112911054606917774)
- [Supplementary project documentation: Deus Ex HXFix and Steam relay](https://github.com/cranebeaker/deus-ex-coop)

[中文](../coop-anything-agent-multiplayer-workflow.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
