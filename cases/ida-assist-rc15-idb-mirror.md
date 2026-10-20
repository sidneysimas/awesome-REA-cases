# IDA Assist rc15：用 SQLite 镜像给 LLM 查询 IDA 分析数据库

分类：应用与客户端 · 其他 AI 逆向
记录日期：2026-10-20
阶段：相关项目

10月20日11:13（北京时间），@in19h 介绍IDA Assist rc15的新功能idb_mirror：以SQLite sidecar实时镜像IDA数据库，绕开IDA主线程处理读取。IDA是二进制分析工具，这项设计针对Agent查询交叉引用、字符串和类型时的阻塞问题，而不是一个已完成的目标程序重建。

帖子称只读工具响应小于20毫秒，提供LLM直接访问的idb_query和Python snapshot API，并支持4倍工具并行。这些是发布者报告的能力与性能，没有给本帖对应的测量方法、负载、硬件或对照输出。没有源码和运行验证可据此确认镜像一致性、写操作安全或所有任务都快4倍；本合集未运行IDA或目标样本。

## 来源

- [in19h：IDA Assist rc15数据库镜像与查询介绍](https://x.com/i/status/2112381687292182586)

[English](en/ida-assist-rc15-idb-mirror.md) | [返回目录](../README.zh-CN.md)
