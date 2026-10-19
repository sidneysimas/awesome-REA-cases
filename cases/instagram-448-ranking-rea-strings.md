# Instagram 448：Claude／REA 从 APK 字符串调查 Reels 排名线索

分类：应用与客户端 · REA
记录日期：2026-10-19
阶段：分析测试

10月19日18:02（北京时间），@err_cod 解释自己的Instagram Reels排名调查：从已root手机提取Android版448.0.0.52.84，使用Claude Code（Opus 4.8）、REA MCP、ADB、strings与grep，从22个代码文件抽取约787,000行文本，再逐项搜索排名相关名称。背景是理解为什么自己的Reels不传播。

补读同分钟作者串，找到pwatch、pcomments、psendbutton、reels_skip_rate、MIXED_UNCONNECTED，以及CLIPS_AUDIO／AUTHOR／TOPIC_NOT_INTERESTED和incrementality score等名称。作者据此讨论完整观看、评论、转发、客户端重排、未关注账号混合和不感兴趣反馈，并给出内容建议。这里记录的是作者对客户端字符串的解释，不认证这些信号的重要性排序、对所有用户的实际启用或服务端因果机制。

作者在18:02:17明确补充：这些是真实出现在App内的名称，只能说明代码含相关功能，不能给出信号准确权重；所列APK SHA256只是省略形式，不能用于精确文件校验。没有完整APK哈希、可复查提取文件、调用链或线上对照实验，本合集未取得APK、执行App或独立复现。候选及补充串均为10月19日，补充帖仅用于解释该候选，不替换原候选。

候选快照2赞、78浏览、0转发；作者串其他帖的传播不混为本候选热度。

## 来源

- [候选：err_cod说明版本、规模与Claude／REA工具](https://x.com/i/status/2112122149695848613)
- [补充作者串开头：Reels传播问题](https://x.com/i/status/2112122119643627844)
- [补充：pwatch、pcomments与psendbutton](https://x.com/i/status/2112122123686936985)
- [补充：客户端排名与skip rate解释](https://x.com/i/status/2112122127608594581)
- [补充作者限制：名称不等于准确权重](https://x.com/i/status/2112122152589873174)

[English](en/instagram-448-ranking-rea-strings.md) | [返回目录](../README.zh-CN.md)
