# Windows QUIC: a report of internal Claude binary research with Ghidra

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-29
Stage: Analysis test

At 09:33:04 Beijing time on October 29, 2026, Ummon describes Anthropic using an unreleased internal model to investigate Windows kernel QUIC. Supplementary reading of the October 27 official text confirms a method of providing the executable, using tools such as Ghidra to reverse it, writing annotated C, comparing reconstructed behavior against the binary for correctness, and then studying flaws. A prompt to prioritize higher-risk issues surfaced this remote issue, a more specific method chain than merely claiming AI found a bug.

The official account describes an out-of-bounds read in native Windows HTTP/3 kernel QUIC that crashes and restarts a listening server, labels it CVE-2026-33096 and says Microsoft resolved it. This is remote denial of service, not remote code execution. 'Likely several million servers' is a project estimate, not a confirmed affected-host count. The investigation starts with human prompting, not human-free autonomous discovery.

The October 27 article supplements the October 29 candidate and is not newly published in this window. This collection did not read Microsoft advisories, the exact binary build, C file or execution logs, independently rerun behavioral comparisons or send network traffic. CVE, remediation and scale estimates remain independently unverified. The internal model has no stated version and REA is unspecified. Triggering data is not included.

Shared candidate snapshot: 0 likes, 157 views, 0 reposts. CVE-2026-33096 is preserved from the text; its advisory was not independently checked.
Denial of service is not RCE. No reproduction was run and no network target accessed.

## Sources

- [The Windows QUIC binary investigation in Ummon's full report, October 29, 2026](https://x.com/i/status/2115617884533907835)
- [Supplementary original research: Anthropic's October 27 Windows section](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude#4-windows-remote-denial-of-service)

[中文](../anthropic-internal-claude-windows-quic-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
