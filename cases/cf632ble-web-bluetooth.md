# CF632BLE 体脂秤：在浏览器里称重，不走厂商后台

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-12
阶段：待验证

guyru 希望直接使用自己的智能体脂秤，报告用 Claude Code 连接 ghidra-rpc 研究 BLE（低功耗蓝牙）协议，先写 Python，再改为 Web Bluetooth。对应 CF632BLE 仓库说明协议与体成分算法来自对 Unique Health 安卓 App 的分析，网页本地计算并保存测量记录，不依赖厂商后台。源码公开，作者称使用效果良好；本合集未连接设备或复核健康指标准确性。Web Bluetooth 需要 Chromium，Safari/iOS 不支持。

发帖：2026-10-12T16:48:02+08:00（北京时间）
热度快照（2026-10-12）：2 赞｜94 浏览｜0 转发

## 来源

- [本周期作者报告](https://x.com/guyru_/status/2109566754540392730)
- [公开实现与设备边界](https://github.com/guyru/cf632ble)

[返回目录](../README.md)
