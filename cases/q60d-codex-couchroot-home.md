# Samsung Q60D：Codex 整理 Couchroot 主页适配与恢复流程

分类：硬件与设备互通 · 其他 AI 逆向
记录日期：2026-10-21
阶段：待验证

2026年10月21日03:56（北京时间），Zona Antiwoke（zonaantiwoke_）发布由 Codex 根据自己操作整理的教程：在 Samsung Q60D 上保留 Tizen，制作应用、电视天线、输入源和快捷方式入口，以 Couchroot 为基础做机型适配。作者称该上游主要文档面向 QN90A 与 S90D，不能直接保证 Q60D 或不同固件兼容。界面采用静态背景、短图标动画，并保留 Samsung 原主页入口。

教程明确区分开发模式下签名安装普通 .wgt 应用与真正替换 Home；后者依赖型号、固件和权限，作者称自己的适配记录了原值并验证改动。电脑预览不等于电视性能，部分备份不等于全机恢复，安装旧包也不保证可回退。作者明确说克隆 Couchroot 不会得到其展示的同一界面。

补查确认此作者不同于现有 Samsung Tizen 清爽启动器案例的 huntsyea，故不将两个设备与操作合并。AI 参与至少包括教程整理，具体逆向和适配由谁完成未给完整记录；本地代码、精确固件、恢复记录与实机测试未取得，REA未明示，不能写成开源可复现的系统主页替换。

AI 参与边界：可确认作者把教程整理归于 Codex；不能据此将上游 Couchroot 或全部设备逆向归于 AI。

## 来源

- [zonaantiwoke_：Q60D、Couchroot 与 Codex 整理的14步教程](https://x.com/i/status/2112634078428102789)

[English](en/q60d-codex-couchroot-home.md) | [返回目录](../README.zh-CN.md)
