# Hark iOS conversation loading: reported REA diagnosis of a timezone/WAF conflict

Category: Applications and clients · REA
Record date: 2026-10-28
Stage: Needs verification

At 10:28:53 Beijing time on October 28, 2026, xxxxxx (@xxx_cccv) reports Hark iOS failing to load conversations. The claimed cause is a timezone parameter in conversation requests triggering Cloudflare WAF, while the web client omits it and works. The author credits REA reverse analysis and suggests rewriting requests with Loon or Quantumult X to remove the parameter, attaching a configuration image. Lookup confirms attribution and the image attachment, not its configuration contents.

The goal is understanding mobile/web request differences and restoring conversation reading without rebuilding the whole client. Hark revision, complete requests/responses, WAF logs, rules, configuration text and post-fix comparisons are absent. Cause and workaround remain author reports, not a confirmed Cloudflare-rule defect or universal fix. Authentication bypass, access to others' conversations and a server-side Hark fix are not inferred. REA analysis is explicit, but the model is unspecified. This is a different fault target from the existing Hark agent-framework research case. No account was accessed, rewritten request sent or client run here. Status remains unverified.

Candidate snapshot: 0 likes, 310 views, 0 reposts. WAF attribution and the parameter-removal workaround were not independently tested.

## Sources

- [Hark iOS timezone fault and REA attribution, October 28, 2026](https://x.com/i/status/2115269542159224846)

[中文](../hark-ios-timezone-rea-waf-diagnosis.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
