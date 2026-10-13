# 算法与功能重建

[返回主目录](../README.md)

- [二进制库：先分析原实现，再写替代代码](../cases/binary-library-rewrite.md) — 分析二进制库并重写；库名和评测细节未公开。 **[REA]**
- [DownUnderCTF：从校验程序中找出正确输入](../cases/masked-squares-ctf.md) — 恢复校验约束，用 Z3 求出被原程序接受的输入。 **[REA]**
- [Aegis：还原验证器 App 的一次性验证码计算](../cases/aegis-totp.md) — 从验证器 APK 提取验证码逻辑并做多实现对照。 **[REA]**
- [Windows 计算器：还原百分号在不同运算中的规则](../cases/windows-calculator-percent.md) — 分析已安装计算器 DLL，解释并重建加法与乘法的百分号行为。 **[REA]**
- [自制 JS / .NET 样本：对照有无 REA 的函数重建](../cases/codex-rea-controlled-samples.md) — 同模型六次运行、360 用例验收，研究 REA 的线索价值而非宣称提速。 **[REA · 分析测试]**
- [DLSS：重实现计算着色器以在 AMD 显卡运行的报告](../cases/dlss-amd-compute-report.md) — 讨论明确提出 AI 辅助重实现 DLSS，具体开发归属仍待核验。 **[未确认使用 REA · 待验证]**
- [REA 分析链路：测试二进制内提示注入的 idea](../cases/rea-binary-injection-test-idea.md) — 计划测试目标文件中的文字能否污染 AI 逆向结论。 **[未确认使用 REA · 待验证]**
- [CapCut 动态字幕：从模板 DSL 重建渲染器的 idea](../cases/capcut-subtitle-renderer-idea.md) — 研究字幕模板、Shader 与 SDF 渲染，再以图片 diff 验证。 **[未确认使用 REA · 待验证]**
- [16 个笔记文件：有无 REA 的解码对照实验转述](../cases/sixteen-note-files-decoder-report.md) — 长文转述对16个笔记文件的限时解码比较，两条语言版本合并。 **[REA · 待验证]**
