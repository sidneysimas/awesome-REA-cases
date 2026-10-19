# BINNY: public beta of a multi-model reverse-engineering harness

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-19
Stage: Related project

BINNY's October 16 announcement introduces a public-beta agent harness for reverse engineers and security researchers: a framework organizing model tools and execution workflows. October 19 candidates from @ainotesus at 12:59 and @QingQ77 at 13:47 explain that BINNY is not the model. Users connect Claude, GPT, DeepSeek, Qwen or local models to read decompiled functions, strings and imports, producing a report draft through a triage/investigate/draft loop. The purpose is reducing repetitive binary research, not replacing human acceptance review.

This round located the public openbin-ai/binny repository and read the README corresponding to commit 000b6aca8c9d266b38252470102ac16c98575cd8, dated October 18 at 00:28 Beijing time. It documents STIX 2.1 malware classification, local Ghidra decompilation, per-step autosave/resume, token budgets, three autonomy levels and draft-report review. Go implementation and AGPL-3.0-or-later are project-documentation statements. The README retains older wording calling the repository private; platform status is not inferred from that. BINNY supports OpenBin/OpenAPK projects and local files. Local processing without upload does not mean the model provider receives no findings.

The README describes scripts running in Docker without networking, with read-only root and sample mounts, dropped capabilities and resource limits. Only documentation was checked: no installation, build, sample execution or container-boundary test was performed. Isolation safety, report accuracy, universal model compatibility and successful analysis of a specific target are not certified. This corrects the older entry's lack of a public project and license contents, without claiming a source-code implementation audit. REA remains unconfirmed. The supplementary README is earlier project background, not a new candidate post.

October 16 candidate snapshot: 96 likes, 3,548 views, 9 reposts; attention is not feature validation.

## Sources

- [BINNY public-beta announcement](https://x.com/i/status/2110767491286716525)
- [October 19 candidate: STIX, Ghidra and checkpoints](https://x.com/i/status/2112045894359027776)
- [October 19 candidate: Go harness, user-supplied models and budgets](https://x.com/i/status/2112057908573675756)
- [Public README: analysis loop, sandbox design and licensing statement](https://github.com/openbin-ai/binny/blob/000b6aca8c9d266b38252470102ac16c98575cd8/README.md)

[中文](../binny-agentic-reverse-harness.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
