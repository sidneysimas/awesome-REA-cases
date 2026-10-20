# Snowboard Kids: Codex records IDO compiler patterns for N64 byte matching

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-20
Stage: Needs verification

At 11:00 Beijing time on October 20, @waynerad quotes an article titled 'Decompiling a Nintendo 64 game in 84 days', concerning Snowboard Kids. The excerpts distinguish its proprietary SGI IDO 5.3 compiler from GCC 2.7.2 used for Snowboard Kids 2. IDO's original environment depended on obsolete SGI hardware and software; the community had already reverse-engineered parts of the toolchain and statically recompiled IDO 5.3/7.1 for modern machines. These are prior community contributions, not work done from scratch by Codex.

The quoted author says both they and LLMs generally understand a function, write C approximating its purpose, then try small changes with a permuter to match machine code. IDO's multiple optimization passes can turn tiny C changes into different register allocations; permutation cannot guarantee a match when the underlying structure is wrong. To share recurring compiler quirks, the author prompted Codex to record observations in DECOMPILATION_LEARNINGS.md for subsequent agents.

This is a secondary research account with concrete toolchain difficulties and a lesson-sharing mechanism, not an independent reproduction by this collection. The 84 days come from the article title, not measured agent labor. The post supplies no complete function-matching output. This collection did not read the article behind the short link or run the game, and cannot establish full byte matching, a complete port or REA involvement.

October 20 candidate snapshot: 0 likes, 27 views, 0 reposts; engagement for the quotation post, not the original article or project validation.

## Sources

- [waynerad's excerpts on Snowboard Kids, IDO and Codex's learning file](https://x.com/i/status/2112378313171951813)

[中文](../snowboard-kids-ido-codex-decompilation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
