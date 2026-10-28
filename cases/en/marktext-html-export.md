# MarkText: a REA-assisted HTML export rebuild

Category: Applications and clients · REA
Record date: 2026-10-28
Stage: In progress

The author reports AI bots using REA to trace HTML-export behavior in a built MarkText application and rebuild the feature, claiming 17 passing tests with one Windows check still open. Evidence consists only of the original-post account and its claimed video receipts. This review did not watch the video, run the project or independently retest, so neither complete compatibility nor Windows validation is established.

At 22:10:09 Beijing time on October 28, 2026, another author says REA investigated export in the Electron Markdown editor MarkText that week, scanning 2,477 files in 82 seconds. The reported path is file menu to main-process exportFile/exportPDF, then mt::response-export IPC, then renderer exportHtml.ts. The author says they opened the named files to check it. The post reports 637 limitations, 23,000 semantic unknowns and 115MB of evidence for a 6.4MB app, explicitly static analysis without execution. This is another user's account, not the same run as the earlier 17 tests. Files, commands, logs and version were not checked; named call paths do not establish dynamic behavior. Unverified promotional claims of 390,000 stars and six months of age are not adopted as facts.

Evidence boundary: author report; not independently retested
17 tests reported passing; Windows check still open
New October 28 candidate snapshot: 0 likes, 23 views, 0 reposts. Eighty-two seconds, 2,477 files and evidence sizes are that author's reports.

## Sources

- [Author's original post](https://x.com/i/status/2109839329933824026)
- [October 28: another user's static export-chain and manual-check report](https://x.com/i/status/2115446020561674428)

[中文](../marktext-html-export.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
