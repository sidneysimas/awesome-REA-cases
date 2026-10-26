# Cloudflare security-audit：以覆盖账本与反驳Agent约束安全审计

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-26
阶段：相关项目

往期待补审候选于2026年10月26日03:36（北京时间）在五仓库周榜中介绍Cloudflare的security-audit。本轮找到准确公开项目cloudflare/security-audit-skill，补读固定c1c8a8c1471069fb0e188eeaff69b8e8db6564a8的README；提交日期为2026年9月14日19:28:54 UTC，属于更早的项目材料，不将周榜或本次阅读当发布日。其他清单项的推理、调优与求职不并入本案例。

项目用于让编程Agent系统研究仓库的架构、输入面与信任边界，建立architecture.md和coverage-ledger.json后，按覆盖单元分派隔离猎手，再由新验证Agent尝试反驳每个候选。随后生成confirmed、needs_validation和rejected三类结构化记录，再由独立Agent核对最终源码主张，才从记录和账本生成报告；复跑继续追覆盖缺口，不把旧证据或未解决工作算成已覆盖。

README将该Skill称为Cloudflare内部漏洞发现harness的单仓库起点，而非等同完整内部系统。它要求支持工具与并行子Agent的模型、Node.js校验器，以及对构建/测试/浏览器/模拟器等目标执行强制禁外网、清理环境、资源限额和限制写路径的操作系统沙盒；控制不足则保持needs_validation而不执行目标代码。新Agent复核不是本合集独立复现，结构校验也不证明发现一定成立。

项目称一次运行约找到重复运行总漏洞的一半，但没有在所读README中提供样本集和基准细节，不能当普遍检出率。其二进制、内存安全、协议与客户端等审计方向使之属于相关AI分析工具项目，REA未提及。本合集未安装Skill、启动子Agent、执行目标或重跑校验器，未确认任何具体漏洞或内部系统成效。

往期待补审工具项目；固定文档早于候选，周榜不当发布日期。
需要操作系统沙盒；Agent反驳、JSON校验与项目测试主张不等于独立漏洞验证，未安装或运行。

## 来源

- [往期候选：五仓库介绍中的Cloudflare security-audit，2026-10-26北京时间](https://x.com/i/status/2114440956242002315)
- [补充公开项目README，固定c1c8a8c，2026-09-14 UTC](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/README.md)

[English](en/cloudflare-security-audit-skill-verifier-workflow.md) | [返回目录](../README.zh-CN.md)
