# Fun2Spec：用LLM从C++函数恢复后置条件，延伸到Spec-Agent

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-24
阶段：相关项目

2026年10月24日00:50:35（北京时间），Julien Vanegue（@jvanegue）把从代码恢复规格称为验证问题的对偶，列出论文《Fun2spec: Code Contract Synthesis At Scale》，并称Spec-Agent把这一方向扩展到分离逻辑，将fuzzing放入反馈循环。这里的目标是为已有实现补出可检查的行为契约，不是恢复遗失的原始源码。

补读bloomberg/fun2spec公开README，项目明确使用LLM生成C++函数的后置条件，以Bloomberg Development Environment（BDE）库和BlazingMQ消息队列为两个案例。文档列出结果CSV中的函数名、生成的后置条件，以及执行中条件成立和不成立的计数；这能记录测试反馈，不等于对任意输入的数学证明。README所列默认模型为microsoft/Phi-3-mini-128k-instruct，支持int、pointer或all返回类型筛选。

补充文档固定于afcc146242d2a2c966cadf632b2775cc47c552ae，提交日期2026-07-06，早于本轮窗口；README把论文列为FSE 2026七月发表。它用于确认方法、案例和结果字段，不是本轮新发布的实验。Spec-Agent的分离逻辑与fuzzing扩展目前只据候选作者说明，未取得其论文或实现细节。未运行工具、安装依赖、复核生成契约或测量正确率；没有提及REA，按相关研究项目收录。

候选2026-10-24 00:50:35，北京时间；补充仓库提交2026-07-06，早于窗口。
Fun2Spec文档已读；Spec-Agent仅作者介绍，未独立生成或检查契约。

## 来源

- [Julien Vanegue：Fun2spec与Spec-Agent，2026-10-24](https://x.com/i/status/2113674455503212738)
- [补充Fun2Spec README：LLM方法、两个案例与CSV字段，2026-07-06提交](https://github.com/bloomberg/fun2spec/blob/afcc146242d2a2c966cadf632b2775cc47c552ae/README.md)

[English](en/fun2spec-llm-code-contract-recovery.md) | [返回目录](../README.zh-CN.md)
