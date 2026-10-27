# PicasaPy：Virág Attila以Ghidra、Claude与Codex重建Picasa3.9照片管理器

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-28
阶段：进行中

2026年10月28日03:13:47（北京时间），Virág Attila（@sanchomuzax）介绍PicasaPy：以Ghidra逆向Picasa3.9，用Claude和Codex构建Python/Qt开源重写，称已可运行。补查同名作者仓库确认Python、PySide6、Qt Quick照片管理/编辑项目，目标是继续使用Google已停止发展的Picasa式本地照片工作流。README说明共用.picasa.ini可读写非破坏编辑，但Picasa以后写入可能覆盖外部修改，并非无冲突实时同步；功能清单是项目说明，不等于逐项实测。

读取固定提交cd9a25459d73abe244f24ed07ff61b60bca32ca7的研究文档：方法页以Picasa3.9.141.259为对象，结合字符串、RTTI、资源与Ghidra线索；paritas-ellenorzes注明最初检查日期10月13日并包含后续修订，区分静态QML可达路径、真实点击与效果输出，保留缺失/占位项、平台差异及停服在线功能非目标等边界。文档里的108/138菜单路径是其特定静态快照，不能充当全功能点击通过率，也不能用文档初始日期代替所有修订日期。

公开CI run40573684760记录该提交成功，创建时间10月28日03:57:11北京时间，晚于候选但仍在本窗口，作为补充项目验证记录，不是另一个候选或本合集重跑。补查时最新提交2a689c1204df7209d0eb286cba186a6dec395fb6在04:03:51、窗口之后，不能冒充窗口内进度；不采用其待运行CI作通过证据。保留进行中重建，不称恢复原始源码、与Picasa所有效果一致、Google服务复活或独立复现；未安装依赖或运行项目。

候选快照0赞、13浏览、0转发；推荐依据是公开研究材料与可检查项目记录，不是高传播量。
文档与CI均为项目证据，未由本合集独立执行；窗口后的最新提交与排队CI不混作窗口内成果。

## 来源

- [Virág Attila的PicasaPy发布帖，2026-10-28](https://x.com/i/status/2115160045243814263)
- [公开仓库与README：项目定位及.picasa.ini边界](https://github.com/sanchomuzax/PicasaPy)
- [固定提交的二进制研究方法，含早于候选的研究背景](https://github.com/sanchomuzax/PicasaPy/blob/cd9a25459d73abe244f24ed07ff61b60bca32ca7/docs/specs/binaris-regeszet-modszertan.md)
- [固定提交的分层parity检查与限制，起始日期2026-10-13](https://github.com/sanchomuzax/PicasaPy/blob/cd9a25459d73abe244f24ed07ff61b60bca32ca7/docs/specs/paritas-ellenorzes.md)
- [补充：cd9a254提交的成功CI，10月28日03:57北京时间创建](https://github.com/sanchomuzax/PicasaPy/actions/runs/40573684760)

[English](en/picasapy-ghidra-claude-codex-photo-manager.md) | [返回目录](../README.zh-CN.md)
