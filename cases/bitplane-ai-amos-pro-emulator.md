# AMOS Pro：bitplane报告AI辅助模拟器、在线IDE与游戏库

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-24
阶段：待验证

2026年10月24日17:05:27（北京时间），davidsong（@bitplane）报告在AI帮助下制作AMOS Pro模拟器，并配套完整在线IDE和游戏库。AMOS Pro是Amiga平台的编程环境，目标是把旧游戏带到网页。作者称过去三十年至少三次团队尝试因规模过大失败，此历史比较未独立核实。

补查公开amos-ts的README，最后修改于2026-09-08，早于本窗口。项目实际是TypeScript重实现，包含解释器、加载器和无界面运行器；代码与AMOS图形源自AMOS-Professional-Official已公开材料，其余为兼容目的逆向，不能全归为黑盒AI反编译。文档称核心语言完成，但保留原生机器行为近似和未实现后端边界，不主张周期精确；测试全绿仍可能被faithfulness gate判失败。

README以MIT列原实现许可，同时承认在线游戏库含版权作品、以abandonware假设提供；该称呼不是取得授权的证明。本合集未运行在线IDE、游戏或测试，不背书分发权，也不把项目完成声明升级为所有AMOS游戏可运行。具体AI模型与REA未说明。

复用公开AMOS源码；其他兼容行为逆向，非周期精确模拟。未运行faithfulness gate；abandonware不等于版权授权。

## 来源

- [bitplane的AI项目清单：AMOS Pro，2026-10-24](https://x.com/i/status/2113919789886218477)
- [补充amos-ts README，最后修改2026-09-08](https://github.com/bitplane/amos-ts/blob/2809fc901c688baa130d884ad5419ab7aa15e4fa/README.md)

[English](en/bitplane-ai-amos-pro-emulator.md) | [返回目录](../README.zh-CN.md)
