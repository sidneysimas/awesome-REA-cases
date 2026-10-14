# 全部案例与项目

[精选首页](README.md) | [English index](INDEX.en.md)

**用 AI 读懂软件与硬件：重建功能、打通协议、迁移旧系统。**

**每天 6 次定时追踪 REA 与 AI 逆向公开案例，自动筛选、去重并更新合集。**

收集 REA 与其他 AI 逆向的案例和项目，覆盖游戏保存、硬件互通、应用重建与算法研究。每条说明作者在研究什么、为什么逆向、具体做了什么，并链接原帖、代码或验证记录。

[REA](https://github.com/morluto/rea)（Reverse Engineer Anything）通过 CLI / MCP，让编程 Agent 调用本地逆向分析工具。本集合不局限于 REA，也收录其他 AI 辅助逆向和为 AI 工具实现互通的项目。

当前收录 **150 个案例与项目**，按用途分类，不设 Top N 或热度门槛。

## 目录

- [游戏与游戏保存](categories/games.md)（28）
- [硬件与设备互通](categories/hardware.md)（37）
- [应用与客户端](categories/apps.md)（76）
- [算法与功能重建](categories/algorithms.md)（9）
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
- [《红色警戒 2》：为强化学习重写游戏引擎](cases/red-alert-2-rl-engine.md) — 参考 Chrono Divide，用 Opus 与测试集重建单位行为。 **[其他 AI 逆向 · 待验证]**
- [《不可思议的机器》：用 Claude 重建浏览器版](cases/incredible-machine-browser.md) — 作者报告 Opus 分析 Sierra 老游戏、重做素材并在浏览器运行。 **[其他 AI 逆向 · 待验证]**
- [《街头霸王 III》：用 AI 重构反编译后的 C 代码](cases/sfiii-codescene-refactoring.md) — 在既有开源反编译代码上用 CodeHealth MCP 与轨迹回放约束重构。 **[其他 AI 逆向 · 相关项目]**
- [经典射击游戏：AI 辅助浏览器移植的传播报告](cases/classic-shooters-browser-report.md) — 传播帖列出多款网页移植，但缺少项目对应与 AI 贡献证据。 **[未确认使用 REA · 待验证]**
- [Nanolathe：重新实现《横扫千军》游戏引擎](cases/nanolathe-total-annihilation.md) — 用公开研究重实现 Total Annihilation，AI 具体贡献仍待核实。 **[其他 AI 逆向 · 待验证]**
- [手游交互：用 Codex + REA 对应脚本与运行活动](cases/mobile-game-interaction-evidence.md) — 一边分析脚本文件，一边观察手游交互的计算活动。 **[REA · 进行中]**
- [Star Fox / Sonic CD：AI 原生移植的待验证传播](cases/arwing-littleplanet-ai-port-report.md) — 传播帖关联三个原生移植仓库，但不等于 AI 完整反编译。 **[其他 AI 逆向 · 待验证]**
- [Dark Sun: Shattered Lands：用 REA 研究并移植老游戏的计划](cases/dark-sun-shattered-lands-port-idea.md) — 提出从 GOG 游戏到 REA 分析，再用攻略帮助移植 Unity/three.js 的路线。 **[REA · 待验证]**
- [Armed and Dangerous：用 Ghidra 与 AI 探索重制路线](cases/armed-and-dangerous-remaster.md) — 作者报告以 Ghidra 反编译并用 AI 编写 C 函数，正在比较运行时替换与 Bevy 重写路线。 **[未确认使用 REA · 进行中]**
- [Fort Apocalypse：用 Codex 与 Ghidra 移植到 Android](cases/fort-apocalypse-android-port.md) — 作者称使用 Codex 和 Ghidra 将 C64 游戏 Fort Apocalypse 移植到 Android。 **[其他 AI 逆向 · 待验证]**
- [Minecraft × Plants vs. Zombies：REA 辅助的可玩混合作品报告](cases/minecraft-pvz-rea-mashup.md) — 一则 quote 帖称试用 REA 逆向后制作出可玩的 Minecraft 与植物大战僵尸混合作品。 **[REA · 待验证]**
- [《三国志14》：将修改器功能组合成 MCP 的报告](cases/three-kingdoms-mod-mcp.md) — 作者称分析《三国志14》修改器与风灵月影，并组合成可批量操作的 MCP。 **[未确认使用 REA · 待验证]**
- [Virtua Fighter 2.1 / 3 TB：AI 辅助反编译进行中](cases/virtua-fighter-ai-decompilation.md) — AI coding agents 辅助恢复两款 SEGA 格斗游戏的可读 C/C++ 逻辑；项目仍在进行。 **[未确认使用 REA · 进行中]**
- [Dragon Ball Budokai：AI 逆向与浏览器移植的待验证报告](cases/dragon-ball-budokai-browser.md) — 传播帖称 AI 逆向《龙珠》游戏并实现可在浏览器运行的 60 fps 版本；项目与 AI 贡献未核实。 **[未确认使用 REA · 待验证]**
- [Friday Night Funkin’：基于反编译成果制作 Claude 辅助的新玩法](cases/friday-night-funkin-claude-gameplay.md) — 作者称基于近期反编译成果，用 Claude 制作含新输入、画面与界面的玩法版本。 **[未确认使用 REA · 待验证]**

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
- [PS5 安全机制：AI 辅助逆向的传播报告](cases/ps5-ai-security-report.md) — 传播帖称 AI 加速 PS5 安全研究，未提供模型与技术过程。 **[未确认使用 REA · 待验证]**
- [空调协议：用 AR 眼镜手势控制家电](cases/ar-air-conditioner-control.md) — 分析官方 App 请求，再把开关和调温控制接到 AR 眼镜。 **[REA · 待验证]**
- [红米电视：研究浏览器 APK，把闲置电视改成数据大屏](cases/redmi-tv-dashboard.md) — Muse + Codex 分析电视浏览器与全屏行为，适配现有数据看板。 **[其他 AI 逆向 · 待验证]**
- [CF632BLE 体脂秤：在浏览器里称重，不走厂商后台](cases/cf632ble-web-bluetooth.md) — Claude Code + ghidra-rpc 研究 BLE 协议，重实现 Python 与网页客户端。 **[其他 AI 逆向 · 待验证]**
- [Kindle：为运行微信读书制作 Android 固件](cases/kindle-android-weread.md) — Codex 与 Claude 接力适配系统；作者报告设备已显示界面。 **[其他 AI 逆向 · 进行中]**
- [全屋联网设备：用 Codex + REA 做电脑控制端](cases/rea-home-device-control-report.md) — 作者称分析自家设备后做电脑控制软件，型号未公开。 **[REA · 待验证]**
- [小米音箱：改固件接入 ChatGPT 语音的 idea](cases/xiaomi-speaker-chatgpt-voice-idea.md) — 提出研究小米音箱固件，让设备支持 ChatGPT voice。 **[未确认使用 REA · 待验证]**
- [Kepler 显卡：为 AI 推理做逆向研究的计划](cases/kepler-ai-inference-idea.md) — 计划研究旧 Kepler 显卡，使其用于 AI 推理。 **[其他 AI 逆向 · 待验证]**
- [散热器 LCD：逆向 USB 协议，做 Rust 状态屏](cases/thermalright-cooler-lcd-rust.md) — 让 Thermalright 散热器屏幕在 Omarchy 显示温度与 AI 使用量。 **[其他 AI 逆向 · 待验证]**
- [相机固件：让 Codex 推进虚拟机启动研究](cases/camera-firmware-vm-boot.md) — 研究自己的相机固件，使其能在虚拟机启动。 **[其他 AI 逆向 · 进行中]**
- [LG 电视：用 REA 核查隐私行为的 idea](cases/lg-tv-ai-privacy-audit-idea.md) — 提出分析电视代码实际行为，检验数据采集与隐私说法。 **[REA · 待验证]**
- [Homatics 盒子：研究固件修复 Dolby Vision 绿屏](cases/homatics-atv14-dolby-vision-fix.md) — 作者称修复 Box R 4K Plus 升 Android TV 14 后的偏色。 **[REA · 待验证]**
- [AYN Odin 2 Portal：用 Codex 研究启动链，原生运行 Omarchy](cases/omarchy-mobile-odin2.md) — 研究掌机分区、启动与设备适配，在内部存储原生运行 Linux 桌面。 **[其他 AI 逆向 · 进行中]**
- [Ledger：让 Claude 重写自定义固件的 idea](cases/ledger-custom-firmware-idea.md) — 针对拆开的 Ledger 设备，提出替换厂商固件与配套软件的设想。 **[其他 AI 逆向 · 待验证]**
- [LG 电视：研究系统后原生运行 Claude Code](cases/lg-tv-native-claude-code.md) — 作者称在 LG 电视上运行 Claude Code，并用遥控器语音转文字输入。 **[未确认使用 REA · 待验证]**
- [HP 打印机：用 Claude 重写固件以支持第三方墨水的 idea](cases/hp-printer-third-party-ink-idea.md) — 转述针对 HP 固件与第三方墨水兼容的设想，未见实现。 **[其他 AI 逆向 · 待验证]**
- [Android 触屏相框：拆机后接 Codex 研究设备](cases/android-photo-frame-codex-bringup.md) — 作者报告拆开廉价 Android 相框，参考 wesbos 项目接入 Codex 研究。 **[其他 AI 逆向 · 进行中]**
- [Echo Show 5 Gen2：研究设备，接入 Hermes 做跨住宅对讲和安防](cases/echo-show5-hermes-intercom.md) — 作者报告改造 Echo Show 5，与 Hermes Agent 连接实现对讲及摄像系统。 **[未确认使用 REA · 待验证]**
- [Elgato X 4K 采集卡：用 REA 研究性能和低延迟](cases/elgato-4k-x-latency-research.md) — 作者开始逆向研究自己的采集卡，目标是更好性能与更低延迟。 **[REA · 进行中]**
- [Gardena 割草机：Codex 控制电机并研究新固件](cases/gardena-mower-codex.md) — 作者称 Codex 已取得割草机电机控制，正研究 ESP32 与蓝牙链路的新固件。 **[未确认使用 REA · 进行中]**
- [电视：用 REA 逆向并制作电脑控制工作台](cases/rea-tv-control-workbench.md) — 作者称用 REA 逆向电视，并列出输入切换、音量、遥控、Mac 屏幕镜像、屏幕时间及画面控制等功能。 **[REA · 待验证]**
- [Canon Pro-1000：用 Claude 研究并模拟打印机固件](cases/canon-pro-1000-firmware-emulation.md) — 作者称正尝试用 Claude 逆向并模拟 Canon Pro-1000 固件；未报告完成或验证。 **[未确认使用 REA · 进行中]**
- [TCL 空调：逆向 TCL Home 并制作 macOS 控制端](cases/tclimate-macos.md) — 第三方称开发者用 REA 分析 TCL Home，并制作原生 Mac 菜单栏控制应用。 **[未确认使用 REA · 待验证]**
- [投影仪红外遥控：用 Codex 推断并验证缺失的对焦命令](cases/projector-ir-focus-command.md) — 根据遥控器 IR 时序推断 Focus+ 命令，并报告已成功控制投影仪对焦。 **[其他 AI 逆向]**
- [Smart pen：用 Codex 反编译并集成现成设备](cases/smart-pen-codex-integration.md) — 团队称用 Codex 反编译现成智能笔，并将其集成进软件系统。 **[其他 AI 逆向]**
- [Ray-Ban Meta 眼镜：逆向通信并制作 Android 助手替代应用](cases/rayban-meta-claude-android.md) — 发帖者称逆向眼镜与手机的通信，并制作 Android 应用将语音助手请求转给 Claude 或自选模型；REA 使用未确认。 **[未确认使用 REA · 待验证]**

### 应用与客户端

- [LG 电视：重做更快的 Plex 客户端](cases/lg-plxnative.md) — 研究 LG 媒体栈，开发更快的原生 Plex 客户端。 **[其他 AI 逆向]**
- [Claude Slides：分析前端代码，重建幻灯片编辑器](cases/claude-slides.md) — 分析混淆前端，重建幻灯片编辑器。 **[REA]**
- [Claude Code：用 Muse + REA 阅读大型压缩代码](cases/claude-code-analysis.md) — 让 Muse 调用 REA 阅读 Claude Code 的压缩代码包。 **[REA]**
- [Notion：追清复制文字和图片的内部链路](cases/notion-clipboard.md) — 追踪桌面客户端复制文字和图片的实现路径。 **[REA]**
- [Flutter App：从安装包识别运行时和编译结构](cases/flutter-aot.md) — 识别 Flutter APK 的运行时、构建与 AOT 结构。 **[REA]**
- [网站重建订单：作者自述的交付报告](cases/website-rebuild-report.md) — 作者称以 REA 辅助网站重建，缺少具体项目与验证。 **[REA · 待验证]**
- [TradingView：传播较多的复刻流程帖](cases/tradingview-workflow.md) — 有 REA 复刻流程，但没有证明恢复付费指标。 **[REA · 待验证]**
- [WHOOP：分析健康追踪设备的 Android App](cases/whoop-apk.md) — 发现 APK 分析讨论，尚未确认完成替代客户端。 **[未确认使用 REA · 待验证]**
- [ArtCraft：不要把从零开发写成逆向 Adobe](cases/artcraft-boundary.md) — 创作软件与 Office 风格工具的从零重建，不等于已完整逆向 Adobe 或 Office。 **[其他 AI 逆向 · 相关项目]**
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
- [Pump.fun：并行 Agent 研究发币平台机制](cases/pumpfun-reconstruction-report.md) — 第三方报告 Codex 与另一 Agent 并行研究 Pump.fun。 **[REA · 待验证]**
- [远程桌面客户端：用 AI 逆向做数据采集监测的 idea](cases/remote-client-privacy-monitor-idea.md) — 在 ToDesk 等远程桌面客户端场景，提出逆向分析并监测数据采集。 **[未确认使用 REA · 待验证]**
- [稿定设计：为固定封面制作自己的工作台](cases/gaoding-cover-workbench.md) — 已用 Codex + Fabric.js 做封面工具，计划再用 REA 研究稿定的界面与逻辑。 **[REA · 进行中]**
- [Axure：反编译原型工具，做 AI 时代版本的 idea](cases/axure-ai-rebuild-idea.md) — 提出研究 Axure 并重做面向 AI 的交互原型工具。 **[未确认使用 REA · 待验证]**
- [Hermes Agent：用 Hark 研究后做新的 Agent 框架](cases/hermes-hark-harness.md) — 作者报告研究 Hermes Agent，随后制作自己的 AI 执行框架。 **[其他 AI 逆向 · 待验证]**
- [Apple Preview：不重建整款 App，直接加 AI 功能](cases/preview-ai-sidebar.md) — 在现有编译应用的副本上增加 AI 侧栏，而非从零复刻。 **[未确认使用 REA · 待验证]**
- [Cameo：从桌面角色应用的编译程序重建交互](cases/cameo-reconstruction.md) — 用 REA 产出伪代码，再由 Claude Code 还原桌面角色应用。 **[REA · 待验证]**
- [wine-uwp：让 Shapr3D 等 Windows 商店应用在 Linux 运行](cases/wine-uwp-shapr3d.md) — 用 Claude 辅助研究封闭应用所需接口，扩展 Wine 的兼容层。 **[其他 AI 逆向 · 待验证]**
- [CleanMyMac：研究核心功能并做原生 Mac 应用雏形](cases/cleanmymac-rebuild-report.md) — 第三方报告宝玉用 REA 分析清理工具，再重建部分功能。 **[REA · 待验证]**
- [Nexalytics：用自己的应用检验 REA 行为重建](cases/nexalytics-rebuild.md) — 研究前后端通信与操作流程，结合 Playwright 重建应用。 **[REA · 待验证]**
- [MetaTrader：为研究交易信号进行逆向的转述](cases/metatrader-signals-report.md) — 评论称有人研究 MetaTrader 以获取信号，缺少具体实现证据。 **[未确认使用 REA · 待验证]**
- [业务软件：从既有程序或网页重建的进行中尝试](cases/business-software-rebuild.md) — 作者称正在用 Agent 逆向工作流克隆一款业务软件。 **[未确认使用 REA · 进行中]**
- [CapCut 转场：研究视频编辑模块并自行重构的线索](cases/capcut-transition-research.md) — 第三方讨论以 CapCut 转场为研究对象，用于理解编辑器设计。 **[未确认使用 REA · 待验证]**
- [Android App：用 Claude Code 识别根检测与证书固定](cases/android-protection-inspection.md) — AMA 转述一次 JADX、Burp Suite MCP 与 Claude Code 的移动应用分析。 **[其他 AI 逆向 · 待验证]**
- [代理客户端：恢复 Clash 所需的订阅导出](cases/proxy-clash-subscription-bridge.md) — Codex 分析客户端二进制，作者自建服务衔接订阅接口。 **[其他 AI 逆向 · 待验证]**
- [Netflix / Prime：统一流媒体界面的逆向转述](cases/streaming-service-integration-report.md) — 第三方称将两个服务整合到一个界面，未说明合法内容获取与 AI 贡献。 **[未确认使用 REA · 待验证]**
- [Slack 音乐 / Claude 会议：跨应用功能组合的 idea](cases/slack-music-claude-zoom-idea.md) — 提出把 YouTube Music 放进 Slack、把 Zoom 放进 Claude，而非只拼接游戏。 **[未确认使用 REA · 待验证]**
- [fowlbrowser：让 Claude 等 Agent 使用现有 Chrome 登录态](cases/fowlbrowser-agent-bridge.md) — 浏览器扩展为不同 Agent 提供前台与后台标签页操作。 **[未确认使用 REA · 待验证]**
- [OpenSetter：重建评论转私信流程，并接入 AI 销售助手](cases/opensetter-manychat-rebuild.md) — 作者称研究 Manychat，公开 Instagram 私信自动化与 AI 回复项目。 **[未确认使用 REA · 相关项目]**
- [zee-rp：让 AI 直接读写 Axure 原型文件](cases/zee-rp-axure-format.md) — 逆向 .rp 格式，以 CLI/MCP 编辑原生交互原型。 **[REA · 待验证]**
- [CapCut：用 REA + Claude Code 做自己的视频编辑器](cases/capcut-rea-editor.md) — 研究剪辑工具，重建字幕、转场、动画与文字功能。 **[REA · 进行中]**
- [ClearSpace：研究 CleanMyMac，做原生 Mac 清理工具](cases/clearspace-cleanmymac.md) — Codex + REA 研究清理工具，报告缓存与文件管理功能。 **[REA · 待验证]**
- [停更记账软件：AI 分析卡在加密层](cases/discontinued-accounting-encryption.md) — 从旧程序研究记账需求，但未突破加密内容。 **[未确认使用 REA · 进行中]**
- [SolidWorks / Creo / Autodesk：重建带 CLI 的开源 CAD idea](cases/cad-cli-open-rebuild-idea.md) — 提出 AI 辅助研究商业 CAD，制作可脚本控制的替代工具。 **[未确认使用 REA · 待验证]**
- [Obsidian：GPT 选择笔记应用并尝试重建](cases/obsidian-gpt-rebuild-report.md) — 以 Obsidian 为目标做快速重建，具体功能与验证未公开。 **[未确认使用 REA · 待验证]**
- [Web Flow：用 REA 梳理请求链，转成 REST 接口定义](cases/rea-webflow-rest-spec-report.md) — 作者称分析某大厂 Web Flow 的时序与请求链，输出接口定义。 **[REA · 待验证]**
- [Android priv-app：用 GPT 检查系统应用特权](cases/android-priv-app-permission-inspection.md) — 分析 priv-app 中疑似电信应用，研究其权限。 **[其他 AI 逆向 · 进行中]**
- [Helm Chart API v2：从实现整理可互通规范](cases/helm-chart-v2-spec-research.md) — 借助 AI 研究 Chart v2，整理便于其他工具使用的规范。 **[其他 AI 逆向 · 进行中]**
- [个人网站：用 REA 拆解设计，再做自定义重建](cases/rea-personal-website-redesign.md) — 作者称从某站设计重建自己的站，展示网页与 iPhone 版本。 **[REA · 待验证]**
- [SaaS 功能子集：Codex 观察，Replit 重建所需 20%](cases/codex-replit-saas-subset-rebuild.md) — 只重建实际用到的 SaaS 功能，以替代整套订阅。 **[其他 AI 逆向 · 待验证]**
- [Virtual Desktop Streamer：研究安装包，做 Linux 适配层](cases/virtual-desktop-streamer-linux.md) — Claude Code + REA 分析官方安装包，复用协议库并替换 macOS 平台层。 **[REA · 进行中]**
- [微信本地聊天记录：Codex 分析加密数据的作者报告](cases/wechat-local-chat-decryption-report.md) — 作者称曾用 Codex 处理微信本地加密聊天记录，过程与范围未公开。 **[其他 AI 逆向 · 待验证]**
- [LightBurn：为自己的激光机重建专用控制软件的报告](cases/lightburn-personal-laser-rebuild.md) — 作者称用 REA 在16分钟内制作只针对自己激光机的 LightBurn 替代。 **[REA · 待验证]**
- [MarkText：用 REA 逆向并重建 HTML 导出](cases/marktext-html-export.md) — 用 AI bots 与 REA 分析 MarkText 的 HTML 导出并重建；17 项测试通过，Windows 检查仍未完成。 **[REA · 进行中]**
- [Screen Studio：用 REA 拆解后复刻录屏演示工具](cases/screen-studio-rebuild.md) — 作者报告用 REA 分析 Screen Studio，并以 Claude Code 复刻、录制演示。 **[REA · 待验证]**
- [Claude Desktop：用 REA 观察界面细节](cases/claude-desktop-ui-details.md) — 作者称用 REA 分析 Claude Desktop，记录暗色字重、换行与逐字淡入等界面细节。 **[REA · 分析测试]**
- [Typeless：用 REA 做本地语音输入替代品](cases/rea-typeless-local.md) — 作者报告用 REA 分析 Typeless，并完成离线运行的 Swift 语音输入应用。 **[REA · 待验证]**
- [Eleven：让 Agent 协助分析应用与二进制](cases/eleven-agent-reverse-engineering.md) — 作者介绍一款开源逆向工具，可查看多平台二进制并让 Agent 协助理解代码。 **[未确认使用 REA · 待验证]**
- [48,000,000 行数据库：REA 辅助查询优化的转述](cases/rea-database-query-optimization-report.md) — 第三方称 Claude Code 与 REA 协助优化仪表板查询；性能与等价结果未独立核验。 **[未确认使用 REA · 待验证]**
- [GTM 工具：用 REA 构建线索与邮件营销工作流](cases/rea-gtm-tool.md) — 作者称用 REA 构建获客工具，涵盖线索管理与邮件活动；未提供实现或测试细节。 **[REA · 待验证]**
- [茶叶出海网站：REA 辅助的本地重建报告](cases/tea-site-rea-rebuild-report.md) — 作者称用 Codex + REA 逆向参考网站，并在约 40 分钟内本地部署重建版。 **[REA · 待验证]**
- [iTerm：借助 REA 规格实现阿拉伯语文本绘制](cases/arabic-terminal-rendering.md) — 作者自述用 REA 分析 iTerm，再按规格制作并在设备上测试阿拉伯语绘制支持；实现与测试尚无独立核验。 **[REA · 待验证]**
- [Bloomberg 风格研究终端：用 REA 与 Claude 构建独立数据工作站](cases/bloomberg-style-research-terminal.md) — 作者称用 REA 与 Claude 构建金融研究终端；使用独立市场数据，未解锁 Bloomberg 专有数据。 **[REA · 待验证]**
- [闭源 Coding Agent：逆向多模型协同逻辑并制作 pi 插件](cases/closed-agent-pi-plugin.md) — 作者自述用 REA 研究闭源 Coding Agent 的多模型协同逻辑，并据此开发 pi 插件；目标与实现尚未公开核验。 **[REA · 待验证]**
- [ChatGPT App：用 REA 分析并为聊天窗口添加渐变背景](cases/chatgpt-app-gradient-background.md) — 作者称用 ChatGPT 与 REA 分析 Electron 应用，并为右侧聊天窗口注入渐变背景。 **[REA · 待验证]**
- [Ledger Reborn：研究 QuickBooks 后制作独立记账应用](cases/ledger-reborn-accounting-app.md) — 第三方 quote 帖称开发者以 REA + Ghidra 研究 QuickBooks 的库存成本、预算与对账，并发布 Windows / Mac 预览版。 **[REA · 相关项目]**
- [红果短剧：用 REA 逆向并去除广告与悬浮窗](cases/hongguo-short-drama-ad-removal.md) — 发帖者自述用 REA 逆向红果短剧应用，实现去广告和去悬浮窗功能；连续观看一天未见广告的结果尚未独立核验。 **[REA · 待验证]**
- [Profound：用 REA 研究并重建 SaaS 工作台](cases/profound-rea-reconstruction.md) — 作者称用 REA 逆向 Profound 的官网、工作台与管理后台并开源重建项目；所述数据为虚构示例，功能尚未独立核验。 **[REA · 待验证]**
- [Codex Desktop：作者尝试用 REA 研究其与 CLI 的差异](cases/codex-desktop-rea-attempt.md) — 作者自述尝试用 REA 逆向 Codex 桌面版，以了解其为何优于 Codex CLI；未报告分析结果或验证。 **[REA · 进行中]**
- [Mac 桌面软件：用 REA 制作分析文档与 UI 参考手册](cases/mac-app-rea-analysis-workflow.md) — 作者称用 WorkBuddy、DeepSeek 与 REA 分析 Mac 软件，并生成技术/UI 文档及采集工具。 **[REA · 待验证]**
- [Apple Weather：作者自述用 REA 重建天气应用](cases/apple-weather-rea-rebuild.md) — 发帖者称用 REA 制作 Apple Weather 克隆；其评分比较未说明方法或独立验证。 **[REA · 待验证]**
- [Linux cal：从无符号程序追出 1752 年日历切换](cases/linux-cal-1752-switch.md) — 用 REA 分析无符号 calendar 二进制，定位 1752 年缺失日期规则并作选项测试。 **[REA]**

### 算法与功能重建

- [二进制库：先分析原实现，再写替代代码](cases/binary-library-rewrite.md) — 分析二进制库并重写；库名和评测细节未公开。 **[REA]**
- [DownUnderCTF：从校验程序中找出正确输入](cases/masked-squares-ctf.md) — 恢复校验约束，用 Z3 求出被原程序接受的输入。 **[REA]**
- [Aegis：还原验证器 App 的一次性验证码计算](cases/aegis-totp.md) — 从验证器 APK 提取验证码逻辑并做多实现对照。 **[REA]**
- [Windows 计算器：还原百分号在不同运算中的规则](cases/windows-calculator-percent.md) — 分析已安装计算器 DLL，解释并重建加法与乘法的百分号行为。 **[REA]**
- [自制 JS / .NET 样本：对照有无 REA 的函数重建](cases/codex-rea-controlled-samples.md) — 同模型六次运行、360 用例验收，研究 REA 的线索价值而非宣称提速。 **[REA · 分析测试]**
- [DLSS：重实现计算着色器以在 AMD 显卡运行的报告](cases/dlss-amd-compute-report.md) — 讨论明确提出 AI 辅助重实现 DLSS，具体开发归属仍待核验。 **[未确认使用 REA · 待验证]**
- [REA 分析链路：测试二进制内提示注入的 idea](cases/rea-binary-injection-test-idea.md) — 计划测试目标文件中的文字能否污染 AI 逆向结论。 **[未确认使用 REA · 待验证]**
- [CapCut 动态字幕：从模板 DSL 重建渲染器的 idea](cases/capcut-subtitle-renderer-idea.md) — 研究字幕模板、Shader 与 SDF 渲染，再以图片 diff 验证。 **[未确认使用 REA · 待验证]**
- [16 个笔记文件：有无 REA 的解码对照实验转述](cases/sixteen-note-files-decoder-report.md) — 长文转述对16个笔记文件的限时解码比较，两条语言版本合并。 **[REA · 待验证]**

## 贡献与收录

欢迎提交新案例、补充验证或纠正描述。修改 `data/cases.json` 后运行 `python3 scripts/build.py`，再提交 PR；详见[贡献指南](CONTRIBUTING.md)。

优先原作者、具体目标与操作记录。同一项目合并来源；作者自述、静态分析和实际运行分别说明。X 热度保留抓取日期，不作为效果证明。

## 说明与许可

非 REA 官方项目。结果据作者和项目记录整理，未由本集合独立复现。仅整理原创摘要与公开链接，不分发原软件、游戏资产、密钥或私人材料。

本仓库原创摘要、数据整理与代码采用 [MIT License](LICENSE)；链接内容保留各自权利与许可证。研究、复现或再利用前，请确认你拥有相应授权。

组织方式参考 [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)。[收集范围](research/collection-scope.md) · [结构调研](research/reference-structure.md)
