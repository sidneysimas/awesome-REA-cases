# Plustek 8200i / ThinkPad MIPI：用 Windows 参考行为改善 Linux 驱动

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-16
阶段：进行中

Christian F. K. Schaller 为扫描家人留下的旧底片购买 Plustek OpticFilm 8200i，却发现新批次使用 Genesys GL128（USB 07b3:1825），不同于已有支持的 GL845 旧款。最初 Claude 研究长期无进展；借鉴 Windows 虚拟机控制与宿主机 usbmon 抓包后，他报告数小时得到首张可识别扫描，数日后支持红外扫描。其 SANE backend 列出彩色、灰度、红外、彩色加红外，300–7200 dpi、每通道8或16位、红外除尘与曝光倍率；作者以自制 Negative Vibes 应用测试。官方 SANE 已于2026年9月另行加入该设备支持，不能把此前支持空缺写成现在仍无支持。作者单台设备、单帧对照称全分辨率34.6秒对54.4秒，上游有更多分辨率档位；他把自己的驱动作为概念验证，并希望上游达到同等功能后转用上游。

随后他用 Claude 研究 ThinkPad X1 Carbon Gen 14 Aura Edition 的 Sony IMX471 / Intel IPU7 MIPI 相机。这里没有相同的 USB 总线可抓，主要从 Windows INF、注册表、ACPI 与配置数据取证，并以 USB 摄像头作图像参考。公开页面列出内核裁剪矩形、测试图寄存器宽度、模拟增益上限，以及 libcamera 缺少镜头阴影校正和白平衡黑电平位深处理等五处问题；调色与阴影数据来自 Windows 驱动包的 CPFF 配置容器布局研究。作者受控低光测试亮度由31.1升至90.9，但低光蓝色仍约少17%，曝光与帧率取舍未修复，没有色卡验证，仅在一个房间、GPU处理路径测试。作者10月15日原文称内核补丁已送交 Kate Hsuan，libcamera 补丁由 Wim Taymans 审阅以供提交；不是已确认上游合并。

10月16日两篇候选转述引出上述10月15日原文、hw-harness README 与相机测量页补证；另补审解决10月15日 Phoronix 同题旧候选。hw-harness 是事后将定制脚本泛化的工具，作者明确原研究并非使用当前通用形态。所有硬件结果仍是作者报告和项目记录，本合集未接设备复测；未见 REA 使用证据。

10月16日候选快照：长文4赞、493浏览；Joshua_WD帖4赞、134浏览。
补充来源原始日期：作者文章与Phoronix新闻为10月15日；项目页面为本轮读取，不是独立复现。

## 来源

- [本轮长文转述：扫描仪与 MIPI 相机](https://x.com/i/status/2110852184988385570)
- [Joshua_WD 的已知良好参考对照转述](https://x.com/i/status/2110869080555082144)
- [往期补审：Phoronix 原帖](https://x.com/i/status/2110740084387672274)
- [10月15日 Schaller 原文](https://blogs.gnome.org/uraeus/2026/10/15/aiandreverseengineerhardware/)
- [Phoronix 10月15日新闻正文](https://www.phoronix.com/news/AI-Reverse-Engineer-Linux-HW)
- [hw-harness 项目与观察边界](https://github.com/cschalle/hw-harness)
- [MIPI 五处修复、测量与未修复问题](https://cschalle.github.io/mipi-fixes-x1-aura/)

[English](en/schaller-opticfilm-thinkpad-linux.md) | [返回目录](../README.md)
