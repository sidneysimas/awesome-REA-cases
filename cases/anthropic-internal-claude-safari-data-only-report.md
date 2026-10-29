# Safari：二手报道内部Claude模型以纯数据链绕过同源策略

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-29
阶段：分析测试

2026年10月29日09:33:04（北京时间），Ummon在五目标报道中转述Anthropic的Safari研究：人工初始提示后的未具名内部模型组合JavaScriptCore TypedArray释放后使用、Gigacage边界与WebContent IPC问题，获得读取历史、cookies和会话数据库的路径，并使同源策略失效。目标是页面间的数据隔离，不把它写成Safari远程代码执行。

补读10月27日发布的官方文章，确认这是不依赖任意代码执行的data-only链，有些单独行为是设计功能，组合才形成缺陷。官方称Apple在收到报告当天确认、随后及时修复，修复已可供用户使用；不是当天必然完成修复。较早官方材料只作候选补证，不算本窗口新发布。

本合集未读Apple公告、源代码或运行演示，没有接触用户历史或会话。未具名研究模型不等于某个已发布Claude版本，人工提示不等于完全自主，REA未提及；修复状态、影响范围和实际测试条件仍是项目报告，未独立复现。

共同候选快照0赞、157浏览、0转发；不把同源策略绕过升级为任意代码执行。
厂商确认和修复为报道归因，未独立验证或读取任何会话数据。

## 来源

- [Ummon完整报道中的Safari纯数据链，2026-10-29](https://x.com/i/status/2115617884533907835)
- [补充原始研究：10月27日Anthropic Safari章节](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude#2-a-one-click-exploit-chain-in-safari)

[English](en/anthropic-internal-claude-safari-data-only-report.md) | [返回目录](../README.zh-CN.md)
