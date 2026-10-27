# Game Decompilation Skill for Claude：把游戏字节匹配、失败诊断与合并编成技能

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-27
阶段：相关项目

2026年10月27日15:30（北京时间），yibie的列表更新推荐Game Decompilation Skill for Claude。补读lemiur/Game-Decompilation-Skill-For-Claude在eedfe281d4fab7d8cdaf98b9f72f6a6ac4db04be提交的README，提交时间为10月26日03:28:55北京时间，早于候选窗口，用于核对项目用途，不冒充本轮发布。

项目把游戏matching decompilation方法交给Claude Code：matcher重建并匹配函数，wall-identifier诊断停滞原因，helper-recovery恢复被内联的辅助逻辑，permute作有界排列搜索，decomp-code-rules检查可读性及伪匹配，orchestrator组织worktree中的并行任务和审核合并。各游戏仓库的AGENTS.md提供命令与约定，并覆盖技能默认规则。目标是可读源代码经原编译器产生相同字节，不等于已找回唯一原始源码。

README明确不提供工具链：需要原编译器／链接器或精确等价物、合法持有的零售二进制、可分单元构建及比较的环境，另可配反汇编、diff、permuter与objdiff。原生移植是达到匹配后的另一步。文中对PS1／PS2可行、PS3／360可能需数月的判断是作者经验，不是工时保证；经典游戏名称仅为方法示例，不能说已由此skill完成。只读文档，未安装技能、启动代理或执行目标。按related-project收录，未确认REA参与。

候选快照1赞、65浏览、0转发；116星为候选自报项目快照，未独立核实。
技能方法与门控不是成功率证明；未运行或验证任何游戏匹配。

## 来源

- [候选：yibie列表更新中的Claude游戏技能，2026-10-27](https://x.com/i/status/2114983062060904506)
- [补充：10月26日固定提交README与工具链要求](https://github.com/lemiur/Game-Decompilation-Skill-For-Claude/blob/eedfe281d4fab7d8cdaf98b9f72f6a6ac4db04be/README.md)

[English](en/lemiur-game-decompilation-claude-skills.md) | [返回目录](../README.zh-CN.md)
