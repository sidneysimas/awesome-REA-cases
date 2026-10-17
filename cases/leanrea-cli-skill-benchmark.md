# LeanREA：8 KB CLI Skill 与 REA 的 Notion／原生库／Go 对照

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-17
阶段：分析测试

10月17日11:09（北京时间），@aicodeking 发布 LeanREA，称用一个8 KB Skill 指导 Agent 直接调用 CLI 工具，不经过 MCP。按名称查到 aicodeking/leanrea，补读 README、bench/BENCHMARK.md 与提交元数据，确认初始仓库提交在当日10:53，基准文档自标10月16日。四项任务是 Notion app.asar 的麦克风／会议检测调用链、mac_utils.node 的导出与 TCC 权限和单实例锁、去符号 gh 的构建依赖信息，以及仅凭反汇编恢复锁的 socket 路径、通信协议与对端认证。

项目用 Claude Code 2.1.301 headless、Sonnet 5.5、macOS arm64，对 LeanREA、无 Skill、REA 6.5.0 MCP 加原 Skill 三组各做每任务三次，共36次。细表列每组12次累计：LeanREA 388秒、2.17美元、55轮、240万 tokens，得分74/75；REA 627秒、3.36美元、124轮、593万 tokens，75/75；无 Skill 479秒、2.21美元、81轮、311万 tokens，67/75且一次拒绝。所谓快38%、便宜35%、少56%轮次是项目的聚合结果，不是本合集测量；宣传“同准确率”不严谨，LeanREA 曾把 v2 IPC 通道答成同时存在的 v1。

答案按作者手写答案表和正则评分，文档还披露无 Skill 的 Go 版本字符串曾被正则误判并更正。单模型、单机器、每格三次；没有安装完整原生分析引擎，不能外推 Ghidra／Hopper／IDA 或 APK 任务。README 另称 jadx 也未安装。REA 组启用按需工具检索，400.7k 上下文数字只对应关闭检索、一次加载全部工具的独立探针，不是36次主对照的默认成本。同串有人质疑 Electron 依赖安装审批等待和统一批处理／输出限制是否计入，本轮没有作者解答。公开基准与原始指标路径使它比单句宣传更可追查，但本合集没有执行仓库、模型或目标，不将本测试推广为 LeanREA 普遍替代 REA。

发布候选快照（2026-10-17）：31赞、557浏览、2转发；补读时变化的浏览数不覆盖原快照。
作者基准，不是独立复现；74/75与75/75有差异，36次不等于36个不同目标。

## 来源

- [LeanREA 发布与36次对照声明](https://x.com/i/status/2111293595529703853)
- [公开项目 README](https://github.com/aicodeking/leanrea)
- [初始提交中的完整基准与限制](https://github.com/aicodeking/leanrea/blob/a07ed0ebf1c585d9db535f91a91ef555b8920b90/bench/BENCHMARK.md)
- [同串读者追问：安装审批等待是否计时](https://x.com/i/status/2111299719888884167)
- [同串读者追问：统一批处理与输出限制](https://x.com/i/status/2111298045421953535)

[English](en/leanrea-cli-skill-benchmark.md) | [返回目录](../README.zh-CN.md)
