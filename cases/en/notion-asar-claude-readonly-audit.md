# Notion app.asar: a Claude read-only file and domain-string inspection

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-17
Stage: Analysis test

At 03:50 Beijing time on October 17, @ChristineAnd1 describes a manual baseline before installing REA: Claude was instructed to read the local Notion app.asar only, without running or editing the app, and the author says nothing left the machine. The reported 6.8 MB package contains 147 files, including 58 JavaScript files, 47 distinct domains written into code, and one Sentry ingest error-reporting address mentioned once. Most domains are reportedly library documentation or links; a domain hidden behind an unresolved short link appears 123 times, and the next actual domain appears 11 times. The author interprets the client as a website shell. The hidden domain is unidentified and is not guessed. Crucially, the author says they do not yet know what is sent or when: a string is a possible destination, not evidence of a request. A second app and comparison with REA remain plans, not completed experiments. This has a different goal from the existing Notion clipboard call-chain case. This collection obtained no ASAR, counting script, image data or network validation and does not independently confirm the counts, package completeness or the claimed no-egress execution constraint.

147 files, 58 JS files, 47 domains and occurrence counts of 123 and 11 are author counts, not packet captures.
The reported phase did not use REA; cross-app and REA comparisons remain planned.

## Sources

- [Author's read-only static Notion baseline experiment](https://x.com/i/status/2111182893313613877)

[中文](../notion-asar-claude-readonly-audit.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
