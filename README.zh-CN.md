# Awesome REA Cases

[English](README.md) | **简体中文**

### 用 AI 读懂软件与硬件。

精选 **AI 逆向的项目、实验与具体想法**：让旧设备继续工作，重建应用功能，保存游戏，理解隐藏的实现。

## 326 个案例与项目

**最近案例更新／维护：**2026 年 10 月 17 日 04:10 · 北京时间（UTC+8）；数量统计截至此次更新。

**每天更新 6 次** · [完整目录](INDEX.md) · [按分类浏览](#分类浏览)

覆盖 [REA](https://github.com/morluto/rea) 与其他 AI 辅助逆向。REA 通过 CLI / MCP，让编程 Agent 调用本地逆向工具。

*据作者与项目报告整理，未经本合集独立复现；证据与项目状态见各案例详情。*

![案例每日累计收录量](assets/case-growth.zh.svg)

## 近期精选

**10 个值得读的案例**，综合实际用途、证据与近期性选编，不是自动排行榜。日期为所选来源或作者更新日期，不是收录日期。

1. **[Plustek 扫描仪与 ThinkPad 相机](cases/schaller-opticfilm-thinkpad-linux.md)** · `2026-10-16` — 用 Windows 参考行为改善 Linux 驱动；公开测量也保留低光与曝光缺陷。`进行中`
2. **[Gears of War 3](cases/gears3-ai-graphics-recompile.md)** · `2026-10-17` — AI 辅助 Linux 重编译与图形后端研究；作者澄清是 **PowerPC 到 C++ 的机械翻译，不是恢复原始源码**，报告的 4K 版本仍有战斗掉帧。`进行中`
3. **[把 Codex 光标设到 Windows](cases/codex-cursor-windows-opus.md)** · `2026-10-17` — 作者称 Opus 在 Ghidra 失败后用 pefile/Capstone 恢复绘制几何。**只取一个视觉元素，不是复刻 Codex**；动画与点击热点未验证。`作者自述`
4. **[Computer + REA：五款应用演示](cases/computer-rea-five-app-rebuild-demos.md)** · `2026-10-16` — 从设计布局、表格与图片，到合同审阅和音轨混合。**官方演示，不是已验证的替代品**，不代表完整复刻 Figma、Calc、Photopea、Harvey 或 Audacity。`REA · 待验证`
5. **[Sonic 3D Blast：先重建编译环境](cases/sonic-3d-blast-saturn-opus-port.md)** · `2026-10-16` — 作者澄清是**从反编译代码构建原生移植，不是静态重编译**；画面缺陷仍在，11 月 20 日只是发行计划。`进行中`
6. **[ReaCut](cases/reacut-jianying-open-editor.md)** · `2026-10-16` — 独立编辑器已有项目报告的导出与插件测试；**版权素材与 AI API 仍是卡点**，签名和平台限制也未消失。`进行中`
7. **[LASRecomp：让《织梦岛》运行在电脑上](cases/links-awakening-claude-pc-port-report.md)** · `2026-10-15` — AI 辅助移植，需自备原作；beta 崩溃及部分平台未实测的限制已公开。`公开项目`
8. **[KEF LSX II：修好音量键体验](cases/kef-lsx-ii-volume-fixer.md)** · `2026-10-15` — USB／局域网桥接改善桌面控制，不修改签名固件；延迟数据为作者测量。`公开实现`
9. **[先读 Notion，再谈通信行为](cases/notion-asar-claude-readonly-audit.md)** · `2026-10-17` — 作者称 Claude 检查 6.8 MB ASAR 与 47 个域名字符串。**可能的目的地不等于实际发出流量**；REA 对照仍为计划。`静态分析`
10. **[先验证 CSV 验收器](cases/rea-csv-evaluator-mutation-test.md)** · `2026-10-16` — 作者称三个故意改坏的导出器通过简单测试，却被 **215 组字节对照**发现；有价值的验收实验，但未公开输入与代码。`REA 分析测试`

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
| [游戏与游戏保存](categories/games.md) | **73** |
| [硬件与设备互通](categories/hardware.md) | **72** |
| [应用与客户端](categories/apps.md) | **151** |
| [算法与功能重建](categories/algorithms.md) | **30** |

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
