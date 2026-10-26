# 旧磁盘镜像：bitplane用客体VM读取历史系统，并保存重建工具链

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-24
阶段：待验证

2026年10月24日17:05:27（北京时间），davidsong（@bitplane）将客体VM挂载旧磁盘镜像的工具列入AI成果清单，目的是让历史研究者访问原系统已无法启动的冷门镜像。他称在Linux构建并用QEMU运行MacOS、RISC OS、TempleOS及另外七种系统，也称无需Mac SDK构建Darwin；配套有跨平台9p服务器和测试数据用Rust mkfs工具。

补查mountin公开README，最后修改于2026-09-25，早于本窗口。它使用客体内核和文件系统驱动，经9p暴露读写，采用rootless Podman构建并宣称归档源码、输出与容器。文档给出Linux、NetBSD、AROS、PureDarwin等格式矩阵及项目端到端测试声明，但明确unstable/pre-alpha/experimental，客体选择、检测与启动层仍在建设；已知部分NTFS、UFS、SysV路径会失败或使客体崩溃，必须先备份镜像。不是任意镜像安全自动挂载的承诺。

未提供具体AI分工；本合集未下载镜像、运行挂载、重建系统或核实归档完整性，保留未验证状态。MacOS与无需SDK等表述只归作者，不把既有系统、文件系统驱动或QEMU归功于AI。

项目明确实验性、应先备份；已知驱动失败或客体崩溃。格式矩阵与归档为项目报告，未运行或核实归档。

## 来源

- [bitplane的旧磁盘镜像与VM工具自述，2026-10-24](https://x.com/i/status/2113919789886218477)
- [补充mountin README，最后修改2026-09-25](https://github.com/bitplane/mountin/blob/11aa2dba490ac0a234c763388dd7c30e8aa83d36/README.md)

[English](en/bitplane-ai-obscure-disk-vm-mount.md) | [返回目录](../README.zh-CN.md)
