# IGI-RE：AI辅助重写Project I.G.I.，以Unicorn核对行为而非要求字节相同

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-27
阶段：进行中

2026年10月27日15:30（北京时间），yibie推荐IGI-RE，目标是保存Innerloop Studios在2000年推出的Project I.G.I.: I'm Going In。补读slickdaddyy/IGI-RE在088950a517a18bfbb15c7dc6b28b09564f85c7d4提交的README，提交日期为10月26日16:00:39北京时间，早于本窗口。作者明确AI编码工具参与开发、调试与测试，未指明模型或REA，不能只凭列表名称归因为REA。

项目将IGI.exe逐函数重写为可读C，用Ghidra定位函数，dinput.dll将原函数跳转至重写实现，以Unicorn从相同状态运行原机器码和重写版本，比较返回值、内存写入、栈清理与调用次序；浮点代码覆盖游戏所用x87舍入模式，任务级脚本再对照画面。目标是functional decompilation，不要求编译成同一字节。README报告5376／5376函数已重写并命名、425文件内90078项差分测试全通过、14个任务与原作并排检查，独立igidecomp.exe可由源码构建。这些是项目声明，不是本合集测试结果或所有输入上的形式证明。

目标限定特定EU（文档也提Chinese）发行版IGI.exe及合法游戏资源，其他发行版未支持；Microsoft C运行库不反编译，而由系统msvcrt.dll替代。运行环境为Windows或Linux上的Wine，文档称开发和实测使用Wine11，并注明目标含no-CD修正。项目感谢既有IGIPatch命名、光盘检查笔记及其他工具；不把前人研究全部归给AI。未编译、安装依赖、运行游戏或重跑测试；按in-progress收录具体实现及可核查方法。

候选快照1赞、65浏览、0转发；8星、1142文件是帖子口径，不代替功能或AI贡献验证。
5376函数、90078项测试、425测试文件、14任务为固定README自报；没有独立重跑或全输入等价证明。

## 来源

- [候选：yibie介绍IGI-RE，2026-10-27](https://x.com/i/status/2114983062060904506)
- [补充：10月26日固定提交README、AI说明与验证范围](https://github.com/slickdaddyy/IGI-RE/blob/088950a517a18bfbb15c7dc6b28b09564f85c7d4/README.md)

[English](en/slickdaddyy-igi-re-ai-functional-decompilation.md) | [返回目录](../README.zh-CN.md)
