# Grokbot：SOL 6.1 辅助恢复 Harness 与 Host 的远程电脑执行链

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-19
阶段：进行中

10月19日04:58（北京时间），@Stephen4171127（熊布朗）报告用三天逆向并跑通 Grokbot 的 Agent Harness 与 Host 核心执行链路，核心版本0.72.0-pre.11。新版外壳未研究，界面沿用旧版。原意是测试REA，但作者特别说明实际主要靠模型读代码、写分析脚本与对照验证，主力模型SOL 6.1；不把成果全归于REA。

远程环境据称是在其VPS上通过Docker部署Cursor universal的sand-box-latest镜像。作者列出的实测路径为主Agent调模型、委派电脑子Agent、查看远程桌面截图、点击打开Chrome、子Agent完成并回报。用途是恢复可运行、可修改的Agent执行核心，而非仅模仿界面。下一步才是把恢复核心整理为可维护源码并补齐剩余宿主能力。

补取原帖确认作者及完整措辞；没有公开恢复源码、可复跑日志或独立验证，作者也表示仅自用、不准备传GitHub。三天及成功链路均为作者报告，不证明整款Grokbot功能等价或所有恢复能力完成。

04:58候选快照6赞、523浏览、1转发、2回复；不是独立复现。

## 来源

- [熊布朗的Grokbot核心恢复与SOL 6.1自述](https://x.com/i/status/2111924992384311338)

[English](en/grokbot-sol61-harness-host-reconstruction.md) | [返回目录](../README.zh-CN.md)
