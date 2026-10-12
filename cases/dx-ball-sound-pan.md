# DX-Ball：恢复老打砖块游戏的声像算法

分类：游戏与游戏保存 · REA
记录日期：2026-10-12

DX-Ball 是老式打砖块游戏。这个案例不是重做整款游戏，而是恢复音效如何根据屏幕横向位置分配到左右声道。贡献者顺着播放音效的调用找到声像计算函数，结合汇编、常量与调用者补全伪代码，恢复 C 实现。证据记录包含 3,205 组原始 x86 差分测试，以及重编译后完整 63 字节函数匹配；解决的是单个音效算法的准确重建。

## 来源

- [案例 PR](https://github.com/morluto/rea/pull/876)
- [证据记录](https://github.com/morluto/rea/blob/main/website/evidence/dx-ball-sound-pan.md)

[返回目录](../README.md)
