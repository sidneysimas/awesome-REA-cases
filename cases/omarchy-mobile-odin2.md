# AYN Odin 2 Portal：用 Codex 研究启动链，原生运行 Omarchy

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-13
阶段：进行中

作者报告与 Codex 一起进行 AYN Odin 2 Portal 的原生 Linux bring-up，先检查实际设备、保存基础系统备份与哈希，再研究 UFS 分区和启动链，安装 Arch Linux ARM/Omarchy，而非 Android 中的虚拟机。报告涉及 AVB 元数据、4096 字节逻辑扇区造成的启动分区故障及恢复验证，目标是触屏桌面、手柄快捷键与本地游戏库。公开 omarchy-mobile-odin2 README 与原帖目标一致，并列出启动、显示、触摸与 Wi-Fi 工作的项目记录；这仍是作者/仓库自述，本合集未接触设备。麦克风语音采集、冷启动、备用槽恢复与其他硬件验收仍未完成，备份恢复本身也未实测。上游 Linux/ROCKNIX 等提供大量基础工作，不归功于 AI 从零重建；未确认使用 REA。

发帖：2026-10-13T04:00:40+08:00（北京时间）
证据边界：进行中；未独立运行验证

## 来源

- [本窗口原帖](https://x.com/i/status/2109736028538093774)
- [看公开项目 README](https://github.com/TechLuddite/omarchy-mobile-odin2)

[English](en/omarchy-mobile-odin2.md) | [返回目录](../README.md)
