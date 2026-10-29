# Kuna: Dopax describes an agent-facing Rust decompiler with WASM access

Category: Applications and clients · REA use unconfirmed
Record date: 2026-10-29
Stage: Related project

At 09:19:57 Beijing time on October 29, 2026, Dopax (@tensorstaff) introduces Kuna in an open-source roundup as an agent-facing Rust decompiler ported from Ghidra and subsequently developed independently. The intended use is binary analysis through CLI, browser WASM or a Ghidra backend, not a completed reconstruction of a particular application.

Supplementary reading of Noelo-Lab/kuna's public README confirms an experiment in agent-driven decompiler refinement, with phased design, natural-language specifications, configurable features and skills for Claude Code/Codex/OpenCode. It says browser WASM processes locally without uploading the binary. The Ghidra GUI plugin does not support every native feature; headless use does not automatically load GUI plugins, and a separate backend replacement is project-tested with Ghidra 12.1.2/REA 3.1.0. This confirms documentation, not independent privacy or compatibility validation.

The post claims approximately three minutes for 19MB, a leading optimized-C DecBench position and 731 stars as of October 29. The README also makes performance claims and describes regression data with 83 files/675 assertions plus several test gates. These are not independently rerun results. Benchmark configurations, actual inputs and logs were not checked, so matched-condition speed, semantic correctness and complete source recovery are not inferred. The README was read on October 29 as supplementary project evidence only. The tool was not run, and compatibility documentation alone does not establish that REA built the project.

Candidate snapshot: 0 likes, 23 views, 0 reposts. The 731 stars and performance figures are roundup claims, not measurements by this collection.

## Sources

- [Dopax's roundup including Kuna and SuperGhidra, October 29, 2026](https://x.com/i/status/2115614583184638042)
- [Supplementary project README: agent-refinement goals, interfaces and regression scope, statically read October 29](https://github.com/Noelo-Lab/kuna/blob/main/README.md)

[中文](../kuna-agent-rust-decompiler-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
