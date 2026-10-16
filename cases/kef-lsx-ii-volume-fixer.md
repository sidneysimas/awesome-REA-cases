# KEF LSX II：让 Mac 音量键控制音箱的细粒度音量

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-15

KEF LSX II 是桌面无线音箱。作者受困于 Mac USB 音量仅有约六档、每档6 dB，称与 Claude 制作 LSX II Volume Fixer：虚拟音频输出把样本原样传给 USB，音量键则控制音箱已有的局域网0–100音量接口，而不是修改签名固件。作者报告192 kHz音频、约2 ms附加延迟，以及默认16档、3.4 dB间距，并实际测量音量曲线，称厂商表在低音量端偏差达20 dB。10月15日补查公开仓库，文档解释驱动和网络控制设计；这些测量与兼容性仍是项目报告，本合集没有运行驱动。仅Mac、仅LSX II经过作者测试；Windows只是文档中的可行方向。

候选快照：0赞｜18浏览；性能为作者测量，非独立复现。

## 来源

- [作者报告](https://x.com/i/status/2110581933533184501)
- [公开实现及测量说明](https://github.com/roberdorfer/kef-lsx-volume)

[English](en/kef-lsx-ii-volume-fixer.md) | [返回目录](../README.zh-CN.md)
