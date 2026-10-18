# Claude Bun 单文件：REA 提取证据后让 Gemini 重写 gzip 判定

分类：算法与功能重建 · REA
记录日期：2026-10-18
阶段：分析测试

10月18日13:15（北京时间），@jiangkoumo_ 报告研究 Claude 的 Mach-O 单文件程序。目的是检验 REA 在本机没有 Hopper、Ghidra 或 IDA 时能做什么，而不是验证能自动重建整款客户端。作者只跑通 inspect-macho，看到 Load Command 与175MB的 __BUN 容器段；直接交给 JS 分析器返回 unsupported_target。他把这三种底层工具统称商业底座，但此处不采纳这一称呼：并不是三者都属商业软件。

作者说用 unbuned 拆出代码，再将带 gzip 判定逻辑的13KB模块交给 REA，得到2,388个AST节点与51项findings。2,451文件目录的完整Evidence由tokenx估算为1,143万tokens，使用 --filter-output 只提关键结构后为395tokens；两者输出范围不同，不是无损压缩率。随后把AST与115行JS片段交给 Gemini 3.8 Flash，一轮9,352tokens、约0.0017美元，重写判定函数；作者报告针对原逻辑构造的69,121组用例全过，并杀死边界变异用例。

补取原帖确认作者与正文，未取得完整样本、测试生成器、模型记录或账单，所有计数、费用和通过结果均为作者自测自述。模型名称按原帖记录，未核验服务型号；测试只覆盖这个函数和作者的用例，不证明整个程序等价、无广告或原始源码恢复。候选中的 Perplexity 额度宣传不是本实验成本证明。本合集未下载目标、运行代码或独立复现。

10月18日候选快照6赞、514浏览；补取原帖确认身份，不等于复现。
69,121组用例、9,352tokens与约0.0017美元均为作者报告；395tokens仅为过滤后的关键结构。

## 来源

- [jiangkoumo_ 的 Mach-O／Bun／gzip 实测自述](https://x.com/i/status/2111687633755910612)

[English](en/claude-bun-gzip-gemini-rea-test.md) | [返回目录](../README.zh-CN.md)
