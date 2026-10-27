# OtterSec的GoonFi V2研究：AI恢复Rust，整程序重编译约束与已披露的记账漏洞

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-27
阶段：待验证

历史来源是2026年10月16日20:08（北京时间）pashov对@osec_io的AI恢复Rust、hash-perfect重编译与Critical漏洞研究的泛化转述，当时未具名目标。10月27日15:19本窗口候选r1cksec明确提GoonFi V2。补读OtterSec的Renato Marziano、Robert Chen署名文章Breaking open a propAMM（页面日期10月15日），以及renato-osec/goonfi-v2-decompiled固定381cc31945474ba6b5b56b32a8cad5266602d612提交的README与VERIFY.sh，提交时间10月15日22:35:39北京时间。这些是窗口前补充材料，不是本轮新发布；沿用既有研究ID和pashov来源，不推断其早期泛称只指这一个目标。

目标是把Solana上闭源GoonFi V2做市程序恢复成可审计Rust。作者称Opus5.5作协调者，Astra子代理处理较小逆向任务，借助Binary Ninja、Solana分析工具、IDL与链上交易，按函数比较重编译指令，结合确定性检查与代理审核合并。只追求相似度会过拟合，因此限制不自然的编译技巧，库代码应通过依赖重现。文章明确逐函数100%匹配后，243k字节程序仍差约93k字节，需再处理函数顺序、指针表及panic路径／行号才能达到其所称hash-perfect；不能把局部零分匹配当整程序一致或唯一原始源码。

公开README限定原部署slot448984043，注明程序已在2026年10月6日升级修复报告问题。VERIFY.sh注释将旧部署定为9月21日、243080字节ELF，需要归档RPC重建旧部署，再构建并用cmp比较；当前线上dump不是旧目标。README另用beyond padding描述一致范围，本文没有独立重跑或解决其口径差异。验证材料可读不等于本合集已验出相同哈希。

作者报告恢复后审计发现依赖金库实时余额的记账／定价缺陷，可能危及610万美元，已负责任披露；风险金额不是实际损失，修复是项目说明，未检查当前合约或执行漏洞。原文章、公开源码与脚本补足了此前只有转述的证据，但本合集未编译、访问归档凭据、运行目标或复现资金风险。保持unverified，未确认REA，不能由此推断任意Rust程序均能恢复或闭源已普遍失效。

历史10月16日快照120赞、4339浏览、11转发；本窗口候选1赞、29浏览、0转发，热度不等于验证。
610万美元是作者报告的风险额，不是损失；原部署9月21日，README称10月6日已升级。
逐函数100%匹配不等于整库字节相同；源码与验证脚本已读，但未编译、重建归档或核对当前链上状态。

## 来源

- [历史：pashov对osec_io Rust研究的转述，2026-10-16](https://x.com/i/status/2111066785890054605)
- [本窗口：r1cksec介绍GoonFi V2的AI逆向，2026-10-27](https://x.com/i/status/2114980383414722716)
- [补充：OtterSec署名文章，页面日期2026-10-15](https://osec.io/blog/goonfi-decompilation/)
- [补充：10月15日固定README，原部署与升级边界](https://github.com/renato-osec/goonfi-v2-decompiled/blob/381cc31945474ba6b5b56b32a8cad5266602d612/README.md)
- [补充：同提交VERIFY.sh，归档重建与cmp流程，未执行](https://github.com/renato-osec/goonfi-v2-decompiled/blob/381cc31945474ba6b5b56b32a8cad5266602d612/VERIFY.sh)

[English](en/osec-ai-rust-hash-recompilation-report.md) | [返回目录](../README.zh-CN.md)
