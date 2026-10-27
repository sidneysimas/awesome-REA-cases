# Merck Hung的iOS跨架构实验：ARM到Intel JIT，Windows11下仍慢且似乎无响应

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-27
阶段：进行中

2026年10月27日17:52:18（北京时间），Merck Hung（@merckhung）报告正在Intel x86_64 Windows11电脑上，以ARM到Intel的JIT运行原厂iOS固件镜像，并称Claude和Codex仍在继续工作。JIT在这里指运行时翻译指令的作者方案，不能据此补出其CPU、设备或系统调用模拟实现。原帖补查确认署名与附带视频存在；作者自己说“Pretty slow”和“Seems unresponsive”，表示之后还会更新。

这是跨指令集固件运行/互通实验，不是已经流畅可用的iOS模拟器，也不是此前Nothing Phone实体机的iOS移植。帖子没有iOS版本、设备镜像身份、仓库、JIT源码、启动日志、帧率、输入响应、应用兼容或安全机制验证。视频未由本合集独立解读，不能确认系统启动到了哪一步。按in-progress收录明确AI参与及失败边界，REA未提及；本合集没有下载iOS镜像、执行目标或安装依赖。

候选快照48赞、2218浏览、0转发；慢与似乎无响应为作者原文，不以演示存在证明可用。

## 来源

- [Merck Hung的Windows11/iOS JIT进展与无响应说明，2026-10-27](https://x.com/i/status/2115018744888225798)

[English](en/merckhung-ios-stock-firmware-x86-windows-jit.md) | [返回目录](../README.zh-CN.md)
