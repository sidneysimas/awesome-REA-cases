# Kong：Ghidra上下文驱动的LLM符号恢复与XZ后门项目基准

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-29
阶段：分析测试

2026年10月29日07:58:40（北京时间），候选介绍Kong将去符号二进制中的FUN_00401a30命名成parse_http_header并恢复类型，询问读者是否信任这些名称。这是能力示意，不是提供了某HTTP程序的真实对照实验。按项目名补查amruth-sn/kong，固定提交8c4ee4bf52e0eb9efc3a0b22ad6da03387543fd2在2026年4月3日，README与BENCHMARKS是较早补证，不是本窗口新开发。

README描述通过PyGhidra/JPype进程内调用Ghidra，先分流、签名匹配和构建调用图，再自底向上将反编译、引用、字符串与已命名被调函数提供给LLM，做清理、语义统一和导出，回写Ghidra数据库。列Claude/OpenAI支持、类型/符号评分与去混淆；这些是公开项目设计与宣称，不能由文档直接认定所有架构和混淆都可靠，也不采纳“世界首个”的宣传。许可标Apache2.0，未安装依赖或执行代码。

同提交基准将目标称为XZ Utils5.6.1来源的去符号liblzma.so.5.4.1：枚举558函数、排队396、分析355；用claude-opus-4-6，报告15分钟与6.63美元。文档列308函数高置信、33中置信、14低置信，五个核心植入函数90%–95%置信，并称恢复RSA验证钩取、ChaCha20载荷链。置信度不是按源码对照的准确率，355/396不是所有函数完成，公开叙述也不是自动发现未知漏洞的独立证明。未核实样本来源/哈希、原始模型输出、费用或链条正确性，未下载或运行恶意样本；文件名按文档保留，不借其版本名推断普通5.4.1也感染。

候选快照0赞、4浏览、0转发；项目基准不是本合集执行结果。
项目自报558枚举、396排队、355分析，15分钟、6.63美元；90%–95%为置信度，不是独立准确率。

## 来源

- [候选：Kong符号恢复与类型推断介绍，2026-10-29](https://x.com/i/status/2115594128167940242)
- [较早固定提交README：分析管线与项目边界，2026-04-03](https://github.com/amruth-sn/kong/blob/8c4ee4bf52e0eb9efc3a0b22ad6da03387543fd2/README.md)
- [同提交BENCHMARKS：XZ样本、模型、费用与置信度](https://github.com/amruth-sn/kong/blob/8c4ee4bf52e0eb9efc3a0b22ad6da03387543fd2/BENCHMARKS.md)

[English](en/kong-ghidra-llm-symbols-xz-benchmark.md) | [返回目录](../README.zh-CN.md)
