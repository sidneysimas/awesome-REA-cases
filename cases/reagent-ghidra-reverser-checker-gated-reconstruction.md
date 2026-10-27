# ReAgent：用Ghidra证据与Reverser／Checker闭环重建C／C++，Gate不是等价证明

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-27
阶段：相关项目

2026年10月27日07:00:01（北京时间），TechVerser（@realfxw）介绍ReAgent：通过Ghidra收集汇编、交叉引用、结构、虚表、控制流和字符串，由Reverser生成代码、Checker检查，再走构建与测试Gate。目标是从已编译程序产生可核查C／C++函数，不是把伪代码直接当原始源码。补查原帖确认署名与全文，随后公开仓库搜索定位Dryxio/reagent。

补充静态阅读固定d12cea338c61898b06a86fe8adb25275fa9d5615提交README；提交日期为2026年9月10日04:39:30北京时间，早于候选，补查时间不冒充新版本发布日期。文档确认支持Claude、Codex及OpenAI兼容模型，两个角色可选不同模型；借ghidra-ai-bridge取得高层P-code、CFG与附近源码等证据，在有界轮次中生成候选，并保留报告、日志和知识图。

成功条件依配置涉及Checker PASS、无强结构不匹配、构建／测试／运行验收及RED/YELLOW parity策略。无验证命令默认UNKNOWN且严格配置拒收，关闭验证的结果不是构建已验证。候选写入报告与叠加层，隔离验证可使用项目副本，不自动覆盖原源码。配置命令由项目所有者控制仍是信任前提；同模型或不同模型审查都不是第三方独立复现。

README明确不能证明语义或二进制等价，功能组覆盖也只限选中清单和验收策略；仍依赖目标上下文、符号、类型、可用证据与本地Ghidra环境。候选2.1k星未独立核对，本合集未安装依赖、运行目标、编译或复跑测试。按related-project收录公开方法与工具，不报告样本成功率；ReAgent不是morluto/rea，REA未提及。

候选快照2赞、96浏览、0转发；不倒填后续热度或采信2.1k星。
固定README为窗口前资料；只做静态方法核对，没有独立执行或等价性证明。

## 来源

- [TechVerser的ReAgent工具介绍，2026-10-27北京时间](https://x.com/i/status/2114854592848490637)
- [补充固定README：Dryxio/reagent，2026-09-10北京时间提交](https://github.com/Dryxio/reagent/blob/d12cea338c61898b06a86fe8adb25275fa9d5615/README.md)

[English](en/reagent-ghidra-reverser-checker-gated-reconstruction.md) | [返回目录](../README.zh-CN.md)
