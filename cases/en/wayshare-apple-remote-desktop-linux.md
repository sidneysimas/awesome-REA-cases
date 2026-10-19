# WayShare: macOS Screen Sharing into Hyprland via Apple's High Performance mode

Category: Applications and clients · REA
Record date: 2026-10-20
Stage: In progress

At 02:29 and 02:31 Beijing time on October 20, @ncfrontiersman (Wes Grimes) reports WayShare: Grok bot runs on Omarchy and Mac, coordinating Claude Code, Codex CLI and REA to investigate Apple Remote Desktop and implement macOS Screen Sharing's High Performance mode in Rust for Wayland/Hyprland. The author reports 60 fps, clipboard sharing, Command-to-Super mapping and Studio Display scaling, with bots operating both machines and fixing bugs. Performance and experience are author reports.

Supplementary reading of commit 0a883def08571c14413193e1cbc3d16d45322b43 (October 19, 07:48 Beijing time, before this window), its README and High Performance/security documents confirms Hyprland 0.56+, systemd and x86_64/ARM64 builds. HEVC/UDP video and audio prefer VA-API, then x265; NVENC is unsupported and audio requires additional libraries. Only one High Performance viewer is allowed and missing feedback falls back to Standard. Public CI for the same commit started October 19 at 07:48 and succeeded, including minimum-Rust cargo check, Linux check/audit and macOS test/clippy. This is not this collection's execution or an end-to-end desktop test.

The security document explicitly leaves Standard screens and clipboard unencrypted. High Performance audio/video use SRTP, keyboard/mouse are encrypted and SRP proves password knowledge. The project recommends a separate password, LAN or VPN use, and no public forwarding of port 5900. Nothing was installed, connected or measured here, including 60 fps or protocol completeness. This is not fully encrypted traffic or generic compatibility with every Wayland desktop.

02:29 candidate: 2 likes, 118 views; the same text at 02:31 has 0 likes and 41 views. No independent 60 fps measurement.

## Sources

- [Wes Grimes's cross-machine research and usage account](https://x.com/i/status/2112249880181616856)
- [Author's repeated announcement](https://x.com/i/status/2112250416331211039)
- [Earlier pinned README: platform requirements](https://github.com/wesleygrimes/wayshare/blob/0a883def08571c14413193e1cbc3d16d45322b43/README.md)
- [Same commit's High Performance mode and fallback](https://github.com/wesleygrimes/wayshare/blob/0a883def08571c14413193e1cbc3d16d45322b43/docs/high-performance.md)
- [Same commit's security document: unencrypted traffic](https://github.com/wesleygrimes/wayshare/blob/0a883def08571c14413193e1cbc3d16d45322b43/docs/security.md)
- [Earlier successful CI for this commit and platform jobs](https://github.com/wesleygrimes/wayshare/actions/runs/39178033593)

[中文](../wayshare-apple-remote-desktop-linux.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
