# Slack's macOS Do Not Disturb state: a secondary REA report on native components and remote-web limits

Category: Applications and clients · REA
Record date: 2026-10-23
Stage: Needs verification

An REA article posted at 04:00:38 Beijing time on October 23, 2026 includes a concrete experiment report: it says developer Connor Turland inspected an installed Slack copy on October 20 to investigate desktop interaction with macOS notification settings, not clone the entire product. October 20 is the experiment date stated by the article, not the current candidate's publication date.

According to the article, the investigation identified relationships involving a native component checking the operating system's Do Not Disturb state, plus caching, timeout and inter-component communication details. Its explicit limit is that some relevant behavior lives in remotely served web code, not the local desktop package. Inspecting local artifacts therefore does not reveal all of Slack's server implementation. The concrete purpose is explaining notification behavior and local/remote responsibilities, not rebuilding a chat system.

The supplied material provides no original Connor article link, Slack version, symbol names, cache/timeout values, logs, source comparison or reproducible steps. Supplementary keyword searching did not locate the original experiment. This is therefore an unverified secondary report with a named researcher and identifiable target. The article's description of an independent experiment is not this collection's independent verification, and exact notification rules are not inferred. The rest of the article's general tutorial and REA self-package figures are not results of this Slack investigation.

Source published October 23, 2026, 04:00:38 Beijing time; reported experiment dated October 20, 2026, with no first-party original obtained.

## Sources

- [October 23 REA article recounting Connor Turland's Slack notification experiment](https://x.com/i/status/2113359897827938505)

[中文](../slack-macos-dnd-rea-secondary-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
