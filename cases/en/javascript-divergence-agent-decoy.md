# JavaScript divergence: formatting switches the game, an AI reversing-decoy idea

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-17
Stage: Related project

At 17:20 Beijing time on October 17, 2026, a post describes research Robert Vähhi calls divergence: exploiting JavaScript-processor bugs so formatted or cleaned-up code behaves differently from the original. The reported demo plays Tetris before formatting and Snake afterward. An example changes '+ +m' to '++m', turning an expression that leaves m unchanged into an increment. The account says the demo chains differences into bytecode for a tiny virtual machine to change the entire game, and reports 186 techniques across more than 37 processors.

The concrete AI-reversing connection is a defensive idea: a human or agent cleans up a script and then spends time analyzing a still-functional decoy. A reconstructed anti-bot or anti-cheat client could consequently differ from the real script in ways a server might detect. This does not establish that a particular AI agent has been misled or that every formatter triggers the effect; the source explicitly makes it tool- and configuration-dependent. This entry is a secondary introduction to named research and a proposed application. Original demo code was not obtained, the 186 techniques were not independently reproduced, and server-side detection was not validated. REA involvement is unconfirmed.

Source published: October 17, 2026; 186 techniques and more than 37 processors are secondary reports.
Related defensive research and an idea, not verified agent deception or a deployed anti-cheat system.

## Sources

- [Secondary account of divergence and its AI-reversing decoy application](https://x.com/i/status/2111386823763411016)

[中文](../javascript-divergence-agent-decoy.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
