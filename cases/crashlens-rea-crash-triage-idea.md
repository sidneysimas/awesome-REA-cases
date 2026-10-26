# crashlens：把 REA 接入崩溃分诊与编程 Agent

分类：应用与客户端 · REA
记录日期：2026-10-25
阶段：相关项目

2026年10月16日，@rae1101x（Minglei）提出在Hermes的reverse-engineer-anything旁加入crash-triage Skill，处理core dump、panic与sanitizer报告，称只读并配合固定rea-agents@6.4.0，愿意提交PR。19:54称目标是日志不足时解释生产崩溃与bug且项目仍早期。同串16:13补充原帖已称在REA上做了crashlens；它不是尚未启动的想法，但提PR意愿和对方愿意审阅不证明已提交、合并或官方发布。

10月25日00:26:57（北京时间），本窗口候选报告在无日志、源码或调试符号的原生崩溃中，Claude Code找原因从4轮变为1轮。02:05:09同作者向另一用户分享调试用途。补读窗口后15:10:24作者解释：1轮成绩是预先反编译崩溃函数与其调用者，将报告交给Claude Code；REA经MCP还可让Agent主动驱动Ghidra继续反编译，但更慢，适合问题超出那两个函数的情况。不能把预生成报告路径的轮数当成完全自主MCP端到端耗时，也不能据此推定所有崩溃四倍提速。

补读公开README，最新修改提交为74c3ace797019d084bbf810f3f1f2ef48adf277b，提交时间10月26日11:45:44北京时间，在窗口后，仅用于核对项目与现有文档，不能倒填为25日凌晨能力。原型支持Linux x86-64 core、多语言堆栈与sanitizer报告，整理故障帧、上下文、可选源码归因及输入哈希；当前文档提供Claude Code插件与4个只读MCP工具，原生core路径需REA，可选Ghidra提供标为反编译输出的伪代码而非原始源码。文档也列出剥符号原生二进制4轮对1轮的小基准，并明确小测试仓库不是研究。无符号二进制身份、完整对照运行与生产故障验收未独立核验。基础分析离线且不运行目标，可选--ai会将包含代码片段和日志的报告交给Anthropic；只读不等于无外发。未安装、执行或运行项目基准，保留related-project与早期状态。

早期候选2026-10-16 19:11、19:54；新增候选10月25日00:26:57、02:05:09，北京时间。
4轮对1轮是作者报告，预生成崩溃函数及调用者报告，不是完全自主MCP的受控端到端对比。
窗口后10月25日15:10:24的作者澄清与10月26日11:45:44提交的README只作补充；Hermes集成未确认，未运行原型或基准。

## 来源

- [候选：作者提出 Hermes 崩溃分诊 Skill](https://x.com/i/status/2111052456151154858)
- [候选：作者说明生产故障愿景与早期状态](https://x.com/i/status/2111063236355498247)
- [同串16:13作者项目介绍（补充来源）](https://x.com/i/status/2111007641715786116)
- [crashlens 公开项目与 README](https://github.com/mingleiw/crashlens)
- [新增候选：无符号原生崩溃4轮对1轮，2026-10-25](https://x.com/i/status/2114030898815611097)
- [新增候选：同作者分享REA调试方向，2026-10-25](https://x.com/i/status/2114055611562500158)
- [窗口后作者澄清：预生成两函数报告与MCP路径不同，2026-10-25](https://x.com/i/status/2114253225247625532)
- [窗口后公开README固定版本，2026-10-26](https://github.com/mingleiw/crashlens/blob/74c3ace797019d084bbf810f3f1f2ef48adf277b/README.md)

[English](en/crashlens-rea-crash-triage-idea.md) | [返回目录](../README.zh-CN.md)
