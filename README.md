# Awesome REA Cases

**中文（默认）** | [English](README.en.md)

**用 AI 读懂软件与硬件：重建功能、打通协议、迁移旧系统。**

当前收录 **128 个案例与项目**。*最近维护：2026 年 10 月 13 日 20:00；案例统计截至 20 点（北京时间）。*

每天 6 次定时追踪 REA 与 AI 逆向公开案例，筛选、去重并更新。本次 16–20 点窗口的收集覆盖有限，所列发现不代表完整检索。首页由维护者亲自阅读与选编，完整收录见[全部案例](INDEX.md)。

[REA](https://github.com/morluto/rea)（Reverse Engineer Anything）通过 CLI / MCP，让编程 Agent 调用本地逆向工具。本合集也收录其他 AI 辅助逆向，以及为 AI 工具实现互通的项目。

## 近期精选 Top 10

综合近期传播热度、具体用途和阅读价值手工挑选，不是实时排行榜。以下热度为 2026 年 10 月 12 日的记录快照；热度不代表成果已被验证。

1. **[Claude Design：把设计功能接进 BaoCut](cases/claude-design-baocut.md)** — 研究设计 Skill 与前端，把它们接进自己的视频 Agent，并公开代码提交。**10/12 · 254 赞 · 未确认使用 REA。**
2. **[Claude Slides：重建幻灯片编辑器](cases/claude-slides.md)** — Codex + REA 分析混淆前端，Claude Code 整理工程，有截图与代码提交；功能完整度为作者报告。**10/11 · 686 赞 · REA。**
3. **[Codex 浏览器：让网页唤起评论框](cases/codex-browser-annotations.md)** — 查 Electron 代码并做测试页，找到弹出和预填评论框的接口；尚不能直接将评论附加到输入框。**10/11 · 252 赞 · REA。**
4. **[Claude Code：读懂 47MB 压缩代码](cases/claude-code-analysis.md)** — 让 Muse 调用 REA 阅读大型代码包，展示工具接入与分析过程，不等于已复刻 Claude Code。**10/10 · 576 赞 · REA。**
5. **[Apple TV 遥控器：接到 Linux 上用](cases/siri-remote-linux.md)** — 研究蓝牙协议，让专用遥控器成为电脑的输入设备，提供开源实现。**10/9 · 5,419 赞 · 未确认使用 REA。**
6. **[LG 电视：重做更快的 Plex 客户端](cases/lg-plxnative.md)** — Ghidra + Claude Code 研究原生媒体栈，作者报告用户选择界面从约 30 秒降到约 3 秒。**10/8 · 7,268 赞 · 其他 AI 逆向。**
7. **[涂鸦 RGB 灯：不用厂商 App，从 Mac 控灯](cases/tuya-rgb-mac.md)** — 分析手机发送的蓝牙数据，再用自己的脚本控制买来的灯，有实际控灯演示。**10/8 · 2,285 赞 · 其他 AI 逆向。**
8. **[《荒野大镖客 2》：把波巴·费特放进游戏](cases/boba-fett-rdr2.md)** — 研究素材格式、写导出器、适配角色骨骼，再加入喷气背包等玩法；是跨游戏 Mod，不是完整反编译。**10/5 · 678 赞 · 其他 AI 逆向。**
9. **[Urban Terror：把多人射击游戏搬进浏览器](cases/urban-terror-web.md)** — 找到引擎与字节码的数据布局差异，作者报告修复后可在浏览器运行并连接多人服务器。**10/3 · 479 赞 · 其他 AI 逆向。**
10. **[GarageBand：研究文件格式，让 AI 使用本地乐器作曲](cases/garageband-file-format.md)** — 把音乐工程格式分析接进音乐视频制作流程，展示最终作品；未公开详细格式规格。**10/2 · 272 赞 · 其他 AI 逆向。**

### 经典案例

- **[Universal Modder](cases/universal-modder.md)** — 分析引擎与素材格式，把 Minecraft 内容放进 GTA V 等游戏；记录快照 **14,340 赞**。`其他 AI 逆向`
- **[Firefighter：从 DOS 二进制到 Rust](cases/firefighter-rust.md)** — 作者报告恢复 Pascal 逻辑，再转写为可维护的 Rust 代码；记录快照 **7,833 赞**。`其他 AI 逆向`
- **[《现代战争 2》：多 Agent 重建代码](cases/mw2-decompilation.md)** — 作者报告 17 个 Agent 协作三个月，83% 函数字节级匹配；代码未公开，未独立复现。`其他 AI 逆向`
- **[智能马桶：从小程序协议到 Mac 状态栏](cases/smart-toilet.md)** — 分析蓝牙通信，控制翻盖；作者后来报告扩展到家中其他设备。`REA · 作者报告`

## 目录

- [游戏与游戏保存](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/games.md)（26）
- [硬件与设备互通](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/hardware.md)（32）
- [应用与客户端](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/apps.md)（61）
- [算法与功能重建](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/algorithms.md)（9）
- [贡献案例](https://github.com/songshikang0111/awesome-REA-cases/blob/main/CONTRIBUTING.md) · [维护方法](https://github.com/songshikang0111/awesome-REA-cases/blob/main/MAINTENANCE.md)

分类页保留全部通过筛选的案例、进行中的项目和具体 idea；首页不展开全量清单。`待验证`、`进行中`、`分析测试`、`相关项目`不是已完成或已独立验证的成果。

## 说明与许可

非 REA 官方项目。内容据作者与项目记录整理，未由本合集独立复现。仅提供原创摘要与公开链接，不分发原软件、游戏资产、密钥或私人材料。

原创摘要、数据整理与代码采用 [MIT License](LICENSE)；链接内容保留各自权利，研究或复现前请确认相应授权。
