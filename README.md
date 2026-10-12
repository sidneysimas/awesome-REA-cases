# Awesome REA Cases

A curated collection of real-world REA and AI-assisted reverse-engineering cases.

收集 REA 与其他 AI 辅助逆向的实际案例。每条讲清楚对象是什么、作者为什么逆向、做了什么，以及报告了什么结果。

> 非 REA 官方项目。收录不代表工具或作者背书；不收集软件安装包、密钥、私人记录或未授权资产。

当前收录 **22 个案例**；另保留 **8 条待补证据、工具测试或未入选线索**。所有结果均据作者或项目记录整理，未由本项目独立复现。

## 目录

- [游戏与游戏保存](categories/games.md)（8）
- [硬件与设备互通](categories/hardware.md)（6）
- [应用与客户端](categories/apps.md)（5）
- [算法与功能重建](categories/algorithms.md)（3）
- [待跟进与未入选线索](LEADS.md)
- [HTML 阅读版](docs/index.html)（下载后用浏览器打开）
- [贡献指南](CONTRIBUTING.md) · [维护方法](MAINTENANCE.md)

## 案例

### 游戏与游戏保存

- [Universal Modder：用 AI 给现有游戏做 Mod](cases/universal-modder.md) — 分析游戏代码与文件格式，制作跨游戏内容 Mod。 **[其他 AI 逆向]**
- [Firefighter：把老 DOS 游戏恢复成可维护的 Rust 代码](cases/firefighter-rust.md) — 从旧 DOS 二进制恢复 Pascal，再转写为 Rust。 **[其他 AI 逆向]**
- [《现代战争 2》：用多 Agent 重建游戏代码](cases/mw2-decompilation.md) — 多 Agent 反编译游戏，以原二进制核对恢复函数。 **[其他 AI 逆向]**
- [Urban Terror：把桌面多人射击游戏移植到浏览器](cases/urban-terror-web.md) — 定位引擎与字节码布局差异，将游戏移植到浏览器。 **[其他 AI 逆向]**
- [DX-Ball：恢复老打砖块游戏的声像算法](cases/dx-ball-sound-pan.md) — 还原打砖块游戏按位置分配左右声道的函数。 **[REA]**
- [《东方幻想乡》：恢复环形弹幕的角度计算](cases/th04-bullet-ring.md) — 恢复《东方幻想乡》环形弹幕的角度计算。 **[REA]**
- [东方系列：用 Agent 重建旧游戏，并迁移到新平台](cases/touhou-reconstruction.md) — 重建东方系列代码，验证并迁移到可玩平台。 **[REA]**
- [Dinosaur：解释网页跑酷游戏如何逐渐加速](cases/dinosaur-speed.md) — 读网页脚本，实验验证跑酷游戏的加速规则。 **[REA]**

### 硬件与设备互通

- [Apple TV 遥控器：让专用配件在 Linux 上工作](cases/siri-remote-linux.md) — 解析蓝牙协议，让 Apple TV 遥控器接入 Linux。 **[未确认使用 REA]**
- [涂鸦 RGB 灯：绕开厂商 App，直接从 Mac 控灯](cases/tuya-rgb-mac.md) — 分析手机蓝牙控灯数据，用 Mac 脚本直接控灯。 **[其他 AI 逆向]**
- [老设备 MIPS 固件：把程序按正确架构读出来](cases/mips-firmware.md) — 为旧设备固件选定正确架构，核对分析结果。 **[REA]**
- [PSP：让 REA 支持掌机程序的静态分析](cases/psp-allegrex.md) — 接入 Allegrex 扩展，使 REA 能分析 PSP 程序。 **[REA]**
- [智能马桶：从微信小程序协议做到电脑状态栏控制](cases/smart-toilet.md) — 分析微信小程序的蓝牙通信，控制智能马桶翻盖。 **[REA]**
- [涂鸦 Zigbee 按钮：用 AI 辅助改造固件](cases/tuya-zigbee-button.md) — 借助 pi + GLM 研究按钮固件并进行改造。 **[其他 AI 逆向]**

### 应用与客户端

- [LG 电视：重做更快的 Plex 客户端](cases/lg-plxnative.md) — 研究 LG 媒体栈，开发更快的原生 Plex 客户端。 **[其他 AI 逆向]**
- [Claude Slides：分析前端代码，重建幻灯片编辑器](cases/claude-slides.md) — 分析混淆前端，重建幻灯片编辑器。 **[REA]**
- [Claude Code：用 Muse + REA 阅读大型压缩代码](cases/claude-code-analysis.md) — 让 Muse 调用 REA 阅读 Claude Code 的压缩代码包。 **[REA]**
- [Notion：追清复制文字和图片的内部链路](cases/notion-clipboard.md) — 追踪桌面客户端复制文字和图片的实现路径。 **[REA]**
- [Flutter App：从安装包识别运行时和编译结构](cases/flutter-aot.md) — 识别 Flutter APK 的运行时、构建与 AOT 结构。 **[REA]**

### 算法与功能重建

- [二进制库：先分析原实现，再写替代代码](cases/binary-library-rewrite.md) — 分析二进制库并重写；库名和评测细节未公开。 **[REA]**
- [DownUnderCTF：从校验程序中找出正确输入](cases/masked-squares-ctf.md) — 恢复校验约束，用 Z3 求出被原程序接受的输入。 **[REA]**
- [Aegis：还原验证器 App 的一次性验证码计算](cases/aegis-totp.md) — 从验证器 APK 提取验证码逻辑并做多实现对照。 **[REA]**

## 收录口径

- REA、其他 AI 逆向与工具未确认分别标注，不把所有 AI 案例写成 REA 成果。
- 有具体对象、过程和结果的优先；自述结果注明边界，工具支持不等于完整产品重建。
- X 热度只保留带日期的抓取快照，不代表实时排名；发布日期不等于项目完成日期。
- 同一项目的多条帖子合并；不同作者或不同目标不人为归并。
- 新案例请修改 `data/cases.json` 并提交 PR，生成文件由脚本统一更新。

## 许可与致谢

本仓库原创摘要、数据整理与代码采用 [MIT License](LICENSE)。链接指向的第三方软件、文档、帖子和游戏资产仍遵循各自权利与许可证；本仓库许可不赋予其使用或分发权。

组织方式参考 [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)，具体调研见 [结构与维护调研](research/reference-structure.md)。
