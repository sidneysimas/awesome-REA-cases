# kindle-ai-usage：Codex辅助越狱旧Kindle，显示AI用量的API等价估价

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-24
阶段：待验证

2026年10月21日至22日，三份You can just build things硬件社区介绍转述：开发者用Codex越狱十年旧Kindle，把墨水屏变为AI用量看板，经Node.js服务取图，每六小时刷新后休眠，显示月累计、月底预测和来源拆分。用途是复用旧电子书的常显与低功耗特性，而不是恢复Kindle源码。

10月26日补查找到与转述特征吻合的Kuberwastaken/kindle-ai-usage，静态阅读固定提交19d9dd8的README（提交日期8月28日，早于候选窗口）。项目引用@kuberwastaken本人称用Codex越狱十年旧Kindle，文档给出原KT3路线、FBInk、RTC唤醒、Wi-Fi取图和休眠流程。它明确显示API-equivalent list price，即按API标价折算的用量估计，不是订阅实付价格；因此不能照搬转述中的“AI订阅花费”当账单事实。文档列出Codex、Claude Code、OpenCode、Gemini CLI的本地采集器，以及Cursor、Claude API、Copilot和Gemini账本等导入方式；只发送每日汇总，并提醒避免镜像历史和多来源重复计数。这些是项目文档描述，未访问任何真实日志、账单或账号。

公开仓库包含Node服务和agent skill，要求先确认确切Kindle型号/固件并查现行越狱兼容指南，不假定原KT3路线适用所有机器；六小时采集后五分钟唤醒，取图失败保留旧画面。主机需在刷新时在线；普通Kindle不能直接加入Tailnet，需要可达私有局域网或显式网关。未安装依赖、运行测试或越狱设备，预测准确性、电池续航和跨型号成功率均未独立验证。补读的旧提交用于核对身份与纠正计费语义，不冒充当前候选窗口中的新发布。

社区转述与公开项目文档交叉核对；10月24日20:05的候选明确@kuberwastaken，补足作者身份，其中rekindle天气屏是另一用途，不合并。原KT3路线不可泛化为所有Kindle，未独立部署。
费用是API等价标价估算，不是订阅账单；源码与skill已定位，但测试、电池续航和实际账单未核验。

## 来源

- [硬件社区介绍，2026-10-21](https://x.com/i/status/2112892660251795697)
- [看板流程转述，2026-10-22](https://x.com/i/status/2113242014242287678)
- [另一份社区项目清单，2026-10-21](https://x.com/i/status/2112738503222349881)
- [8月28日固定提交README，10月26日静态补读](https://github.com/Kuberwastaken/kindle-ai-usage/blob/19d9dd82167c961cc7c93bcafd0225859ddc6390/README.md)
- [10月24日补证：明确作者为kuberwastaken](https://x.com/i/status/2113965002994733345)

[English](en/codex-kindle-ai-spending-dashboard-report.md) | [返回目录](../README.zh-CN.md)
