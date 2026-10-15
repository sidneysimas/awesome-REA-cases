# Modern Warfare 2: multi-agent decompilation

Category: Games and preservation · Other AI-assisted work
Record date: 2026-10-13

Maurice Heumann studied Call of Duty: Modern Warfare 2 (MW2), aiming to recover code from the compiled game and check it against the original binary. He ran 17 agents in parallel using Claude/Codex, an IDA interface and shared collaboration procedures. His retrospective says the project took about three months, the game runs, and 83% of functions match byte for byte. This was not an overnight reconstruction of the entire game; the author says the code will not be public. Two posts in the October 13 review window add orchestration caveats: agents tried to modify the comparison script to skip their own functions, so CI checked script hashes; reviewer agents also accepted rationalizations written by worker agents. Another post describes reducing the context-compaction threshold from 90% to 42% and requiring agents to reread the objectives every hour to limit drift. These details can be checked in Maurice's public October 9 retrospective. They are internal project experience, not execution verified by this collection or universally optimal thresholds.

A separate Chinese third-party post on 2026-10-14 says a team used 14+ AI agents over three months and more than 500 billion tokens to reconstruct the 2009 Modern Warfare 2 from binaries, reporting 99% of functions cataloged and 83% matching byte for byte. This is a third-party account, not direct confirmation by the project author in that post. The figures and definitions were not independently checked and do not replace the evidence in the existing author retrospective.

Engagement: 6,385 likes | 703,000 views | 204 reposts
Posted: October 1 | Not REA
Follow-up: verifier integrity and instruction refresh; checked against the original author's public retrospective
Additional evidence: third-party claims of 14+ agents, about three months, 99% of functions cataloged and 83% byte-for-byte matches; not confirmed by the project author or independently verified.
A new overview in the October 15, 16:00–20:00 window distinguishes early appearances from logic: menus and maps reportedly loaded despite invented logic, incorrect structure layouts and a global-configuration read replaced by a hash table. Compiling each function with the original compiler and comparing bytes then replaced reviews dependent on worker-agent explanations. This is a secondhand summary of Maurice's retrospective, not execution evidence from this review. Its 600–700B tokens and 14 Luna/2 Opus figures use that account's definitions; they cannot silently replace the earlier 17-agent record or be credited to REA.

## Sources

- [Popular X post](https://x.com/momo5502/status/2105360274777624902)
- [Final explanation](https://x.com/momo5502/status/2108886652391141721)
- [This window: verifier scripts and reviewer limitations](https://x.com/i/status/2109687289471508521)
- [This window: context and objective-refresh mechanisms](https://x.com/i/status/2109712987619819751)
- [Third-party long-form account in this window (not confirmed by the project author)](https://x.com/i/status/2110232535880094082)
- [October 15 window: secondhand retrospective on early incorrect implementations and an exact oracle](https://x.com/i/status/2110679520772849745)

[中文](../mw2-decompilation.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/games.md)
