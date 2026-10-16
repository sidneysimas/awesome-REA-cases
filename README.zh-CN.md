# Awesome REA Cases

[English](README.md) | **简体中文**

### 用 AI 读懂软件与硬件。

精选 **AI 逆向的项目、实验与具体想法**：让旧设备继续工作，重建应用功能，保存游戏，理解隐藏的实现。

## 277 个案例与项目

**案例更新：**2026 年 10 月 16 日 12:33 · 北京时间（UTC+8）

**每天更新 6 次** · [完整目录](INDEX.md) · [按分类浏览](#分类浏览)

覆盖 [REA](https://github.com/morluto/rea) 与其他 AI 辅助逆向。REA 通过 CLI / MCP，让编程 Agent 调用本地逆向工具。

*据作者与项目报告整理，未经本合集独立复现；证据与项目状态见各案例详情。*

## 近期精选

**10 个值得读的案例**，综合实际用途、证据与近期性选编，不是自动排行榜。日期为所选来源或作者更新日期，不是收录日期。

1. **[Plustek 扫描仪与 ThinkPad 相机](cases/schaller-opticfilm-thinkpad-linux.md)** · `2026-10-16` — 用 Windows 参考行为改善 Linux 驱动；公开测量也保留低光与曝光缺陷。`进行中`
2. **[Sonic 3D Blast：先重建编译环境](cases/sonic-3d-blast-saturn-opus-port.md)** · `2026-10-16` — 作者自述 Claude／Opus 参与编译环境研究及 Saturn 到 PC 的原生移植；画面问题仍在，**11 月 20 日是计划，并非已经发行**。`进行中`
3. **[ReaCut](cases/reacut-jianying-open-editor.md)** · `2026-10-15` — 从剪映研究走向独立编辑器，项目记录包含视频导出与插件测试；签名和平台限制仍在。`REA`
4. **[LASRecomp：让《织梦岛》运行在电脑上](cases/links-awakening-claude-pc-port-report.md)** · `2026-10-15` — AI 辅助移植，需自备原作；beta 崩溃及部分平台未实测的限制已公开。`公开项目`
5. **[让读板仪恢复工作的报告](cases/plate-reader-filter-wheel-claude-repair.md)** · `2026-10-15` — 作者称 Claude 在开机故障后研究通信、重置固件。**无独立验收或临床质量证明。**`作者自述`
6. **[ScanSnap iX500：旧扫描仪继续用](cases/scansnap-ix500-claude-mac.md)** · `2026-10-15` — 作者称用 Claude 做出支持 Wi-Fi、实体按钮和 OCR 的 Mac 替代应用；缺少协议细节与独立测试。`作者自述`
7. **[KEF LSX II：修好音量键体验](cases/kef-lsx-ii-volume-fixer.md)** · `2026-10-15` — USB／局域网桥接改善桌面控制，不修改签名固件；延迟数据为作者测量。`公开实现`
8. **[飞书：一台 Mac，两个账号](cases/feishu-dual-instance-codex-rea.md)** · `2026-10-15` — Codex／REA 研究后隔离应用副本；本地签名、关闭更新仍有维护风险。`作者实测`
9. **[Electron Notes：答案全对，输出却膨胀](cases/rea-electron-notes-ipc-answer-key-test.md)** · `2026-10-16` — 作者报告识别 **4/4 通道**，同时 **2.3 KB 源码产生 1.0 MB JSON**；小样本不代表通用准确率。`REA 分析测试`
10. **[MoonBit：让调试符号重新可读](cases/moonbit-claude-debugger-demangling.md)** · `2026-10-16` — 作者称 Claude 研究符号编码，写出 VSCode 显示辅助；**未提供代码与测试**。`作者自述`

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
| [游戏与游戏保存](categories/games.md) | **65** |
| [硬件与设备互通](categories/hardware.md) | **63** |
| [应用与客户端](categories/apps.md) | **124** |
| [算法与功能重建](categories/algorithms.md) | **25** |

[**查看全部案例 →**](INDEX.md) · [贡献案例](CONTRIBUTING.md) · [维护方法](MAINTENANCE.md)

<details>
<summary><strong>更新时间与证据说明</strong></summary>

- **连续已解决材料的证据截止：**2026 年 10 月 15 日 16:00，北京时间。往期未解决来源会使截止时间暂缓，较新的案例仍可收录；这不是每个项目的验证日期。
- 每天检索 6 次，受关键词和分页限制，不代表全网全量。来源日期、证据边界与热度快照见各案例详情。
- 每个案例均提供完整介绍、公开来源及中英文切换。

</details>

## 范围与许可

**非 REA 官方项目。**只整理原创摘要与公开链接，不分发原软件、游戏资产、密钥或私人材料。

原创整理与代码采用 **[MIT](LICENSE)**。链接内容保留各自权利；研究和复现请使用合法取得的目标，并确认相应授权。
