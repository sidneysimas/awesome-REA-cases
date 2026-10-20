# xbox-boot-re：从单张 BIOS 恢复初代 Xbox 开机动画

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-20
阶段：进行中

10月20日15:30（北京时间），候选目录更新介绍bennyborn/xbox-boot-re：从一张1MB BIOS恢复初代Xbox的绿色球体、场景、标志与声音，再提供可独立运行的渲染器。补读固定提交12a3396的README，项目明确分析、规格与重建主要由Claude Code中的Opus 5.5完成，人类持续决定方向并审阅，并非无人参与。输入是作者自有改机导出的Complex 4627 Retail (1.0)修改版BIOS，不是未经修改的零售原厂dump；没有覆盖其他BIOS版本。

项目报告时间、相机、几何、球体、纹理及GPU命令流与xemu录制运行逐位匹配，声音序列器及DSP程序逐字匹配；音频声部合成则依据xemu对未充分文档化硬件的理解作近似，不能称所有音频或最终像素均原生精确。重建是可编译为本机及wasm32的C核心，WebGPU前端另加自由相机、线框和Next Gen视觉改编，不是完整Xbox模拟器。仓库提供规格、向量与测试代码；10月16日05:08开始的该提交构建和Pages部署CI均成功，这证明项目流水线通过，不等于本合集复跑BIOS对照或实机验证。

原提交为10月16日05:06（北京时间），是本轮候选引出的补充历史材料，不是10月20日新完成的研发。README注明数据目录含Microsoft原有几何、采样与表格，其权利不因AI重建改变；重做研究需自备合法BIOS。本合集只阅读文档、测试布局与CI状态，未下载BIOS、执行目标代码或观看完整演示。

10月20日候选快照0赞、46浏览；26星为该帖转述的目录快照，未独立核数。

## 来源

- [10月20日候选：xbox-boot-re目录介绍](https://x.com/i/status/2112446312104825271)
- [10月16日固定提交README：AI归因、匹配范围与数据权利](https://github.com/bennyborn/xbox-boot-re/blob/12a3396aa77f72c8d2fd94c0988c7e11539b47e7/README.md)
- [同提交核心文档：接口、测试布局与未重建状态](https://github.com/bennyborn/xbox-boot-re/blob/12a3396aa77f72c8d2fd94c0988c7e11539b47e7/docs/core.md)
- [项目CI：构建与Pages部署成功，非独立复现](https://github.com/bennyborn/xbox-boot-re/actions/runs/38807512169)

[English](en/xbox-boot-re-claude-reconstruction.md) | [返回目录](../README.zh-CN.md)
