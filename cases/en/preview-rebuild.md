# macOS Preview: rebuilds with and without REA and the limits of self-tests

Category: Applications and clients · REA
Record date: 2026-10-16

Preview is macOS's built-in image and PDF tool. Mahesh used rebuilding it to compare work with and without REA, saying plain Claude was faster while the REA version was closer to the original in zooming, sharing, rotation, annotation and saving. An October 15 Chinese account further describes the two routes: REA parsed CommonToolbar.plist, MainMenu.nib and private selectors, wrote Swift and reported 47 passing self-tests; the other route used general AppKit knowledge to generate 18 Swift files and fix its own bugs, delivering faster. A new October 16 account lists image opening, cropping, color adjustment, exporting and slideshows, while explicitly saying AI wrote and executed the 47 tests and set their passing criteria. This importantly limits the self-test claim; it is not independent QA. The new post's 'one prompt, ten minutes' lacks replayable logs and is not verified total labor. Neither account provides replayable source or uniform system tests. They supplement the comparison's narrative, not an independent reproduction here or by a third party. Star counts, inferred private classes and speed differences are not adopted as general conclusions.

Posted: 2026-10-11 (UTC) | @maheshboda006
Original-post snapshot (2026-10-12): 5 likes, 494 views, 1 repost; new account's candidate snapshot (October 16): 0 likes, 130 views.
The source describes 47 AI-written, AI-run checks, not uniform system tests or independent reproduction.

## Sources

- [Author's original post](https://x.com/maheshboda006/status/2109154423712977359)
- [October 15 Chinese process account (not an independent reproduction)](https://x.com/i/status/2110613996382654771)
- [October 16 account of features and AI self-test criteria](https://x.com/i/status/2110935009775546599)

[中文](../preview-rebuild.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
