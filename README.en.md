# Awesome REA Cases

[中文（默认）](README.md) | **English**

A curated collection of REA and AI-related reverse-engineering cases: the target, the author’s purpose, what they did, and the reported outcome.

> Unofficial collection. Inclusion is not an endorsement. No proprietary binaries, keys, private records or unauthorized assets are distributed.

**36 cases**, plus **11 leads** with incomplete evidence, tool tests or exclusion notes. Results are attributed to authors and project records, not independently reproduced by this collection.

The index below is in English. Linked case details, category pages, contribution and maintenance guides are currently in Chinese.

## Contents

- [Games and preservation](categories/games.md) (9)
- [Hardware and interoperability](categories/hardware.md) (8)
- [Applications and clients](categories/apps.md) (15)
- [Algorithms and feature recovery](categories/algorithms.md) (4)
- [Leads and excluded material](LEADS.md)
- [Contributing](CONTRIBUTING.md) · [Maintenance](MAINTENANCE.md)

## Cases

### Games and preservation

- [Universal Modder: AI-assisted game mods](cases/universal-modder.md) — Analyze engines and asset formats, then create and test cross-game mods. **[Other AI-assisted work]**
- [Firefighter: from DOS binary to Rust](cases/firefighter-rust.md) — Recover Pascal logic from an old binary and rewrite it in Rust. **[Other AI-assisted work]**
- [Modern Warfare 2: multi-agent decompilation](cases/mw2-decompilation.md) — Reconstruct game functions and compare compiled bytes to the original binary. **[Other AI-assisted work]**
- [Urban Terror in the browser](cases/urban-terror-web.md) — Resolve engine/bytecode layout differences blocking a WebAssembly port. **[Other AI-assisted work]**
- [DX-Ball: positional audio function](cases/dx-ball-sound-pan.md) — Recover and verify a single sound-panning function from a classic game. **[REA]**
- [Touhou TH04: ring-bullet angles](cases/th04-bullet-ring.md) — Explain how Lotus Land Story calculates a ring of bullets. **[REA]**
- [Touhou reconstruction projects](cases/touhou-reconstruction.md) — Recover old game code, validate it and produce playable platform builds. **[REA]**
- [Dinosaur: the acceleration rule](cases/dinosaur-speed.md) — Inspect a web game and experimentally check its speed-update logic. **[REA]**
- [Boba Fett in Red Dead Redemption 2](cases/boba-fett-rdr2.md) — Reverse asset formats, write an exporter and adapt a Battlefront II character into a working game mod. **[Other AI-assisted work]**

### Hardware and interoperability

- [Siri Remote on Linux](cases/siri-remote-linux.md) — Decode the Bluetooth protocol to use an Apple TV remote on Linux. **[REA use unconfirmed]**
- [Tuya RGB lights from a Mac](cases/tuya-rgb-mac.md) — Analyze phone Bluetooth traffic and directly control lights with a script. **[Other AI-assisted work]**
- [MIPS32 firmware analysis](cases/mips-firmware.md) — Select the correct architecture and cross-check analysis on real firmware. **[REA]**
- [PSP/Allegrex analysis](cases/psp-allegrex.md) — Connect Ghidra platform support and validate on a source-built PSP program. **[REA]**
- [Smart toilet from the desktop](cases/smart-toilet.md) — Analyze a mini-program Bluetooth protocol and demonstrate lid control. **[REA]**
- [Tuya Zigbee button firmware](cases/tuya-zigbee-button.md) — Use pi and GLM to investigate and modify button firmware; latency gains unquantified. **[Other AI-assisted work]**
- [Layered firmware: extraction to Ghidra](cases/firmware-extract-handoff.md) — Identify regions, extract files and inspect an ELF using source-controlled fixtures rather than a claimed device hack. **[REA]**
- [Bluetooth gamepad on Windows](cases/bluetooth-gamepad-windows.md) — Reverse the control protocol and write a ViGEm compatibility layer for an unsupported controller. **[Other AI-assisted work]**

### Applications and clients

- [LG PlxNative: a faster Plex client](cases/lg-plxnative.md) — Investigate the native media stack and build a Rust/OpenGL client. **[Other AI-assisted work]**
- [Claude Slides: rebuilding the editor](cases/claude-slides.md) — Analyze bundled front-end code and rebuild slide-editing functionality. **[REA]**
- [Claude Code: inspecting a compressed codebase](cases/claude-code-analysis.md) — Use Muse and REA to investigate a large compressed JavaScript package. **[REA]**
- [Notion: clipboard paths](cases/notion-clipboard.md) — Trace static copy-text and copy-image paths across Electron processes. **[REA]**
- [Flutter: build identity and AOT structure](cases/flutter-aot.md) — Identify runtime/build clues in real APKs, not complete Dart source. **[REA]**
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

### Algorithms and feature recovery

- [Binary-library rewrite](cases/binary-library-rewrite.md) — Analyze and reimplement an unnamed library; evaluation details remain private. **[REA]**
- [DownUnderCTF: masked squares checker](cases/masked-squares-ctf.md) — Recover input constraints and solve them with Z3; test against the original. **[REA]**
- [Aegis: one-time code calculation](cases/aegis-totp.md) — Extract a TOTP routine and compare reconstructed implementations. **[REA]**
- [Windows Calculator: recovering percentage rules](cases/windows-calculator-percent.md) — Inspect the installed model DLL and reconstruct different percentage rules for addition and multiplication. **[REA]**

## Leads

- [Website rebuild: delivery report](cases/website-rebuild-report.md) — A reported REA-assisted job without detailed target or acceptance evidence. **[REA]**
- [TradingView: reconstruction workflow claim](cases/tradingview-workflow.md) — A popular workflow post does not establish recovery of paid indicators. **[REA]**
- [WHOOP Android app investigation](cases/whoop-apk.md) — An APK discussion without a confirmed public replacement client. **[REA use unconfirmed]**
- [ArtCraft: not proven Adobe reverse engineering](cases/artcraft-boundary.md) — From-scratch creative software should not be labeled a complete Adobe decompilation. **[Other AI-assisted work]**
- [Obsidian ASAR: large-package analysis](cases/obsidian-asar.md) — The user confirms analysis completed, without a demonstrated feature rebuild. **[REA]**
- [Unity/Valheim assemblies](cases/unity-valheim.md) — Real game-analysis requests without a confirmed re-test of the original target. **[REA]**
- [Large multidex Android APK](cases/large-android-apk.md) — A production-scale request; the original 133MB APK lacks a post-fix re-test. **[REA]**
- [.NET NativeAOT recovery request](cases/nativeaot.md) — Partial metadata recovery does not establish restoration of the original C# project. **[REA]**
- [GameCube/Wii PowerPC support request](cases/wii-powerpc-request.md) — A Wii researcher describes an external Ghidra workflow and requests REA integration; no completed REA reconstruction is claimed. **[REA use unconfirmed]**
- [Gamepad settings after Bluetooth analysis](cases/gamepad-settings-request.md) — The author reports protocol analysis with REA, but the Mac/Windows settings app is still planned. **[REA]**
- [ASUS ACPI and Linux GPU support](cases/asus-acpi-gpu.md) — A brief Codex-assisted ACPI report without enough hardware details or logs to reproduce it. **[Other AI-assisted work]**

## Selection and evidence

- No Top-N or fixed date limit. Prefer concrete targets, methods and results over popularity.
- REA, other AI-assisted work and unconfirmed REA use are labeled separately. An AI-tool integration does not prove AI performed the investigation itself.
- Static analysis, source-built fixtures, author reports and runtime checks have different scopes. A supported platform is not a complete product reconstruction.
- X engagement is a dated snapshot, not a live ranking. Post date is not necessarily project completion date.
- Merge multiple posts about the same project. Keep separate targets or independent projects distinct.
- Edit data/cases.json and run python3 scripts/build.py. Generated files must stay synchronized.

## License and acknowledgements

Original summaries, curation data and code use the [MIT License](LICENSE). Linked software, documents, posts and game assets retain their own rights and licenses; this license does not authorize their redistribution.

Organization inspired by [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills). See the [reference study](research/reference-structure.md).
