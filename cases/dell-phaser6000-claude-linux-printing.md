# Dell／Phaser 6000：Claude 辅助恢复 Arch 打印与诊断旧驱动

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-20
阶段：待验证

2026年10月20日21:19（北京时间），Xiao Tan（tvytlx）转述一名全科医生用 Claude Code 约一小时，让2011年 Dell 彩色激光打印机在 Arch Linux 打印。叙述称 USB ID 指向贴牌 Xerox Phaser 6000，使用 HBPL v1，而所尝试的 foo2zjs 路线只支持 v2；随后找到 AUR 包，用 Wayback Machine 的2025年7月存档取回官方失效链接中的旧压缩包，并与 PKGBUILD 的 SHA256 核对。

报告的排障包括：PDF 输出白纸，先离线通过 CUPS 过滤器观察到0%墨量，再以 Ghostscript 重写 ReportLab PDF；请求两份却打印四份，是 CUPS 与旧驱动各重复一次，用八行 wrapper 修正。另从 USB 状态字符串解析碳粉余量并与机器屏幕格子比较。叙述也保留 Agent 把尚在编译误说成安装完成、后来主动纠正的失误；sudo 密码由人输入。

未来想基于他人已逆向的格式写开源64位驱动并真机测试，不等于该驱动已实现。一小时、两天人工估计、哈希相符与碳粉对照均为转述，未取得医生原文、精确 Dell 型号、包校验值、wrapper 或测试日志，本合集未打印；也不将复用已有二进制驱动写成从零恢复整个协议。

## 来源

- [Xiao Tan：Dell旧打印机恢复、驱动排障与重写计划的转述](https://x.com/i/status/2112534046769111446)

[English](en/dell-phaser6000-claude-linux-printing.md) | [返回目录](../README.zh-CN.md)
