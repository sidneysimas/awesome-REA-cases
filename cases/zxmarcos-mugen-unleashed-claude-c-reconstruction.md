# mugen-unleashed：从2013年M.U.G.E.N引擎恢复C，提交披露Claude协作

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-28
阶段：进行中

2026年10月28日15:30:46（北京时间），列表更新帖推荐mugen-unleashed，称从2013年可执行文件恢复M.U.G.E.N为C，并指出AI披露在commit trailer而不是README。补查公开仓库zxmarcos/mugen-unleashed：初始提交eea065966ab4c6557f811d707ec05221ba0f7ae9日期为10月23日12:01:46（北京时间），署名Marcos Medeiros，明确Co-Authored-By: Claude Opus 5.5。该较早提交只作方法归因补证，不冒充本窗口新实验。

M.U.G.E.N是可使用角色与场景数据的2D格斗游戏引擎；项目目标是重建Elecbyte于2013-08-11构建的mugen.exe 1.1.0 Beta1 P1，以原生Windows x86程序继续运行自有游戏数据。README称全部游戏函数已恢复为C，每函数与原二进制做差分检查；Debug和优化构建在标题、快速VS、AI对战、角色选择演示、选项、storyboard、禁声音/音乐及缺失角色错误框上写相同mugen.log，并刻意保留原版怪癖与bug。这些是项目测试声明，不等于本合集复现或所有可观察行为、图像、音频、时序均已证明等价。

静态依赖Lua5.1.4、libpng1.2.38、GLEW1.5.4和minizip0.15据称使用相同版本原源码；运行仍需要合法取得的原版数据和Elecbyte.MUGEN.libs动态库。README说GitHub Actions每次push构建，但未核验具体成功run，也未下载或执行产物。代码与文档公开不等于获Elecbyte许可；README明确原始版权、无官方关联且不额外授予超出适用法律的许可。未把原README的游戏内AI当模型证据，未量化Claude贡献或确认REA使用；保留进行中项目。

候选快照0赞、70浏览、0转发；9星、274文件为候选列表口径，未当作本合集实时统计。
提交与README静态阅读，不执行目标或安装依赖；未核验成功CI或逐函数日志。

## 来源

- [候选列表帖介绍mugen-unleashed与AI署名，2026-10-28](https://x.com/i/status/2115345512325099569)
- [公开仓库zxmarcos/mugen-unleashed](https://github.com/zxmarcos/mugen-unleashed)
- [窗口外补证：10月23日初始提交与Claude共同署名](https://github.com/zxmarcos/mugen-unleashed/commit/eea065966ab4c6557f811d707ec05221ba0f7ae9)
- [固定提交README：目标、差分测试范围与版权边界](https://github.com/zxmarcos/mugen-unleashed/blob/eea065966ab4c6557f811d707ec05221ba0f7ae9/README.md)

[English](en/zxmarcos-mugen-unleashed-claude-c-reconstruction.md) | [返回目录](../README.zh-CN.md)
