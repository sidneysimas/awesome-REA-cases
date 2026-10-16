# crashlens：把 REA 接入崩溃分诊与编程 Agent

分类：应用与客户端 · REA
记录日期：2026-10-16
阶段：相关项目

10月16日 @rae1101x（Minglei）提出在 Hermes 的 reverse-engineer-anything 旁加入 crash-triage Skill，用于 core dump、panic 和 sanitizer 报告，称只读并可配合固定的 rea-agents@6.4.0，愿意提交 PR。19:54 他又说明愿景是日志不足时解释生产崩溃、异常和 bug，并明确项目仍早期。补查同串16:13原帖，作者已称在 REA 上做了 crashlens，而不只是一个尚未启动的想法；这条补充原帖不是额外候选。

本轮阅读 mingleiw/crashlens 的公开 README：项目自称 early prototype，支持 Linux x86-64 core dump、多语言堆栈与 sanitizer 报告，整理故障帧、原因、此前日志、可选源码归因及输入哈希；提供 Claude Code Skill 和三个只读 MCP 工具，原生 core dump 路径还需 REA。文档说不运行被分析程序，基础分析离线；可选 --ai 才把报告交给 Anthropic 请求修复建议，不能将“只读”理解成开启该选项后仍无外发。这里只核查文档和项目存在，未安装或执行，没有独立崩溃定位准确率或生产故障验收。Hermes PR 的意愿与对方愿意审阅不等于已提交、合并或官方发布；保留为公开相关项目。

候选更新：2026-10-16 19:11、19:54，北京时间。
公开文档为本轮补证；原型能力是项目声明，不是独立复现，Hermes 集成仍为计划。

## 来源

- [候选：作者提出 Hermes 崩溃分诊 Skill](https://x.com/i/status/2111052456151154858)
- [候选：作者说明生产故障愿景与早期状态](https://x.com/i/status/2111063236355498247)
- [同串16:13作者项目介绍（补充来源）](https://x.com/i/status/2111007641715786116)
- [crashlens 公开项目与 README（本轮只读检查）](https://github.com/mingleiw/crashlens)

[English](en/crashlens-rea-crash-triage-idea.md) | [返回目录](../README.zh-CN.md)
