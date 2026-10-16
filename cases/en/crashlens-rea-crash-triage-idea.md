# crashlens: connecting REA crash triage to coding agents

Category: Applications and clients · REA
Record date: 2026-10-16
Stage: Related project

On October 16, @rae1101x (Minglei) proposes a crash-triage Skill beside Hermes's reverse-engineer-anything for core dumps, panics and sanitizer reports, describing it as read-only and compatible with pinned rea-agents@6.4.0, and offering to submit a PR. At 19:54 the author describes the wider aim of explaining production crashes, exceptions and bugs when logs are insufficient, explicitly calling it early. A supplemental reading of the same thread's 16:13 post establishes that the author already says crashlens was built on REA; it is not merely an unstarted idea. That supplemental original is not an extra candidate.

This review read the public mingleiw/crashlens README. The project calls itself an early prototype supporting Linux x86-64 core dumps, multilingual stack traces and sanitizer reports, assembling failing frames, causes, preceding logs, optional source attribution and input hashes. It provides a Claude Code Skill and three read-only MCP tools; native core-dump analysis also needs REA. Documentation says it never runs the analyzed program and basic analysis is offline; optional --ai sends the report to Anthropic for a proposed fix. 'Read-only' therefore does not mean no outbound data when that option is enabled. Only documentation and project existence were checked, with no installation or execution, independent crash-diagnosis accuracy or production acceptance. An offer to submit a Hermes PR and willingness to review it do not establish submission, merge or official release. This is retained as a public related project.

Candidate updates: 2026-10-16 19:11 and 19:54 Beijing time.
Public documentation is supplemental evidence read this review; prototype capabilities are project claims, not independent reproduction, and Hermes integration remains proposed.

## Sources

- [Candidate: author's proposed Hermes crash-triage Skill](https://x.com/i/status/2111052456151154858)
- [Candidate: production-debugging vision and early status](https://x.com/i/status/2111063236355498247)
- [Same-thread 16:13 project introduction (supplemental source)](https://x.com/i/status/2111007641715786116)
- [Public crashlens project and README (read-only inspection this review)](https://github.com/mingleiw/crashlens)

[中文](../crashlens-rea-crash-triage-idea.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
