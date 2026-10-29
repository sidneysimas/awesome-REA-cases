# Claude Code status summaries: reported telemetry costs and a Bun timer hook

Category: Applications and clients · REA use unconfirmed
Record date: 2026-10-29
Stage: Related project

At 13:50:16 Beijing time on October 29, 2026, thinkszyg relays Flamerix AI's telemetry study of Claude Code background-agent status summaries. It claims agent_summary represented 16.4% of estimated spending in a week-long snapshot versus 15.7% for the main conversation, describing historical context sent about every 30 seconds to generate 3–5 status words. The problem is invisible auxiliary-request consumption, not main-task output quality.

Supplementary reading of public anthropics/claude-code issue #86879, opened August 15 before this window, finds a four-hour session on 2.1.233/darwin 25.6.0 with 27 subagents. Of 1,496 requests, 339 were summaries, about 22.7%; they represented 18.0% under the author's Opus-price weighting and produced 21,966 output tokens. The table's 22.2% raw-token share and 22.7% request share measure different things. The issue analyzes a separate bundle call that denies tools and skips the main transcript, requesting an official switch. It remained open when read, which is not official endorsement of every causal claim.

The candidate also describes an approximately 80-line, MIT-licensed Flamerix Bun preload hook that intercepts the summary timer, reportedly reducing summary requests to zero in tests on 2.1.257–2.1.312. The status panel stops refreshing; macOS was untested, Windows may not work and upgrades may invalidate it. The script and all measurements were not obtained and reviewed, so compatibility, licensing and zero-request results remain secondhand. Dollar consumption is a list-price estimate, not an extra subscription charge, and does not directly establish an equivalent share of subscription limits.

This is a concrete reverse-engineering/telemetry project concerning an AI client. Sources do not specify AI assistance in conducting the research, so REA is unknown rather than inferred from Claude being the target. This collection did not access local telemetry, credentials or configuration, install a hook, stop processes or reproduce measurements.

Candidate snapshot: 0 likes, 117 views, 1 repost. The issue is earlier supplementary evidence.
The week-long 16.4% cost share and single-session 18.0% weighted share are different reports. Hook not reviewed or measurements independently repeated.

## Sources

- [thinkszyg relays Flamerix's cost analysis and Bun hook, October 29, 2026](https://x.com/i/status/2115682610848714853)
- [Supplementary: August 15 public issue #86879, session table and 2.1.233 bundle analysis](https://github.com/anthropics/claude-code/issues/86879)

[中文](../claude-code-agent-summary-telemetry-timer-research.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
