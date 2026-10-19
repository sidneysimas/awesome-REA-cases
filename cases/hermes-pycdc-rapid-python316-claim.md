# pycdc-rapid：Hermes 用户称 Agent 私改支持 Python 3.16 反编译

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-19
阶段：待验证

10月19日22:59（北京时间），@wyant_dalto 回复称为Hermes Agent配置Ghidra以研究软件，并添加pycdc-rapid这一Python反编译工具。作者说原工具只处理3.15，Agent做了某种个人更新后现在可以反编译3.16。具体目标是扩展反编译工具对Python字节码版本的支持，而不是重建Python解释器。

补读原帖确认作者与原文中的3.15、3.16，按原样保留，不据此确认Python发行状态或上游兼容范围。没有fork、提交、字节码样本、反编译输出、语法或行为回归测试，不能认定完整支持3.16。作者使用Hermes不等于使用REA，帖子反而表示已转向自行接工具；其对REA无用的评价不是本合集结论。

## 来源

- [Hermes用户的Ghidra与pycdc-rapid个人修改自述](https://x.com/i/status/2112196958039535665)

[English](en/hermes-pycdc-rapid-python316-claim.md) | [返回目录](../README.zh-CN.md)
