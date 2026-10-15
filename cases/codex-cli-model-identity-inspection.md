# Codex CLI：检查模型身份提示词与路由字段

分类：应用与客户端 · 未确认使用 REA
记录日期：2026-10-16
阶段：分析测试

一篇讨论Agent自适应策略的帖子报告检查本地codex-cli 0.162.1：模型条目包括gpt-6.1-sol，但四个GPT-6条目的提示词开场仍统一为“You are Codex, an agent based on GPT-6.”，并提到ModelRerouteEvent与from_model字段。作者借此解释为何skills路由、快速模式策略和PR模型归属可能需要宿主补充模型身份。没有公开提取命令、样本哈希或代码定位，也没有说明AI是否参与二进制读取；以AI工具互通相关的内部行为分析收录，rea标为unknown。客户端字符串不能证明服务端偷偷降级模型，帖子中的该怀疑不作为结论。

10月15日来源；版本、模型与字段名沿用原帖；未独立提取或核实服务端路由。

## 来源

- [本地CLI检查与Agent模型身份讨论](https://x.com/i/status/2110751118343164066)

[English](en/codex-cli-model-identity-inspection.md) | [返回目录](../README.md)
