# kindle-ai-usage: Codex-assisted Kindle jailbreaking for an API-equivalent usage display

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-24
Stage: Needs verification

Three October 21–22, 2026 introductions to the You can just build things hardware community describe using Codex to jailbreak a ten-year-old Kindle into an AI usage display. It reportedly fetches an image from a Node.js service every six hours, shows month-to-date totals, month-end forecasts and source breakdowns, then sleeps. The goal is to reuse an e-reader's persistent, low-power display, not recover Kindle source code.

Supplementary lookup on October 26 found Kuberwastaken/kindle-ai-usage with matching characteristics. Static reading examined README at commit 19d9dd8, dated August 28, before the candidate window. It quotes @kuberwastaken saying Codex helped jailbreak a ten-year-old Kindle and documents the original KT3 route, FBInk, RTC wake alarms, Wi-Fi image fetches and suspend. Crucially, it reports API-equivalent list price, an estimate valued at API list prices, not paid subscription fees. The readers' description of AI-subscription spending must not be treated as billing evidence. The README lists local collectors for Codex, Claude Code, OpenCode and Gemini CLI, plus importers for Cursor, Claude API, Copilot, Gemini ledgers and other sources. It describes sending daily aggregates only and warns against counting mirrored histories or multiple sources twice. These are project-documentation statements; no actual sessions, bills or accounts were accessed.

The public repository includes a Node service and an agent skill that first require the exact Kindle model/firmware and current jailbreak-compatibility guidance, rather than assuming the original KT3 route works everywhere. Its six-hour collection schedule wakes the Kindle five minutes later; failed image fetches preserve the previous frame. A host must be awake at refresh time. A stock Kindle cannot join a Tailnet directly and needs a reachable private LAN or explicit gateway. No dependencies were installed, tests run or devices jailbroken here; forecast accuracy, battery life and cross-model success remain independently unverified. The older commit was read to establish identity and correct pricing semantics, not presented as a new release in the current candidate window.

Community accounts cross-checked against public project documentation; an October 24 candidate at 20:05 explicitly names @kuberwastaken, establishing the author identity, while its rekindle weather screen is a separate use, not merged here. The original KT3 route cannot be generalized to all Kindles, and no independent deployment was performed.
Values estimate API-equivalent list prices, not subscription bills; source and skill were located, but tests, battery life and actual bills were not verified.

## Sources

- [Hardware-community introduction, October 21, 2026](https://x.com/i/status/2112892660251795697)
- [Reported dashboard workflow, October 22, 2026](https://x.com/i/status/2113242014242287678)
- [Another community-project list, October 21, 2026](https://x.com/i/status/2112738503222349881)
- [README at an August 28 commit, statically read on October 26](https://github.com/Kuberwastaken/kindle-ai-usage/blob/19d9dd82167c961cc7c93bcafd0225859ddc6390/README.md)
- [October 24 corroboration explicitly identifying kuberwastaken](https://x.com/i/status/2113965002994733345)

[中文](../codex-kindle-ai-spending-dashboard-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
