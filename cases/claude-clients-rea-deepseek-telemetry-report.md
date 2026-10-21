# Claude 客户端遥测：REA 与 DeepSeek 分析 Mac／Android 的代理规则报告

分类：应用与客户端 · REA
记录日期：2026-10-21
阶段：分析测试

2026年10月21日11:28（北京时间），WquGuru（wquguru）称在Mac上用REA、DeepSeek Harness与flatkey模型接入，分析其称为Claude Code的Mac CLI、Mac App和Android App，整理代理规则；指定模型为deepseek-v4-1-flash-1017。

作者报告Android通过Sift反欺诈、检查SIM国家并结合ANDROID_ID、Play Integrity和硬件key，声称重装仍不变；Mac端用Sentry与Datadog遥测，随机ID不绑硬件。iOS“差不多”明确只是推测。本条保存调查线索与归因，不把各应用品牌、SDK字符串、实际上传行为和硬件标识生命周期混为已确认事实。

帖子没有精确安装包、构建、哈希、调用链、网络捕获或重装对照，完整规则链接未展开核验；不能称全网最全、永久硬件追踪、代理规则能防封或保证隐私。原文含模型网关促销，不能将推广描述当安全评估。本合集未安装客户端、操作账号或独立验证流量，未采用补查串中较晚回复作为严格窗口新结果。

## 来源

- [WquGuru：REA／DeepSeek客户端分析与代理规则报告](https://x.com/i/status/2112747723078422809)

[English](en/claude-clients-rea-deepseek-telemetry-report.md) | [返回目录](../README.zh-CN.md)
