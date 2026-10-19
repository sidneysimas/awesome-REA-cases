# 热像仪：Mehdi 的 Claude 辅助 Mac App 与 Seek XR 扩展建议

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-19
阶段：待验证

10月19日05:52（北京时间），@MehdiHacks 回复说自己只提示Claude，没有SDK，借助论坛上其他型号的逆向资料，Claude也现场枚举了设备。05:30父帖的目标是实验室热像仪：原设备只支持Windows与Android，因此用Claude制作原生macOS App。此前回复询问是研究USB协议还是封装SDK，这一补充明确否认有SDK。

不能把论坛资料说成Claude独立发现协议，也不能从现场枚举推断完整协议兼容。没有原设备品牌、型号、源码、USB抓包或温度精度对照，也无独立设备测试；未确认REA。

10月19日21:26，@W00fer 提议用Claude反编译Android APK，看看Mehdi的软件能否兼容其设备。补读同串较早回复确认所指是Seek Thermal XR：W00fer在07:22请求支持，Mehdi在17:22说自己没有这台设备。读者不愿牺牲设备调试，APK静态研究是降低设备试错风险的建议，不是已进行的分析。Seek XR不是已确认的Mehdi原设备型号，更没有兼容或刷写成功结果。较早回复仅补充背景，不作为新候选。

## 来源

- [无SDK、论坛资料与现场枚举补充](https://x.com/i/status/2111938443987276204)
- [较早父帖：热像仪的Claude原生macOS App](https://x.com/i/status/2111933013722587430)
- [21:26候选：读者建议Claude分析Android APK](https://x.com/i/status/2112173523439399347)
- [较早背景：W00fer请求Seek Thermal XR支持](https://x.com/i/status/2111961135138120050)
- [较早背景：Mehdi说明没有Seek XR设备](https://x.com/i/status/2112112218380861730)

[English](en/mehdi-thermal-camera-claude-macos.md) | [返回目录](../README.zh-CN.md)
