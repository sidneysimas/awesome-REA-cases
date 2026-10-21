# DecompPipeline：用受限 Haiku 与行为 oracle 重建 Dreamcast 函数

分类：游戏与游戏保存 · 其他 AI 逆向
记录日期：2026-10-21
阶段：进行中

2026年10月21日15:30（北京时间），yibie的目录更新介绍GeneralAtrox/DecompPipeline，关注小模型Haiku能否在严格流程中完成游戏函数反编译。补查公开仓库，固定70b248a5提交日期为10月19日09:20（北京时间），早于本轮窗口，只作为背景与实现核查。当前目标为Dreamcast SH-4，每款游戏使用自己的项目工作区，仓库不含游戏数据。

README描述受限claude -p会话读取汇编、Ghidra结果与上下文后写C，机器判定PASS／FAIL而非接受Agent口头成功。Ghidra p-code模拟原函数，默认96个输入分为48开发、48隐藏向量，对照返回值、原函数写入的内存字节、调用目标／次序／参数及SH-4额外寄存器状态；被调函数采用mock。候选用MSVC编译，因此这里的byte-exact是所测行为的字节结果相同，不是用原编译器复现原始指令。文档另设覆盖率与突变检查，不能把有限输入的通过当完整语义证明。

固定提交的core/oracle_stamp.py确认harness戳记包含脚本、facts、函数地址、向量数、hints、目录与二进制指纹等输入；current还检查callee记录是否与被调函数自身harness签名一致。它解决旧测试夹具冒充当前证据的问题，但戳记不是判定器正确性或实际游戏兼容性的证明。未获得本次端到端运行记录，也未运行目标或安装依赖。目录帖17星只属其发布快照，不是本合集独立核数；REA工具使用未明示。

## 来源

- [yibie：DecompPipeline目录更新与输入戳记](https://x.com/i/status/2112808681918337410)
- [10月19日固定提交README：Haiku流程、96向量与行为判定边界](https://github.com/GeneralAtrox/DecompPipeline/blob/70b248a5ade720b469716c39ec6da0db0953f5a4/README.md)
- [相同提交core/oracle_stamp.py：输入与callee签名检查](https://github.com/GeneralAtrox/DecompPipeline/blob/70b248a5ade720b469716c39ec6da0db0953f5a4/core/oracle_stamp.py)

[English](en/decomppipeline-haiku-behavioral-oracle.md) | [返回目录](../README.zh-CN.md)
