# Universal Modder：用 AI 给现有游戏做 Mod

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-19

Rehan Sheikh 把修改游戏的过程做成了 Universal Modder。Mod 是在原有游戏上增加角色、玩法或内容，而不是重新开发整款游戏。作者让 Claude 分析游戏引擎、代码和文件格式，再生成素材、修改内容并进入游戏测试。演示包括给《帝国时代 II》加入 Robotaxi 文明，以及把 Minecraft 的角色和场景放进 GTA V。目标是让 Agent 串起原本需要多种工具的游戏改造过程；不代表这些游戏都被完整反编译。

10月19日20:46（北京时间），另一传播帖声称用Opus 5.5与REA把Fortnite放进Minecraft、Minecraft放进GTA 5，并称画面含洛圣都街道上的Fortnite建造与武器栏。它叙述以Ghidra处理Windows程序、读取Java字节码或从规则重建，搜索滑翔、建造、风暴线索，观察60秒游戏行为，写入SPEC.md，其中风暴有14条规则，再重建对照。此来源作为同类跨游戏目标的补充，不确认它是Universal Modder的新版本、同作者或同一实现。没有代码、函数地址、规则规格或测试记录，未观看完整演示，不能把60秒、14规则或逐功能匹配写成独立验证，也不认定整个Fortnite被反编译。原项目仍按原来源归为其他AI；REA仅出现在新增宣传中。

原项目热度快照（2026-10-12）：14,340赞、382.2万浏览、896转发。
原项目发帖9月30日，原来源非REA；新增10月19日宣传快照10赞、367浏览、0转发，不是同一传播统计。
10月20日15:00候选介绍rehan-remade/universal-modder：称11个技能、um CLI与fal MCP覆盖侦察、素材、测试和发布，20+引擎playbook由um scan辨认版本、原生或.NET、反作弊与加载器；只有game-worker接触运行中游戏，orchestrator规划核验、offline-worker做离线研究，发布检查阻止打包游戏文件、反编译代码与密钥。以上是第三方介绍，未读完仓库或执行检查，不保证所有引擎实测或秘密不会泄漏；8344星为其快照，候选本身0赞、17浏览。

## 来源

- [看 X 热门帖](https://x.com/rehan_shei/status/2105161487509852622)
- [10月19日Fortnite混合规则宣传，未确认同项目](https://x.com/i/status/2112163474553884870)
- [10月20日15:00：Universal Modder工作流第三方介绍](https://x.com/i/status/2112438757505015891)

[English](en/universal-modder.md) | [返回目录](../README.zh-CN.md)
