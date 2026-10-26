# Flutter二进制：hiroyuki称Codex接Ghidra后自行抽对象池定位地址

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-26
阶段：分析测试

2026年10月26日19:52（北京时间），hiroyuki（@ionis_h）报告Codex连接Ghidra后，即使只有简略指令也能读取Flutter二进制。他原以为不同版本反序列化细节的差异会让地址定位很困难，但称Codex自行编写对象池提取脚本，定位地址后继续分析。补查原帖确认作者及完整措辞。

这是针对Flutter编译产物结构的具体AI辅助分析报告，区别于基线flutter-aot的REA PR记录，不因同属Flutter就归并。可读正文没有应用名、Flutter或Dart版本、架构、脚本、对象池内容、定位准确性测试或恢复功能，不能声称跨版本稳定、完整反编译或恢复源码。REA未提及，未运行脚本或目标二进制；状态analysis-test描述实验性质，不表示独立验证。

应用、版本、架构与脚本未公开于可读正文；地址定位及继续分析仅为作者报告。

## 来源

- [hiroyuki报告Codex/Ghidra提取Flutter对象池并定位地址，2026-10-26](https://x.com/i/status/2114686560323125596)

[English](en/ionis-h-codex-ghidra-flutter-object-pool-analysis.md) | [返回目录](../README.zh-CN.md)
