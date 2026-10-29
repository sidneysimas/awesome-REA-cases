# Kong: Ghidra-context-driven LLM symbol recovery and a project XZ backdoor benchmark

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-29
Stage: Analysis test

At 07:58:40 Beijing time on October 29, 2026, a candidate introduces Kong turning FUN_00401a30 into parse_http_header in a stripped binary, with types, and asks whether readers would trust the names. This illustrates capability, not an actual comparative experiment on a supplied HTTP program. A project-name lookup found amruth-sn/kong. Pinned commit 8c4ee4bf52e0eb9efc3a0b22ad6da03387543fd2 dates to April 3, 2026. Its README and BENCHMARKS provide earlier supplementary evidence, not new development in this window.

The README describes in-process Ghidra through PyGhidra/JPype, triage, signature matching and a call graph, then bottom-up LLM context containing decompilation, references, strings and named callees, followed by cleanup, semantic unification, export and Ghidra database writeback. It lists Claude/OpenAI support, type/symbol scoring and deobfuscation. These are public project design and capability claims, not proof of reliability across every architecture or obfuscation scheme. The 'world's first' slogan is not endorsed. The license is labeled Apache 2.0; no dependencies or code were installed or executed.

The same-commit benchmark calls its target a stripped liblzma.so.5.4.1 from XZ Utils 5.6.1: 558 functions enumerated, 396 queued, 355 analyzed, using claude-opus-4-6 in a reported 15 minutes for $6.63. It lists 308 high-confidence, 33 medium-confidence and 14 low-confidence functions, five core implant functions at 90%–95% confidence, and claims recovery of RSA-verification hooking and a ChaCha20 payload chain. Confidence is not source-checked accuracy, 355/396 is not completion of every function, and the narrative is not independent proof of autonomous unknown-vulnerability discovery. Sample provenance/hash, raw model outputs, cost and chain correctness were not verified. No malicious sample was downloaded or executed. The filename is retained as documented, not evidence that ordinary 5.4.1 builds are infected.

Candidate snapshot: 0 likes, 4 views, 0 reposts. The project benchmark is not execution by this collection.
Project-reported: 558 enumerated, 396 queued, 355 analyzed, 15 minutes and $6.63. 90%–95% denotes confidence, not independently measured accuracy.

## Sources

- [Candidate: Kong symbol recovery and type inference, October 29, 2026](https://x.com/i/status/2115594128167940242)
- [Earlier pinned README: pipeline and project scope, April 3, 2026](https://github.com/amruth-sn/kong/blob/8c4ee4bf52e0eb9efc3a0b22ad6da03387543fd2/README.md)
- [Same-commit BENCHMARKS: XZ sample, model, cost and confidence](https://github.com/amruth-sn/kong/blob/8c4ee4bf52e0eb9efc3a0b22ad6da03387543fd2/BENCHMARKS.md)

[中文](../kong-ghidra-llm-symbols-xz-benchmark.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
