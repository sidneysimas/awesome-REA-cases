# ReAgent: Ghidra evidence and a reverser/checker loop reconstruct C/C++; gates are not equivalence proofs

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-27
Stage: Related project

At 07:00:01 Beijing time on October 27, 2026, TechVerser (@realfxw) introduces ReAgent: collect assembly, cross-references, structures, vtables, control flow and strings through Ghidra, have a reverser generate code and a checker inspect it, then apply build and test gates. The goal is checkable C/C++ functions from compiled programs, not treating pseudocode as original source. Original-post lookup confirms attribution and full text; a public repository search identifies Dryxio/reagent.

Supplementary static reading pins its README to d12cea338c61898b06a86fe8adb25275fa9d5615, committed at 04:39:30 Beijing time on September 10, 2026, before the candidate. Lookup time is not a new release date. The document supports Claude, Codex and OpenAI-compatible models, optionally different models for the two roles. It uses ghidra-ai-bridge for evidence including high P-code, CFG and nearby source, produces candidates in bounded rounds and retains reports, logs and a knowledge graph.

Configured success conditions include checker PASS, no strong structural mismatch, build/test/runtime acceptance and RED/YELLOW parity policy. Missing validation commands default to UNKNOWN and strict configurations reject that state; disabling validation does not make output build-verified. Candidates go to reports and overlays, with project copies available for isolated validation, rather than automatically overwriting original source. Project-owner control of configured commands remains a trust prerequisite. Review by the same or a different model is not independent third-party reproduction.

The README explicitly disclaims proof of semantic or binary equivalence; function-group coverage is limited to the selected inventory and acceptance policy. Results still depend on target context, symbols, types, available evidence and the local Ghidra environment. The candidate's 2.1k stars were not independently checked. This collection installed no dependencies, executed no target, compiled nothing and reran no tests. Included as a related public method/tool, without a sample success rate. ReAgent is distinct from morluto/rea; REA is not mentioned.

Candidate snapshot: 2 likes, 96 views, 0 reposts. Later engagement is not backfilled, and 2.1k stars is not independently accepted.
The pinned README predates the window and is used for static methodological checks, not independent execution or equivalence proof.

## Sources

- [TechVerser's ReAgent introduction, October 27, 2026 Beijing time](https://x.com/i/status/2114854592848490637)
- [Supplementary pinned README: Dryxio/reagent, committed September 10, 2026 Beijing time](https://github.com/Dryxio/reagent/blob/d12cea338c61898b06a86fe8adb25275fa9d5615/README.md)

[中文](../reagent-ghidra-reverser-checker-gated-reconstruction.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
