# re3 / GTA III: an Opus-built NPC agent layer on an existing reverse-engineered game

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-20
Stage: Needs verification

At 14:55 Beijing time on October 20, @vladrezdev (Vlad Rez) says Claude Opus 5.5 added a System 1 / System 2-style NPC layer to re3, the existing reverse-engineered GTA III project. An activation cheat turns nearby characters into agents. TypeSafe Jev decides actions such as walking, running, fighting, talking and driving. GPT-4.1-mini supplies speech and thoughts and takes over when Jev is uncertain or an action is consequential, such as an unprovoked attack.

The author describes the game sending a street snapshot once per second over local HTTP to a Python bridge, which returns actions, speech and thoughts. Characters have names, personalities, city plans, event memories and trust relationships. Examples include an NPC driving the player to hospital, or witnesses fighting back or calling police from a payphone. Multiple videos are attached, but this collection did not watch them in full, run the project or obtain source, latency or multi-agent stability tests. Once per second is the author's stated exchange cadence, not measured performance. This is a concrete AI extension of existing reverse-engineered code, not Opus doing re3's original decompilation or independent verification of every narrated behavior. REA use is unconfirmed.

## Sources

- [Vlad Rez's re3 Jev/GPT NPC layer and local-bridge account](https://x.com/i/status/2112437552183701557)

[中文](../re3-gta3-jev-npc-agent-layer.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
