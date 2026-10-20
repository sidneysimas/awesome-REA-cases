# BigSky 与 Ursa Major：先模拟固件，再转 C++ 的 Opus 自述

分类：算法与功能重建 · 其他 AI 逆向
记录日期：2026-10-20
阶段：待验证

10月20日16:00整（北京时间，包含于本轮窗口），@mylifcc转述一位音频设备经营者用Claude研究竞争者算法的经历。补查HN原评论，作者valdiorn于10月15日23:19说自己经营吉他踏板与音效公司，正在做类似Eventide H90、以混响、延迟和合唱算法竞争的处理器；称此前72小时研究了三个竞争产品，包括Strymon Big Sky，Opus 5.5一次提示用三小时完成；Ursa Major全系列据称只用20分钟。这些时间和范围全为其自述，没有产品清单或运行账单。

其具体方法是先让Claude建立模拟器执行原固件/ROM，再转成独立C++库与模拟器结果比较，以避免只是生成听感相似的效果。作者说均已试听且声音很好，但没有公布模型输出、固件版本、C++库、测试信号、误差阈值或逐样本日志，不能由此推出100%原生精确或已独立复现。他还明确说Lexicon 224部分发现并复用了别人已有代码，不是所有成果均由本次提示从零恢复。

转述串另提joelanders/reflecticon-224；补读10月13日提交的README，确认这是运行自备ROM的Lexicon 224/224X/224XL浏览器和插件模拟项目，文档仍在进行中。它不证明valdiorn的BigSky或Ursa Major结果，也不验证转述中电路图到Verilog的全部过程。HN评论及该仓库是窗口外补充材料，不冒充本轮新帖或新研发。本合集未执行固件、下载目标ROM或试听；算法权利与商业复制许可也不能由研究报告推定。

## 来源

- [本轮16:00候选：音效算法逆向转述](https://x.com/i/status/2112453769220780514)
- [10月15日HN原评论：valdiorn的方法、工时与自述限制](https://news.ycombinator.com/item?id=50104955)
- [16:00:01同作者补充，窗口外背景：模拟器、C++及代码复用](https://x.com/i/status/2112453770357481754)
- [窗口外项目README：reflecticon-224运行自备ROM，非BigSky验证](https://github.com/joelanders/reflecticon-224/blob/37fde47f6cf94d4f4f96f3c233382e2c43a70354/README.md)

[English](en/audio-effects-opus-emulator-cpp-report.md) | [返回目录](../README.zh-CN.md)
