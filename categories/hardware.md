# 硬件与设备互通

[返回主目录](../README.md)

- [Apple TV 遥控器：让专用配件在 Linux 上工作](../cases/siri-remote-linux.md) — 解析蓝牙协议，让 Apple TV 遥控器接入 Linux。 **[未确认使用 REA]**
- [涂鸦 RGB 灯：绕开厂商 App，直接从 Mac 控灯](../cases/tuya-rgb-mac.md) — 分析手机蓝牙控灯数据，用 Mac 脚本直接控灯。 **[其他 AI 逆向]**
- [老设备 MIPS 固件：把程序按正确架构读出来](../cases/mips-firmware.md) — 为旧设备固件选定正确架构，核对分析结果。 **[REA]**
- [PSP：让 REA 支持掌机程序的静态分析](../cases/psp-allegrex.md) — 接入 Allegrex 扩展，使 REA 能分析 PSP 程序。 **[REA]**
- [智能马桶：从微信小程序协议做到电脑状态栏控制](../cases/smart-toilet.md) — 分析微信小程序的蓝牙通信，控制智能马桶翻盖。 **[REA]**
- [涂鸦 Zigbee 按钮：用 AI 辅助改造固件](../cases/tuya-zigbee-button.md) — 借助 pi + GLM 研究按钮固件并进行改造。 **[其他 AI 逆向]**
- [分层固件：解包后把原生程序交给 Ghidra](../cases/firmware-extract-handoff.md) — 串起 Binwalk 区域识别、Unblob 解包和 Ghidra 函数分析。 **[REA]**
- [蓝牙手柄：写兼容层让不支持 Windows 的设备可用](../cases/bluetooth-gamepad-windows.md) — 逆向控制协议，以 ViGEm 虚拟手柄适配 Windows。 **[其他 AI 逆向]**
- [蓝牙小手柄：协议研究后计划做跨平台设置程序](../cases/gamepad-settings-request.md) — 作者报告协议已逆向，但设置程序仍计划中。 **[REA · 进行中]**
- [华硕笔记本：通过 ACPI 研究改善 Linux 显卡支持](../cases/asus-acpi-gpu.md) — 作者称 Codex 启用了 NVIDIA 显卡，缺少具体复现材料。 **[其他 AI 逆向 · 待验证]**
- [游戏鼠标：为 macOS 恢复 RGB、DPI 与按键设置](../cases/gaming-mouse-macos.md) — 用 ChatGPT 辅助逆向鼠标配套软件，补上 Mac 设置能力。 **[其他 AI 逆向 · 待验证]**
- [PS5 安全机制：AI 辅助逆向的传播报告](../cases/ps5-ai-security-report.md) — 传播帖称 AI 加速 PS5 安全研究，未提供模型与技术过程。 **[未确认使用 REA · 待验证]**
- [空调协议：用 AR 眼镜手势控制家电](../cases/ar-air-conditioner-control.md) — 分析官方 App 请求，再把开关和调温控制接到 AR 眼镜。 **[REA · 待验证]**
- [红米电视：研究浏览器 APK，把闲置电视改成数据大屏](../cases/redmi-tv-dashboard.md) — Muse + Codex 分析电视浏览器与全屏行为，适配现有数据看板。 **[其他 AI 逆向 · 待验证]**
- [CF632BLE 体脂秤：在浏览器里称重，不走厂商后台](../cases/cf632ble-web-bluetooth.md) — Claude Code + ghidra-rpc 研究 BLE 协议，重实现 Python 与网页客户端。 **[其他 AI 逆向 · 待验证]**
- [Kindle：为运行微信读书制作 Android 固件](../cases/kindle-android-weread.md) — Codex 与 Claude 接力适配系统；作者报告设备已显示界面。 **[其他 AI 逆向 · 进行中]**
- [全屋联网设备：用 Codex + REA 做电脑控制端](../cases/rea-home-device-control-report.md) — 作者称分析自家设备后做电脑控制软件，型号未公开。 **[REA · 待验证]**
- [小米音箱：改固件接入 ChatGPT 语音的 idea](../cases/xiaomi-speaker-chatgpt-voice-idea.md) — 提出研究小米音箱固件，让设备支持 ChatGPT voice。 **[未确认使用 REA · 待验证]**
- [Kepler 显卡：为 AI 推理做逆向研究的计划](../cases/kepler-ai-inference-idea.md) — 计划研究旧 Kepler 显卡，使其用于 AI 推理。 **[其他 AI 逆向 · 待验证]**
- [散热器 LCD：逆向 USB 协议，做 Rust 状态屏](../cases/thermalright-cooler-lcd-rust.md) — 让 Thermalright 散热器屏幕在 Omarchy 显示温度与 AI 使用量。 **[其他 AI 逆向 · 待验证]**
- [相机固件：让 Codex 推进虚拟机启动研究](../cases/camera-firmware-vm-boot.md) — 研究自己的相机固件，使其能在虚拟机启动。 **[其他 AI 逆向 · 进行中]**
- [LG 电视：用 REA 核查隐私行为的 idea](../cases/lg-tv-ai-privacy-audit-idea.md) — 提出分析电视代码实际行为，检验数据采集与隐私说法。 **[REA · 待验证]**
- [Homatics 盒子：研究固件修复 Dolby Vision 绿屏](../cases/homatics-atv14-dolby-vision-fix.md) — 作者称修复 Box R 4K Plus 升 Android TV 14 后的偏色。 **[REA · 待验证]**
