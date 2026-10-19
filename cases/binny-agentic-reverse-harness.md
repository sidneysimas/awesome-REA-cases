# BINNY：面向逆向研究的多模型 Agent harness 公测

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-19
阶段：相关项目

BINNY的10月16日发布帖把它介绍为面向逆向工程师和安全研究者的public beta Agent harness，即组织模型工具与执行流程的框架。10月19日12:59的@ainotesus和13:47的@QingQ77候选进一步说明：BINNY本身不是模型，用户接入Claude、GPT、DeepSeek、Qwen或本地模型，让它读取反编译函数、字符串和导入表，按triage、investigate、draft循环形成报告草稿。用途是减少重复二进制研究，而非取代人工验收。

本轮找到openbin-ai/binny公开仓库，读取10月18日00:28北京时间提交000b6aca8c9d266b38252470102ac16c98575cd8对应README。文档给出STIX 2.1恶意软件分类、Ghidra本地反编译、逐步自动保存与恢复、token预算、三种自主程度及报告草稿复核。Go实现与AGPL-3.0-or-later为项目文档声明；README另保留仓库私有的旧措辞，不据此猜平台状态。它可以用OpenBin/OpenAPK项目，也可本地处理文件；本地不上传不等于模型提供商不会收到分析内容。

README说明脚本在Docker无网络、只读根和样本挂载、去capabilities及资源限制下运行。这里只核对文档，没有安装、构建、执行样本或测试容器边界，因此不认证隔离安全、报告准确率、所有模型兼容或具体目标分析成功。更正旧条目‘未取得公开项目与许可证内容’的证据状态，但并未完成源码实现审计；REA使用未确认。补充README是较早项目背景，不当成新候选帖子。

10月16日候选快照：96赞、3548浏览、9转发；热度不代表功能验证。

## 来源

- [BINNY public beta 发布帖](https://x.com/i/status/2110767491286716525)
- [10月19日候选：STIX、Ghidra与检查点介绍](https://x.com/i/status/2112045894359027776)
- [10月19日候选：Go框架、自带模型与预算定位](https://x.com/i/status/2112057908573675756)
- [公开README：分析循环、沙箱设计与许可声明](https://github.com/openbin-ai/binny/blob/000b6aca8c9d266b38252470102ac16c98575cd8/README.md)

[English](en/binny-agentic-reverse-harness.md) | [返回目录](../README.zh-CN.md)
