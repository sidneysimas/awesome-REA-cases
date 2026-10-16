# Awesome REA Cases

[English](README.md) | **简体中文**

**用 AI 读懂软件与硬件：重建功能、打通协议、迁移旧系统。**

当前收录 **277 个案例与项目**。*最近维护与案例数统计：2026 年 10 月 16 日 12:33；连续已解决材料的案例证据截止：2026 年 10 月 15 日 16:00（北京时间）。*

每天 6 次定时追踪 REA 与 AI 逆向公开案例，筛选、去重并更新。本次逐条审读所提供的 10 月 16 日 08:00 至 12:00（北京时间，起点不含、终点含）132 条候选，另补审 16 条往期材料，新增 13 个项目、作者报告与具体 idea，并补明预览重建的 47 项检查由 AI 自写自跑。新内容包括能追溯编译环境研究的 Saturn 移植、MoonBit 调试符号、Linux 远程被控端，以及签名与结构体分析的证据边界；早期原帖单独注明日期，不冒充本轮新成果。仍有 27 条材料待核实，含全部 16 条往期线索，最早窗口始于 10 月 15 日 16:00，因此连续证据截止保持不变，可判断的较新项目照常收录。检索受关键词与分页边界限制，不代表全网全量；证据截止不表示所有项目已独立验证。首页由维护者亲自阅读与选编，完整收录见[全部案例](INDEX.md)。

[REA](https://github.com/morluto/rea)（Reverse Engineer Anything）通过 CLI / MCP，让编程 Agent 调用本地逆向工具。本合集也收录其他 AI 辅助逆向，以及为 AI 工具实现互通的项目。

## 近期精选 Top 10

综合近期传播热度、具体用途和阅读价值手工挑选，不是实时排行榜。以下热度为 2026 年 10 月 12–16 日各来源的记录快照，不是当前实时数据；条目日期为来源发帖日期，热度不代表成果已被验证。

1. **[底片与相机：给 Claude 一个能对照的 Windows 参考](cases/schaller-opticfilm-thinkpad-linux.md)** — Schaller 从家人旧底片出发，用 USB 抓包研究新版 Plustek 8200i，再改善 ThinkPad MIPI 相机。公开测量也写清单机样本、低光蓝色不足与未修复曝光问题；补丁送审不等于合并。**10/16 转述 · 10/15 原文补证 · 其他 AI 逆向 · 作者与项目报告。**
2. **[Sonic 3D Blast：模型之外，还要重建编译环境](cases/sonic-3d-blast-saturn-opus-port.md)** — 作者本轮确认 Opus 参与；早期更新讲清 Claude 重建 Hitachi 编译环境、字节匹配与 Saturn 到 PC 的原生移植，也保留未修复画面问题。**10/16 确认 · 7–10 月背景补证 · 其他 AI 逆向 · 进行中；11/20 是计划，不是已经发行。**
3. **[ReaCut：不止画界面，也公开导出与验证边界](cases/reacut-jianying-open-editor.md)** — 从剪映本地行为研究走向独立编辑器，项目记录包含真实视频导出与插件测试；同时明示未公证、跨平台与 CI 限制。**10/15 · REA · 进行中；验收为项目报告。**
4. **[LASRecomp：把 Switch《织梦岛》带到电脑](cases/links-awakening-claude-pc-port-report.md)** — 公开项目自述几乎由 Claude Code 完成，需自备原作；beta 文档也列出特定操作崩溃、Linux ARM 未实测等问题。**10/15 · 此前转述快照 144 赞 · 其他 AI 逆向 · 未独立运行。**
5. **[读板仪：先研究通信，再谈“修好了”](cases/plate-reader-filter-wheel-claude-repair.md)** — 滤光轮机械与光学检查正常，却卡在开机自检。作者称 Claude 找到通信方法、重置固件并建立监测；设备型号、命令与临床质量验收仍缺。**10/15 · 其他 AI 辅助研究 · 作者报告，不是医疗设备安全认证。**
6. **[ScanSnap iX500：系统升级后，旧扫描仪不退休](cases/scansnap-ix500-claude-mac.md)** — 官方 Mac 应用失效后，Jonas Wagner 称用 Claude Code 做出 Wi-Fi 扫描、实体按钮、OCR 和空白页处理；未公布可核对的协议过程。**10/15 · 2 赞 · 其他 AI 逆向 · 作者报告，未独立验收。**
7. **[KEF LSX II：修好桌面音箱的音量键体验](cases/kef-lsx-ii-volume-fixer.md)** — Claude 辅助做 USB 音频透传与局域网音量桥，不改签名固件；测量曲线和约 2 ms 附加延迟均为作者报告。**10/15 · 其他 AI 辅助互通 · 有公开实现。**
8. **[飞书：两个账号，不再来回切换](cases/feishu-dual-instance-codex-rea.md)** — Codex + REA 分析后，作者报告在副本中隔离数据与单实例锁，并做签名和目录检查；本地签名、关闭更新仍有维护风险。**10/15 · REA · 作者实测，非独立复现。**
9. **[Electron Notes：答案表全对，输出却大了很多](cases/rea-electron-notes-ipc-answer-key-test.md)** — 三次静态分析识别 4/4 通道、handler 与 preload 成员；作者也指出 2.3 KB 源码产生 1.0 MB JSON。只证明这次小样本观察，不是所有 Electron 的准确率保证。**10/16 · REA · 作者分析测试，未独立复跑。**
10. **[MoonBit：让调试器里的符号重新可读](cases/moonbit-claude-debugger-demangling.md)** — 为研究项目试新语言，却遇到满屏改名符号；作者称 Claude 分析编码规则，写出 VSCode customDescriptionGenerator，未提供代码与测试。**10/16 · 其他 AI 逆向 · 作者报告，未独立运行。**

### 经典案例

- **[Universal Modder](cases/universal-modder.md)** — 分析引擎与素材格式，把 Minecraft 内容放进 GTA V 等游戏；记录快照 **14,340 赞**。`其他 AI 逆向`
- **[Firefighter：从 DOS 二进制到 Rust](cases/firefighter-rust.md)** — 作者报告恢复 Pascal 逻辑，再转写为可维护的 Rust 代码；记录快照 **7,833 赞**。`其他 AI 逆向`
- **[《现代战争 2》：多 Agent 重建代码](cases/mw2-decompilation.md)** — 作者报告 17 个 Agent 协作三个月，83% 函数字节级匹配；代码未公开，未独立复现。`其他 AI 逆向`
- **[智能马桶：从小程序协议到 Mac 状态栏](cases/smart-toilet.md)** — 分析蓝牙通信，控制翻盖；作者后来报告扩展到家中其他设备。`REA · 作者报告`
- **[Apple TV 遥控器接入 Linux](cases/siri-remote-linux.md)** — 蓝牙协议互通与公开实现；记录快照 **5,419 赞**。`未确认 REA`
- **[LG PlxNative](cases/lg-plxnative.md)** — 研究原生媒体栈，作者报告用户选择从约 30 秒到 3 秒；记录快照 **7,268 赞**。`其他 AI 逆向`

## 目录

- [游戏与游戏保存](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/games.md)（65）
- [硬件与设备互通](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/hardware.md)（63）
- [应用与客户端](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/apps.md)（124）
- [算法与功能重建](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/algorithms.md)（25）
- [贡献案例](https://github.com/songshikang0111/awesome-REA-cases/blob/main/CONTRIBUTING.md) · [维护方法](https://github.com/songshikang0111/awesome-REA-cases/blob/main/MAINTENANCE.md)

分类页保留全部通过筛选的案例、进行中的项目和具体 idea；首页不展开全量清单。`待验证`、`进行中`、`分析测试`、`相关项目`不是已完成或已独立验证的成果。

## 说明与许可

非 REA 官方项目。内容据作者与项目记录整理，未由本合集独立复现。仅提供原创摘要与公开链接，不分发原软件、游戏资产、密钥或私人材料。

原创摘要、数据整理与代码采用 [MIT License](LICENSE)；链接内容保留各自权利，研究或复现前请确认相应授权。
