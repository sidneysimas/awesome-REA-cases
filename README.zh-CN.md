<img src="assets/rea-banner.png" alt="REA Cases — AI + Reverse Engineering" width="1280">

# Awesome REA Cases

[English](README.md) | **简体中文**

### 用 AI 读懂软件与硬件。

精选 **AI 逆向的项目、实验与具体想法**：让旧设备继续工作，重建应用功能，保存游戏，理解隐藏的实现。

# 871 个案例与项目

**最近案例更新：**2026 年 10 月 26 日 17:34 · **最近维护：**2026 年 10 月 26 日 17:34 · 北京时间（UTC+8）；数量统计截至此次维护。

**每天更新 6 次** · [完整目录](INDEX.md) · [按分类浏览](#分类浏览)

覆盖 [REA](https://github.com/morluto/rea) 与其他 AI 辅助逆向。REA 通过 CLI / MCP，让编程 Agent 调用本地逆向工具。

*据作者与项目报告整理，未经本合集独立复现；证据与项目状态见各案例详情。*

![案例每日累计收录量](assets/case-growth.zh.svg)

## 近期精选

**10 个值得读的案例**：探索设备互通、游戏保存，以及有可查证据的功能重建。优先推荐公开实现与限制明确的项目；完整目录也保留自用工具、失败实验与具体想法。下列日期为来源或作者更新日期，不是收录日期。

1. **[Plustek 扫描仪与 ThinkPad 相机](cases/schaller-opticfilm-thinkpad-linux.md)** · `2026-10-15` — 用 Windows 参考行为改善 Linux 驱动；公开测量也保留低光与曝光缺陷。`进行中`
2. **[NIST 曲线种子从哪来](cases/nist-ecdsa-origin-claude-report.md)** · `2026-10-16` — Anthropic 报告 Claude 追到 **lrand48 与时间戳**，公开代码，也保留未解问题。**不是破解 ECDSA**，本合集未独立复算。`研究报告`
3. **[LG UltraFine：修更新器，而不是破解固件](cases/lg-ultrafine-codex-updater-patch.md)** · `2026-10-19` — Codex 辅助诊断，公开**精确构建限定的内存补丁**；作者报告 scaler 更新达 **100%、CRC 通过**。注明前人错误报告；仅一套 Apple Silicon 配置，本合集未独立刷机。`作者实测补丁`
4. **[Brother：扫描直接进 NAS](cases/brother-scan-button-claude-rea-server.md)** · `2026-10-18` — 以 **Claude/REA 辅助的公开 Go 服务替代电脑按键应用，支持 SMB、FTP、S3 与本地保存**，复用前人协议研究。仍需服务器；项目只报告测试 MFC-L2800DW 固件1.32。`公开实现`
5. **[Claude 写证明，Rocq 检查二进制](cases/anthropic-theorem-claude-binary-formal-verification.md)** · `2026-10-22` — Anthropic／Theorem 报告为 **123 库的 239 个入口**建立机器码无崩溃证明。限单线程静态 RISC-V/Linux、小于64MB输入；**不等于整库无 bug**，本合集未独立重跑检查器。`分析测试`
6. **[MagicSwipe：iPad 上的 Magic Mouse 手势](cases/magic-mouse-ipad-opus-virtual-hid.md)** · `2026-10-20` — Opus 辅助研究，把**私有触摸回调接到虚拟 HID 快捷键**，补足通用控制操作。代码公开，仅项目报告设备测试；需高权限驱动，替代为快捷键而非原生连续手势。`进行中`
7. **[xbox-boot-re：重建初代 Xbox 的绿色开机动画](cases/xbox-boot-re-claude-reconstruction.md)** · `2026-10-16` — 人类指导 Opus，从单张 BIOS 恢复为 **C 核心与 WebGPU 查看器**，有 xemu 对照文档和成功项目 CI。仅一版修改 BIOS，声音合成有近似；不是完整主机模拟器，本合集未重跑。`进行中`
8. **[初代文明：重建1991年的 DOS 可执行文件](cases/civilization-dos47405-ai-reconstruction-report.md)** · `2026-10-21` — Steve Melia 的 AI 辅助 C／汇编重建有**公开代码与精确提交的哈希校验 CI 成功记录**。**四字节启动修正**是受检构建步骤，不是最终仍有差异。命名为推断，依赖前人 OpenCiv1；不是原始源码，本合集未独立编译。`进行中`
9. **[WayShare：从 Mac 连接 Hyprland](cases/wayshare-apple-remote-desktop-linux.md)** · `2026-10-20` — REA 辅助研究 Apple Remote Desktop，产出**公开 Rust 实现及成功项目 CI**。60fps 仍为作者说法，未独立测量；Standard 屏幕与剪贴板未加密。`进行中`
10. **[Precursor：在 Android 手机运行 Jak](cases/precursor-opengoal-claude-android-arm64.md)** · `2026-10-23` — Claude 辅助**ARM64 编译器与 Android 运行时移植**，明确依托 OpenGOAL 既有反编译。项目报告三作启动，但**无一端到端验证**，Jak 3 首段过场后白屏；本合集未运行。`进行中`

## 经典案例

- **[Universal Modder](cases/universal-modder.md)** — AI 辅助跨游戏 Mod，把 Minecraft 内容放进 GTA V 等游戏。
- **[Firefighter：DOS 二进制到 Rust](cases/firefighter-rust.md)** — 作者报告先恢复 Pascal 逻辑，再转写为 Rust。
- **[《现代战争 2》](cases/mw2-decompilation.md)** — 作者报告多 Agent 重建，**83% 函数字节级匹配**；代码未公开，未独立复现。
- **[Mac 菜单栏控制智能马桶](cases/smart-toilet.md)** — 作者报告研究蓝牙通信，并扩展到其他家居设备。
- **[Apple TV 遥控器接入 Linux](cases/siri-remote-linux.md)** — 蓝牙互通与公开实现，未确认使用 REA。
- **[LG PlxNative](cases/lg-plxnative.md)** — 原生 Plex 客户端；作者报告用户选择时间从 **30 秒降到 3 秒**。

## 分类浏览

| 分类 | 数量 |
| :--- | ---: |
| [游戏与游戏保存](categories/games.md) | **190** |
| [硬件与设备互通](categories/hardware.md) | **231** |
| [应用与客户端](categories/apps.md) | **371** |
| [算法与功能重建](categories/algorithms.md) | **79** |

[**查看全部案例 →**](INDEX.md) · [贡献案例](CONTRIBUTING.md) · [维护方法](MAINTENANCE.md)

<details>
<summary><strong>更新时间与证据说明</strong></summary>

- **连续已解决材料的证据截止：**2026 年 10 月 15 日 16:00，北京时间。往期未解决来源会使截止时间暂缓，较新的案例仍可收录；这不是每个项目的验证日期。
- 每天检索 6 次，受关键词和分页限制，属于有界覆盖，不代表全网全量，部分链接证据仍待核实。来源日期、证据边界与热度快照见各案例详情。
- 每个案例均提供完整介绍、公开来源及中英文切换。

</details>

## 范围与许可

**非 REA 官方项目。**只整理原创摘要与公开链接，不分发原软件、游戏资产、密钥或私人材料。

原创整理与代码采用 **[MIT](LICENSE)**。链接内容保留各自权利；研究和复现请使用合法取得的目标，并确认相应授权。
