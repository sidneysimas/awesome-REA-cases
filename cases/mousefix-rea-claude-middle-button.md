# MouseFix：REA 与 Claude 研究2004年鼠标去抖工具，补上中键与拖拽模式

分类：硬件与设备互通 · REA
记录日期：2026-10-21
阶段：进行中

2026年10月21日08:01（北京时间），Felipe Mikeias（felipemikeias）称用 REA＋Claude 研究自2004年流传的 MouseFix 双击修复工具，再从零制作开源替代版，新增中键等功能。目标是缓解磨损鼠标一次点击变两次及拖拽中途松开的现象，不是修复物理微动开关。

补查公开仓库 a7092b4c 提交于当天08:02:58，在候选窗口内。原版分析以SHA256限定两份2004年1月29日的PE32文件，说明用objdump研究头、导入与反汇编：原版仅左键固定40毫秒，拦下按下却放过配对松开，不能保持故障中的拖拽，且相对路径加载DLL有风险。新工具以进程内 WH_MOUSE_LL 钩子和单个EXE替代EXE＋DLL，五键可选、默认左键与40毫秒，托盘可调。默认模式成对丢弃重复按下与松开；drag-safe延迟每次松开以吸收反弹，因此有释放延迟成本。软件注入事件不被过滤。

对应提交的GitHub Actions运行39518884317于08:03创建并成功，属于项目构建与测试证据，不是本合集设备复测。README声称Windows XP至11兼容，并描述PE头与导入检查；不能据此保证所有系统与程序实测可用。普通权限钩子对提升权限程序有限制；物理故障仍应更换微动或鼠标。未执行目标、测试实际点击或独立核定代码来源；原版分析未发现恶意行为不等于对所有下载副本作安全保证。

证据边界：a7092b4c 对应项目CI成功；本合集未实测鼠标，软件去抖不能修复物理开关。

## 来源

- [Felipe Mikeias：REA／Claude与MouseFix替代版](https://x.com/i/status/2112695748374749631)
- [MouseFix README：a7092b4c的模式与限制](https://github.com/felipemikeias/MouseFix/blob/a7092b4ce524cceab259ccd1c6ca460765f2fed0/README.md)
- [相同提交的原版分析与哈希限定](https://github.com/felipemikeias/MouseFix/blob/a7092b4ce524cceab259ccd1c6ca460765f2fed0/docs/original-analysis.md)
- [对应提交的成功项目CI](https://github.com/felipemikeias/MouseFix/actions/runs/39518884317)

[English](en/mousefix-rea-claude-middle-button.md) | [返回目录](../README.zh-CN.md)
