# game.exe 示意演示：双房间与三类重建 oracle

分类：算法与功能重建 · REA
记录日期：2026-10-16
阶段：分析测试

一则演示解说帖把目标写为本地x86 PE32的game.exe，描述Claude Opus 5.5与REA的双房间流程：Reader通过REA MCP读取二进制（称后端为Ghidra/Hopper/IDA），把观察写入NOTES.md并标obs、inf、unk；Builder只读SPEC.md，不接收代码和地址，逐函数重建。演示设三类oracle（决定是否接受结果的检查）：字节比较、第12天允许const-bytes的例外；故意放入off-by-one、分支颠倒和错误常量三种缺陷以测试检查器；最后检查是否能启动、游玩和观看。关键限制是帖子两次说明697函数、约12天和696/697匹配来自REA博客，仪表板明标illustrative；屏幕上的零行复制、3/3植错被抓和playable也只是此演示叙述，不是可下载项目的独立实验结果。未提供实际game.exe身份、构建产物或运行日志，不把示意数字与东方既有项目合并，也不据双房间说法证明法律上的clean room。

10月16日候选快照：1赞、37浏览；属于流程示意，非本合集执行测试。

## 来源

- [明标 illustrative 的双房间与 oracle 演示解说](https://x.com/i/status/2110783611800522897)

[English](en/rea-clean-room-illustrative-oracles.md) | [返回目录](../README.zh-CN.md)
