# Awesome REA Cases

**中文（默认）** | [English](README.en.md)

**用 AI 读懂软件与硬件：重建功能、打通协议、迁移旧系统。**

当前收录 **160 个案例与项目**。*最近维护：2026 年 10 月 15 日 13:26；案例证据截止保留在 2026 年 10 月 15 日 08:00（北京时间）。*

每天 6 次定时追踪 REA 与 AI 逆向公开案例，筛选、去重并更新。本次审读 10 月 15 日 08:00 至 12:00（北京时间）的候选，检索受关键词与分页边界限制，不代表全网全量。已能判断的材料继续补录；仍有来源尚待核实，完整证据边界因此保留在 08:00。首页由维护者亲自阅读与选编，完整收录见[全部案例](INDEX.md)。

[REA](https://github.com/morluto/rea)（Reverse Engineer Anything）通过 CLI / MCP，让编程 Agent 调用本地逆向工具。本合集也收录其他 AI 辅助逆向，以及为 AI 工具实现互通的项目。

## 近期精选 Top 10

综合近期传播热度、具体用途和阅读价值手工挑选，不是实时排行榜。以下热度为 2026 年 10 月 12–15 日各来源的记录快照，不是当前实时数据；条目日期为来源发帖日期，热度不代表成果已被验证。

1. **[Claude Desktop：拆出界面手感，也追踪改版边界](cases/claude-desktop-ui-details.md)** — 作者称用 REA 整理交互手册与 React 组件；随后桌面端大改，计划重新对比，旧版弹簧、字重与渐隐参数不能直接套用新版。**10/15 更新 · 74 赞 · REA · 分析报告。**
2. **[GAMEKB-K17：不用厂商网页配置宏键盘](cases/claude-code-rgb-macropad.md)** — Denis Darkin 用 Claude Code 研究配置协议，公开离线配置工具；文档说明将按键、宏和 RGB 写入设备并读回核验，Windows 测试为项目自述。**10/15 · 7 赞 · 其他 AI 逆向。**
3. **[智能笔：买现成设备，接进自己的软件](cases/smart-pen-codex-integration.md)** — 团队报告用 Codex 反编译并集成现成智能笔，替代自制原型；设备型号与技术细节未公开。**10/14 · 79 赞 · 其他 AI 逆向 · 团队报告。**
4. **[Claude Design：把设计功能接进 BaoCut](cases/claude-design-baocut.md)** — 研究设计 Skill 与前端，把它们接进自己的视频 Agent，并公开代码提交。**10/12 · 254 赞 · 未确认使用 REA。**
5. **[Claude Slides：重建幻灯片编辑器](cases/claude-slides.md)** — Codex + REA 分析混淆前端，Claude Code 整理工程，有截图与代码提交；功能完整度为作者报告。**10/11 · 686 赞 · REA。**
6. **[Codex 浏览器：让网页唤起评论框](cases/codex-browser-annotations.md)** — 查 Electron 代码并做测试页，找到弹出和预填评论框的接口；尚不能直接将评论附加到输入框。**10/11 · 252 赞 · REA。**
7. **[REA 6.4.0：用 .NET 和 Electron 样本看清边界](cases/rea-640-windows-managed-electron-test.md)** — 测评帖报告程序集解码预算限制、Electron 语义图和单常量变更定位；是特定版本的样本实验，不是通用方法数阈值或安全保证。**10/15 · 主帖 1 赞 · REA · 未独立复核。**
8. **[Apple TV 遥控器：接到 Linux 上用](cases/siri-remote-linux.md)** — 研究蓝牙协议，让专用遥控器成为电脑的输入设备，提供开源实现。**10/9 · 5,419 赞 · 未确认使用 REA。**
9. **[LG 电视：重做更快的 Plex 客户端](cases/lg-plxnative.md)** — Ghidra + Claude Code 研究原生媒体栈，作者报告用户选择界面从约 30 秒降到约 3 秒。**10/8 · 7,268 赞 · 其他 AI 逆向。**
10. **[涂鸦 RGB 灯：不用厂商 App，从 Mac 控灯](cases/tuya-rgb-mac.md)** — 分析手机发送的蓝牙数据，再用自己的脚本控制买来的灯，有实际控灯演示。**10/8 · 2,285 赞 · 其他 AI 逆向。**

### 经典案例

- **[Universal Modder](cases/universal-modder.md)** — 分析引擎与素材格式，把 Minecraft 内容放进 GTA V 等游戏；记录快照 **14,340 赞**。`其他 AI 逆向`
- **[Firefighter：从 DOS 二进制到 Rust](cases/firefighter-rust.md)** — 作者报告恢复 Pascal 逻辑，再转写为可维护的 Rust 代码；记录快照 **7,833 赞**。`其他 AI 逆向`
- **[《现代战争 2》：多 Agent 重建代码](cases/mw2-decompilation.md)** — 作者报告 17 个 Agent 协作三个月，83% 函数字节级匹配；代码未公开，未独立复现。`其他 AI 逆向`
- **[智能马桶：从小程序协议到 Mac 状态栏](cases/smart-toilet.md)** — 分析蓝牙通信，控制翻盖；作者后来报告扩展到家中其他设备。`REA · 作者报告`

## 目录

- [游戏与游戏保存](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/games.md)（32）
- [硬件与设备互通](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/hardware.md)（39）
- [应用与客户端](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/apps.md)（79）
- [算法与功能重建](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/algorithms.md)（10）
- [贡献案例](https://github.com/songshikang0111/awesome-REA-cases/blob/main/CONTRIBUTING.md) · [维护方法](https://github.com/songshikang0111/awesome-REA-cases/blob/main/MAINTENANCE.md)

分类页保留全部通过筛选的案例、进行中的项目和具体 idea；首页不展开全量清单。`待验证`、`进行中`、`分析测试`、`相关项目`不是已完成或已独立验证的成果。

## 说明与许可

非 REA 官方项目。内容据作者与项目记录整理，未由本合集独立复现。仅提供原创摘要与公开链接，不分发原软件、游戏资产、密钥或私人材料。

原创摘要、数据整理与代码采用 [MIT License](LICENSE)；链接内容保留各自权利，研究或复现前请确认相应授权。
