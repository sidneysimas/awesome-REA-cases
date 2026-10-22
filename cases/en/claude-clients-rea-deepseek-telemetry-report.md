# Claude-client telemetry: Mac/Android investigation and a Linux REA/DeepSeek follow-up

Category: Applications and clients · REA
Record date: 2026-10-22
Stage: Analysis test

At 11:28 Beijing time on October 21, 2026, WquGuru (wquguru) says they used REA, DeepSeek Harness and flatkey model access on a Mac to study what they call Claude Code's Mac CLI, Mac app and Android app and compile proxy rules, specifying deepseek-v4-1-flash-1017.

The author reports Sift anti-fraud, SIM-country checks and ANDROID_ID plus Play Integrity and hardware keys on Android, claiming persistence after reinstall. They describe Sentry/Datadog telemetry and random non-hardware-bound IDs on Mac. Similar iOS behavior is explicitly that author's speculation. This entry preserves attributed investigative leads, not established equivalence between product names, SDK strings, actual uploads and hardware-identifier lifetimes.

In the current candidate at 15:30 on October 22, molang (@123molang) replies that REA and DeepSeek investigation of the Linux version produced almost the same conclusions as on Mac. A supplementary parent-thread read identifies the client context. At 15:57 the same author adds that the CLI is essentially shared and desktop code is highly shared, with GPT summarizing differences: the Linux SSH module reads interface IP/MAC information for network-change detection and reconnection, with no raw-value upload found in that chain; Mac has VPN diagnostic reporting during particular VM failures. These are limited author-reported observations and a model summary, not proof that all Linux clients never upload network information. Shared origin does not establish source-level equivalence. The 15:57 reply is supporting context, not a separate new candidate.

No exact package/build, hash, call chain, network capture or reinstall comparison is provided, and the full rules' shortened destination was not verified. This does not establish the most complete rules on the web, permanent hardware tracking, account-protection efficacy or guaranteed privacy. The original post includes model-gateway promotion, not a security assessment. No client was installed, account operated or traffic independently verified here.

New candidate originally posted 2026-10-22T15:30:55+08:00; supplementary author reply at 15:57:14 that day, Beijing time.

## Sources

- [WquGuru's REA/DeepSeek client-analysis and proxy-rule report](https://x.com/i/status/2112747723078422809)
- [Current candidate: molang investigates the Linux version with REA/DeepSeek](https://x.com/i/status/2113171225874960572)
- [Supplementary author reply: GPT summary of limited Linux/Mac differences](https://x.com/i/status/2113177847636648398)

[中文](../claude-clients-rea-deepseek-telemetry-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
