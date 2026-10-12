# Awesome REA Cases

**中文（默认）** | [English](README.en.md)

**用 AI 读懂软件与硬件：重建功能、打通协议、迁移旧系统。**

收集 REA 与其他 AI 逆向的案例和项目，覆盖游戏保存、硬件互通、应用重建与算法研究。每条说明作者在研究什么、为什么逆向、具体做了什么，并链接原帖、代码或验证记录。

[REA](https://github.com/morluto/rea)（Reverse Engineer Anything）通过 CLI / MCP，让编程 Agent 调用本地逆向分析工具。本集合不局限于 REA，也收录其他 AI 辅助逆向和为 AI 工具实现互通的项目。

当前收录 **55 个案例与项目**，按用途分类，不设 Top N 或热度门槛。

## 目录

- [游戏与游戏保存](categories/games.md)（13）
- [硬件与设备互通](categories/hardware.md)（11）
- [应用与客户端](categories/apps.md)（27）
- [算法与功能重建](categories/algorithms.md)（4）
- [贡献案例](CONTRIBUTING.md) · [维护方法](MAINTENANCE.md)

工具标注：`REA` / `其他 AI 逆向` / `未确认使用 REA`。阶段标注：`待验证` / `进行中` / `分析测试` / `相关项目`；有标注的也列在主目录，但不等同于已完成成果。

## 案例与项目

### 游戏与游戏保存

- [Universal Modder：用 AI 给现有游戏做 Mod](cases/universal-modder.md) — 分析游戏代码与文件格式，制作跨游戏内容 Mod。 **[其他 AI 逆向]**
- [Firefighter：把老 DOS 游戏恢复成可维护的 Rust 代码](cases/firefighter-rust.md) — 从旧 DOS 二进制恢复 Pascal，再转写为 Rust。 **[其他 AI 逆向]**
- [《现代战争 2》：用多 Agent 重建游戏代码](cases/mw2-decompilation.md) — 多 Agent 反编译游戏，以原二进制核对恢复函数。 **[其他 AI 逆向]**
- [Urban Terror：把桌面多人射击游戏移植到浏览器](cases/urban-terror-web.md) — 定位引擎与字节码布局差异，将游戏移植到浏览器。 **[其他 AI 逆向]**
- [DX-Ball：恢复老打砖块游戏的声像算法](cases/dx-ball-sound-pan.md) — 还原打砖块游戏按位置分配左右声道的函数。 **[REA]**
- [《东方幻想乡》：恢复环形弹幕的角度计算](cases/th04-bullet-ring.md) — 恢复《东方幻想乡》环形弹幕的角度计算。 **[REA]**
- [东方系列：用 Agent 重建旧游戏，并迁移到新平台](cases/touhou-reconstruction.md) — 重建东方系列代码，验证并迁移到可玩平台。 **[REA]**
- [Dinosaur：解释网页跑酷游戏如何逐渐加速](cases/dinosaur-speed.md) — 读网页脚本，实验验证跑酷游戏的加速规则。 **[REA]**
- [Unity / Valheim：游戏程序集分析需求](cases/unity-valheim.md) — 真实游戏分析需求，原游戏目标复测仍缺少证据。 **[REA · 进行中]**
- [《荒野大镖客 2》：写导出器移入波巴·费特](cases/boba-fett-rdr2.md) — Claude 研究游戏素材格式，迁移角色并制作喷气背包等玩法。 **[其他 AI 逆向]**
- [GameCube / Wii：从实际 Wii 分析提出 PowerPC 支持](cases/wii-powerpc-request.md) — 已有 Ghidra 研究经验，REA 内部支持仍是需求。 **[未确认使用 REA · 进行中]**
- [《航空霸业2》：用 REA + Kimi 反编译老游戏](cases/aerobiz-2-decompilation.md) — 研究 KOEI 1993 年航空经营游戏的编译程序。 **[REA · 待验证]**
- [《超级马里奥阳光》：AI 参与说法下的原生 PC 移植](cases/super-mario-sunshine-pc.md) — 传播帖称 AI Agent 参与反编译并将 GameCube 游戏移植到 PC。 **[未确认使用 REA · 待验证]**

### 硬件与设备互通

- [Apple TV 遥控器：让专用配件在 Linux 上工作](cases/siri-remote-linux.md) — 解析蓝牙协议，让 Apple TV 遥控器接入 Linux。 **[未确认使用 REA]**
- [涂鸦 RGB 灯：绕开厂商 App，直接从 Mac 控灯](cases/tuya-rgb-mac.md) — 分析手机蓝牙控灯数据，用 Mac 脚本直接控灯。 **[其他 AI 逆向]**
- [老设备 MIPS 固件：把程序按正确架构读出来](cases/mips-firmware.md) — 为旧设备固件选定正确架构，核对分析结果。 **[REA]**
- [PSP：让 REA 支持掌机程序的静态分析](cases/psp-allegrex.md) — 接入 Allegrex 扩展，使 REA 能分析 PSP 程序。 **[REA]**
- [智能马桶：从微信小程序协议做到电脑状态栏控制](cases/smart-toilet.md) — 分析微信小程序的蓝牙通信，控制智能马桶翻盖。 **[REA]**
- [涂鸦 Zigbee 按钮：用 AI 辅助改造固件](cases/tuya-zigbee-button.md) — 借助 pi + GLM 研究按钮固件并进行改造。 **[其他 AI 逆向]**
- [分层固件：解包后把原生程序交给 Ghidra](cases/firmware-extract-handoff.md) — 串起 Binwalk 区域识别、Unblob 解包和 Ghidra 函数分析。 **[REA]**
- [蓝牙手柄：写兼容层让不支持 Windows 的设备可用](cases/bluetooth-gamepad-windows.md) — 逆向控制协议，以 ViGEm 虚拟手柄适配 Windows。 **[其他 AI 逆向]**
- [蓝牙小手柄：协议研究后计划做跨平台设置程序](cases/gamepad-settings-request.md) — 作者报告协议已逆向，但设置程序仍计划中。 **[REA · 进行中]**
- [华硕笔记本：通过 ACPI 研究改善 Linux 显卡支持](cases/asus-acpi-gpu.md) — 作者称 Codex 启用了 NVIDIA 显卡，缺少具体复现材料。 **[其他 AI 逆向 · 待验证]**
- [游戏鼠标：为 macOS 恢复 RGB、DPI 与按键设置](cases/gaming-mouse-macos.md) — 用 ChatGPT 辅助逆向鼠标配套软件，补上 Mac 设置能力。 **[其他 AI 逆向 · 待验证]**

### 应用与客户端

- [LG 电视：重做更快的 Plex 客户端](cases/lg-plxnative.md) — 研究 LG 媒体栈，开发更快的原生 Plex 客户端。 **[其他 AI 逆向]**
- [Claude Slides：分析前端代码，重建幻灯片编辑器](cases/claude-slides.md) — 分析混淆前端，重建幻灯片编辑器。 **[REA]**
- [Claude Code：用 Muse + REA 阅读大型压缩代码](cases/claude-code-analysis.md) — 让 Muse 调用 REA 阅读 Claude Code 的压缩代码包。 **[REA]**
- [Notion：追清复制文字和图片的内部链路](cases/notion-clipboard.md) — 追踪桌面客户端复制文字和图片的实现路径。 **[REA]**
- [Flutter App：从安装包识别运行时和编译结构](cases/flutter-aot.md) — 识别 Flutter APK 的运行时、构建与 AOT 结构。 **[REA]**
- [网站重建订单：作者自述的交付报告](cases/website-rebuild-report.md) — 作者称以 REA 辅助网站重建，缺少具体项目与验证。 **[REA · 待验证]**
- [TradingView：传播较多的复刻流程帖](cases/tradingview-workflow.md) — 有 REA 复刻流程，但没有证明恢复付费指标。 **[REA · 待验证]**
- [WHOOP：分析健康追踪设备的 Android App](cases/whoop-apk.md) — 发现 APK 分析讨论，尚未确认完成替代客户端。 **[未确认使用 REA · 待验证]**
- [ArtCraft：不要把从零开发写成逆向 Adobe](cases/artcraft-boundary.md) — 创作软件与 WordCraft 的从零重建，不等于已完整逆向 Adobe 或 Word。 **[其他 AI 逆向 · 相关项目]**
- [Obsidian：真实桌面包的大规模分析测试](cases/obsidian-asar.md) — 用户确认原 ASAR 包可完成分析，但没有具体功能重建。 **[REA · 分析测试]**
- [大型 Android APK：真实生产包的分析需求](cases/large-android-apk.md) — 133MB、11 DEX 的安装包；原目标未见修复后复测。 **[REA · 进行中]**
- [.NET NativeAOT：从原生二进制恢复 C# 信息的诉求](cases/nativeaot.md) — 已有部分元数据恢复，不是原 C# 工程恢复。 **[REA · 进行中]**
- [Android ApiDemos：从 APK 追到具体 Java 方法](cases/android-apidemos.md) — 用真实演示 APK 查类、读方法、追踪静态引用。 **[REA]**
- [鸿蒙 App：识别安装包结构与组件](cases/harmony-package-inventory.md) — 用真实 HAP 发布包核查组件路径、哈希和打包线索。 **[REA]**
- [macOS 预览：对比有无 REA 的功能重建](cases/preview-rebuild.md) — 同一作者用两条路线重建缩放、旋转、标注与保存。 **[REA]**
- [Codex 浏览器：找出网页唤起评论框的链路](cases/codex-browser-annotations.md) — 分析 Electron 代码并用测试页验证评论接口的部分能力。 **[REA]**
- [Claude Design：把设计功能接进 BaoCut](cases/claude-design-baocut.md) — 研究设计 Skill 与前端，把它们集成到自己的视频 Agent 中。 **[未确认使用 REA]**
- [Claude Chrome：把本地浏览器协议桥接到云浏览器](cases/claude-chrome-remote.md) — 还原原生消息协议，转成 CDP 在远端执行。 **[未确认使用 REA]**
- [pi-computer-use：把 Codex 桌面操作接给其他模型](cases/pi-computer-use.md) — 研究 Computer Use，提供优先无障碍树、辅以视觉的 macOS 工具。 **[未确认使用 REA]**
- [后台 Computer Use：用 Swift 暴露电脑操作 API](cases/background-computer-use.md) — 研究 Codex 后台操作，提供本机可脚本调用的接口。 **[未确认使用 REA]**
- [GarageBand：研究文件格式，用现有乐器自动作曲](cases/garageband-file-format.md) — Claude 分析音乐工程格式，作为本地音乐视频流程的一环。 **[其他 AI 逆向]**
- [Apple Notes：迁移笔记、文件夹和图片到 Grape](cases/apple-notes-migration.md) — 研究笔记数据以实现跨产品导入。 **[其他 AI 逆向]**
- [扑克桌面整理：重建牌桌管理工具](cases/poker-table-organizer.md) — 用 REA、Ghidra 和 Codex 重建整理扑克桌面的功能。 **[REA · 待验证]**
- [Codex 电脑操作：研究浏览器能力并接入其他 Agent](cases/codex-cua-harness-research.md) — 研究 Codex 电脑操作和浏览器功能，以便其他模型在独立框架中使用。 **[REA · 进行中]**
- [Pump.fun：并行 Agent 研究发币平台机制](cases/pumpfun-reconstruction-report.md) — 第三方报告 Codex 与另一 Agent 并行研究 Pump.fun。 **[未确认使用 REA · 待验证]**
- [远程桌面客户端：用 AI 逆向做数据采集监测的 idea](cases/remote-client-privacy-monitor-idea.md) — 在 ToDesk 等远程桌面客户端场景，提出逆向分析并监测数据采集。 **[未确认使用 REA · 待验证]**
- [稿定设计：为固定封面制作自己的工作台](cases/gaoding-cover-workbench.md) — 已用 Codex + Fabric.js 做封面工具，计划再用 REA 研究稿定的界面与逻辑。 **[REA · 进行中]**

### 算法与功能重建

- [二进制库：先分析原实现，再写替代代码](cases/binary-library-rewrite.md) — 分析二进制库并重写；库名和评测细节未公开。 **[REA]**
- [DownUnderCTF：从校验程序中找出正确输入](cases/masked-squares-ctf.md) — 恢复校验约束，用 Z3 求出被原程序接受的输入。 **[REA]**
- [Aegis：还原验证器 App 的一次性验证码计算](cases/aegis-totp.md) — 从验证器 APK 提取验证码逻辑并做多实现对照。 **[REA]**
- [Windows 计算器：还原百分号在不同运算中的规则](cases/windows-calculator-percent.md) — 分析已安装计算器 DLL，解释并重建加法与乘法的百分号行为。 **[REA]**

## 贡献与收录

欢迎提交新案例、补充验证或纠正描述。修改 `data/cases.json` 后运行 `python3 scripts/build.py`，再提交 PR；详见[贡献指南](CONTRIBUTING.md)。

优先原作者、具体目标与操作记录。同一项目合并来源；作者自述、静态分析和实际运行分别说明。X 热度保留抓取日期，不作为效果证明。

## 说明与许可

非 REA 官方项目。结果据作者和项目记录整理，未由本集合独立复现。仅整理原创摘要与公开链接，不分发原软件、游戏资产、密钥或私人材料。

本仓库原创摘要、数据整理与代码采用 [MIT License](LICENSE)；链接内容保留各自权利与许可证。研究、复现或再利用前，请确认你拥有相应授权。

组织方式参考 [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)。[收集范围](research/collection-scope.md) · [结构调研](research/reference-structure.md)
