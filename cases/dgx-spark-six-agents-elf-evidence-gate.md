# DGX Spark 上的六 Agent ELF 分析：用 nonce 与原始字节约束结论

分类：应用与客户端 · REA
记录日期：2026-10-21
阶段：分析测试

2026年10月21日17:36（北京时间），Nikolaos Chrysaidos（@virqdroid）介绍在一台 DGX Spark 上分析 ELF 可执行文件的六 Agent 实验。作者称所有 Agent 共用本地 Qwen3.8 Flash Next NVFP4，经 hub 的 gate 调度，容器内无网络、不使用云端模型。每个 Agent 得到 REA skill，分别负责初筛、静态分析、字符串与 IOC、密码与配置、行为、报告。重点是防止待分析二进制中的恶意文字冒充可信发现。

按作者描述，只有带真实工具调用及样本无法预知 nonce 的发现才被接受，hub 再用自己保存的原始字节核查。帖子报告70条提交、52条 verified（其中22条 byte-checked）、12条 rejected、18条 unconfirmed 且不入报告；后三组相加为82而非70，未解释是否重试、重叠或不同计数阶段，不能整理成互斥通过率。作者称视频是完整运行，但未提供可核对的样本哈希、项目仓库、分类日志或独立复测。verified 是该系统的标签，不等于全部做过字节核对或语义正确，更不等于已证明抵抗提示注入。补查原帖确认作者；本合集未执行 ELF 或实验。

来源更新：2026-10-21T17:36:56+08:00；保留70／52／22／12／18原始统计及口径限制。

## 来源

- [Nikolaos Chrysaidos：六 Agent 本地 ELF 实验及计数](https://x.com/i/status/2112840552240566508)

[English](en/dgx-spark-six-agents-elf-evidence-gate.md) | [返回目录](../README.zh-CN.md)
