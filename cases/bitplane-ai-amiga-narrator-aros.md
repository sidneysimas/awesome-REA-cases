# Amiga narrator：TypeScript重写并把自由软件语音回移AROS的自述

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-24
阶段：待验证

davidsong（@bitplane）在2026年10月24日17:05:27（北京时间）的AI项目清单中，将Amiga narrator语音重写列作AMOS Pro工作的独立子成果。他说先用TypeScript重写，再把自由软件voice回移到AROS，供SPEAK:设备使用，并称运行于真实Amiga。用途是为旧系统补回语音能力，目标不同于模拟器和在线IDE，因此单列。

AI归因来自整份清单的开场说明，未点名具体模型、REA或生成比例。原帖没有说明语音合成算法、硬件型号、对照音频、代码或兼容性测试；短链未解析。所谓AROS自九十年代需要SPEAK:以及真实硬件运行均为作者说法，不是本合集历史考证或真机复现；也不把重写等同原源码恢复或原声音逐样本一致。

仅为核对项目身份，补读最后修改于2026-09-08、早于本窗口的amos-ts README：它把narrator-ts列为narrator.device与translator.library的MIT重实现，并链接npm包。本合集未安装该包，此文档不验证AROS回移或真实硬件成果。

TypeScript重写、AROS回移及真实Amiga运行均为作者报告；无对照音频或真机验证。补充amos-ts文档将narrator-ts列为narrator.device与translator.library的MIT重实现，仅核对身份。

## 来源

- [bitplane清单中的narrator与AROS子项目，2026-10-24](https://x.com/i/status/2113919789886218477)
- [补充amos-ts README中的语音依赖说明，最后修改2026-09-08](https://github.com/bitplane/amos-ts/blob/2809fc901c688baa130d884ad5419ab7aa15e4fa/README.md)
- [上述README链接的narrator-ts包入口，未安装](https://www.npmjs.com/package/narrator-ts)

[English](en/bitplane-ai-amiga-narrator-aros.md) | [返回目录](../README.zh-CN.md)
