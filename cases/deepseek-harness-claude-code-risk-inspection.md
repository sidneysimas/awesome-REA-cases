# Claude Code 风控：用户将拒答后的研究交给 DeepSeek Harness

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-20
阶段：待验证

10月20日10:44（北京时间），@wquguru 介绍个人工作分配：Claude Code约占95%，DeepSeek Harness约占5%。对Claude Code认为有风险或不愿处理的事，作者转用DeepSeek Harness，具体列出逆向分析、配置代理与拆Claude Code自身风控，并认为1017版本在一些场景更顺手。

可记录的具体目标是研究Claude Code的风控行为，背景是原工具拒绝后的替代模型选择。来源没有给规则、样本、补丁或对照结果，不能将工具偏好写成已绕过风控、恢复安全策略或实现代理；也没有确认REA参与。95%/5%只是作者自报使用比例，不是任务成功率，本合集未做绕过测试。

## 来源

- [wquguru：DeepSeek Harness与Claude Code风控研究的用途自述](https://x.com/i/status/2112374333184311413)

[English](en/deepseek-harness-claude-code-risk-inspection.md) | [返回目录](../README.zh-CN.md)
