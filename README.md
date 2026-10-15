# Awesome REA Cases

**中文（默认）** | [English](README.en.md)

**用 AI 读懂软件与硬件：重建功能、打通协议、迁移旧系统。**

当前收录 **203 个案例与项目**。*最近维护与案例数统计：2026 年 10 月 15 日 20:14；连续已解决材料的案例证据截止：2026 年 10 月 15 日 16:00（北京时间）。*

每天 6 次定时追踪 REA 与 AI 逆向公开案例，筛选、去重并更新。本次逐条审读 10 月 15 日 16:00 至 20:00（北京时间，起点不含、终点含）的 133 条候选，新增 22 项、补充 8 项既有记录；仍有 1 条来源待核实，因此连续证据截止保留在 16:00，已可判断的本轮项目照常收录。检索受关键词与分页边界限制，不代表全网全量；证据截止也不表示所有项目已独立验证。首页由维护者亲自阅读与选编，完整收录见[全部案例](INDEX.md)。

[REA](https://github.com/morluto/rea)（Reverse Engineer Anything）通过 CLI / MCP，让编程 Agent 调用本地逆向工具。本合集也收录其他 AI 辅助逆向，以及为 AI 工具实现互通的项目。

## 近期精选 Top 10

综合近期传播热度、具体用途和阅读价值手工挑选，不是实时排行榜。以下热度为 2026 年 10 月 12–15 日各来源的记录快照，不是当前实时数据；条目日期为来源发帖日期，热度不代表成果已被验证。

1. **[ReaCut：不止画界面，也公开导出与验证边界](cases/reacut-jianying-open-editor.md)** — 从剪映本地行为研究走向独立编辑器，项目记录包含真实视频导出与插件测试；同时明示未公证、跨平台与 CI 限制。**10/15 · REA · 进行中；验收为项目报告。**
2. **[LASRecomp：把 Switch《织梦岛》带到电脑](cases/links-awakening-claude-pc-port-report.md)** — 公开项目自述几乎由 Claude Code 完成，需自备原作；beta 文档也列出特定操作崩溃、Linux ARM 未实测等问题。**10/15 · 本轮转述 144 赞 · 其他 AI 逆向 · 未独立运行。**
3. **[ScanSnap iX500：系统升级后，旧扫描仪不退休](cases/scansnap-ix500-claude-mac.md)** — 官方 Mac 应用失效后，Jonas Wagner 称用 Claude Code 做出 Wi-Fi 扫描、实体按钮、OCR 和空白页处理；未公布可核对的协议过程。**10/15 · 2 赞 · 其他 AI 逆向 · 作者报告，未独立验收。**
4. **[KEF LSX II：修好桌面音箱的音量键体验](cases/kef-lsx-ii-volume-fixer.md)** — Claude 辅助做 USB 音频透传与局域网音量桥，不改签名固件；测量曲线和约 2 ms 附加延迟均为作者报告。**10/15 · 其他 AI 辅助互通 · 有公开实现。**
5. **[飞书：两个账号，不再来回切换](cases/feishu-dual-instance-codex-rea.md)** — Codex + REA 分析后，作者报告在副本中隔离数据与单实例锁，并做签名和目录检查；本地签名、关闭更新仍有维护风险。**10/15 · REA · 作者实测，非独立复现。**
6. **[东方 TH08：字节匹配，也可能漏掉错误常量](cases/touhou-reconstruction.md)** — 本轮提醒追溯到 9 月 2 日原始 issue 与修复：指令引用的地址匹配了，数据却把 128.0 写成 0.0；项目随后补上浮点引用核验。**10/15 分享 · 历史修复补证 · 项目测试，非本合集重跑。**
7. **[洛克输入法：只用苹果端侧语音能力](cases/rokoinput-apple-local-voice.md)** — REA 研究后公开的个人输入工具，不支持端侧识别就停止；文字历史却默认明文保存，隐私不能只看“不联网”。**10/15 · 3 赞 · REA · 个人非商业许可。**
8. **[IsaacRecomp：Flash《以撒》的原生路线](cases/isaacrecomp-flash-cpp-report.md)** — 作者明确承认 AI 辅助，称将逻辑转为 C++，保留 30 Hz 逻辑并插值绘制；资源从用户自有原作读取，性能尚未独立测试。**10/15 · 其他 AI 逆向 · 公开项目。**
9. **[GAMEKB-K17：不用厂商网页配置宏键盘](cases/claude-code-rgb-macropad.md)** — Claude Code 研究配置协议，公开离线按键、宏和 RGB 工具；写入后读回核验，Windows 测试为项目自述。**10/15 · 7 赞 · 其他 AI 逆向。**
10. **[人类 vs. Agent：逆向能力不只看答对率](cases/humans-machines-sre-study.md)** — 九模型、两项 IDA 静态任务，再看 4,000 个程序的上下文饱和；论文强调导航与选择性检索，而不是仅增大窗口。**10/15 分享 · 10/10 论文 · 非 REA 测评。**

### 经典案例

- **[Universal Modder](cases/universal-modder.md)** — 分析引擎与素材格式，把 Minecraft 内容放进 GTA V 等游戏；记录快照 **14,340 赞**。`其他 AI 逆向`
- **[Firefighter：从 DOS 二进制到 Rust](cases/firefighter-rust.md)** — 作者报告恢复 Pascal 逻辑，再转写为可维护的 Rust 代码；记录快照 **7,833 赞**。`其他 AI 逆向`
- **[《现代战争 2》：多 Agent 重建代码](cases/mw2-decompilation.md)** — 作者报告 17 个 Agent 协作三个月，83% 函数字节级匹配；代码未公开，未独立复现。`其他 AI 逆向`
- **[智能马桶：从小程序协议到 Mac 状态栏](cases/smart-toilet.md)** — 分析蓝牙通信，控制翻盖；作者后来报告扩展到家中其他设备。`REA · 作者报告`
- **[Apple TV 遥控器接入 Linux](cases/siri-remote-linux.md)** — 蓝牙协议互通与公开实现；记录快照 **5,419 赞**。`未确认 REA`
- **[LG PlxNative](cases/lg-plxnative.md)** — 研究原生媒体栈，作者报告用户选择从约 30 秒到 3 秒；记录快照 **7,268 赞**。`其他 AI 逆向`

## 目录

- [游戏与游戏保存](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/games.md)（40）
- [硬件与设备互通](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/hardware.md)（53）
- [应用与客户端](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/apps.md)（94）
- [算法与功能重建](https://github.com/songshikang0111/awesome-REA-cases/blob/main/categories/algorithms.md)（16）
- [贡献案例](https://github.com/songshikang0111/awesome-REA-cases/blob/main/CONTRIBUTING.md) · [维护方法](https://github.com/songshikang0111/awesome-REA-cases/blob/main/MAINTENANCE.md)

分类页保留全部通过筛选的案例、进行中的项目和具体 idea；首页不展开全量清单。`待验证`、`进行中`、`分析测试`、`相关项目`不是已完成或已独立验证的成果。

## 说明与许可

非 REA 官方项目。内容据作者与项目记录整理，未由本合集独立复现。仅提供原创摘要与公开链接，不分发原软件、游戏资产、密钥或私人材料。

原创摘要、数据整理与代码采用 [MIT License](LICENSE)；链接内容保留各自权利，研究或复现前请确认相应授权。
