# Chrome：Anthropic报告内部模型串联浏览器漏洞与越沙箱

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-29
阶段：分析测试

2026年10月29日09:33:04（北京时间），署名Ummon的报道引用Anthropic文章“Discovering and exploiting vulnerabilities in critical, real-world software with Claude”，称团队数月使用未发布、未具名内部研究模型调查浏览器和操作系统。Chrome目标是从网页输入达到沙箱外执行，涉及V8内存破坏、V8内存区域边界、CacheStorage竞态与FedCM释放后使用；只记录研究形态，不提供复现载荷。

补查读到官方文章，页面发布日期为10月27日，早于候选，不是报道所说当天新发布。官方正文确实报告macOS默认配置Chrome页面载入后数秒启动计算器，无需进一步操作；称Google分配、截至Chrome156修复62个高危或严重CVE，其中13个沙箱逃逸、21个可影响renderer。不同子类不擅自相加，62不是本次单条链的漏洞数。

本合集确认官方项目自述与转述一致，但没有读厂商公告或运行演示。官方说研究从人工初始提示开始，“少量人工介入”不等于完全自主，内部研究模型不与访问计划中的具名模型混同。文章说明90天修复加45天细节披露政策；没有报告在野利用或受害者，不将其改写为已证实无人利用。CVE与修复仍是Anthropic对Google处理的描述，不是本合集安全认证；REA未提及。

共同候选快照0赞、157浏览、0转发；同帖五个独立目标分开记录。
已读10月27日官方研究；未读Google公告、运行PoC或独立核验CVE，不收录攻击载荷。

## 来源

- [Ummon完整报道中的Chrome研究，2026-10-29](https://x.com/i/status/2115617884533907835)
- [补充原始研究：Anthropic Chrome章节，页面发布于10月27日](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude#1-one-click-remote-code-execution-in-chrome)

[English](en/anthropic-internal-claude-chrome-chain-report.md) | [返回目录](../README.zh-CN.md)
