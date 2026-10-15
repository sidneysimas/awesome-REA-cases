# Awesome REA Cases

[中文（默认）](README.md) | **English**

**Explore software and hardware with AI: rebuild features, bridge protocols, and modernize legacy systems.**

Currently **203 cases and projects**. *Last maintained and counted: October 15, 2026, 20:14; continuous resolved-material case-evidence cutoff: October 15, 2026, 16:00 Beijing time (UTC+8).*

Public REA and AI reverse-engineering cases are tracked six times daily, screened and deduplicated. This review reads all 133 candidates from October 15, 16:00–20:00 Beijing time (start exclusive, end inclusive), adding 22 entries and supplementing eight existing ones. One source still needs clarification, so the continuous evidence cutoff remains at 16:00; assessable projects from this window are included. Keyword and pagination limits make this a bounded search, not exhaustive coverage. The cutoff does not imply independent validation of every project. The maintainer reads and edits this homepage; the [complete index](INDEX.en.md) contains every accepted entry.

[REA](https://github.com/morluto/rea), Reverse Engineer Anything, lets coding agents call local reverse-engineering tools through CLI and MCP interfaces. This collection also covers other AI-assisted work and interoperability projects for AI tools.

## Recent picks: Top 10

Manually selected for recent attention, concrete use, and reading value—not a live leaderboard. Engagement figures are source-specific snapshots collected October 12–15, 2026, not live counts or proof of verified results. Dates below refer to source posts.

1. **[ReaCut: an editor with explicit export and validation boundaries](cases/reacut-jianying-open-editor.md)** — Jianying research informs an independent editor. Project records describe real video exports and plugin tests while documenting signing, platform and CI limitations. **Oct 15 · REA · In progress; project-reported validation.**
2. **[LASRecomp: Switch Link's Awakening on desktop](cases/links-awakening-claude-pc-port-report.md)** — The public project credits Claude Code with most work and requires the user's original game. Its beta documentation lists crash triggers and untested Linux ARM support. **Oct 15 · Secondary post: 144 likes · Other AI-assisted work · Not run here.**
3. **[ScanSnap iX500: an OS upgrade need not retire the scanner](cases/scansnap-ix500-claude-mac.md)** — After the official Mac app stopped working, Jonas Wagner reports a Claude-built replacement with Wi-Fi scanning, the hardware button, OCR and blank-page handling. Protocol details are not supplied. **Oct 15 · 2 likes · Other AI-assisted work · Author report, not independently tested.**
4. **[KEF LSX II: volume keys that work better at a desk](cases/kef-lsx-ii-volume-fixer.md)** — A Claude-assisted USB passthrough and LAN volume bridge avoids patching signed firmware. The volume curve and roughly 2 ms added latency are author measurements. **Oct 15 · AI-assisted interoperability · Public implementation.**
5. **[Feishu: two accounts without constant switching](cases/feishu-dual-instance-codex-rea.md)** — After Codex/REA research, the author reports isolating a second copy's data and single-instance lock, with signature and directory checks. Local signing and disabled updates carry maintenance risks. **Oct 15 · REA · Author-tested, not independently reproduced.**
6. **[Touhou TH08: matching bytes can still miss a wrong constant](cases/touhou-reconstruction.md)** — This window's warning leads back to a September 2 issue and fix: instruction addresses matched while referenced data used 0.0 instead of 128.0. The project added floating-literal verification. **Shared Oct 15 · Historical repair evidence · Project tests, not rerun here.**
7. **[Roko Input: Apple's on-device speech rather than a cloud service](cases/rokoinput-apple-local-voice.md)** — Published after REA research, it stops when local recognition is unavailable. Plaintext history is enabled by default: privacy takes more than an offline label. **Oct 15 · 3 likes · REA · Personal non-commercial license.**
8. **[IsaacRecomp: a native path for Flash Isaac](cases/isaacrecomp-flash-cpp-report.md)** — The author acknowledges AI assistance and describes C++ translation with 30 Hz logic and interpolated rendering. Assets come from the user's original game; performance has not been independently tested. **Oct 15 · Other AI-assisted work · Public project.**
9. **[GAMEKB-K17: configure a macropad without the vendor website](cases/claude-code-rgb-macropad.md)** — Claude Code assists protocol research for an offline keys, macros and RGB tool with readback checks. Windows testing is project-reported. **Oct 15 · 7 likes · Other AI-assisted work.**
10. **[Humans versus agents: more than getting the answer right](cases/humans-machines-sre-study.md)** — Nine models, two static IDA tasks and context saturation across 4,000 programs. The paper emphasizes navigation and selective retrieval, not just bigger windows. **Shared Oct 15 · Paper submitted Oct 10 · Not an REA benchmark.**

### Classic cases

- **[Universal Modder](cases/universal-modder.md)** — Investigate engines and asset formats to bring Minecraft content into GTA V and other games; recorded snapshot: **14,340 likes**. `Other AI-assisted work`
- **[Firefighter: DOS binary to Rust](cases/firefighter-rust.md)** — Recover Pascal logic and rewrite maintainable Rust, according to the author; recorded snapshot: **7,833 likes**. `Other AI-assisted work`
- **[Modern Warfare 2: multi-agent reconstruction](cases/mw2-decompilation.md)** — The author reports 17 agents, three months, and byte-level matches for 83% of functions; code is not public and has not been independently reproduced here. `Other AI-assisted work`
- **[Smart toilet from the Mac menu bar](cases/smart-toilet.md)** — Investigate Bluetooth communication for lid control; the author later reports extending the app to other home devices. `REA · Author-reported`
- **[An Apple TV remote on Linux](cases/siri-remote-linux.md)** — Bluetooth interoperability with a public implementation; recorded snapshot: **5,419 likes**. `REA unconfirmed`
- **[LG PlxNative](cases/lg-plxnative.md)** — Investigate the native media stack; the author reports user selection falling from about 30 seconds to 3 seconds. Recorded snapshot: **7,268 likes**. `Other AI-assisted work`

## Contents

- [Games and preservation](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/games.md) (40)
- [Hardware and interoperability](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/hardware.md) (53)
- [Applications and clients](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/apps.md) (94)
- [Algorithms and feature recovery](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/algorithms.md) (16)
- [Contribute a case](https://github.com/songshikang0111/awesome-REA-cases/blob/main/CONTRIBUTING.md) · [Maintenance](https://github.com/songshikang0111/awesome-REA-cases/blob/main/MAINTENANCE.md)

Category pages contain every accepted case, ongoing project, and concrete idea; the homepage does not expand the full listing. Labels such as Needs verification, In progress, Analysis test, and Related project do not indicate completed or independently verified results. Case details and maintenance guides are currently in Chinese.

## Scope and license

Unofficial collection. Results are attributed to authors and project records, not independently reproduced here. Only original summaries and public links are curated; no proprietary software, game assets, keys, or private material are distributed.

Original summaries, curation data, and code use the [MIT License](LICENSE). Linked content retains its own rights. Ensure appropriate authorization before investigating or reproducing it.
