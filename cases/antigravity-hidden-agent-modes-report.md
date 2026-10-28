# Antigravity内部研究：旧隐藏模式转述与Jerry的Gemini辅助2.27.0枚举分析

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-28
阶段：分析测试

2026年10月21日19:37（北京时间）的历史来源称Antigravity的jetski/language_server.exe藏有/owl、/battle、/benchmark、/compaction四种未公开多Agent模式，并推荐扩展Skill。其/battle被描述为两个subagent在隔离Git分支工作、critic选胜者合并，/benchmark用于测优化。该旧来源未给二进制版本、偏移、代码或命令记录，也未说明AI角色；四个名字是否内建可用、Skill是否调用隐藏实现仍未知，不能由新来源倒证。

10月28日13:57:26，Jerry Xiong（@Jerry_Galaxy）报告本地研究客户端2.27.0的156MB language_server，称看到Gemini4 Argon的High/Medium/Low，未见Carbon或4-Flash独立代号；发现MODEL_CUSTOM_VLLM、MODEL_CUSTOM_OPEN_ROUTER及Claude BYOK协议，又指出gemini-v4s-jarvis-sc、MODEL_GOOGLE_JARVIS_PROXY、Step_ClickBrowserPixel与鼠标、拖拽、键盘、DOM、滚动等浏览器动作，并列OrionFire、CosmicForge、RiftRunner及Thinking、InfinityBloom/InfinityJet。大小、代号和功能解释都是作者的静态分析报告，不当Google正式路线图。补查原帖确认署名和枚举截图附件；同日14:02:40作者也说最终以Google正式发布为准。

窗口外同日17:05:47，Jerry补充没有专业逆向工具：在Mac将安装包复制到独立工程目录，解压后直接让Gemini模型分析。这只补充本窗口候选的方法归因，不是另一候选或新实验；明确了AI角色，不推断REA参与。协议枚举至多表明客户端预留或包含字段，不证明服务可用、路由已上线、BYOK受支持或Jarvis完整可执行。没有二进制哈希、偏移、反编译文本、代码仓库、模型版本或运行验证，截图未独立核验；也不能以未见某代号证伪其他版本或服务端模型。

同目标追加而保留既有ID与历史URL，区分旧扩展模式转述和新版本研究；不与OpenCodex签名丢失项目混同。不提供启用隐藏功能的安装指令，未取得或执行安装包、连接服务或独立复现，状态为分析测试而非已证实功能清单。

历史来源2026-10-21T19:37:00+08:00的隐藏模式仍未验证；新版本枚举不证明旧扩展行为。
10月28日候选快照3赞、523浏览、1转发；2.27.0、156MB及全部代号按作者报告，未运行目标。
17:05方法回复晚于本窗口16:00 end，仅作候选研究方法补证；连续证据截止不因此推进。

## 来源

- [历史：Antigravity四个隐藏模式与扩展Skill转述，2026-10-21](https://x.com/i/status/2112870764991181226)
- [候选：Jerry的2.27.0 language_server枚举研究，2026-10-28](https://x.com/i/status/2115322026089205783)
- [同日14:02补充：作者称以Google正式发布为准](https://x.com/i/status/2115323343943729371)
- [窗口外同日17:05补证：Mac解包后用Gemini分析](https://x.com/i/status/2115369425616679197)

[English](en/antigravity-hidden-agent-modes-report.md) | [返回目录](../README.zh-CN.md)
