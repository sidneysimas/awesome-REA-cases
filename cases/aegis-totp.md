# Aegis：还原验证器 App 的一次性验证码计算

分类：算法与功能重建 · REA
记录日期：2026-10-12

Aegis 是 Android 上的开源双因素验证器，会生成随时间变化的登录验证码。贡献者从 APK 中追踪验证码显示和复制的调用，提取时间计数、HMAC、截断与补零逻辑，再写出 Python 和网页 WebCrypto 对照实现。记录中三种实现对 133 组输入给出一致结果，含标准参考向量。目的是还原与验证这个具体功能，不是破解用户密钥或绕过认证；没有运行原 APK。

## 来源

- [案例 PR](https://github.com/morluto/rea/pull/1266)
- [证据记录](https://github.com/morluto/rea/blob/main/website/evidence/aegis-login-code.md)

[English](en/aegis-totp.md) | [返回目录](../README.zh-CN.md)
