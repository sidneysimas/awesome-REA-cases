# PlainMount：REA研究NTFSTool，为旧硬盘做原生Mac读写工具

分类：应用与客户端 · REA
记录日期：2026-10-28
阶段：进行中

2026年10月28日18:03:02（北京时间），Laplaced（@0xlaplaced）报告找到2008年的512GB Transcend硬盘，先无法访问，后来只能读不能写。AI Agent将问题定位到macOS的NTFS支持；作者不想为所试工具付费，于是让Agent以REA研究NTFSTool，再围绕既有NTFS组件写原生Mac应用PlainMount。作者称在这块真实硬盘上测试读、写和重连，公开源码及下载版，个人使用免费、无需账号或订阅，限Apple Silicon与macOS14以上。旧MEW钱包文件只是发现硬盘内容的背景，不是密钥恢复或资金找回结果。

补读同作者0xlaplaced/PlainMount固定提交a984a55236f1bd24f344b0adddc5be96644f7c87的README，提交于同日18:11:15，晚于候选帖但仍在本轮窗口内。文档列出卷信息、Finder打开、只读挂载、弹出与打包后端写入；1.0.5 arm64下载包为ad-hoc签名、未经Apple公证，写入涉及Full Disk Access与管理员批准。默认源码构建只有检查和标准只读操作；下载包另带NTFS-3G、libfuse与FUSE-T，不能把应用的MIT许可扩展到整包：前两者分别GPL、LGPL，FUSE-T仅非商业免费，商业使用需另行许可。

项目文档称会在磁盘操作前重新核对身份，不保存管理员密码、不装永久特权服务、不格式化或强制卸载；这些是设计声明，不是本合集安全审计。核心测试使用合成数据，不能替代真实磁盘写入验证。没有NTFSTool版本、REA分析日志、逐功能对照、数据完整性或多设备长期测试；读写重连仍是作者报告，不是新NTFS驱动、完整功能等价或独立复现。本合集只静态阅读，未下载应用、访问钱包或操作磁盘。

候选快照0赞、83浏览、0转发；读写与重连只在作者一块512GB旧盘报告。
应用MIT不等于写入整包MIT；未公证、权限与第三方非商业条款须分别考虑。

## 来源

- [Laplaced的REA／NTFSTool到PlainMount报告，2026-10-28](https://x.com/i/status/2115383833570758955)
- [公开PlainMount源码仓库](https://github.com/0xlaplaced/PlainMount)
- [同日18:11:15固定README：构建、许可与测试边界](https://github.com/0xlaplaced/PlainMount/blob/a984a55236f1bd24f344b0adddc5be96644f7c87/README.md)

[English](en/laplaced-plainmount-rea-ntfstool-macos.md) | [返回目录](../README.zh-CN.md)
