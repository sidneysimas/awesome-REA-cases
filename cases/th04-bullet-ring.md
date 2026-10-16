# 《东方幻想乡》：恢复环形弹幕的角度计算

分类：游戏与游戏保存 · REA
记录日期：2026-10-12

TH04 是《东方幻想乡》，东方 Project 系列的一款弹幕射击游戏，原版运行在 PC-98 的 DOS 环境。贡献者研究的是“敌人如何发出一圈子弹”：恢复角度间隔、瞄准玩家的方向偏移、模板旋转，以及最终角度写入的逻辑，并用 C++ 与示意图说明。REA 的指令检查引用了历史重建项目中的编译匹配记录，不是本次从零复刻完整游戏。

## 来源

- [案例 PR](https://github.com/morluto/rea/pull/970)
- [证据记录](https://github.com/morluto/rea/blob/main/website/evidence/th04-bullet-ring.md)

[English](en/th04-bullet-ring.md) | [返回目录](../README.zh-CN.md)
