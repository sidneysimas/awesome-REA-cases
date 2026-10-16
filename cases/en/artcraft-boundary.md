# ArtCraft: not proven Adobe or Office reverse engineering

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-13
Stage: Related project

ArtCraft has circulated as an alternative direction for creative software. Its website says its software is written from scratch in Rust, with several products in early testing or development. Popular posts cannot be read as 'AI has completely reverse-engineered Adobe.' It is included as a related AI software-reconstruction project rather than a completed reverse-engineering result. The already included WordCraft, GridCraft and DeckCraft rebuild Word-style word processing, Excel-style spreadsheets and PowerPoint-style slide software, offering the corresponding Office file formats and MCP control; their public READMEs still mark them alpha. October 12 brought specific PhotoCraft interoperability and validation material: its public README says the PSD implementation uses Adobe's public specification, and the UI, CLI, JSON and MCP share over 500 commands. The project reports matching rendered output after opening and saving 307 of 309 psd-tools samples, not byte-identical files in all cases. PhotoCraft remains early alpha and cannot be presented as a professional everyday Photoshop replacement or evidence that Adobe was decompiled. In the October 13, 2026, 04:00–08:00 window, one user reported trying PhotoCraft and specifically criticized non-floating panels, opaque color management, missing compression and other save-format options, slow PSD opening, active-image focus/mask readings and text controls, finding it unsuitable for professional work. This is one user's experience and opinion, not an official admission, a reproduction by this collection or a conclusion about all versions. It supplements existing early-alpha limitations without changing the boundary: Rust reconstruction from scratch, not established decompilation of Adobe.

Another third-party post on 2026-10-14 says PhotoCraft and related projects are rebuilding the Adobe suite with similar reverse-engineering workflows and explicitly mentions REA. The poster's identity is unconfirmed, so this is not confirmation from PhotoCraft's author. This batch did not verify the claim or add implementation or test evidence, and it does not expand conclusions about project capabilities or REA's contribution.

Office follow-up posted: 2026-10-12T14:33:01+08:00 (Beijing time)
Office follow-up engagement snapshot (2026-10-12): 0 likes | 19 views | 0 reposts
PhotoCraft follow-up posted: 2026-10-12T16:08:50+08:00 (Beijing time)
PhotoCraft follow-up engagement snapshot (2026-10-12): 2 likes | 69 views | 0 reposts
Follow-up posted: 2026-10-13T05:58:20+08:00 (Beijing time)
Additional evidence: specific third-party usage feedback; software not independently run.
New usage report at 20:48 on October 15: the poster says all 13 apps from the website were installed on Ubuntu and opened. This is only a launch experience, not proof of complete functionality. The poster also recounts a maintainer saying on Hacker News that they do not decompile binaries, prohibit Ghidra on the team, and use public information and observed behavior for clean-room reconstruction. This collection did not additionally check the original HN statement, so it remains secondhand; launch, method and legal boundaries are not upgraded to independent acceptance.
2026-10-14: third-party post claims PhotoCraft uses an REA-like reverse-engineering workflow; poster identity unconfirmed, not project-author confirmation, not independently verified.
October 15, 16:00–20:00 follow-up: a new circulating post describes public PSD/Office specifications, observed button behavior and pixel-by-pixel comparison with Photoshop renders as the reconstruction approach, and claims independently implemented video codecs. Public specifications and implementation from scratch do not mean Adobe decompilation. Pixel validation and codec scope remain that post's account, not proof of suite-wide compatibility, a legal guarantee or tests by this collection. Its star-count promotion is not a new engagement snapshot.

## Sources

- [Original record](https://x.com/iamdavidhill/status/2107248003543384170)
- [Official website status](https://getartcraft.com/apps)
- [This review: WordCraft introduction](https://x.com/realfxw/status/2109465865221550341)
- [WordCraft project and development stage](https://github.com/storytold/wordcraft)
- [This review: Office reconstruction introduction](https://x.com/OLD9Gaming/status/2109532775170859138)
- [GridCraft project and stage](https://github.com/storytold/gridcraft)
- [DeckCraft project and stage](https://github.com/storytold/deckcraft)
- [This review: PhotoCraft file interoperability and agent control](https://x.com/i/status/2109556887645479114)
- [PhotoCraft project testing definitions and early-alpha limits](https://github.com/storytold/photocraft)
- [This window: third-party PhotoCraft usage experience](https://x.com/i/status/2109765636750532915)
- [Third-party post: claimed PhotoCraft REA workflow (poster identity unconfirmed, not author confirmation)](https://x.com/i/status/2110249246138245143)
- [This October 15 window: account of format specifications and validation workflow](https://x.com/i/status/2110655957436965228)
- [October 15, 20:48: Ubuntu installation experience and secondhand non-decompilation boundary](https://x.com/i/status/2110714534591713611)

[中文](../artcraft-boundary.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
