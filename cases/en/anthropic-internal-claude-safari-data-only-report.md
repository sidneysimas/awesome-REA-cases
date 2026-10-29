# Safari: a report of an internal Claude model's data-only same-origin bypass

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-29
Stage: Analysis test

At 09:33:04 Beijing time on October 29, 2026, Ummon's five-target report relays Anthropic's Safari investigation. After initial human prompting, an unnamed internal model reportedly combines a JavaScriptCore TypedArray use-after-free, a Gigacage boundary bypass and WebContent IPC issues into access to history, cookies and session databases, disabling the same-origin policy. The target is cross-page data isolation, not Safari remote code execution.

Supplementary reading of the official article published October 27 confirms a data-only chain requiring no arbitrary code execution, with some individually intended behaviors exploitable only in combination. The official text says Apple acknowledged the report on receipt day and implemented a fix promptly, now available to users; it does not necessarily say patching finished that same day. This earlier official material supplements the candidate and is not newly published in this window.

This collection did not read Apple advisories or source, run a demonstration or access user history or sessions. An unnamed research model is not an identified released Claude version, prompting is not full autonomy and REA is unspecified. Patch status, affected scope and test conditions remain project reports, not independent reproduction.

Shared candidate snapshot: 0 likes, 157 views, 0 reposts. A same-origin bypass is not upgraded to arbitrary code execution.
Vendor acknowledgment and patching are attributed to the report. No independent validation or access to session data.

## Sources

- [The Safari data-only chain in Ummon's full report, October 29, 2026](https://x.com/i/status/2115617884533907835)
- [Supplementary original research: Anthropic's October 27 Safari section](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude#2-a-one-click-exploit-chain-in-safari)

[中文](../anthropic-internal-claude-safari-data-only-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
