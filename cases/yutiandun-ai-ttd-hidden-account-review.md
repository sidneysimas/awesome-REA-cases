# 御天盾加密U盘：Xusheng Li的AI辅助TTD与隐藏账号调查

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-25
阶段：分析测试

10月25日07:18:48（北京时间）的候选转述Xusheng Li对四种U盘保护产品的调查。本条只记录SecZure的YutianDun（御天盾）。补充阅读Binary Ninja官方10月22日文章，原页面时间为16:00 UTC，即北京时间10月23日00:00；这是窗口前研究来源，不冒充本轮新实验。

御天盾通过附带阅读器展示加密文件并试图阻止复制、截图和打印。Li此前2024年研究过复制保护；本次称在AI帮助下使用time-travel debugging，发现阅读器钩住NtCreateFile/NtReadFile提供明文，并继续分析密码系统。作者报告管理员密码用于解包内容identifier，后者导出文件AES密钥；两个不在管理界面显示的内置账号各有相同内容identifier的包裹副本，固定密码可在其测试的两只盘上解包并解密文件。

作者从技术意义称之为backdoor，明确不推定恶意动机；这不是破解正常AES，也不是单凭MD5或64bit密钥熵推定暴力破解可行。本合集未取得样本、运行工具或解密文件，不转载固定口令或密钥；模型和AI逐步贡献未详列，REA未提及，保留作者测试与独立复现的区别。

原研究10月22日16:00 UTC（北京时间10月23日00:00）；候选10月25日07:18:48仅为转述。
两只盘与AI辅助TTD为研究者报告；未独立测试，不推定故意后门或全部版本受影响。

## 来源

- [窗口候选：四种USB保护产品调查转述，2026-10-25](https://x.com/i/status/2114134544836407379)
- [窗口前Xusheng Li原研究：Binary Ninja博客，2026-10-22 UTC](https://binary.ninja/2026/10/22/breaking-more-encrypted-usb-drives-with-ai.html#a-copy-protected-usb-drive)

[English](en/yutiandun-ai-ttd-hidden-account-review.md) | [返回目录](../README.zh-CN.md)
