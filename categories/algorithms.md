# 算法与功能重建

[返回主目录](../README.md) | [English](en/algorithms.md)

- [二进制库：先分析原实现，再写替代代码](../cases/binary-library-rewrite.md) — 分析二进制库并重写；库名和评测细节未公开。 **[REA]**
- [DownUnderCTF：从校验程序中找出正确输入](../cases/masked-squares-ctf.md) — 恢复校验约束，用 Z3 求出被原程序接受的输入。 **[REA]**
- [Aegis：还原验证器 App 的一次性验证码计算](../cases/aegis-totp.md) — 从验证器 APK 提取验证码逻辑并做多实现对照。 **[REA]**
- [Windows 计算器：还原百分号在不同运算中的规则](../cases/windows-calculator-percent.md) — 分析已安装计算器 DLL，解释并重建加法与乘法的百分号行为。 **[REA]**
- [自制 JS / .NET 样本：对照有无 REA 的函数重建](../cases/codex-rea-controlled-samples.md) — 同模型六次运行、360 用例验收，研究 REA 的线索价值而非宣称提速。 **[REA · 分析测试]**
- [DLSS：重实现计算着色器以在 AMD 显卡运行的报告](../cases/dlss-amd-compute-report.md) — 讨论明确提出 AI 辅助重实现 DLSS，具体开发归属仍待核验。 **[未确认使用 REA · 待验证]**
- [REA 分析链路：测试二进制内提示注入的 idea](../cases/rea-binary-injection-test-idea.md) — 计划测试目标文件中的文字能否污染 AI 逆向结论。 **[未确认使用 REA · 待验证]**
- [CapCut 动态字幕：从模板 DSL 重建渲染器的 idea](../cases/capcut-subtitle-renderer-idea.md) — 研究字幕模板、Shader 与 SDF 渲染，再以图片 diff 验证。 **[未确认使用 REA · 待验证]**
- [16 个笔记文件：有无 REA 的解码对照实验转述](../cases/sixteen-note-files-decoder-report.md) — 长文转述对16个笔记文件的限时解码比较，两条语言版本合并。 **[REA · 待验证]**
- [CPU kernels：Claude Code 编排 Astra 做汇编层优化](../cases/rea-cpu-kernel-optimization.md) — 作者称正在由 Claude Code 管理 Astra，借 REA 研究 CPU 内核优化。 **[REA · 进行中]**
- [禁止逆向的许可：一次 Codex 与 Claude 行为对照](../cases/agent-reverse-license-test.md) — 作者测试 Agent 是否尊重禁止逆向条款，报告两组工具表现不同。 **[其他 AI 逆向 · 分析测试]**
- [旧二进制：Agent 读反编译输出时编造 API 的失败报告](../cases/legacy-binary-agent-api-hallucination.md) — 作者回忆一次旧程序分析，Agent 自信引用实际不存在的接口。 **[其他 AI 逆向 · 分析测试]**
- [人类与 Agent：两项静态逆向任务及上下文扩展性研究](../cases/humans-machines-sre-study.md) — 论文比较九个模型与人类理解二进制的表现，并分析4000个程序的上下文饱和。 **[其他 AI 逆向 · 分析测试]**
- [热工与流体力学求解器：REA + Opus 的进行中重建报告](../cases/rea-thermofluid-equation-solver.md) — 作者称用 T3 Code、Opus 与 REA 推进求解器，同时开发移动/web RTS。 **[REA · 进行中]**
- [旧图片处理软件：用 AI 学习预设与处理方法的 idea](../cases/image-presets-ai-study-idea.md) — 永久权益用户希望研究自己所购软件的图片预设，仍在询问许可边界。 **[其他 AI 逆向 · 进行中]**
- [Windows 图形启动：用 Agent 群反编译与剖析系统 DLL 的 idea](../cases/windows-graphics-startup-ai-profile-idea.md) — 针对 D3D11 创建设备和 DirectWrite 首次字形栅格化瓶颈提出逆向优化建议。 **[其他 AI 逆向 · 进行中]**
- [游戏机制百科：让 AI 逆向真实数值与公式的 idea](../cases/game-formulas-ai-guide-idea.md) — 提议从游戏实现提取公式、分支和隐藏剧情，用作攻略证据。 **[其他 AI 逆向 · 待验证]**
- [SentinelOne / Daybreak：缩短复杂恶意软件逆向时间的转述](../cases/sentinelone-daybreak-malware-report.md) — 传播帖称恶意软件分析由4–6周缩短至约8小时，缺原始样本与测试。 **[其他 AI 逆向 · 待验证]**
- [Linux Easy Anti-Cheat：经 IDA Assist MCP 的 AI 去虚拟化报告](../cases/linux-eac-ai-devirtualization-report.md) — 作者称Gemini 4 Argon与GPT 6.1 Sol辅助分析Linux EAC，没有可复核结果。 **[其他 AI 逆向 · 待验证]**
- [REA JavaScript 示例：陈旧价格检查的 400 ms 边界](../cases/rea-js-stale-price-boundary-demo.md) — 作者用自制模块追踪调用链并测边界，明确不是真实交易或Claude现场演示。 **[REA · 分析测试]**
- [game.exe 示意演示：双房间与三类重建 oracle](../cases/rea-clean-room-illustrative-oracles.md) — 帖子具体描述 Reader/Builder 隔离及字节、植错、运行检查，但数字明标 illustrative。 **[REA · 分析测试]**
- [两款游戏 RNG：Codex 与 ILSpy 辅助预测跟踪的自述](../cases/two-game-rng-codex-ilspy-report.md) — 作者称当天研究出两款游戏的随机机制，Codex 不够时再用 ILSpy 搜索。 **[其他 AI 逆向 · 待验证]**
- [博彩 App：用 REA 研究结果机制的假设性提问](../cases/betting-app-rea-outcome-idea.md) — 作者问能否通过研究博彩应用影响结果；没有命名服务或报告可行性。 **[REA · 待验证]**
