# Awesome REA Cases

**English (default)** | [简体中文](README.zh-CN.md)

**Explore software and hardware with AI: rebuild features, bridge protocols, and modernize legacy systems.**

Currently **277 cases and projects**. *Last maintained and counted: October 16, 2026, 12:33; continuous resolved-material case-evidence cutoff: October 15, 2026, 16:00 Beijing time (UTC+8).*

Public REA and AI reverse-engineering cases are tracked six times daily, screened and deduplicated. This review covers 132 supplied candidates from October 16, 08:00 to 12:00 Beijing time (start exclusive, end inclusive), plus 16 older unresolved sources. It adds 13 projects, author reports and concrete ideas, and clarifies that Preview's 47 checks were written and run by AI itself. New reading includes a Saturn port with historical compiler-workflow evidence, MoonBit debugger symbols, a Linux remote-control endpoint, and the limits of signature and structure-layout analysis. Earlier posts used for context are dated separately, not presented as new-window achievements. Twenty-seven sources still need clarification, including all 16 older leads; their earliest window starts October 15 at 16:00, so the continuous evidence cutoff stays there. Newer assessable work remains included with explicit evidence limits. Search coverage is bounded by keywords and pagination, not exhaustive; the cutoff does not imply independent validation. The maintainer reads and edits this homepage; the [complete index](INDEX.en.md) contains every accepted entry.

[REA](https://github.com/morluto/rea), Reverse Engineer Anything, lets coding agents call local reverse-engineering tools through CLI and MCP interfaces. This collection also covers other AI-assisted work and interoperability projects for AI tools.

## Recent picks: Top 10

Manually selected for recent attention, concrete use, and reading value—not a live leaderboard. Engagement figures are source-specific snapshots collected October 12–16, 2026, not live counts or proof of verified results. Dates below refer to source posts.

1. **[Negatives and cameras: give Claude a Windows reference to compare](cases/en/schaller-opticfilm-thinkpad-linux.md)** — Starting with family negatives, Schaller captures USB behavior for a newer Plustek 8200i, then improves a ThinkPad MIPI camera. Published measurements disclose the single-device sample, a low-light blue deficit and unresolved exposure issues. Patch review is not upstream merging. **Reported Oct 16 · Oct 15 original read as supplementary evidence · Other AI-assisted work · Author/project reports.**
2. **[Sonic 3D Blast: the compiler matters as much as the model](cases/en/sonic-3d-blast-saturn-opus-port.md)** — The author confirms Opus assistance. Earlier updates describe Claude recreating a Hitachi compiler environment, byte-matching work and a native Saturn-to-PC port that still has visual issues. **Oct 16 confirmation · July–October context · Other AI-assisted work · In progress; November 20 is a plan, not a shipped release.**
3. **[ReaCut: an editor with explicit export and validation boundaries](cases/en/reacut-jianying-open-editor.md)** — Jianying research informs an independent editor. Project records describe real video exports and plugin tests while documenting signing, platform and CI limitations. **Oct 15 · REA · In progress; project-reported validation.**
4. **[LASRecomp: Switch Link's Awakening on desktop](cases/en/links-awakening-claude-pc-port-report.md)** — The public project credits Claude Code with most work and requires the user's original game. Its beta documentation lists crash triggers and untested Linux ARM support. **Oct 15 · Secondary post: 144 likes · Other AI-assisted work · Not run here.**
5. **[A plate reader: investigate communication before declaring a repair](cases/en/plate-reader-filter-wheel-claude-repair.md)** — A filter wheel passed mechanical and optical checks but failed startup QC. The author says Claude worked out communication, reset firmware and added monitoring; device details, commands and clinical validation are absent. **Oct 15 · Other AI-assisted work · Author report, not medical-device safety certification.**
6. **[ScanSnap iX500: an OS upgrade need not retire the scanner](cases/en/scansnap-ix500-claude-mac.md)** — After the official Mac app stopped working, Jonas Wagner reports a Claude-built replacement with Wi-Fi scanning, the hardware button, OCR and blank-page handling. Protocol details are not supplied. **Oct 15 · 2 likes · Other AI-assisted work · Author report, not independently tested.**
7. **[KEF LSX II: volume keys that work better at a desk](cases/en/kef-lsx-ii-volume-fixer.md)** — A Claude-assisted USB passthrough and LAN volume bridge avoids patching signed firmware. The volume curve and roughly 2 ms added latency are author measurements. **Oct 15 · AI-assisted interoperability · Public implementation.**
8. **[Feishu: two accounts without constant switching](cases/en/feishu-dual-instance-codex-rea.md)** — After Codex/REA research, the author reports isolating a second copy's data and single-instance lock, with signature and directory checks. Local signing and disabled updates carry maintenance risks. **Oct 15 · REA · Author-tested, not independently reproduced.**
9. **[Electron Notes: the answer key matches, but the output grows](cases/en/rea-electron-notes-ipc-answer-key-test.md)** — Three static runs identify 4/4 channels, handlers and preload members. The author also reports 1.0 MB of JSON from 2.3 KB of source. This small-sample observation is not an accuracy guarantee for all Electron apps. **Oct 16 · REA · Author's analysis test, not independently rerun.**
10. **[MoonBit: make debugger symbols readable again](cases/en/moonbit-claude-debugger-demangling.md)** — Trying a language for a research project led to mangled debugger output. The author says Claude investigated the encoding and wrote a VSCode customDescriptionGenerator; code and tests are not supplied. **Oct 16 · Other AI-assisted work · Author report, not independently run.**

### Classic cases

- **[Universal Modder](cases/en/universal-modder.md)** — Investigate engines and asset formats to bring Minecraft content into GTA V and other games; recorded snapshot: **14,340 likes**. `Other AI-assisted work`
- **[Firefighter: DOS binary to Rust](cases/en/firefighter-rust.md)** — Recover Pascal logic and rewrite maintainable Rust, according to the author; recorded snapshot: **7,833 likes**. `Other AI-assisted work`
- **[Modern Warfare 2: multi-agent reconstruction](cases/en/mw2-decompilation.md)** — The author reports 17 agents, three months, and byte-level matches for 83% of functions; code is not public and has not been independently reproduced here. `Other AI-assisted work`
- **[Smart toilet from the Mac menu bar](cases/en/smart-toilet.md)** — Investigate Bluetooth communication for lid control; the author later reports extending the app to other home devices. `REA · Author-reported`
- **[An Apple TV remote on Linux](cases/en/siri-remote-linux.md)** — Bluetooth interoperability with a public implementation; recorded snapshot: **5,419 likes**. `REA unconfirmed`
- **[LG PlxNative](cases/en/lg-plxnative.md)** — Investigate the native media stack; the author reports user selection falling from about 30 seconds to 3 seconds. Recorded snapshot: **7,268 likes**. `Other AI-assisted work`

## Contents

- [Games and preservation](categories/en/games.md) (65)
- [Hardware and interoperability](categories/en/hardware.md) (63)
- [Applications and clients](categories/en/apps.md) (124)
- [Algorithms and feature recovery](categories/en/algorithms.md) (25)
- [Contribute a case (Chinese)](CONTRIBUTING.md) · [Maintenance (Chinese)](MAINTENANCE.md)

Category pages contain every accepted case, ongoing project, and concrete idea; the homepage does not expand the full listing. Labels such as Needs verification, In progress, Analysis test, and Related project do not indicate completed or independently verified results. Case details and category pages are available in English, with reciprocal Chinese links. Contribution and maintenance guides are in Chinese.

## Scope and license

Unofficial collection. Results are attributed to authors and project records, not independently reproduced here. Only original summaries and public links are curated; no proprietary software, game assets, keys, or private material are distributed.

Original summaries, curation data, and code use the [MIT License](LICENSE). Linked content retains its own rights. Ensure appropriate authorization before investigating or reproducing it.
