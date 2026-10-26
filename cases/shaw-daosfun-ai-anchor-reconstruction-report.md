# daos.fun：wei转述Shaw以AI重建Anchor合约与同哈希二进制

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-25
阶段：待验证

2026年10月25日13:02:23（北京时间），wei（@8853wei）转述Shaw（@shawmakesmagic）10月24日对daos.fun的研究。目标是理解部署在Solana链上的闭源程序：从链上取得程序，再借助AI重建为Anchor源码。帖子称重编译后的1120784字节二进制与部署版本逐字节一致且SHA-256相同，代码和审计已放GitHub。

同一转述称审计有一项critical、四项medium和一项low；critical涉及DAO与资金池缺少绑定，可误导迁移费用并破坏另一DAO的状态，并将“影响新发起、而非已bonded项目”的范围归于Shaw。这里仅概述作者报告的问题类型，不提供调用或利用步骤。私密安全赏金和Umia是文中的后续建议，不作为独立逆向项目，也不证明漏洞已被确认或修复。

10月26日补查原帖确认转述作者；公开仓库检索没有定位到可核验的原重建与审计提交，因此不猜测仓库或合约地址。AI参与、字节长度、同哈希和审计等级均保留为wei转述Shaw的主张；未获取链上目标、重编译、重算哈希或测试任何资金操作。不将这条记录与未指明合约的pump.fun或OpenSolana概括自动合并，也不将源码可读等同任意合约都能安全还原。

二手转述，1120784字节、同哈希及1 critical/4 medium/1 low均未独立核验。
原重建仓库、审计提交和链上地址未确认；未进行链上操作。

## 来源

- [wei转述Shaw的daos.fun重建与审计，2026-10-25](https://x.com/i/status/2114221010853781864)

[English](en/shaw-daosfun-ai-anchor-reconstruction-report.md) | [返回目录](../README.zh-CN.md)
