# Virtual Desktop Streamer：研究安装包，做 Linux 适配层

分类：应用与客户端 · REA
记录日期：2026-10-13
阶段：进行中

补读 cudanexus 的6帖线程，目标是把 Virtual Desktop Streamer 的桌面、音频与输入串流带到 Linux。作者称 Windows 安装包路线因 .NET Framework/驱动受阻，转而研究 macOS 的 .NET 8 版本，定位平台调用并用 PipeWire/X11、GStreamer、PulseAudio 与 uinput 替换。公开 vd-streamer-linux README 明确由 Claude Code + REA 开发，复用官方 macOS 协议库，而不是从零恢复全部源代码；官方库由用户自行取得，带这些库的包不能再分发。线程还报告 Ubuntu 使用后修复延迟累积、滚动和网络切换。项目不支持 Windows 版提供的 SteamVR/OpenXR 游戏。虽然线程使用“real use”描述反馈，README 的 Not verified yet 明确所有测试使用模拟头显，未有真实头显、Wi-Fi 或 GPU 编码器，Ubuntu 测试是在容器中；滚动修复也未直接观察 X11 应用收到事件。本轮未构建或独立验证互通。

发帖：2026-10-13T06:06:16+08:00（北京时间）
证据边界：进行中；未独立运行验证
线程“real use”不等于实机验收：仓库明确仅模拟头显/容器测试。

## 来源

- [本窗口原帖（作者报告）](https://x.com/i/status/2109767636452265990)
- [看公开项目 README](https://github.com/cudanexus/vd-streamer-linux)

[English](en/virtual-desktop-streamer-linux.md) | [返回目录](../README.zh-CN.md)
