# MCP native-addon audit: Mika reports delayed exfiltration found with Claude/REA, incident unverified

Category: Applications and clients · REA
Record date: 2026-10-28
Stage: Needs verification

At 05:47:14 Beijing time on October 28, 2026, Mika (@mika_systems) says a free project-search MCP with about 2,000 stars had read sensitive files over four days. Claude Code allegedly noticed a sandbox-blocked unfamiliar domain and investigated with REA. The JavaScript appeared normal, but an undocumented 900 KB native .node addon allegedly contained about 2,300 functions: a cheaper model triaged them in about 40 seconds, Opus 5.5 read only six network-related functions, and 14 XOR strings were decoded. The author claims a child process started 1.4 seconds after initialization, read three paths outside the project, sent 3.1 KB as telemetry and activated only after 72 hours of uptime.

The author also says a file held the private key of a trading wallet with $4,200. Following Claude's advice, they moved funds from another device, seven minutes before an attempted drain of the old wallet, and later rotated AWS and SSH keys. All timings, amounts, function and exfiltration details are the author's narrative. Package name, version, hash, disassembly, domain, captures, transactions and rotation records are absent. This does not authenticate an attack, successful loss prevention or an accusation against any named MCP. Original-post lookup obtained the full text; a shortened candidate display was not grounds to discard the case.

At 05:48:30 the same author's reply provides an audit prompt: read-only inventory of MCPs, plugins, skills, hooks, commands and actually installed code; static checks of compiled files, networking, child processes, sensitive paths, obfuscation and delayed triggers; comparison of stated purpose and permissions; and evidence by file/line or function/address, ranked risks, remediation impact and permission before settings changes. It acknowledges limited strings/nm/objdump visibility if REA is absent. This supplements the method, not validation output for the alleged malicious sample, and does not establish that static analysis detects every hidden behavior. No prompt was executed, credentials read, or target installed or run here. Status remains unverified.

Main candidate snapshot: 17 likes, 511 views, 1 repost. Reply: 0 likes, 35 views, 0 reposts.
900 KB, 2,300 functions, 40 seconds, six functions, 14 strings, 1.4 seconds, three paths, 3.1 KB, 72 hours, four days, $4,200 and seven minutes are all author figures.

## Sources

- [Mika's REA/native MCP-addon incident account, October 28, 2026](https://x.com/i/status/2115198661625852047)
- [Same-author read-only audit prompt, 05:48 that day](https://x.com/i/status/2115198983249297803)

[中文](../mika-rea-mcp-native-addon-exfiltration-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
