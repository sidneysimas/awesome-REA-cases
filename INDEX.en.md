# All cases and projects

[Editor picks](README.en.md) | [中文总目录](INDEX.md)

**Explore software and hardware with AI: rebuild features, bridge protocols, and modernize legacy systems.**

**Tracks public REA and AI reverse-engineering cases six times daily, automatically screening, deduplicating, and updating the collection.**

A collection of REA and AI reverse-engineering cases and projects, covering game preservation, hardware interoperability, app reconstruction, and algorithm research. Each entry explains the target, the author’s purpose and approach, and links to original posts, code, or verification records.

[REA](https://github.com/morluto/rea) (Reverse Engineer Anything) lets coding agents call local reverse-engineering tools through CLI and MCP interfaces. This collection also includes work with other AI tools and interoperability projects built for AI agents.

**69 entries**, organized by use case, without a Top-N or popularity threshold.

The index is in English; linked case details, category pages, and contribution/maintenance guides are currently in Chinese.

## Contents

- [Games and preservation](categories/games.md) (14)
- [Hardware and interoperability](categories/hardware.md) (14)
- [Applications and clients](categories/apps.md) (37)
- [Algorithms and feature recovery](categories/algorithms.md) (4)
- [Contribute a case](CONTRIBUTING.md) · [Maintenance](MAINTENANCE.md)

Tool labels distinguish REA, other AI work, and unconfirmed REA use. Stage labels—Needs verification, In progress, Analysis test, and Related project—keep all entries discoverable without presenting them as completed results.

## Cases and projects

### Games and preservation

- [Universal Modder: AI-assisted game mods](cases/universal-modder.md) — Analyze engines and asset formats, then create and test cross-game mods. **[Other AI-assisted work]**
- [Firefighter: from DOS binary to Rust](cases/firefighter-rust.md) — Recover Pascal logic from an old binary and rewrite it in Rust. **[Other AI-assisted work]**
- [Modern Warfare 2: multi-agent decompilation](cases/mw2-decompilation.md) — Reconstruct game functions and compare compiled bytes to the original binary. **[Other AI-assisted work]**
- [Urban Terror in the browser](cases/urban-terror-web.md) — Resolve engine/bytecode layout differences blocking a WebAssembly port. **[Other AI-assisted work]**
- [DX-Ball: positional audio function](cases/dx-ball-sound-pan.md) — Recover and verify a single sound-panning function from a classic game. **[REA]**
- [Touhou TH04: ring-bullet angles](cases/th04-bullet-ring.md) — Explain how Lotus Land Story calculates a ring of bullets. **[REA]**
- [Touhou reconstruction projects](cases/touhou-reconstruction.md) — Recover old game code, validate it and produce playable platform builds. **[REA]**
- [Dinosaur: the acceleration rule](cases/dinosaur-speed.md) — Inspect a web game and experimentally check its speed-update logic. **[REA]**
- [Unity/Valheim assemblies](cases/unity-valheim.md) — Real game-analysis requests without a confirmed re-test of the original target. **[REA · In progress]**
- [Boba Fett in Red Dead Redemption 2](cases/boba-fett-rdr2.md) — Reverse asset formats, write an exporter and adapt a Battlefront II character into a working game mod. **[Other AI-assisted work]**
- [GameCube/Wii PowerPC support request](cases/wii-powerpc-request.md) — A Wii researcher describes an external Ghidra workflow and requests REA integration; no completed REA reconstruction is claimed. **[REA use unconfirmed · In progress]**
- [Aerobiz 2: REA and Kimi decompilation](cases/aerobiz-2-decompilation.md) — Investigate a 1993 KOEI airline-management game; no complete code recovery or playable rebuild is established. **[REA · Needs verification]**
- [Super Mario Sunshine: reported AI-assisted PC port](cases/super-mario-sunshine-pc.md) — A post claims AI-assisted decompilation for a native port; public port documentation does not establish the AI contribution or exact link identity. **[REA use unconfirmed · Needs verification]**
- [Red Alert 2: an engine rewrite for reinforcement learning](cases/red-alert-2-rl-engine.md) — The author reports using Chrono Divide, Opus and over 6,000 tests to rebuild unit behavior; their implementation and test results are not public. **[Other AI-assisted work · Needs verification]**

### Hardware and interoperability

- [Siri Remote on Linux](cases/siri-remote-linux.md) — Decode the Bluetooth protocol to use an Apple TV remote on Linux. **[REA use unconfirmed]**
- [Tuya RGB lights from a Mac](cases/tuya-rgb-mac.md) — Analyze phone Bluetooth traffic and directly control lights with a script. **[Other AI-assisted work]**
- [MIPS32 firmware analysis](cases/mips-firmware.md) — Select the correct architecture and cross-check analysis on real firmware. **[REA]**
- [PSP/Allegrex analysis](cases/psp-allegrex.md) — Connect Ghidra platform support and validate on a source-built PSP program. **[REA]**
- [Smart toilet from the desktop](cases/smart-toilet.md) — Analyze a mini-program Bluetooth protocol for lid control; the author now reports extending the Mac menu-bar app to other home devices. **[REA]**
- [Tuya Zigbee button firmware](cases/tuya-zigbee-button.md) — Use pi and GLM to investigate and modify button firmware; latency gains unquantified. **[Other AI-assisted work]**
- [Layered firmware: extraction to Ghidra](cases/firmware-extract-handoff.md) — Identify regions, extract files and inspect an ELF using source-controlled fixtures rather than a claimed device hack. **[REA]**
- [Bluetooth gamepad on Windows](cases/bluetooth-gamepad-windows.md) — Reverse the control protocol and write a ViGEm compatibility layer for an unsupported controller. **[Other AI-assisted work]**
- [Gamepad settings after Bluetooth analysis](cases/gamepad-settings-request.md) — The author reports protocol analysis with REA, but the Mac/Windows settings app is still planned. **[REA · In progress]**
- [ASUS ACPI and Linux GPU support](cases/asus-acpi-gpu.md) — A brief Codex-assisted ACPI report without enough hardware details or logs to reproduce it. **[Other AI-assisted work · Needs verification]**
- [Gaming mouse settings on macOS](cases/gaming-mouse-macos.md) — A ChatGPT-assisted report of restoring RGB, DPI and button configuration for an unsupported mouse; hardware and test details remain private. **[Other AI-assisted work · Needs verification]**
- [PS5 security: reported AI-assisted investigation](cases/ps5-ai-security-report.md) — A secondary post claims accelerated security research; AI contribution and library-access claims lack primary technical evidence. **[REA use unconfirmed · Needs verification]**
- [Air-conditioner protocol for AR gesture control](cases/ar-air-conditioner-control.md) — A secondary demo describes analyzing app requests with REA and using Codex/Lens Studio to control an appliance from AR glasses. **[REA · Needs verification]**
- [Redmi TV: browser inspection for a dashboard](cases/redmi-tv-dashboard.md) — A Muse/Codex report combines APK inspection, browser selection and full-screen interaction to repurpose an idle TV as a dashboard. **[Other AI-assisted work · Needs verification]**

### Applications and clients

- [LG PlxNative: a faster Plex client](cases/lg-plxnative.md) — Investigate the native media stack and build a Rust/OpenGL client. **[Other AI-assisted work]**
- [Claude Slides: rebuilding the editor](cases/claude-slides.md) — Analyze bundled front-end code and rebuild slide-editing functionality. **[REA]**
- [Claude Code: inspecting a compressed codebase](cases/claude-code-analysis.md) — Use Muse and REA to investigate a large compressed JavaScript package. **[REA]**
- [Notion: clipboard paths](cases/notion-clipboard.md) — Trace static copy-text and copy-image paths across Electron processes. **[REA]**
- [Flutter: build identity and AOT structure](cases/flutter-aot.md) — Identify runtime/build clues in real APKs, not complete Dart source. **[REA]**
- [Website rebuild: delivery report](cases/website-rebuild-report.md) — A reported REA-assisted job without detailed target or acceptance evidence. **[REA · Needs verification]**
- [TradingView: reconstruction workflow claim](cases/tradingview-workflow.md) — A popular workflow post does not establish recovery of paid indicators. **[REA · Needs verification]**
- [WHOOP Android app investigation](cases/whoop-apk.md) — An APK discussion without a confirmed public replacement client. **[REA use unconfirmed · Needs verification]**
- [ArtCraft: not proven Adobe or Office reverse engineering](cases/artcraft-boundary.md) — From-scratch creative apps, WordCraft, GridCraft and DeckCraft are early software rebuilds, not proof of complete Adobe or Office decompilation. **[Other AI-assisted work · Related project]**
- [Obsidian ASAR: large-package analysis](cases/obsidian-asar.md) — The user confirms analysis completed, without a demonstrated feature rebuild. **[REA · Analysis test]**
- [Large multidex Android APK](cases/large-android-apk.md) — A production-scale request; the original 133MB APK lacks a post-fix re-test. **[REA · In progress]**
- [.NET NativeAOT recovery request](cases/nativeaot.md) — Partial metadata recovery does not establish restoration of the original C# project. **[REA · In progress]**
- [Android ApiDemos: tracing Java methods from an APK](cases/android-apidemos.md) — Inspect a real demo APK, select method overloads and trace static references through JADX. **[REA]**
- [HarmonyOS packages: mapping components](cases/harmony-package-inventory.md) — Inspect a published HAP package to identify components and packaging hints, without claiming Ark-code recovery. **[REA]**
- [macOS Preview: rebuilding with and without REA](cases/preview-rebuild.md) — A first-hand comparison of two rebuilds covering zoom, rotation, annotation and saving. **[REA]**
- [Codex browser annotations: finding the interaction bridge](cases/codex-browser-annotations.md) — Inspect Electron code and test a page that opens and pre-fills an annotation dialog; direct composer insertion was not achieved. **[REA]**
- [Claude Design in BaoCut](cases/claude-design-baocut.md) — A public skill/front-end integration into a video agent; REA use is not explicitly confirmed. **[REA use unconfirmed]**
- [Claude Chrome on remote browsers](cases/claude-chrome-remote.md) — Reverse the native-messaging bridge and translate browser commands to CDP for cloud execution. **[REA use unconfirmed]**
- [pi-computer-use: desktop interaction for other models](cases/pi-computer-use.md) — A macOS tool inspired by Codex Computer Use, using accessibility-first navigation and a vision fallback. **[REA use unconfirmed]**
- [Background Computer Use in Swift](cases/background-computer-use.md) — Expose local APIs for background window interaction, with a real-time demo and public source. **[REA use unconfirmed]**
- [GarageBand format for automated composition](cases/garageband-file-format.md) — Reverse the music-project format to compose with local instruments as part of a larger music-video workflow. **[Other AI-assisted work]**
- [Apple Notes migration to Grape](cases/apple-notes-migration.md) — Use Claude Code to investigate Notes data and demonstrate importing folders, notes and images. **[Other AI-assisted work]**
- [Poker table organizer](cases/poker-table-organizer.md) — A first-hand report of rebuilding table organization with REA, Ghidra and Codex; the app and tests are not public. **[REA · Needs verification]**
- [Codex computer-use interoperability research](cases/codex-cua-harness-research.md) — An ongoing REA-assisted investigation of browser and computer-use features for another model in an independent agent harness. **[REA · In progress]**
- [Pump.fun reconstruction report](cases/pumpfun-reconstruction-report.md) — A third-party report of parallel-agent investigation, with launch-curve and Raydium migration development as context; full reconstruction is not established. **[REA use unconfirmed · Needs verification]**
- [Remote-desktop client privacy monitoring idea](cases/remote-client-privacy-monitor-idea.md) — An idea to use AI-assisted inspection of local clients and build a data-collection monitor; no implementation or misconduct is established. **[REA use unconfirmed · Needs verification]**
- [Gaoding-inspired cover workbench](cases/gaoding-cover-workbench.md) — A Codex/Fabric.js cover tool is reported; using REA to inspect Gaoding UI and logic is still described as a plan. **[REA · In progress]**
- [Axure: an AI-era rebuild idea](cases/axure-ai-rebuild-idea.md) — A proposal to study Axure and build a new prototyping tool; no implementation or AI-assisted investigation is established. **[REA use unconfirmed · Needs verification]**
- [Hermes Agent: Hark-assisted harness reconstruction](cases/hermes-hark-harness.md) — The author reports studying the open-source agent and creating a new harness; no public implementation or parity tests are supplied. **[Other AI-assisted work · Needs verification]**
- [Apple Preview: adding AI directly to a compiled app](cases/preview-ai-sidebar.md) — An OmniSE demo reports modifying a copy of Preview to add AI functionality rather than rebuilding the entire application; not independently reproduced. **[REA use unconfirmed · Needs verification]**
- [Cameo: reconstructing desktop-character behavior](cases/cameo-reconstruction.md) — A REA-to-Claude workflow reports rebuilding a compiled macOS character app; matching-animation claims are not independently verified. **[REA · Needs verification]**
- [wine-uwp: Windows Store apps and Shapr3D on Linux](cases/wine-uwp-shapr3d.md) — Claude-assisted investigation extends Wine with app-model and composition support; the related Shapr3D package remains an unofficial beta. **[Other AI-assisted work · Needs verification]**
- [CleanMyMac: reported native-app prototype](cases/cleanmymac-rebuild-report.md) — A secondary report describes inspecting four functions with REA and rebuilding a Mac prototype; exact functions and primary implementation evidence are absent. **[REA · Needs verification]**
- [Nexalytics: testing REA on the author's own app](cases/nexalytics-rebuild.md) — Inspect UI flows and front/back-end communication with Playwright; the author reports a close but not one-to-one reconstruction. **[REA · Needs verification]**
- [MetaTrader: a reported signal-analysis use case](cases/metatrader-signals-report.md) — A comment names trading-signal investigation as a goal but supplies no researcher, toolchain or demonstrated results. **[REA use unconfirmed · Needs verification]**
- [Business software: an ongoing agent-assisted rebuild](cases/business-software-rebuild.md) — The author reports cloning an unnamed professional application using an investigation/rebuild workflow; no delivery or exact REA use is established. **[REA use unconfirmed · In progress]**
- [CapCut transitions: a module-reconstruction lead](cases/capcut-transition-research.md) — A secondary discussion names transition research and an independent rebuild; design questions raised by the commenter are not demonstrated recoveries. **[REA use unconfirmed · Needs verification]**

### Algorithms and feature recovery

- [Binary-library rewrite](cases/binary-library-rewrite.md) — Analyze and reimplement an unnamed library; evaluation details remain private. **[REA]**
- [DownUnderCTF: masked squares checker](cases/masked-squares-ctf.md) — Recover input constraints and solve them with Z3; test against the original. **[REA]**
- [Aegis: one-time code calculation](cases/aegis-totp.md) — Extract a TOTP routine and compare reconstructed implementations. **[REA]**
- [Windows Calculator: recovering percentage rules](cases/windows-calculator-percent.md) — Inspect the installed model DLL and reconstruct different percentage rules for addition and multiplication. **[REA]**

## Contributing and selection

Submit new cases, additional verification, or corrections. Edit data/cases.json, run python3 scripts/build.py, and open a PR. See [Contributing](CONTRIBUTING.md).

Prefer original authors, concrete targets and recorded work. Merge multiple sources for one project. Distinguish author reports, static analysis and actual execution. X engagement is a dated snapshot, not proof of effectiveness.

## Scope and license

Unofficial collection. Results are attributed to authors and project records, not independently reproduced here. Only original summaries and public links are curated; no proprietary software, game assets, keys or private material are distributed.

Original summaries, curation data and code use the [MIT License](LICENSE). Linked content retains its own rights and licenses. Ensure you have the relevant authorization before investigating, reproducing or reusing it.

Organization inspired by [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills). [Collection scope](research/collection-scope.md) · [Reference study](research/reference-structure.md)
