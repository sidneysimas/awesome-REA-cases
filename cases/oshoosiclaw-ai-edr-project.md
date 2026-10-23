# OshoosiClaw：把自动二进制分析与YARA-X合成接入EDR的项目

分类：应用与客户端 · 未确认使用 REA
记录日期：2026-10-24
阶段：相关项目

2026年10月23日22:52:53（北京时间），候选介绍开源OshoosiClaw端点检测与响应（EDR）及AI Agent隔离项目，称以Rust面向Linux和Windows，包含14引擎检测管线、内存SQL遥测，以及结合Magika文件识别和YARA-X规则合成的自动逆向。作者同时招募渗透测试者测试自定义加载器和Agent逃逸等边界。

公开仓库检索找到oyesanyf/OshoosiClaw。其文档工具归属表将REA列为项目自己的二进制检查、反编译和规则生成模块，不能据名称就确认使用morluto/rea。候选还宣传Windows Ring 0 minifilter/ELAM、Linux BPF LSM、低于20微秒的cgroup隔离与后量子P2P共享；本次不逐项验证实现、签名驱动、密码方案或性能。

收录的是具有具体自动分析与规则输出用途的相关安全项目，不是已完成独立测试的EDR推荐。仓库补查用于定位与名称归属，不把动态文档中的全部后续功能倒填为候选日期成果；未安装、构建、运行端点防御或执行攻击测试。

候选来源2026-10-23 22:52:53，北京时间；仓库为补充定位来源。
性能和内核防护未验证；REA同名模块不等同确认使用morluto/rea。

## 来源

- [候选：OshoosiClaw架构、自动逆向与测试邀请，2026-10-23](https://x.com/i/status/2113644836876415239)
- [补充公开项目仓库：REA模块归属，动态文档](https://github.com/oyesanyf/OshoosiClaw)

[English](en/oshoosiclaw-ai-edr-project.md) | [返回目录](../README.zh-CN.md)
