# Linux MPTCP: a report of internal Claude research on a kernel-network race chain

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-29
Stage: Analysis test

At 09:33:04 Beijing time on October 29, 2026, Ummon's five-target report relays Anthropic's Linux networking investigation. The target is a kernel path exposed through a multipath-TCP listener. The account outlines a race-induced use-after-free, a kernel-address disclosure and callback control-flow influence, claiming root command execution without credentials or user interaction. This records research shape only, without triggering packets, exploit code or instructions.

Supplementary reading of the October 27 official article confirms the project's reported demonstration: about 48 minutes to obtain an address and another five minutes to reach command execution, with a lost race failing the handshake rather than crashing the system. It labels the issue CVE-2026-98432 and says upstream and all maintained stable branches were patched. These timings are not universal time-to-success or performance benchmarks; the listener requirement does not imply that every Linux system is exposed. The earlier official document supplements the candidate only.

The internal model is unnamed and starts with initial human prompting. The article describes coordinated disclosure and reports no in-the-wild exploitation, which is not assurance that no attackers exist. This collection did not read vendor/kernel advisories, builds or logs, run an exploit or send packets. Included as a project analysis test, without independent confirmation of CVE, remediation or impact. REA is unspecified.

Shared candidate snapshot: 0 likes, 157 views, 0 reposts. The 48-minute and five-minute timings are from the relayed project demonstration.
CVE-2026-98432 and patch status were not independently checked. No reproduction or network operation here.

## Sources

- [The Linux MPTCP investigation in Ummon's full report, October 29, 2026](https://x.com/i/status/2115617884533907835)
- [Supplementary original research: Anthropic's October 27 Linux section](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude#5-zero-click-remote-code-execution-in-linux)

[中文](../anthropic-internal-claude-linux-mptcp-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
