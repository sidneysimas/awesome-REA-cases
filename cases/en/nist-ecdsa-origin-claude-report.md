# NIST ECDSA curves: Claude traces the generation of public parameters

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-17
Stage: Analysis test

Candidates at 04:59 and 07:05 Beijing time on October 17 discuss Claude tracing NIST ECDSA parameters. ECDSA is used for digital signatures; the question here is not private-key recovery but the provenance of curve-generation seeds supplied by the NSA and published in NIST standards. A supplementary reading of Anthropic's October 16 original research found the team's report that an internal research model identified the P-192, P-224, P-256, P-384 and P-521 seeds in under half an hour as outputs of the C library's lrand48 generator initialized with Unix timestamps. The method scans adjacent outputs and high-bit patterns, enumerates hidden bits, uses LLL lattice reduction to recover truncated-generator states and reverses them to srand48 initialization. The article provides generation code and outputs: for example, P-256 corresponds to 1997-08-16 01:52:34 UTC and candidate 1842. This collection did not execute that code.

The research separately links the base points of P-192 and five ANSI example curves to FreeLIP's zrandom, initialized with small integers and skipping seven outputs. That is distinct from the lrand48 curve-seed finding; loose conflation in candidate commentary is corrected here. The original retains unanswered questions about the B-163 seed, several other base points and why some viable candidates were skipped, so not all parameter origins are explained. Anthropic explicitly says this is not a cryptographic break, new attack or curve weakness and calls for no change in use. The half-hour duration and donation of the $36,864 bounty to ISRG are team reports. Algorithms and project-reported outputs are public, but were not independently recomputed here. The October 16 article is supplementary primary evidence, not a new post in this window; contemporaneous REA popularity does not establish REA involvement.

Original research dated 2026-10-16; in-window candidates dated 2026-10-17; reproduction code was not independently executed.
lrand48 explains curve seeds and FreeLIP explains some base points; neither means recovery of signing keys or an ECDSA break.

## Sources

- [October 17 post on NIST curve origins](https://x.com/i/status/2111200317866172887)
- [October 17 discussion of generators and public parameters](https://x.com/i/status/2111231968549666836)
- [October 16 Anthropic original research, reproduction code and open questions](https://www.anthropic.com/research/ecdsa-curve-origins)

[中文](../nist-ecdsa-origin-claude-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
