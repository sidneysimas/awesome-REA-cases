# HeartGold/SoulSilver单屏fork：Claude改界面，明确归功pret既有反编译

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-23
阶段：进行中

这条线索来自2026年10月23日15:31:12（北京时间）yibie的目录更新，属于此前12:00至16:00窗口补审，不冒充本轮新抓取。该帖同时提到Monster Hunter 2和Champagne；本记录只收录具备直接文档核对的HeartGold/SoulSilver单屏目标，不把几个项目当一次共同验证。通过yibie/awesome-rea找到ClickingMaster/pokeheartgold-single-screen，阅读其README。

项目基于ctrl-cheeb-del/pokeheartgold及pret/pokeheartgold，为Pokémon HeartGold/SoulSilver反编译树增加SINGLE_SCREEN构建模式，供ssrecomp重编译为单屏设备的原生SoulSilver。战斗命令与招式、背包、队伍等原触摸屏部分改画到上屏区域，公开菜单与选择状态，方便前端布置宽屏和控制器操作。README明确原工具和反编译归功pret；几乎全部fork改动由Claude经Claude Code编写，由维护者指导、试玩，提醒可能出现人类不会犯的bug。不能把上游多年工作写成AI从零完成。

README称全部代码为C/C++，正常配置HeartGold与SoulSilver两个ROM可逐字节构建；这是项目声明，本次未独立编译。SINGLE_SCREEN会故意改变游戏，不能将原始构建的字节一致性说成单屏版也与原ROM字节相同。单屏安装程序与资源脚本仅以美版SoulSilver测试；用户需自备合法ROM、mwccarm和Nitro SDK，项目不分发游戏、编译器或SDK。pret不接受AI生成贡献，文档要求不要把本fork改动提交上游。

补充README固定于6984a3d67592157195940049be2e4bbbf933f9ff，提交原始时间为2026-10-22 03:08:18 UTC，早于候选，仅用作目标、归因与验证边界的一手来源。未采纳候选的13星和11,231文件为当前统计；未下载ROM、运行安装器或测试单屏版。按进行中保存与界面改造项目收录，保留各部分权利与上游归属，不将仓库的许可说明扩张为对游戏资产的授权。

往期候选2026-10-23 15:31:12，北京时间；补充提交2026-10-22 03:08:18 UTC。
逐字节为正常配置的项目声明，非单屏修改版等价证明；未独立构建。

## 来源

- [往期候选：yibie目录更新中的HGSS单屏线索，2026-10-23](https://x.com/i/status/2113533682187211069)
- [补充一手：ClickingMaster固定提交README，2026-10-22](https://github.com/ClickingMaster/pokeheartgold-single-screen/blob/6984a3d67592157195940049be2e4bbbf933f9ff/README.md)

[English](en/pokeheartgold-singlescreen-claude-fork.md) | [返回目录](../README.zh-CN.md)
