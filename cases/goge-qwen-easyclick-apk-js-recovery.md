# EasyClick APK：Goge称本地Qwen在44分58秒还原自写加密JS

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-28
阶段：分析测试

2026年10月28日14:18:49（北京时间），Goge（@niandwo）报告AMD R9700 32G、DDR5 64G和Strata0.1.52运行Qwen3.8-next-flash-iq3_s，以256K上下文作本地模型测试。逆向目标是其以前用easyclick框架写的Android自动化脚本App；使用opencode与基础逆向skills，明确没有REA工具集。Agent发现Mac上的jadx和OrbStack，启动调试容器，打算加载APK中的原生解密库，打开IEC2脚本包、导出js/main.js。作者在17分29秒时看到上述进度，最终称44分58秒找全并准确还原自己的JS逻辑。补查原帖确认署名及四张截图附件，未核验截图代码。

动机是检验长上下文工具调用及自有App的脚本保护，不是破解他人账户。没有原APK、原始/还原代码对照、哈希、可复算测试或完整Agent日志；完整与准确均为作者判断。容器镜像及JDK网络下载造成等待，44分58秒不是纯推理耗时或普遍性能保证。240K上下文约80tok/s、比RTX3090配置慢约15%、同机比llama.cpp跑Qwen3.8-27B Q5快至少1.5倍，均为作者另报推理比较，不是逆向精度；6分27秒生成射击游戏也不是本次恢复结果。未安装目标依赖、执行APK或运行解密库，保留分析测试自述。

候选快照7赞、349浏览、0转发；17分29秒为进度点，44分58秒为作者总时长，含下载等待。

## 来源

- [Goge的本地Qwen推理与EasyClick脚本恢复报告，2026-10-28](https://x.com/i/status/2115327409520267434)

[English](en/goge-qwen-easyclick-apk-js-recovery.md) | [返回目录](../README.zh-CN.md)
