# Xiaomi exercise calorie accumulation: a report of DeepSeek investigation into repeat counting on refresh

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-22
Stage: Needs verification

At 13:07 Beijing time on October 22, 2026, LanzhiAI (@LanzhiAI) relays someone's use of DeepSeek to reverse-engineer a Xiaomi exercise algorithm. Repeated pull-to-refresh within one minute allegedly accumulates consumption again: 40 steps expected to count as 1.6 calories display as 8.28. The concrete target is an exercise app's calorie-accumulation and refresh logic, not actual energy expenditure caused by refreshing. The exact app name, version and platform are unspecified, so this is not merged with other Xiaomi health-export projects.

Supplementary replies at 13:18 and 13:34 suggest timestamp deduplication/idempotency as an explanation; the poster says they are waiting for packet captures or a full reproduction. These are hypotheses and an intention to obtain evidence, not proof that source was located or that the server trusts client data. The candidate attributes the investigation to DeepSeek but supplies no original researcher, prompt, decompilation output, test record or fix commit. This is an unverified report of a specific algorithm bug, not an independent reproduction. The post's colloquial fivefold characterization is not adopted as a measured conclusion. REA is not mentioned.

Candidate originally posted 2026-10-22T13:07:56+08:00; supplementary replies at 13:18:05 and 13:34:32 that day, Beijing time.

## Sources

- [Candidate: LanzhiAI relays the calorie-refresh issue](https://x.com/i/status/2113135243876319654)
- [Supplementary: commenter suggests idempotency and awaits reproduction](https://x.com/i/status/2113137794369700148)
- [Supplementary: poster awaits captures or full reproduction](https://x.com/i/status/2113141936542622180)

[中文](../xiaomi-motion-deepseek-calorie-refresh-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
