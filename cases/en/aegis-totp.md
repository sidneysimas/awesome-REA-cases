# Aegis: one-time code calculation

Category: Algorithms and feature recovery · REA
Record date: 2026-10-12

Aegis is an open-source Android two-factor authenticator that generates time-based login codes. A contributor traced code-display and copy calls in the APK, extracted the time-counter, HMAC, truncation and zero-padding logic, and wrote comparison implementations in Python and browser WebCrypto. The records show identical results across all three implementations for 133 inputs, including standard reference vectors. The goal was to recover and verify this particular feature, not recover users' keys or bypass authentication. The original APK was not run.

## Sources

- [Case PR](https://github.com/morluto/rea/pull/1266)
- [Evidence record](https://github.com/morluto/rea/blob/main/website/evidence/aegis-login-code.md)

[中文](../aegis-totp.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
