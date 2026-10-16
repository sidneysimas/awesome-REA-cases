# macOS Preview: rebuilding with and without REA

Category: Applications and clients · REA
Record date: 2026-10-12

Preview is macOS's built-in image and PDF tool. Mahesh used rebuilding it to compare work with and without REA, saying plain Claude was faster while the REA version was closer to the original in zooming, sharing, rotation, annotation and saving. A Chinese article among the October 15 candidates further describes the two approaches: the REA side parsed CommonToolbar.plist, MainMenu.nib and private selectors, wrote a Swift implementation and reported 47 passing self-tests; the other side used general AppKit knowledge to generate 18 Swift files and fix its own bugs, delivering faster. The article supplies neither replayable source code nor uniform system tests. It supplements the comparison's narrative rather than independently reproducing it here or through a third party. Star counts, inferred private classes and speed differences are not adopted as general conclusions.

Posted: 2026-10-11 (UTC) | @maheshboda006
Engagement snapshot (2026-10-12): 5 likes | 494 views | 1 repost

## Sources

- [Author's original post](https://x.com/maheshboda006/status/2109154423712977359)
- [October 15 Chinese process account (not an independent reproduction)](https://x.com/i/status/2110613996382654771)

[中文](../preview-rebuild.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
