# Civic安卓车机：Indra转述Crunchy-Nut1用Claude Code调查后台服务并清理18包

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-26
阶段：待验证

2026年10月26日23:32:45（北京时间），Indra（@IndraVahan）转述r/claudecode用户u/Crunchy-Nut1，把Claude Code连接到Honda Civic的中国安卓车机进行调查。帖称助手一直等待唤醒词，隐藏WebView在无人说话时占约30% CPU；蓝牙通话设备预装通话录音器，固件含厂商root后门，开机脚本会安装隐藏目录里的APK后删除文件，厂商更新器可远程推固件，百度定位和厂商日志收集器后台运行。另称商品标8核Android 15，实际4核Android 9、安全补丁2021年10月。均为二手报告，不据预装组件证明实际录音或外泄，也不独立确认硬件参数造假。

转述中Claude Code参与停用助手和其他应用、备份后移除18包、关闭所谓root后门和隐藏APK安装机制及厂商云更新器、设置AdGuard Private DNS、WebView从66升级至138、制作Civic launcher与图标、调整倒车摄像头辅助线，以及安装经SHA-256检查的开源App并限制网络。数量、版本和CPU占用保留为转述，不保证措施完整或安全；哈希检查也不等于信任软件作者。

补查X原帖确认转述账号和全文；Reddit用户公开帖子接口返回403，未取得原作者正文、车机型号、包名、启动脚本、日志、代码或道路测试。候选只指这一车机项目，不把Civic车辆控制系统也算已逆向。REA未提及，按unverified调查与改装报告收录，不运行代码、操作车辆或声称设备已无后门、无跟踪及完全安全。

候选快照：10赞、467浏览、1转发；不以补查时大幅增加的热度替换。
二手报告；Reddit公开接口403，未获得原始日志、代码、型号或实车验证。移除18包与版本升级不是完整安全审计。

## 来源

- [Indra转述Crunchy-Nut1的Civic车机调查与Claude清理，2026-10-26](https://x.com/i/status/2114742034183733424)

[English](en/crunchy-nut1-civic-claude-head-unit-audit-report.md) | [返回目录](../README.zh-CN.md)
