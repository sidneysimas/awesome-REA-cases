# Awesome REA Cases

**English (default)** | [简体中文](README.zh-CN.md)

### Explore software and hardware with AI.

A curated collection of **reverse-engineering projects, experiments, and ideas**: revive old devices, rebuild apps, preserve games, and understand hidden behavior.

## 277 cases & projects

**Collection updated:** October 16, 2026, 12:33 · Beijing time (UTC+8)

Updates **6× daily** · [Full index](INDEX.en.md) · [Browse categories](#browse-by-category)

Covers [REA](https://github.com/morluto/rea) and other AI-assisted work. REA connects coding agents to local reverse-engineering tools through CLI and MCP.

*Based on author and project reports; not independently reproduced here. Evidence and project status are recorded in each case.*

## Recent picks

**10 worth reading**, selected for practical use, evidence, and recency—not an automated ranking. Dates refer to featured sources or author updates, not collection dates.

1. **[Plustek scanner & ThinkPad camera](cases/en/schaller-opticfilm-thinkpad-linux.md)** · `2026-10-16` — Use Windows reference behavior to improve Linux drivers. Published measurements also disclose low-light and exposure defects. `In progress`
2. **[Sonic 3D Blast: recreate the compiler first](cases/en/sonic-3d-blast-saturn-opus-port.md)** · `2026-10-16` — The author credits Claude/Opus with compiler-environment research and a native Saturn-to-PC port. Visual issues remain; **November 20 is a plan, not a release**. `In progress`
3. **[ReaCut](cases/en/reacut-jianying-open-editor.md)** · `2026-10-15` — An independent editor informed by Jianying research, with project-reported video exports and plugin tests. Signing and platform limitations remain. `REA`
4. **[LASRecomp](cases/en/links-awakening-claude-pc-port-report.md)** · `2026-10-15` — An AI-assisted Link’s Awakening port for desktop. Requires the original game; beta crashes and untested platform support are documented. `Public project`
5. **[A plate reader brought back to work](cases/en/plate-reader-filter-wheel-claude-repair.md)** · `2026-10-15` — Claude reportedly investigated communication and reset firmware after a startup fault. **No independent or clinical validation.** `Author report`
6. **[ScanSnap iX500](cases/en/scansnap-ix500-claude-mac.md)** · `2026-10-15` — A reported Claude-built replacement Mac app with Wi-Fi scanning, hardware-button support, and OCR. Protocol details and independent tests are absent. `Author report`
7. **[KEF LSX II volume keys](cases/en/kef-lsx-ii-volume-fixer.md)** · `2026-10-15` — A USB/LAN bridge improves desktop volume control without patching signed firmware. Latency figures are the author’s measurements. `Public implementation`
8. **[Two Feishu accounts on one Mac](cases/en/feishu-dual-instance-codex-rea.md)** · `2026-10-15` — Codex/REA research supports isolated app copies. Local signing and disabled updates bring maintenance risks. `Author-tested`
9. **[Electron Notes: accuracy has an output cost](cases/en/rea-electron-notes-ipc-answer-key-test.md)** · `2026-10-16` — The author reports **4/4 channels** identified, but **1.0 MB JSON from 2.3 KB source**. A small static-analysis sample, not a general accuracy guarantee. `REA test`
10. **[MoonBit: readable debugger symbols](cases/en/moonbit-claude-debugger-demangling.md)** · `2026-10-16` — Claude reportedly investigated symbol encoding and wrote a VSCode display helper. **Code and tests are not supplied.** `Author report`

## Classic cases

- **[Universal Modder](cases/en/universal-modder.md)** — AI-assisted cross-game mods, including Minecraft content in GTA V.
- **[Firefighter](cases/en/firefighter-rust.md)** — Recover Pascal logic from a DOS binary, then rewrite it in Rust, according to the author.
- **[Modern Warfare 2](cases/en/mw2-decompilation.md)** — Author-reported multi-agent reconstruction; **83% function byte matches**, no public code or independent reproduction here.
- **[Smart toilet from the Mac menu bar](cases/en/smart-toilet.md)** — Author-reported Bluetooth research and home-device control.
- **[Apple TV remote on Linux](cases/en/siri-remote-linux.md)** — Bluetooth interoperability with a public implementation; REA use unconfirmed.
- **[LG PlxNative](cases/en/lg-plxnative.md)** — Native Plex client; user-selection time reportedly falls from **30 seconds to 3 seconds**.

## Browse by category

| Category | Entries |
| :--- | ---: |
| [Games & preservation](categories/en/games.md) | **65** |
| [Hardware & interoperability](categories/en/hardware.md) | **63** |
| [Applications & clients](categories/en/apps.md) | **124** |
| [Algorithms & feature recovery](categories/en/algorithms.md) | **25** |

[**View all cases →**](INDEX.en.md) · [Contribute (中文)](CONTRIBUTING.md) · [Maintenance (中文)](MAINTENANCE.md)

<details>
<summary><strong>Update & evidence notes</strong></summary>

- **Continuous resolved-material cutoff:** October 15, 2026, 16:00, Beijing time. Older unresolved sources can hold this cutoff back while newer entries are added; it is not a verification date for every project.
- Searches run six times daily with keyword and pagination limits; coverage is not exhaustive. Source dates, evidence boundaries, and any engagement snapshots are recorded in case details.
- Full descriptions, sources, and language switching are available on every case page.

</details>

## Scope & license

**Unofficial collection.** Original summaries and public links only; no proprietary software, game assets, keys, or private material.

Original curation and code: **[MIT](LICENSE)**. Linked work retains its own rights; use legally obtained targets and check the relevant permissions.
