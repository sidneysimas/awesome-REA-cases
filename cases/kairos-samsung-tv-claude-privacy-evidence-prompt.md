# Samsung电视隐私检查：kairos让Claude从包声明与语音设置区分观察和推断

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-23
阶段：待验证

2026年10月23日03:12:46（北京时间），kairos（@ka1r0seve）在同串两帖给出Samsung电视配置的Claude分析方法：使用可读截图、XML或包列表，保留精确包名、标记不可读处，查找alwaysonvoice、adinfo、network、multimedia并逐项引用和计数。背景是读者容易把系统包名称直接理解为隐私侵犯；该方法要求区分材料能确认什么与名称只能暗示什么。

完整提示词要求用户提供型号、固件与语音设置，与对应机型的官方Samsung文档对照，检查Bixby／Voice Wake-up是否存在且菜单名如何变化，再提出三个普通用户可做的后续检查。它明确禁止连接设备或修改设置，并要求说明要确认麦克风录音或数据上传还需要哪些证据，不能从包声明推出录音已经发生。

已读帖子没有实际电视型号、截图内容、包计数结果、录音捕获、网络流量或完成的Claude报告。候选是具体的静态证据检查idea，不是Samsung电视已被证实监听，也不是全机型兼容保证。REA未提及；保留为other-ai、unverified。本合集未连接电视、修改配置或获取私人音视频。

两候选均原发2026-10-23T03:12:46+08:00；只读提示词未附实际检测结果。

## 来源

- [kairos：Samsung电视配置隐私只读检查完整提示词](https://x.com/i/status/2113347851715576106)
- [同串前导：精确包名、Bixby设置与证据分层](https://x.com/i/status/2113347849228280112)

[English](en/kairos-samsung-tv-claude-privacy-evidence-prompt.md) | [返回目录](../README.zh-CN.md)
