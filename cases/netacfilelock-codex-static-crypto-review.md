# NetacFileLock：Codex七分钟静态复查文件加密的研究者报告

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-25
阶段：分析测试

10月25日07:18:48（北京时间）候选转述NetacFileLock调查，补读Xusheng Li的Binary Ninja官方文章（10月22日16:00 UTC，北京时间23日00:00）。这是一项窗口前研究的窗口内传播，不是本合集复现。作者此前已用TTD研究该文件加密工具，这次用一个提示词让Codex通过Binary Ninja MCP检查密码系统，称约七分钟静态分析便定位可执行文件内固定32字节AES-256密钥，用户密码检查与文件密钥无关。

作者还报告诊断日志写用户密码、独立16字节块的ECB式行为、MD5密码校验与无密钥MD5文件签名、SM4另一固定密钥。fast模式对大于1024字节文件仅部分加密，解决了其此前测试文件仅三分之一加密的疑问，非PDF独有。没有将七分钟推广为所有工具的恢复时间；没有记录模型版本、完整调用轨迹或独立对照。

结论是该研究者所分析软件的密钥管理与密码脱钩，不是AES-256算法本身被破解，也不能直接涵盖朗科全部产品。未下载样本、执行工具、访问用户日志或解密数据，不转载密钥；REA未被提及。

七分钟、一个提示词及附加发现均为研究者自述；本合集只读原文，未独立测试。

## 来源

- [窗口候选：NetacFileLock的Codex分析转述，2026-10-25](https://x.com/i/status/2114134544836407379)
- [窗口前Xusheng Li原研究，2026-10-22 UTC](https://binary.ninja/2026/10/22/breaking-more-encrypted-usb-drives-with-ai.html#breaking-netacfilelock-again)

[English](en/netacfilelock-codex-static-crypto-review.md) | [返回目录](../README.zh-CN.md)
