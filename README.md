# Awesome REA Cases

**English (default)** | [简体中文](README.zh-CN.md)

### Explore software and hardware with AI.

A curated collection of **reverse-engineering projects, experiments, and ideas**: revive old devices, rebuild apps, preserve games, and understand hidden behavior.

## 344 cases & projects

**Latest case update / maintenance:** October 17, 2026, 08:11 · Beijing time (UTC+8). Counts as of this update.

Updates **6× daily** · [Full index](INDEX.en.md) · [Browse categories](#browse-by-category)

Covers [REA](https://github.com/morluto/rea) and other AI-assisted work. REA connects coding agents to local reverse-engineering tools through CLI and MCP.

*Based on author and project reports; not independently reproduced here. Evidence and project status are recorded in each case.*

![Cumulative case collection growth, by day](assets/case-growth.en.svg)

## Recent picks

**10 worth reading**, selected for practical use, evidence, and recency—not an automated ranking. Dates refer to featured sources or author updates, not collection dates.

1. **[Plustek scanner & ThinkPad camera](cases/en/schaller-opticfilm-thinkpad-linux.md)** · `2026-10-16` — Use Windows reference behavior to improve Linux drivers. Published measurements also disclose low-light and exposure defects. `In progress`
2. **[Where NIST curve seeds came from](cases/en/nist-ecdsa-origin-claude-report.md)** · `2026-10-16` — Anthropic reports Claude traced public parameters to **lrand48 and timestamps**, publishing code and unresolved questions. **Not an ECDSA break**; not independently recomputed here. `Research report`
3. **[Gears of War 3](cases/en/gears3-ai-graphics-recompile.md)** · `2026-10-17` — AI-assisted Linux recompilation and graphics work. The author clarifies **mechanical PowerPC-to-C++ translation, not recovered original source**; the reported 4K WIP still drops frames in combat. `In progress`
4. **[ArkWeb: Spider-Man in Gotham](cases/en/arkweb-spiderman-arkham-report.md)** · `2026-10-03` — Run two owned games together, stream collision and composite the character. Public code and Claude setup guidance; **experimental, version-bound, REA use unconfirmed**. `In progress`
5. **[Computer + REA: five app demos](cases/en/computer-rea-five-app-rebuild-demos.md)** · `2026-10-16` — Design layouts, edit spreadsheets, process images, review contracts, and mix audio. **Official demos, not verified replacements** for Figma, Calc, Photopea, Harvey, or Audacity. `REA · Unverified`
6. **[Sonic 3D Blast: recreate the compiler first](cases/en/sonic-3d-blast-saturn-opus-port.md)** · `2026-10-16` — **A native port from decompiled code, not static recompilation**, according to the author. Visual defects remain; November 20 is a release plan. `In progress`
7. **[ReaCut](cases/en/reacut-jianying-open-editor.md)** · `2026-10-16` — An independent editor with project-reported exports and plugin tests. **Licensed assets and AI APIs remain bottlenecks**; signing and platform limits remain. `In progress`
8. **[LASRecomp](cases/en/links-awakening-claude-pc-port-report.md)** · `2026-10-15` — An AI-assisted Link’s Awakening desktop port. Requires the original game; beta crashes and untested platform support are documented. `Public project`
9. **[KEF LSX II volume keys](cases/en/kef-lsx-ii-volume-fixer.md)** · `2026-10-15` — A USB/LAN bridge improves desktop volume control without patching signed firmware. Latency figures are the author’s measurements. `Public implementation`
10. **[Test the CSV evaluator first](cases/en/rea-csv-evaluator-mutation-test.md)** · `2026-10-16` — Three deliberately broken exporters reportedly passed simple tests; **215 byte comparisons** exposed them. A useful acceptance-testing experiment, without published test inputs or code. `REA test`

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
| [Games & preservation](categories/en/games.md) | **76** |
| [Hardware & interoperability](categories/en/hardware.md) | **77** |
| [Applications & clients](categories/en/apps.md) | **158** |
| [Algorithms & feature recovery](categories/en/algorithms.md) | **33** |

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
