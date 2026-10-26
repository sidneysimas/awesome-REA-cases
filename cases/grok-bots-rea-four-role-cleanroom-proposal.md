# Grok Bots四角色REA流程：观察、规格、隔离重建与验证的提案

分类：应用与客户端 · REA
记录日期：2026-10-25
阶段：相关项目

2026年10月25日06:45:34（北京时间），francescofaenzi提出在Grok Bots的共享云电脑上改编Claude Code与REA的四角色流程，服务于自有或获授权软件的小功能互操作。Analyst独自接触REA与目标，输出标注观察、推断及未知的evidence.md；Spec Writer产出无地址、偏移或反编译命名的行为SPEC.md及测试；Rebuilder只读规格写新代码；Verifier以相同输入对照原版和重建，将差异变成测试而非直接补丁。可加Team Lead顺序协调，失败最多循环约三轮。

完整补读的原帖给出lab/与clean/目录、机器人描述、MCP注册示例、原生分析需Ghidra/Hopper/IDA及可更强环境隔离等建议。它没有命名已分析应用、运行报告、匹配率或代码；“搜索排序”只是示例请求。共享电脑上的角色指示与目录约定不等于操作系统强制隔离，不能据此保证clean-room法律合规、数据不泄漏或工具权限已限制。作为具体工程流程提案收录，不声称已部署Grok集成；本合集未执行注册命令、安装REA或运行原版目标。

来源06:45:34，北京时间；完整原帖补读，无具体目标的匹配验收。

## 来源

- [francescofaenzi完整提案：Grok Bots四角色REA工作流，2026-10-25](https://x.com/i/status/2114126178806079784)

[English](en/grok-bots-rea-four-role-cleanroom-proposal.md) | [返回目录](../README.zh-CN.md)
