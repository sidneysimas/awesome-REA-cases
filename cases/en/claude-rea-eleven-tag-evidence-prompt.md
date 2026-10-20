# An eleven-tag REA prompt: engine checks, evidence levels and negative-control tests

Category: Applications and clients · REA
Record date: 2026-10-20
Stage: Related project

At 13:22 Beijing time on October 20, @xmyttle (Myttle) introduces an eleven-tag prompt they wrote for Claude Code connected to REA. Users fill three slots: feature, application and path. The tags goal, role, scope, engine_check, inputs, evidence, spec, verify, report, rules and start structure the investigation. Its concrete aim is to avoid guessing first and rationalizing later: identify the required tools, mark every claim OBSERVED, INFERRED or UNKNOWN, and supply a test the checker must reject.

The author limits targets to owned or authorized software, excludes DRM, license and anti-cheat bypass, and requires an engine check and three-step plan before awaiting approval. This is a concrete workflow idea and prompt introduction, not an automated guarantee of authorization or correctness. The post names no tested application and supplies no full execution or negative-control rejection logs; this collection did not run the template. 'Not allowed to guess' does not establish zero hallucinations. REA is the proposed companion tool, not evidence of an official template.

## Sources

- [Myttle's eleven-tag prompt design and authorization boundaries](https://x.com/i/status/2112414005293985823)

[中文](../claude-rea-eleven-tag-evidence-prompt.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
