# CPU kernels: REA assembly-optimization research and a multi-model review workflow

Category: Algorithms and feature recovery · REA
Record date: 2026-10-20
Stage: In progress

In the October 15 original, the author says they spent the day using Claude Code to manage Astra and investigate CPU-kernel optimization at assembly level through REA, exploring what frontier models can achieve in low-level implementations. Kernel here means a compute kernel, not an identified operating-system kernel. No algorithm, instruction set, test cases or performance results are supplied; this remains ongoing research.

At 07:10 Beijing time on October 20, a reader adds a suggestion for the same compute-kernel optimization direction, not a confirmed continuation of the same author's experiment: prime context with ten examples of hand-tuned assembly optimization, configure REA in Claude, Grok and Codex, have Claude decompile an already heavily optimized kernel and analyze it against the hardware instruction set, then request independent optimization ideas from other models. The opening suggests 10% faster kernels, but the conclusion asks readers to share results and supplies no benchmark or measured improvement. This is retained as a workflow idea, not a result. This collection executed no code and verified neither correctness, performance nor model agreement.

Neither original research nor added workflow reports optimization benchmarks; 10% is a reader's proposition, not a measurement.

## Sources

- [Original author's work-in-progress report](https://x.com/i/status/2110566660113625486)
- [October 20 reader addition: instruction-set comparison and multi-model optimization idea](https://x.com/i/status/2112320598403936339)

[中文](../rea-cpu-kernel-optimization.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
