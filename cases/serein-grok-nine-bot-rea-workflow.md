# Serein 九 Bot 工作流：REA 行为规格交给隔离 Builder

分类：应用与客户端 · REA
记录日期：2026-10-17
阶段：待验证

2026年10月17日15:54（北京时间），一则中文帖转述九个专职 Grok Bot 的每周产品开发流程，称原作者的 Mac 浏览器 Serein 由此做出。具体逆向环节是在 Grok 云电脑中把 REA 接为自定义 MCP：Behavior Reverser 只提取“用户动作→内部步骤→结果”的行为链，Spec Writer 整理为 SPEC.md，再交完全隔离的 Builder 编写代码和自动化测试，禁止导出私有源码。目的是把竞品功能研究转为独立实现的输入。

流程还描述用文件与 HANDOFF.md 交接、上游标记 DONE 后下游才开始，并用市场差评、策略和分销指标决定是否继续。上述是来源对模板和作者实践的转述，不是本合集实际部署九 Bot 或验证隔离。没有读到原始长文、Serein 仓库、被研究的具体竞品、测试结果或运行记录；不能由“clean-room”标签推定隔离或法律合规已获证明，也不把定时任务模板当持续运行的证据。

二手流程报告；原长文与实现未核实，未运行 Bot 或调度。

## 来源

- [九 Bot、Serein 与 REA 规格交接的中文转述](https://x.com/i/status/2111365135143219711)

[English](en/serein-grok-nine-bot-rea-workflow.md) | [返回目录](../README.zh-CN.md)
