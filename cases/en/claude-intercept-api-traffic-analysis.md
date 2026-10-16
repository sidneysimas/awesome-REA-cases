# Claude Intercept: authorized HTTP/S captures for Claude Code analysis

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-16
Stage: Related project

An earlier candidate at 19:30 Beijing time on October 16 lists Claude Intercept among Ship Systems projects, describing decrypted computer traffic and undocumented APIs, with William Haesemeyer's involvement. It was previously deferred because the AI role and public project were unclear. A supplementary search now finds whaesemeyer/claude-intercept matching the name and author. Its public README explicitly describes an HTTP/S man-in-the-middle proxy built for Claude Code, with local capture, a live dashboard, SQLite storage, an /intercept skill and api-docs, summary and full exports for Claude to investigate request patterns and APIs. AI involvement is supported by this documented interface, not inferred from the name.

The README was read as supplementary material, not as independently tested functionality at the earlier candidate's timestamp. It requires proxy setup and trust in a local CA on authorized devices, warns that some certificate-pinned domains fail and that the dashboard binds to 0.0.0.0 and should not run on untrusted networks, and says leaving system proxy settings on after stopping the proxy disrupts connectivity. Thus the original claim about decrypting all traffic is not adopted. Local storage also does not mean content sent to a cloud model cannot leave the machine. The README specifies CC BY-NC 4.0, so open-source promotion does not imply unrestricted commercial licensing. Documentation establishes the intended use and AI interface, not successful interception, permission safety, privacy or analysis quality. Nothing was installed, no proxies or certificates changed and no credentials accessed. REA involvement is unconfirmed.

Follow-up from the October 16, 16:00–20:00 source window, not a newly fetched post in this window.
Public documentation only; CC BY-NC 4.0, certificate-pinning and LAN-exposure limitations retained from project statements.

## Sources

- [Earlier candidate: Ship Systems' Claude Intercept introduction](https://x.com/i/status/2111057177200738632)
- [Supplementary public README: Claude Code integration and security limits](https://github.com/whaesemeyer/claude-intercept)

[中文](../claude-intercept-api-traffic-analysis.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
