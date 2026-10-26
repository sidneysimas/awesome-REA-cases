# Borer: a Rust reverse-engineering engine for AI agents with emulator comparisons

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-26
Stage: Related project

At 06:21 Beijing time on October 26, 2026, prism (@dear_prism) introduced Borer, a Rust engine written from scratch to give AI agents a reverse-engineering tool surface without Ghidra, IDA or Binary Ninja underneath. It has its own loader, lifters, emulator and decompiler, keeps MCP answers compact, and compares decompiled results against emulation. The author says every component is still being improved, not that correctness has been certified for all architectures.

Supplementary lookup found imjustprism/borer and read its README at fixed commit 2e5b49b5a665f0b1772e4122ac84fd11c570d950, dated October 26 at 11:35:23 UTC, or 19:35 Beijing time, after the strict window. This is later documentation, not proof that every feature existed at 06:21. It describes one Rust binary acting as an MCP server without arguments or a CLI with arguments: load a target, triage it, find functions by strings/symbols, decompile, then follow cross-references and data flow. Listed inputs include PE, ELF, Mach-O, raw code and memory dumps. Filtered/paged lists, delta responses and explicit checking scope aim to reduce context overhead.

The README says decompiled C blocks are run from seeded states and compared against machine code, leaving unmodeled instructions as asm markers. This is a project validation design, not a complete formal proof or a result rerun by this collection. It does not guarantee correct analysis of arbitrary binaries or crash-free handling of hostile inputs. Explicit limits include no 32-bit ARM emulation; refusal of taint/layout/solve/unpack/devirt on arm64; no .NET IL or Swift decompilation; Windows-only live reading without breakpoints or writes; and gotos for unproven control structures.

It is included as a related AI reverse-engineering tool project, not a confirmed REA engine. No installer was executed, MCP configuration changed, dependency installed, target loaded or project test run. Speed, memory use, security and recovery rates were not independently checked. The later documentation uses AGPL-3.0-only while noting versions 0.1.0/0.1.1 were MIT; the current license is not projected onto every historical version.

Related tool project, not installed or run; emulator comparisons are a scoped project design, not proof of universal equivalence.
The fixed README postdates the window. Architecture/ARM and live-access limitations are retained without backdating capabilities or licensing.

## Sources

- [Window candidate: prism introduces Borer, October 26, 2026 at 06:21 Beijing time](https://x.com/i/status/2114482427477246149)
- [Post-window supplementary README and limits at fixed commit 2e5b49b, October 26, 2026 at 19:35 Beijing time](https://github.com/imjustprism/borer/blob/2e5b49b5a665f0b1772e4122ac84fd11c570d950/README.md)

[中文](../borer-rust-agent-first-re-engine.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
