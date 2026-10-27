# 仿AirDrop的Mac/Windows传输：Opus写Electron应用，非Apple协议兼容证明

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-28
阶段：待验证

2026年10月28日01:14:27（北京时间），作者称用Opus5.5逆向Apple AirDrop，让Mac与Windows直接传文件，不需云、账号或线缆。可见步骤是Claude Code在空目录选择Electron，局域网每1.5秒UDP广播发现，直接流传文件，接收端Accept/Decline并可总是接受自有设备。具体用途是跨平台本地分享，不据标题认定可与系统AirDrop互通。

作者报告先以两个假设备测试文件夹与3MB文件逐字节一致，Agent分别做iOS17 NameDrop式WebGL光效、图标及网站，审查发现Mac黑屏shader问题，GitHub Actions打包dmg/exe；首次Mac启动只有图标跳动，添加启动日志与强制开窗后下一构建能打开。一个下午、零手写代码和成功传输均为自述。未取得仓库、测试记录或包，未证明Apple发现/加密协议恢复，也未评估总是接受的安全性；按功能体验重建报告收录，未运行应用。

候选快照55赞、2051浏览、1转发；1.5秒、3MB和一个下午均来自作者。

## 来源

- [Opus/Electron跨平台文件分享构建自述，2026-10-28](https://x.com/i/status/2115130015260291145)

[English](en/opus-electron-airdrop-like-local-transfer.md) | [返回目录](../README.zh-CN.md)
