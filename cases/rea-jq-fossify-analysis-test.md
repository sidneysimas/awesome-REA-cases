# jq 与 Fossify Calculator：REA 定位函数和初步调查

分类：算法与功能重建 · REA
记录日期：2026-10-17
阶段：分析测试

10月17日03:05（北京时间），@JohanSlattavik 用挪威语说明自己还没有重建任何东西，但已测试 REA 对去符号 Linux 二进制 jq 1.8.2 的分析，用 Ghidra 识别一个函数并把它对应回原始源码。jq 是 JSON 命令行处理器，这里的目标是检查无符号程序是否仍可定位已知实现，而非宣称整个程序被恢复。作者同时说开始调查 Android 的 Fossify Calculator，尚未给该应用具体发现。没有函数名、构建参数、对应源码位置、反编译输出或对照记录供核验；原版本号按帖子保留，不据此推定发行状态。属于初步分析测试，不能改写为完成移植或功能等价复刻。

明确尚未重建；jq 1.8.2 是作者标注，未核对二进制或发行信息。

## 来源

- [作者对 jq 与 Fossify 初步测试的回复](https://x.com/i/status/2111171612149985567)

[English](en/rea-jq-fossify-analysis-test.md) | [返回目录](../README.zh-CN.md)
