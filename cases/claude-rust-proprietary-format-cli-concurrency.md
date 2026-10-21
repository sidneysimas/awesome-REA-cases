# 专有格式 Rust CLI：Claude 八个子 Agent 对照200份文件导致资源饱和

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-21
阶段：进行中

2026年10月21日09:08及09:10（北京时间），Dwayne（CtrlAltDwayne）解释电脑卡住的原因：Claude同时启动8个子Agent运行他正在开发的专有文件格式Rust CLI，对照200份文件进行benchmark；部分文件要提取数十万行数据。作者称恢复后将并发限制为3，以免再次出现系统忙碌指针。

这是AI辅助开发私有格式读取／提取工具的进行中报告，后帖补充数据规模和降低并发，合为一条。格式名、样本、仓库、对照基准、正确率、耗时与内存测量未给；不能把200文件写成全部通过，也不能断言降低并发解决了解析正确性。REA未明示，本合集未运行工具。

## 来源

- [Dwayne：8个Claude子Agent、200文件与降至3](https://x.com/i/status/2112712706218447004)
- [同作者补充：数十万行提取与并发限制](https://x.com/i/status/2112713050117869783)

[English](en/claude-rust-proprietary-format-cli-concurrency.md) | [返回目录](../README.zh-CN.md)
