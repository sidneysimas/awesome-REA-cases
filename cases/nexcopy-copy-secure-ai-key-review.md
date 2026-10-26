# Nexcopy Copy Secure：AI追踪查看器、配置与3DES内容密钥

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-25
阶段：分析测试

10月25日07:18:48（北京时间）候选将Nexcopy与其他保护产品并列，补读Xusheng Li窗口前官方文章（10月22日16:00 UTC）。本条独立记录Nexcopy Copy Secure，由Drive Wizard 1.0.81制备，盘上有Windows和macOS查看器。作者称Mac查看器保留Objective-C方法名，便于AI跟踪其设计；目的为核验复制保护与密码是否真正约束文件加密。

原文报告内容使用三密钥Triple-DES CBC，应用内固定值先打开加密配置，配置再提供24字节内容密钥与8字节IV；用户密码只是独立的UI字符串比较，设备ID也是软件检查，不参与内容密钥。研究者展示324字节配置与140字节测试文件的布局，称AI成功解密并恢复自有文件原始内容，解包、追踪密码系统与发现密钥管理问题总计约10分钟、五提示词。

查看器还枚举进程、拦截截图键与使用剪贴板API，但这些不阻止研究者检查客户端密钥。上述为作者分析和测试，不是本合集运行验证，不推定每版Nexcopy或所有盘均同样受影响，更不是3DES算法被AI攻破。没有取得工具样本或访问第三方文件，不转载配置密钥；AI型号和REA未明确，候选把所有产品简写为密钥写死在软件中不代替实际两级密钥链。

Drive Wizard 1.0.81、约10分钟与五提示词均为原文口径；未独立测试或验证全部产品。

## 来源

- [窗口候选：Nexcopy保护缺陷转述，2026-10-25](https://x.com/i/status/2114134544836407379)
- [窗口前Xusheng Li原研究：Nexcopy密钥链与测试，2026-10-22 UTC](https://binary.ninja/2026/10/22/breaking-more-encrypted-usb-drives-with-ai.html#nexcopy)

[English](en/nexcopy-copy-secure-ai-key-review.md) | [返回目录](../README.zh-CN.md)
