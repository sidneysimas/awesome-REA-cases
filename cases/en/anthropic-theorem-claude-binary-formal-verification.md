# Claude and Theorem: turning OSS-Fuzz binaries into Rocq no-crash proofs

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-23
Stage: Analysis test

Candidates posted at 08:29:18 and 09:24:12 Beijing time on October 23, 2026 recount Anthropic and Theorem's formal-verification research. This review located the official article through Anthropic's research directory and read it in full. Its original publication date is October 22; it is supplementary first-party evidence, not a new post in the current window. The goal is checking explicit security properties of compiled real-world open-source programs, not cloning interfaces or recovering original source. REA is not mentioned.

The team compiles existing OSS-Fuzz tests and libraries into RISC-V executables. Theorem's RISC-V instruction and Linux process semantics mechanically yield a specification that an entry point never crashes on any input below 64MB. Claude writes Rocq proofs; the external Rocq kernel checks that they satisfy that specification. The team reports patching encountered bugs and proving 239 entry points across 123 libraries in a few weeks, with about 180 million proof lines, a typical proof around 600,000 lines and a median target-binary length of 18,000 instructions. The model is not the verifier, and this collection did not independently rerun the checker.

Official examples include a decompressor counter underflow/out-of-bounds write requiring a specially laid-out input of around 20MB and rediscovery of CVE-2026-56132 in libexpat. One cpp-httplib proof also required a machine-code argument that libc++ red-black trees retain logarithmic depth, excluding stack overflow from recursive std::set destruction. The article separately describes x86-binary specification verification for Linux zlib and a Rust interpreter for a Python subset. Those are different experiments; their scale and behavioral-comparison figures are not folded into the 239-entry-point result.

Scope is strictly single-threaded, statically musl-linked RISC-V/Linux formal models with a fixed memory budget, covering modeled OS responses and memory layouts. Actual deployments commonly use x86/ARM and dynamic glibc. ASan does not detect every memory error, and the entry points do not cover whole libraries, dead code or callers misusing a library. Exact theorem statements, machine/OS semantics, Rocq and its underlying execution tools must be trusted. The proof checker cannot judge whether the specification matches reality.

Claude's patches cause specifications to be regenerated and reproved. The team acknowledges possible reward hacking by changing behavior, reporting patch penalties, extra credit for proofs of behavior changes and log audits as mitigations; this does not establish that every patch is equivalent. Only a subset of proofs and semantics is published, withholding proofs that could expose unpatched bugs. This review read the article only and downloaded or ran no proof, target program or dependency. This is a project-reported binary-security analysis experiment, not independent verification, complete correctness of all 123 libraries or elimination of every vulnerability.

First-party article originally dated October 22, 2026; candidates posted October 23, 08:29:18 and 09:24:12 Beijing time. The retrieval date does not replace the research date. 123 libraries, 239 entry points, about 180 million lines, a typical 600,000-line proof and an 18,000-instruction median are official reports; the checker was not independently run.
Below 64MB, single-threaded static musl RISC-V/Linux and a fixed memory budget; not bug-free whole libraries or guarantees for x86/ARM deployments.

## Sources

- [Candidate: Claude proofs, external Rocq checking and scope](https://x.com/i/status/2113427508008042669)
- [Candidate: YU recounts 239 entry points and bug discovery](https://x.com/i/status/2113441326612324670)
- [Supplementary first-party Anthropic/Theorem formal-verification research, October 22, 2026](https://www.anthropic.com/research/formal-verification)

[中文](../anthropic-theorem-claude-binary-formal-verification.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
