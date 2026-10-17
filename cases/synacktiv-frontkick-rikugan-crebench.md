# Frontkick 与 Rikugan：两项密码二进制任务中的提示词混杂因素

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-18
阶段：分析测试

2026年10月18日00:17（北京时间），@MalwareBibleJP 介绍Synacktiv的Frontkick/Rikugan比较。本轮补读Matthieu Breuil于10月13日发表的原文，用于核对实验而非冒充窗口内新发布。目标是从去符号密码二进制识别算法和密钥，重新实现解密并取得flag。作者从CREBench选AES-128-CBC与ChaCha20，在hardcode_plain、O0条件下，以Claude 5.5 Sonnet为每种工具各跑每题四次，设累计输入输出100万token预算；不是全套基准评测。

Rikugan通过预定义工具与参数校验操作；Frontkick直接在Binary Ninja的Python环境运行生成代码，无逐动作schema校验。后者将已安装库与已打开二进制信息放入初始提示，旧于最近四轮的内容截到500字符，满上下文时压缩历史，并在代码报错时检索由Opus 5.5生成、经项目验证的Python示例。文章同时指出频繁截断影响提示缓存，计划改进；文中没有提供Frontkick下载入口。

原文笼统称Frontkick约省一半token、得分近三倍。按公开八次表逐项计算，token总量比约0.634，平均得分为85.9375/100对31.25/100，不能写成三倍成功次数。Frontkick第一轮AES仍耗1,007,262 token、42轮、得分0；Rikugan八次中六次超过100万token，预算并非未越界的硬保证。Rikugan反复尝试未安装的pycryptodome，未利用现有cryptography；Frontkick因明确库列表而使用后者。Synacktiv因此不认定CodeAct内在优于ToolAgent，建议对齐库提示再比较。这里是作者公开实验与本合集对表格的计算，不是独立重跑，也不保证真实软件或其他模型同样表现。

候选日期2026-10-18 00:17北京时间；原文日期2026-10-13，是补充核查材料。
两题、每工具每题四次；库提示不对等，未独立重跑，不外推完整CREBench。
本合集按公开表计算token比约0.634、平均分85.9375对31.25；分数不是成功次数。

## 来源

- [窗口候选：吉川孝志的实验整理](https://x.com/i/status/2111491684156752278)
- [补充原文：Synacktiv 2026-10-13 实验与逐次结果](https://www.synacktiv.com/en/publications/ufc-666-frontkick-vs-rikugan)

[English](en/synacktiv-frontkick-rikugan-crebench.md) | [返回目录](../README.zh-CN.md)
