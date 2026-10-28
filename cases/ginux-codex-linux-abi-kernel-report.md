# Ginux：Codex在人的架构与验收约束下重建Linux用户态兼容内核

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-28
阶段：进行中

2026年10月28日18:11:05（北京时间），corleone jack（@jackcorleone19）转述Gregory Kurtzer的Ginux：一个Codex任务持续11天，约13.9万行代码，独立实现Linux二进制接口而非Linux分支，Rocky Linux10启动到systemd。作者用HDAE称呼人定架构、约束、里程碑、验收与停止点，Agent写、启动、测试和排错的分工。按AI辅助兼容行为重建项目收录，不是恢复Linux原始源码，也不推断反编译过Linux。

10月28日补读gmkurtzer/ginux公开README，项目说明一个Rust优先x86-64内核直接经UEFI启动，Linux用户态运行在原生domain里，不依赖底层Linux宿主内核。文档确认一项持续OpenAI Codex任务使用GPT-5.6 Sol、11天保留约139000行实现和测试代码，并明确论文评估的是10月23日d11c126a048a51fe7eb9c4105f31760add1027ea，而非后来仓库全部变化。本轮只读项目文档，未查看或重跑论文测量。

README称特定Q35/OVMF、Intel IOMMU与virtio的QEMU配置中，部分Alpine和Rocky程序可运行，Rocky10 systemd到multi-user.target；Linux6.12的375个syscall中82完整、245部分、48按策略拒绝，分类穷尽不等于兼容完整。聚合make test并非全通过，保留post-execve系统监督器生命周期探针失败。硬件、隔离、持久化、网络和安全验证仍不完整，未独立审计，无物理硬件覆盖或生产替代Linux的保证。不能将11天、行数或一个启动路径写成任意Linux软件都能运行；REA未提及，本合集未编译、启动或安装目标依赖。

候选快照0赞、14浏览、0转发；11天与139000行是项目报告，含测试代码。
syscall分类82/245/48及systemd启动是文档状态，不是独立测试或发行版全面兼容。

## 来源

- [corleone jack转述Ginux／Codex研究，2026-10-28](https://x.com/i/status/2115385859633475649)
- [补充：Ginux公开README、验证边界与研究说明，10月28日读取](https://github.com/gmkurtzer/ginux)

[English](en/ginux-codex-linux-abi-kernel-report.md) | [返回目录](../README.zh-CN.md)
