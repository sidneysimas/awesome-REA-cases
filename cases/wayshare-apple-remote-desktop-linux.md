# WayShare：macOS 自带屏幕共享连接 Hyprland，研究 Apple 高性能模式

分类：应用与客户端 · REA
记录日期：2026-10-20
阶段：进行中

10月20日02:29及02:31（北京时间），@ncfrontiersman（Wes Grimes）报告WayShare：在Omarchy与Mac运行Grok bot，协调Claude Code、Codex CLI和REA研究Apple Remote Desktop，以Rust实现Wayland/Hyprland到macOS屏幕共享High Performance模式。作者报告60fps、剪贴板共享、Command映射Super与Studio Display缩放，bot操作两机并修Bug；性能与体验均为作者自述。

补读固定提交0a883def08571c14413193e1cbc3d16d45322b43（10月19日07:48，北京时间，早于本轮）README及高性能、安全文档：要求Hyprland 0.56+与systemd，有x86_64/ARM64构建。HEVC与UDP音视频优先VA-API、否则x265，不支持NVENC，音频需要额外库；仅一个高性能观看者，反馈超时退回Standard。同提交公开CI于10月19日07:48启动并成功，含最低Rust cargo check、Linux check/audit、macOS test/clippy，不是本合集执行或端到端桌面实测。

安全文档明确Standard屏幕与剪贴板不加密，高性能音视频用SRTP、键鼠加密、密码通过SRP证明。项目建议独立密码、局域网或VPN，不把5900转发公网。未安装或连接机器、测量60fps或验证协议完整性，不能称全链路加密或兼容任意Wayland桌面。

02:29候选2赞、118浏览；02:31同文0赞、41浏览，60fps没有独立测量。

## 来源

- [Wes Grimes的跨机器研究与使用自述](https://x.com/i/status/2112249880181616856)
- [作者同文项目发布](https://x.com/i/status/2112250416331211039)
- [较早固定提交README：平台要求](https://github.com/wesleygrimes/wayshare/blob/0a883def08571c14413193e1cbc3d16d45322b43/README.md)
- [同提交高性能模式与退回条件](https://github.com/wesleygrimes/wayshare/blob/0a883def08571c14413193e1cbc3d16d45322b43/docs/high-performance.md)
- [同提交安全文档：未加密部分](https://github.com/wesleygrimes/wayshare/blob/0a883def08571c14413193e1cbc3d16d45322b43/docs/security.md)
- [较早同提交成功CI及平台jobs](https://github.com/wesleygrimes/wayshare/actions/runs/39178033593)

[English](en/wayshare-apple-remote-desktop-linux.md) | [返回目录](../README.zh-CN.md)
