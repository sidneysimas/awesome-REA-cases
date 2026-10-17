# Open Scrantic：用 REA 与 Claude Code 重建 Johnny Castaway 屏保引擎

分类：应用与客户端 · REA
记录日期：2026-10-18
阶段：进行中

2026年10月17日22:45（北京时间），Glauber Lima（@glauberlima）在作者串中说明，以REA负责逆向、Claude Code写实现，自己指导和审阅。目标是Sierra/Dynamix的Windows 3.1屏保Screen Antics: Johnny Castaway，让怀旧的荒岛人物与逐日故事在现代Windows、macOS和Linux继续运行。父帖22:42报告从反汇编重建为Rust，22:43说明MIT开源且不分发原文件。

补读公开仓库glauberlima/open-scrantic的README，确认项目名Open Scrantic，以及明确的AI披露：拆解SCRANTIC.SCR，恢复资源格式和TTM/ADS脚本语义，再实现Rust引擎、测试与文档；开发者对照原屏保检查。架构将资源解码、故事规划、脚本调度、帧绘制和音效分开。运行仍需自备SCRANTIC.SCR、RESOURCE.MAP和RESOURCE.001；加载器仅接受已知原程序版本，不能推定任意版本兼容。

项目也说明刻意偏差，例如全帧重绘代替脏矩形，以及未重建原设置对话框、改用SCRANTIC.INI。不能把“同样行为”扩大为逐帧或逐字节完全一致。补查10月17日22:14提交2bdbd87af4cd9641dd33739ba4681c0273f095aa及对应GitHub CI结果为success；这是项目构建检查记录，不是本合集实机复现或全部故事路径验收。公开文档和流程可读，未下载资产、编译或运行目标。

候选与父串发布：2026-10-17 22:42—22:45，北京时间；仓库补查用于核对项目与AI披露。
2bdbd87提交时间2026-10-17 22:14，北京时间，对应CI成功；未独立编译运行。
仅重建引擎；原资产自备，已知版本限制与刻意行为偏差不能省略。

## 来源

- [候选：作者披露 REA、Claude Code 与人工审阅](https://x.com/i/status/2111468525286002699)
- [补充父帖：Johnny Castaway 三平台 Rust 重建](https://x.com/i/status/2111467934082363521)
- [同串：MIT 与需自备原文件](https://x.com/i/status/2111468253394485547)
- [公开仓库与 AI 披露、实现和兼容边界](https://github.com/glauberlima/open-scrantic)
- [2026-10-17 文档提交](https://github.com/glauberlima/open-scrantic/commit/2bdbd87af4cd9641dd33739ba4681c0273f095aa)
- [项目 CI 记录（可变状态，本次对应提交成功）](https://github.com/glauberlima/open-scrantic/actions/workflows/ci.yml)

[English](en/johnny-castaway-rust-rea.md) | [返回目录](../README.zh-CN.md)
