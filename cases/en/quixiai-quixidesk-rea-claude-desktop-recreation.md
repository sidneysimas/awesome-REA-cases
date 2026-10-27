# QuixiDesk: Eric Hartford uses REA to investigate Claude Desktop and rebuild a model-switchable Rust client

Category: Applications and clients · REA
Record date: 2026-10-27
Stage: In progress

At 09:08 Beijing time on October 27, 2026, Eric Hartford (@QuixiAI) says he reverse-engineered Claude Desktop with morluto's REA to create an open-source alternative supporting local and cloud models. At 10:50 that day he identifies it as QuixiDesk, unrelated to T3 Code. It is also distinct from the previously collected Open Claude UI interface research and must not be merged into the same author or implementation.

Supplementary reading covers the README and Cargo.toml at QuixiAI/QuixiDesk commit 72c9d8836f69cdc7d02372b84b1cf7054bdf2658. Its timestamp is 13:34:46 Beijing time on October 27, after this candidate window; it is later project background, not a claim about features already implemented inside the window. The project credits REA with mapping over 1,400 IPC channels and native macOS helper protocols, replacing Electron/Node.js with tao/wry and WKWebView in a reconstructed Rust workspace. Its README claims 17 model providers, 11 UI languages, built-in browser/computer use and a unified task/chat view. Cargo member declarations confirm a Rust workspace manifest exists, not that every feature is implemented.

The goal is preserving desktop interaction while removing dependence on one model provider, not copying Claude's model weights. Documentation requires macOS 14 or later, cargo 1.80 or later and Xcode Command Line Tools; it does not establish working Linux or Windows support. Full feature parity, zero configuration and safe filesystem access remain project claims. This collection did not build, run, audit permissions or inspect every channel. Replies question source links and tool permission configuration; the author asks the latter commenter to file an issue. These comments establish neither a confirmed vulnerability nor feature equivalence. Included as an in-progress public reconstruction project.

Original candidate snapshot: 122 likes, 4,022 views, 13 reposts; later lookup engagement is not substituted.
Over 1,400 channels, 17 providers and 11 languages are project claims. Only documentation and the manifest were read; compatibility, permissions and performance were not independently verified.

## Sources

- [Eric Hartford's REA/Claude Desktop reconstruction report, October 27, 2026](https://x.com/i/status/2114886957603991752)
- [Author identifies QuixiDesk and distinguishes it from T3 Code, October 27, 2026](https://x.com/i/status/2114912658306814150)
- [Supplement: QuixiDesk README at the post-window 13:34 commit](https://github.com/QuixiAI/QuixiDesk/blob/72c9d8836f69cdc7d02372b84b1cf7054bdf2658/README.md)
- [Supplement: Rust workspace manifest at the same commit](https://github.com/QuixiAI/QuixiDesk/blob/72c9d8836f69cdc7d02372b84b1cf7054bdf2658/Cargo.toml)

[中文](../quixiai-quixidesk-rea-claude-desktop-recreation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
