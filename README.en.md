# Awesome REA Cases

[中文（默认）](README.md) | **English**

**Explore software and hardware with AI: rebuild features, bridge protocols, and modernize legacy systems.**

Currently **252 cases and projects**. *Last maintained and counted: October 16, 2026, 04:05; continuous resolved-material case-evidence cutoff: October 15, 2026, 16:00 Beijing time (UTC+8).*

Public REA and AI reverse-engineering cases are tracked six times daily, screened and deduplicated. This review reads all 128 candidates from October 16, 00:00 to 04:00 Beijing time (start exclusive, end inclusive), plus eight previously unresolved sources. It adds 19 projects, author reports and concrete ideas, combining two posts by the same author about a robot vacuum. New material includes old-phone firmware running in Wasm, a Codex attempt on Slipstream 5000 and multi-model reverse-engineering tools. Unverified ports, costs and features remain attributed claims; illustrative demonstrations are not treated as measured results. Nine sources still need clarification; the oldest comes from the window starting October 15 at 16:00, so the continuous evidence cutoff stays there while assessable newer projects are included. Keyword and pagination limits make this a bounded search, not exhaustive coverage. The cutoff does not imply independent validation of every project. The maintainer reads and edits this homepage; the [complete index](INDEX.en.md) contains every accepted entry.

[REA](https://github.com/morluto/rea), Reverse Engineer Anything, lets coding agents call local reverse-engineering tools through CLI and MCP interfaces. This collection also covers other AI-assisted work and interoperability projects for AI tools.

## Recent picks: Top 10

Manually selected for recent attention, concrete use, and reading value—not a live leaderboard. Engagement figures are source-specific snapshots collected October 12–16, 2026, not live counts or proof of verified results. Dates below refer to source posts.

1. **[ReaCut: an editor with explicit export and validation boundaries](cases/en/reacut-jianying-open-editor.md)** — Jianying research informs an independent editor. Project records describe real video exports and plugin tests while documenting signing, platform and CI limitations. **Oct 15 · REA · In progress; project-reported validation.**
2. **[LASRecomp: Switch Link's Awakening on desktop](cases/en/links-awakening-claude-pc-port-report.md)** — The public project credits Claude Code with most work and requires the user's original game. Its beta documentation lists crash triggers and untested Linux ARM support. **Oct 15 · Secondary post: 144 likes · Other AI-assisted work · Not run here.**
3. **[A plate reader: investigate communication before declaring a repair](cases/en/plate-reader-filter-wheel-claude-repair.md)** — A filter wheel passed mechanical and optical checks but failed startup QC. The author says Claude worked out communication, reset firmware and added monitoring; device details, commands and clinical validation are absent. **Oct 15 · Other AI-assisted work · Author report, not medical-device safety certification.**
4. **[ScanSnap iX500: an OS upgrade need not retire the scanner](cases/en/scansnap-ix500-claude-mac.md)** — After the official Mac app stopped working, Jonas Wagner reports a Claude-built replacement with Wi-Fi scanning, the hardware button, OCR and blank-page handling. Protocol details are not supplied. **Oct 15 · 2 likes · Other AI-assisted work · Author report, not independently tested.**
5. **[KEF LSX II: volume keys that work better at a desk](cases/en/kef-lsx-ii-volume-fixer.md)** — A Claude-assisted USB passthrough and LAN volume bridge avoids patching signed firmware. The volume curve and roughly 2 ms added latency are author measurements. **Oct 15 · AI-assisted interoperability · Public implementation.**
6. **[Feishu: two accounts without constant switching](cases/en/feishu-dual-instance-codex-rea.md)** — After Codex/REA research, the author reports isolating a second copy's data and single-instance lock, with signature and directory checks. Local signing and disabled updates carry maintenance risks. **Oct 15 · REA · Author-tested, not independently reproduced.**
7. **[Touhou TH08: matching bytes can still miss a wrong constant](cases/en/touhou-reconstruction.md)** — An October 15 warning leads back to a September 2 issue and fix: instruction addresses matched while referenced data used 0.0 instead of 128.0. The project added floating-literal verification. **Shared Oct 15 · Historical repair evidence · Project tests, not rerun here.**
8. **[Roko Input: Apple's on-device speech rather than a cloud service](cases/en/rokoinput-apple-local-voice.md)** — Published after REA research, it stops when local recognition is unavailable. Plaintext history is enabled by default: privacy takes more than an offline label. **Oct 15 · 3 likes · REA · Personal non-commercial license.**
9. **[IsaacRecomp: a native path for Flash Isaac](cases/en/isaacrecomp-flash-cpp-report.md)** — The author acknowledges AI assistance and describes C++ translation with 30 Hz logic and interpolated rendering. Assets come from the user's original game; performance has not been independently tested. **Oct 15 · Other AI-assisted work · Public project.**
10. **[The 400 ms line: turn an REA explanation into a boundary check](cases/en/rea-js-stale-price-boundary-demo.md)** — A self-made JS module passes at 400 ms and blocks at 401 ms. The author distinguishes static tracing from local checks and labels the video as edited CLI results, not a live Claude session or order submission. **Oct 15 · REA · Author-reported analysis test, not rerun here.**

### Classic cases

- **[Universal Modder](cases/en/universal-modder.md)** — Investigate engines and asset formats to bring Minecraft content into GTA V and other games; recorded snapshot: **14,340 likes**. `Other AI-assisted work`
- **[Firefighter: DOS binary to Rust](cases/en/firefighter-rust.md)** — Recover Pascal logic and rewrite maintainable Rust, according to the author; recorded snapshot: **7,833 likes**. `Other AI-assisted work`
- **[Modern Warfare 2: multi-agent reconstruction](cases/en/mw2-decompilation.md)** — The author reports 17 agents, three months, and byte-level matches for 83% of functions; code is not public and has not been independently reproduced here. `Other AI-assisted work`
- **[Smart toilet from the Mac menu bar](cases/en/smart-toilet.md)** — Investigate Bluetooth communication for lid control; the author later reports extending the app to other home devices. `REA · Author-reported`
- **[An Apple TV remote on Linux](cases/en/siri-remote-linux.md)** — Bluetooth interoperability with a public implementation; recorded snapshot: **5,419 likes**. `REA unconfirmed`
- **[LG PlxNative](cases/en/lg-plxnative.md)** — Investigate the native media stack; the author reports user selection falling from about 30 seconds to 3 seconds. Recorded snapshot: **7,268 likes**. `Other AI-assisted work`

## Contents

- [Games and preservation](categories/en/games.md) (55)
- [Hardware and interoperability](categories/en/hardware.md) (60)
- [Applications and clients](categories/en/apps.md) (114)
- [Algorithms and feature recovery](categories/en/algorithms.md) (23)
- [Contribute a case (Chinese)](CONTRIBUTING.md) · [Maintenance (Chinese)](MAINTENANCE.md)

Category pages contain every accepted case, ongoing project, and concrete idea; the homepage does not expand the full listing. Labels such as Needs verification, In progress, Analysis test, and Related project do not indicate completed or independently verified results. Case details and category pages are available in English, with reciprocal Chinese links. Contribution and maintenance guides are in Chinese.

## Scope and license

Unofficial collection. Results are attributed to authors and project records, not independently reproduced here. Only original summaries and public links are curated; no proprietary software, game assets, keys, or private material are distributed.

Original summaries, curation data, and code use the [MIT License](LICENSE). Linked content retains its own rights. Ensure appropriate authorization before investigating or reproducing it.
