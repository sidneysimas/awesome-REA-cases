# Red Alert 3 and Corona: DeepSeek-assisted trainer rewrite and LLM game control

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-21
Stage: Needs verification

At 20:12 Beijing time on October 21, 2026, 探姬 (@ProbiusOfficial) describes using dsv4.1f to study Red Alert 3 and its Corona mod. A frequently crashing 31-option trainer generated with Cheat Engine (CE) in 2009 prompted an attempt to bring skirmish protocol abilities into the original campaign. Black-box experiments from v0 through v26 reportedly failed to summon random units by airdrop. Only after examining unpacked material did the author identify missing campaign ability-release resources. Some unit and warp logic existed but lacked art assets, while some special hash objects were absent. Finishing a trainer is not success on this initial objective.

The author then asked the model to analyze and rewrite the old CE trainer. It reportedly mistook already-modified target assembly for invalid edits and improvised changes, requiring human interruption every one or two modifications. WorkBuddy stored guesses and unstable black-box observations in memory, while the model often tested even random-function behavior only once. After iteration 1017, the author attributed roughly 50% of problems to old black-box records and 40% to failure to follow testing instructions: a personal diagnosis, not audited statistics. Removing speculative and unstable records reportedly improved matters. Runtime unpacking is said to have revealed some core mod structures and ways to call game functions. The author reports completing the trainer rewrite and connecting an LLM to internal functions to influence battles.

The main breakthroughs reportedly happened on a clean Windows machine using only Python. Earlier work included IDA exports without MCP, showing components on the main machine and trying REA; the result cannot be credited as an independent REA accomplishment. No public source, patch, random-test logs or stability comparison is supplied. Safer, more powerful and completed integration remain author claims, not independently run here, and no online anti-cheat bypass is described.

Source update: 2026-10-21T20:12:09+08:00; candidate snapshot: 22 likes, 2,158 views, 2 reposts; engagement is not verification.

## Sources

- [ProbiusOfficial's full account of Red Alert 3/Corona, the old CE trainer and LLM integration](https://x.com/i/status/2112879611084427419)

[中文](../ra3-corona-deepseek-trainer-llm.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
