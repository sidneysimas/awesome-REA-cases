# 初代文明 civd：AI 辅助重建，四字节启动修正后通过项目哈希验证

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-21
阶段：进行中

2026年10月20日23:22（北京时间），Xiao Tan（tvytlx）转述1991年初代《文明》DOS版的AI辅助重建。10月21日13:08及13:09，Jimmy Young（jimmyyangrz）的两条候选进一步点名Steve Melia及旧工具链、命名推断和内存限制。补查公开sjmelia/civd仓库后，修正此前仅能描述四字节差异、未定位代码的证据边界：现在有可检查的源码、技术书、构建规则与项目CI，但仍非本合集独立复现。

固定6dff0891提交于10月20日03:02（北京时间），早于本轮候选窗口。README说明使用OpenAI、Anthropic、Google模型编写代码与文档，再编辑并做构建验证，明确依赖前人OpenCiv1；此前转述也承认前人代码可能在训练数据中，因此不能宣称完全从零、无已有实现影响。命名、注释和部分类型是推断，字节匹配不证明找回MicroProse原始源码。项目另指向现代平台重建reciv，本记录没有验证该移植的运行效果。

同提交的构建说明与justfile使用Microsoft C 5.1、MASM 5.10、LINK 5.01和MAKE 4.07。CONTROL.C与CITYMGT.C用loadfix -192限制编译内存，因为可用内存和标识符拼写都会影响生成布局。原始链接产物保留为CIVRAW.EXE；CRTEDIT检查长度、CRC与预期字节后修改一处far call的四个目标字节，再检查结果，最终产物为CIV.EXE。该调用从运行库环境初始化改到立即返回的empty_hook，原版为何绕过初始化仍未知。因此四字节是明确的构建后修正，不应继续写成最终产物仍有四字节未匹配。

just verify干净构建后按仓库固定SHA-256检查原始链接输出、最终CIV.EXE 474.05、MCGA图形驱动、AdLib声音驱动和MISC.EXE。GitHub Actions运行39505519022对应6dff0891，于10月21日06:05（北京时间，本轮之前）创建，verify作业与安装工具／校验／文档步骤均成功；工作流明确调用just verify。这是项目自己的固定哈希与CI证据，不是本合集重新取得原版作哈希对照或游戏测试。

Jimmy的候选另称120个源文件中44个C、7个汇编，断续数月使用三家约15英镑每月档位且额度未用满；这些仍是转述，未独立清点文件或核账，不能写成项目总费用或精确工时。REA未明示。目标是可读实现与游戏历史保存，不是《文明VI》的策略AI；本合集未执行目标、安装旧编译器或核定资产与源码的法律来源。

## 来源

- [原有来源：Xiao Tan的工具链与四字节差异转述](https://x.com/i/status/2112565000372101178)
- [10月21日13:08 Jimmy：Steve Melia与DOS文明重建](https://x.com/i/status/2112773003981594700)
- [同作者13:09：文件数、命名与内存限制转述](https://x.com/i/status/2112773213134745743)
- [补充旧提交6dff0891 README：AI归因与重建边界](https://github.com/sjmelia/civd/blob/6dff0891f163827b40911c048d2f0715be06dd39/README.md)
- [同提交构建说明：内存与四字节调用修正](https://github.com/sjmelia/civd/blob/6dff0891f163827b40911c048d2f0715be06dd39/book/src/architecture/toolchain_clues.md)
- [同提交justfile：干净构建与固定哈希检查](https://github.com/sjmelia/civd/blob/6dff0891f163827b40911c048d2f0715be06dd39/justfile)
- [10月21日06:05同提交成功项目CI](https://github.com/sjmelia/civd/actions/runs/39505519022)
- [同提交工作流：verify作业的实际命令](https://github.com/sjmelia/civd/blob/6dff0891f163827b40911c048d2f0715be06dd39/.github/workflows/build.yml)

[English](en/civilization-dos47405-ai-reconstruction-report.md) | [返回目录](../README.zh-CN.md)
