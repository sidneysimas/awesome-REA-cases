# Samshush：Matt Silverlock用Codex/Astra研究Samsung Frame并关闭选定后台服务

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-26
阶段：待验证

2026年10月26日01:09（北京时间），Matt Silverlock（@elithrar）在Samshush发布串中明确说，工作在Windows电脑、普通Pro订阅的Codex与Astra中完成。最初他想修接收器音量的休眠/唤醒问题，打算构建并签名自己的固件；Astra建议改走网络登录。作者感谢lucataco的LG主页改造和log4j的三星调查，但Samshush是他自己Frame电视的独立项目，不能并成log4j的成果。

作者称工具关闭或清理选定的麦克风/监听、广告、遥测、存在感知和eMudhra根证书，通过启动脚本让部分改动在重启后重新应用，并关闭自动固件更新避免失效。这是研究并调整原系统服务的报告，不是成功重签或刷入定制固件。

补充阅读10月26日19:35:13北京时间提交e70d2bb3800daf344b4227c452f0c630b966f446的公开README；这晚于严格候选窗口，仅用于界定当前实现。文档把支持范围限定为Frame Pro QN65LS03FWFXZA、固件1301.0，描述经Samsung SDB连接、临时root和Python工具保存原状态，禁用而非卸载App，提供恢复和可选启动钩子。它称保留HDMI-CEC、ARC/eARC、播放、网络、手动Art Mode等核心功能；部分存在感知和免手语音会损失，共享传感服务等需保留。README明确仍可能有其他遥测及麦克风输入，固件更新会重置改动或修补root路径，不证明已消除全部采集。

同一文档声明用GPT-6 Astra开发，原帖没有确认REA使用。源码和文档公开不等于本合集已经验证root、重启持久性、恢复或隐私效果；没有安装依赖、执行目标代码或连接电视。按有公开项目的未验证作者报告收录，不把服务能力、作者措辞或证书过滤当作实际监听外传及证书遭滥用的证明。

作者报告；补充README晚于00:00至04:00候选窗口，未执行代码或测试电视。
文档支持Frame Pro QN65LS03FWFXZA、1301.0；非通用三星兼容保证，REA未确认。
禁用App及选定服务而非刷固件或证明停止全部遥测；启动钩子与固件更新各有风险。

## 来源

- [候选：Matt说明Codex/Astra、Windows及网络登录建议，2026-10-26 01:09北京时间](https://x.com/i/status/2114403952468910538)
- [作者Samshush发布与服务清理目标，2026-10-26北京时间](https://x.com/i/status/2114403936476033220)
- [作者报告Frame、启动脚本与重启持久性，2026-10-26北京时间](https://x.com/i/status/2114403940301418754)
- [窗口后公开README，固定提交e70d2bb，2026-10-26 19:35北京时间](https://github.com/elithrar/samshush/blob/e70d2bb3800daf344b4227c452f0c630b966f446/README.md)

[English](en/samshush-frame-codex-astra-cleanup.md) | [返回目录](../README.zh-CN.md)
