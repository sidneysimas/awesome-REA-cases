# KakaSoft USB Copy Protection：AI追踪自定义哈希与受保护测试文件

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-25
阶段：分析测试

10月25日07:18:48（北京时间）的候选简述KakaSoft USB Copy Protection，补读窗口前Xusheng Li的官方研究文章（10月22日16:00 UTC）。作者在macOS让AI解包Windows安装器并分析5.6.0.299版，指出Normal档不加密，High档至多异或前16385字节且只有256种单字节key。Highest档标称256-bit Blowfish，作者选择它并用自有小文本在U盘上生成测试。

原文比候选“密钥写死”更具体：AI读取exFAT原始目录，定位隐藏且名称特殊的667字节测试文件，跟踪32位Delphi客户端的TBlowfishEncryption类，确认逐文件salt、IV与Blowfish-CBC布局。问题在于由内嵌seed经修改MD5产生固定内部口令，再经RIPEMD-128与salt导出文件密钥；AI模拟相关客户端代码恢复内部值，作者报告测试文件原始字节恢复成功。

作者给出安装器解包约2分钟、密码分析另7分钟且两提示词；提供受保护盘后约26分钟、六个简短提示完成隐藏文件提取、修改哈希恢复及无用户密码解密的证明。这些是人工指导的作者报告，不是通用速度或所有版本结果。未独立运行样本、访问盘或重放解密，不转载内部口令；AI型号和REA未明确，不能把原文的AI写成所有阶段均为Codex。

原文针对5.6.0.299与自有测试；2+7分钟静态阶段和后续26分钟不可混作一段端到端工时。

## 来源

- [窗口候选：KakaSoft保护缺陷转述，2026-10-25](https://x.com/i/status/2114134544836407379)
- [窗口前Xusheng Li原研究：KakaSoft完整流程，2026-10-22 UTC](https://binary.ninja/2026/10/22/breaking-more-encrypted-usb-drives-with-ai.html#kakasoft-usb-copy-protection)

[English](en/kakasoft-usb-copy-protection-ai-review.md) | [返回目录](../README.zh-CN.md)
