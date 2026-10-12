# Awesome REA Cases

[中文（默认）](README.md) | **English**

**Unsupported software. Incompatible hardware. Lost source code. People are using AI to make these things work on their own terms.**

A collection of practical REA and AI-assisted reverse-engineering projects: maintaining old games, making hardware work across platforms, and bringing existing software capabilities into new products.

**Public cases are tracked six times daily. This homepage is read, selected, and written by the maintainer—not generated from a ranking or a list of every accepted entry.**

[All cases](INDEX.en.md) · [Games](categories/games.md) · [Hardware](categories/hardware.md) · [Applications](categories/apps.md) · [Algorithms](categories/algorithms.md)

## Recent picks

### [Running Shapr3D on Linux instead of rebuilding it](cases/wine-uwp-shapr3d.md)

The author reports Claude-assisted investigation of Windows Store app interfaces, extends Wine's compatibility layer, and publishes the implementation. The interesting move is supplying the environment an existing app needs—not building a lookalike. **Other AI-assisted work; unofficial beta, not tested by this collection.**

### [Adding an AI sidebar to Preview instead of cloning the whole app](cases/preview-ai-sidebar.md)

A research team demonstrates modifying a copy of macOS Preview and publishes a proof-of-concept project. The question shifts from rebuilding a product to changing software that already exists. **Needs verification; REA use unconfirmed, modified apps are personal experiments.**

### [Controlling an air conditioner with AR-glasses gestures](cases/ar-air-conditioner-control.md)

A secondary demo describes inspecting the official app's control requests and connecting power and temperature controls to AR glasses. A new interaction surface, rather than another appliance app. **REA · Needs verification: no public hardware model, protocol specification, or code; general appliance compatibility is not established.**

## Start with these

### [Universal Modder: Minecraft content in GTA V](cases/universal-modder.md)

Claude investigates engines and asset formats, then modifies content and tests it in-game. The idea is immediately understandable; the recorded post snapshot exceeds 14,000 likes. It demonstrates cross-game modding, not complete game decompilation. **Other AI-assisted work.**

### [Plex was slow on an LG TV, so a developer rebuilt the client](cases/lg-plxnative.md)

Ghidra and Claude Code helped investigate the TV's native media stack and build a Rust/OpenGL client. The author reports reducing the user-selection screen from about 30 seconds to 3 seconds: a clear user problem driving the investigation. **Other AI-assisted work; performance is author-reported.**

### [Recovering maintainable code from a DOS binary](cases/firefighter-rust.md)

The Firefighter author reports recovering Pascal logic and rewriting it in Rust. The goal is software preservation: turning an old executable into code someone can keep maintaining. **Other AI-assisted work.**

### [Using an Apple TV remote on Linux](cases/siri-remote-linux.md)

Investigate the Bluetooth protocol so Linux can understand touch, button, and microphone data, with a public implementation. A closed-ecosystem accessory becomes an input device for another system. **REA use unconfirmed.**

### [Rebuilding the Claude Slides editor from bundled front-end code](cases/claude-slides.md)

Codex and REA analyze the scripts; Claude Code organizes the project. Screenshots and a code commit provide something concrete to inspect. **REA; feature completeness is author-reported.**

### [17 agents, three months, and Modern Warfare 2](cases/mw2-decompilation.md)

The author reports a running game and byte-level matches for 83% of functions. The interesting work is parallel coordination and comparison against the original binary—not an overnight-rebuild story. **Other AI-assisted work; code is not public, and the collection has not independently reproduced it.**

## Keep exploring

The homepage is a selection. Every accepted case, ongoing project, and concrete idea remains in the [complete index](INDEX.en.md). Absence from the homepage is not a rejection.

[REA](https://github.com/morluto/rea), Reverse Engineer Anything, lets coding agents call local reverse-engineering tools through CLI and MCP interfaces. This collection also includes other AI-assisted work and interoperability projects for AI tools.

The English homepage and index are available; linked case details and maintenance guides are currently in Chinese.

## Contributing and scope

[Submit cases, verification, or corrections](CONTRIBUTING.md). Homepage picks favor specific, distinctive projects worth reading. Engagement is a discovery signal, not proof of results. See [Maintenance](MAINTENANCE.md) for editorial rules.

Unofficial collection. Results are attributed to authors and project records, not independently reproduced here. Only original summaries and public links are curated; no proprietary software, game assets, keys, or private material are distributed.

Original summaries, curation data, and code use the [MIT License](LICENSE). Linked content retains its own rights. Ensure appropriate authorization before investigating or reproducing it.
