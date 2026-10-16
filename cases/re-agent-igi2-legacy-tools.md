# RE-Agent：研究《秘密潜入2》GConv / QVM 老工具

分类：游戏与游戏保存 · REA
记录日期：2026-10-16
阶段：进行中

Haseeb Mir（@HaseebMir91）介绍REA分支RE-Agent，目标是为失去支持的老软件与游戏排障，首个具体案例是2003年《秘密潜入2》（Project I.G.I. 2）的GConv/QVM工具。其流程描述为复现故障、用Ghidra/IDA/Hopper与Frida收集静态和运行证据，在独立工作区修复，并比较原版与修复版，输出pass、mismatch或unknown。稍后帖子补充无界面Ghidra分析、IDA桥和内存跟踪。作者未在候选中给出具体故障、修复补丁、输入样本或通过记录；本合集确认原帖作者但未定位其仓库或测试，因此这是项目方向及进行中目标，而非已修复所有IGI工具或普遍避免幻觉的保证。

10月15日作者报告；未取得补丁或实际验证输出。

## 来源

- [作者介绍RE-Agent与IGI 2首个案例](https://x.com/i/status/2110744399567073616)
- [后续工具与验证循环介绍](https://x.com/i/status/2110751222437150721)

[English](en/re-agent-igi2-legacy-tools.md) | [返回目录](../README.zh-CN.md)
