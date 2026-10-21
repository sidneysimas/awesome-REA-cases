# Nothing Phone 3a：Claude Code 辅助移植 iOS 16 的启动自述

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-20
阶段：待验证

2026年10月20日20:24（北京时间），Sajid Khan（msfbeast007）报告将 iPhone X 的 iOS 16 移植到 Nothing Phone 3a：Claude Code 写驱动、修改 XNU 内核并阅读崩溃日志，人负责持机、刷写与拍照。作者称从锁定引导加载器到锁屏约两天，随后列出主屏、设置、控制中心、触摸、按键与八核可用，并称上滑或 Essential Key 可返回主页。目标是跨硬件操作系统适配，而不是 Android 外观主题；上述真实性仍属作者报告。

作者明确承认 Wi-Fi、蓝牙、通话、声音、相机、App Store 与 GPU 均不可用，靠 CPU 绘图，大部分安全机制关闭，不能日用。他注明基于 dipa-studio 的 ios-sweet，不分发 iOS 文件；另提正在探索 Snapdragon 笔记本上的 macOS，尚无该方向结果。帖子中的法律判断不作为本合集的法律结论。

补读公开 ios-sweet README（仓库提交时间10月20日00:44北京时间；文档状态日期10月18日），确认该上游描述 Redmi Note 10 Pro 上 XNU 与 iOS 16.7.16 用户态、UFS/HFS+、触摸驱动及大量安全限制，并警告清空 userdata。它只报告六个 A55 核与不能退出应用，不能用来证明 Nothing 分支的八核或主页手势；两台设备与两个进度不能混同。没有取得 Nothing 专用代码、启动日志或独立实机测试，REA未明示。

## 来源

- [Sajid Khan：Nothing Phone 3a 的 Claude Code 移植报告](https://x.com/i/status/2112520362382811236)
- [上游补证：ios-sweet README，10月18日状态，不是Nothing实测](https://github.com/dipa-studio/ios-sweet/blob/11da58bd050672960c0a83b5bef2176047eea479/README.md)

[English](en/nothing-phone-3a-claude-ios16-port.md) | [返回目录](../README.zh-CN.md)
