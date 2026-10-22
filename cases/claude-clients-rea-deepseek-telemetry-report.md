# Claude 客户端遥测：Mac／Android分析与Linux的REA／DeepSeek跟进

分类：应用与客户端 · REA
记录日期：2026-10-22
阶段：分析测试

2026年10月21日11:28（北京时间），WquGuru（wquguru）称在Mac上用REA、DeepSeek Harness与flatkey模型接入，分析其称为Claude Code的Mac CLI、Mac App和Android App，整理代理规则；指定模型为deepseek-v4-1-flash-1017。

作者报告Android通过Sift反欺诈、检查SIM国家并结合ANDROID_ID、Play Integrity和硬件key，声称重装仍不变；Mac端用Sentry与Datadog遥测，随机ID不绑硬件。iOS“差不多”明确只是该作者的推测。本条保存调查线索与归因，不把各应用品牌、SDK字符串、实际上传行为和硬件标识生命周期混为已确认事实。

10月22日15:30的本轮候选中，molang（@123molang）回复称用REA与DeepSeek研究Linux版本，结论与Mac几乎一致。本次补查父串确认所指客户端。15:57同作者补充说CLI基本同源、desktop高度共享，并让GPT总结差异：Linux SSH模块读取网卡IP/MAC用于网络变化检测与重连，未发现这条链上传原值；Mac存在特定VM故障时VPN诊断上报。这是作者报告的局部观察与模型总结，不证明全部Linux客户端不上传网络信息，也不能用“同源”代替源码级等价检查。15:57回复是补充上下文，不另算新候选。

来源没有精确安装包、构建、哈希、调用链、网络捕获或重装对照，完整规则链接未展开核验；不能称全网最全、永久硬件追踪、代理规则能防封或保证隐私。原文含模型网关促销，不能将推广描述当安全评估。本合集未安装客户端、操作账号或独立验证流量。

新增候选原发：2026-10-22T15:30:55+08:00；补充作者回复同日15:57:14，北京时间。

## 来源

- [WquGuru：REA／DeepSeek客户端分析与代理规则报告](https://x.com/i/status/2112747723078422809)
- [本轮候选：molang用REA与DeepSeek研究Linux版本](https://x.com/i/status/2113171225874960572)
- [补充作者回复：GPT总结Linux与Mac局部差异](https://x.com/i/status/2113177847636648398)

[English](en/claude-clients-rea-deepseek-telemetry-report.md) | [返回目录](../README.zh-CN.md)
