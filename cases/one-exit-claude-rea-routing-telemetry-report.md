# one-exit：据REA客户端研究整理Claude多端统一出口模板，不等于还原完整风控

分类：应用与客户端 · REA
记录日期：2026-10-24
阶段：相关项目

2026年10月24日22:47:15（北京时间），候选分享@wquguru使用REA研究Claude多端风控及one-exit项目，声称将解释链式代理、Mac与Shadowrocket配置；22:51:44同串补充将核心发现和分流规则归于wquguru。REA角色是分享者的归因，不把分享者当原研究作者，也不接受彻底解开封号机制的宣传结论。

补查公开wquguru/one-exit仓库并静态阅读README，其最后修改为2026年10月21日10:04:26（北京时间），早于本窗口。文档提供Clash Party、FlClash和Shadowrocket三份统一出口模板，将Claude、Google、Persona、Stripe、验证码及Sentry/Datadog/Sift/Segment等流量指向同一静态住宅出口。文档区分中转节点和最终出口，指出Chrome QUIC与Claude Code代理路径可能不同，提供出口一致性的检查方法，也说明占位配置、订阅覆盖与节点不可用限制。这里只记录设计，不执行配置或访问代理凭据。

公开README可以确认模板的用途，不能独立确认列出的域名是全部风控输入、所有客户端行为已恢复，或统一IP可防止封号；本次未取得原始反编译记录、抓包、服务端规则或账号对照测试。无依据将其写成绕过认证或匿名保证。按related-project保留候选的REA关联和可查模板，未安装代理、改全局配置、登录服务或运行目标代码。

REA研究归因来自候选分享；README原始更新2026-10-21T02:04:26Z，只作窗口外补充，不冒充新候选。
统一出口模板不证明完整服务端风控或防封效果；未访问凭据、安装配置或执行模板。

## 来源

- [候选：one-exit与REA研究的分享归因，2026-10-24](https://x.com/i/status/2114005807625044046)
- [同串候选：原作者归属与Mac/Shadowrocket延展说明，2026-10-24](https://x.com/i/status/2114006934491906345)
- [补充公开README，最后修改2026-10-21](https://github.com/wquguru/one-exit/blob/a34803405f7b4ddabc48081ed83929376e3c6a9d/README.md)

[English](en/one-exit-claude-rea-routing-telemetry-report.md) | [返回目录](../README.zh-CN.md)
