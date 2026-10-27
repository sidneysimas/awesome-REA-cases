# 旧iPhone备份审计：Borya称Claude还原照片索引，REA追查cleaner的MobileSync访问

分类：应用与客户端 · REA
记录日期：2026-10-27
阶段：待验证

2026年10月27日18:10:40（北京时间），Borya | Official（@BoryaOfficial）称在一次普通iPhone备份期间让Claude Code检查Windows笔记本风险，发现MobileSync\Backup中三份旧手机备份，最早2020年，共152GB、196530个随机文件名且无扩展名的文件，均未加密码。他说自己一直关闭iCloud Photos，所以备份保留当日相机胶卷以及iMessage、WhatsApp聊天照片。以上均为作者对其环境的描述，不推广到所有Windows备份。

作者报告Claude读取备份索引恢复照片身份，并将旧备份与新备份比较，找到5207张已不在手机上的照片。这是从旧备份找回仍保存的数据，不是证明恢复了磁盘上已安全擦除的文件。他又称Claude写了本地OCR脚本，仅返回命中文件名，找到护照、银行卡截图、证件照和12词钱包助记词相关内容；没有披露这些敏感值，本合集不索取或访问。作者说无照片离开笔记本，但这不是本合集验证过的完整数据流保证。

安全检查部分列出两个PC cleaner、PDF转换器、旧VPN和一个游戏启动器共五个程序；作者称REA打开五者，在一个cleaner中找到MobileSync字样，Process Monitor显示该程序每次启动会进入备份目录。这支持的仅是作者报告的字符串与访问观察，不证明它上传了照片、窃取了助记词或两年持续外传。完整长帖与署名已补查，作者说稍后会置顶一条检查prompt；本合集未取得该prompt、脚本、二进制名、抓包或Process Monitor日志。按unverified收录具体备份索引分析与程序审计流程，未独立复现。

候选快照1赞、197浏览、1转发；5207照片、三备份、152GB及196530文件均是作者数值。
访问备份目录不等于已证明外传；没有读取或公开任何证件、银行卡或钱包秘密。

## 来源

- [Borya的Claude/REA备份恢复与cleaner访问报告，2026-10-27](https://x.com/i/status/2115023366792839466)

[English](en/borya-iphone-backup-claude-rea-cleaner-audit.md) | [返回目录](../README.zh-CN.md)
