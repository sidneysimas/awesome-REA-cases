# Snowboard Kids：Codex 记录 IDO 编译器规律，辅助 N64 字节匹配

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-20
阶段：待验证

10月20日11:00（北京时间），@waynerad 引用题为“Decompiling a Nintendo 64 game in 84 days”的文章，目标为N64游戏Snowboard Kids。引文区分它使用的SGI专有IDO 5.3与续作Snowboard Kids 2使用的GCC 2.7.2；IDO原环境依赖旧SGI软硬件，社区此前已对部分工具链逆向，并把IDO 5.3/7.1静态重编译到现代机器。这些是社区前置工作，不是Codex从零完成。

引文作者说自己与LLM通常先读懂函数，再写功能近似的C，最后用permuter尝试小改动以获得机器码匹配。但IDO多轮优化会让细微C改动引起寄存器分配变化；底层结构写错时，排列搜索不能保证匹配。为共享重复出现的编译器规律，作者让Codex把观察记录到DECOMPILATION_LEARNINGS.md，供后续Agent使用。

这是有具体工具链难点与经验共享方式的二手研究转引，不是本合集独立复现。84天是所引文章标题，不等于全部为Agent工时；帖子未附完整函数匹配输出，本合集也未读取短链后的全文或运行游戏，不能据此宣布项目全量字节匹配、完整移植或确认REA参与。

10月20日候选快照：0赞、27浏览、0转发；为转引帖传播快照，不是原文热度或项目验证。

## 来源

- [waynerad转引：Snowboard Kids、IDO与Codex经验文件](https://x.com/i/status/2112378313171951813)

[English](en/snowboard-kids-ido-codex-decompilation.md) | [返回目录](../README.zh-CN.md)
