# Brother 扫描按键：Claude + REA 把 Scan to PC 接到 NAS 与对象存储

分类：硬件与设备互通 · REA
记录日期：2026-10-18

10月18日18:39（北京时间），@aurimasniekis 说为父母的 Brother 打印机逆向 Scan to PC 按键应用，让扫描直接进入 SMB、FTP、S3 或本地目录，不再需要常开装有 Brother 软件的个人电脑。作者自述 Claude + REA 参与，约一小时解决需求，没有继续深入打印机固件。这里仍需要运行 Go 服务的主机或 NAS，不是打印机脱离服务器直接上传。

补读同日作者串与公开 README：项目从 macOS Push Scan Tool 2.3.1 的 NETserver、BRPhoenixConnection，以及 Linux brscan5 的 libLxBsScanCoreApi 研究协议，后者注明 REA 与 Ghidra；扫描命令处理建立在前人 brother-scand 上，另参考 sane-airscan。服务通过 HTTPS／SNMP 注册为可选电脑，接收 UDP 54925 按键事件，再通过 TCP 54921 获取面板选项与扫描数据。作者报告保留 PDF、多页 TIFF、JPEG 与彩色／灰度／黑白选择，另有历史下载和自定义扫描网页。

README 明确只测试 Brother MFC-L2800DW、固件1.32；其他机型是兼容预期。它列出 amd64、arm64、armv7 镜像和约13MB体积，均为项目说明而非本合集构建结果。OCR 文字格式会回退 PDF，不运行文字识别；PDF/A、加密与签名 PDF 也保存为普通 PDF。公开文档与实现仓库已找到，但未运行目标、镜像、集成测试或真实扫描，不能保证所有目的地、分辨率和机型通过，也不能将软件互通写成固件破解。

10月18日候选快照：主帖0赞、18浏览；不是独立扫描验证。仅项目报告MFC-L2800DW固件1.32测试；约一小时与13MB是作者／项目数值。
GitHub API显示仓库创建于10月17日19:47 UTC，即北京时间10月18日03:47；仓库文档为补充核验，不另当新候选。

## 来源

- [Aurimas Niekis 的 Claude + REA 扫描按键报告](https://x.com/i/status/2111769060631609593)
- [同串：约一小时、三架构镜像与测试机型](https://x.com/i/status/2111769069020176520)
- [同日补充：注册、UDP事件与扫描协议来源](https://x.com/i/status/2111769064590970940)
- [同日补充：面板格式与网页界面](https://x.com/i/status/2111769066360766602)
- [公开 Go 项目与 README：兼容范围、协议和前人工作](https://github.com/aurimasniekis/go-brother-scan-to-network-server)

[English](en/brother-scan-button-claude-rea-server.md) | [返回目录](../README.zh-CN.md)
