# Decepticon Reverser：把 REA/Ghidra 静态证据接进授权安全调查

分类：应用与客户端 · REA
记录日期：2026-10-18
阶段：相关项目

2026年10月18日01:28（北京时间），@chaitanyamkj 介绍Decepticon安全Agent项目，称其Reverser能接REA/Ghidra，编排16种专家，XBOW通过102/104。补读BitterSecurity/Decepticon公开README与专门逆向文档，确认这是授权范围内的安全调查系统，而非Adobe重建工具。仓库main当时对应0647e8bd24110960a8c8e3654a8a944647bee3d0，提交于10月17日19:34北京时间；仓库材料用于核对实现边界，不作为窗口内另一个候选。

文档指定REA 6.3.0、Ghidra 12.1.4。Reverser对工作区已有二进制先检查状态，再发现该会话工具及schema并调用；网关在向Agent返回前保存原始Evidence与完整性manifest，绑定分析字节。它不替代Ghidra反编译器，不意味着安装其他provider。文档明确静态结果不证明运行时路径执行，也不保留用户编辑的Ghidra工程；不可用时退回本地radare2与分诊工具。

README确有XBOW总102/104、困难7/8的项目成绩表，不能当成本合集复测、任意目标攻破率或REA逆向正确率。候选介绍的多Agent、数据库与沙盒是系统架构，不是某个二进制被成功恢复的证据。本合集仅读文档，没有启动Agent、执行攻击、安装依赖或运行目标。

候选2026-10-18 01:28；补充仓库提交2026-10-17 19:34，北京时间。
项目文档说明REA 6.3.0/Ghidra 12.1.4与Evidence留存；静态分析不证明运行时路径。
XBOW 102/104、困难7/8仅为项目渗透测试成绩；未独立复测，不代表逆向正确率。

## 来源

- [窗口候选：Decepticon 与 Reverser 介绍](https://x.com/i/status/2111509697211806150)
- [公开仓库与项目基准说明](https://github.com/BitterSecurity/Decepticon)
- [固定提交：REA 逆向集成与静态分析边界](https://github.com/BitterSecurity/Decepticon/blob/0647e8bd24110960a8c8e3654a8a944647bee3d0/docs/features/rea-reversing.md)

[English](en/decepticon-reverser-rea-project.md) | [返回目录](../README.zh-CN.md)
