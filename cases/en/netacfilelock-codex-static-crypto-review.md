# NetacFileLock: a researcher reports a seven-minute Codex static cryptography review

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-25
Stage: Analysis test

The October 25 candidate at 07:18:48 Beijing time recounts a NetacFileLock investigation. Xusheng Li's original on Binary Ninja's official blog was read as supplementary evidence: October 22 at 16:00 UTC, or October 23 at 00:00 Beijing time. This is earlier research circulated within the window, not independent reproduction here. Li had already studied this file-encryption tool through TTD. With one prompt asking Codex to inspect its cryptosystem through Binary Ninja MCP, he reports roughly seven minutes of static analysis identified a fixed 32-byte AES-256 key embedded in the executable, separate from the user-password check.

He also reports user passwords in diagnostic logs, independent 16-byte blocks with ECB-style behavior, MD5 password verification and an unkeyed MD5 file signature, plus another fixed key for SM4. Fast mode partially encrypts files larger than 1,024 bytes, resolving his earlier observation of a test file encrypted only one-third of the way; this is not limited to PDFs. Seven minutes is not generalized to other tools. A model version, complete call trace and independent comparison were not supplied.

The finding concerns password-independent key management in the analyzed software, not a break of AES-256 itself or a conclusion about all Netac products. No sample was downloaded or executed, no user logs or encrypted data were accessed, and keys are not reproduced. REA is not mentioned.

Seven minutes, one prompt and additional findings are researcher reports. This collection read the original without independently testing it.

## Sources

- [Window candidate: account of Codex analyzing NetacFileLock, October 25, 2026](https://x.com/i/status/2114134544836407379)
- [Earlier original research by Xusheng Li, October 22, 2026 UTC](https://binary.ninja/2026/10/22/breaking-more-encrypted-usb-drives-with-ai.html#breaking-netacfilelock-again)

[中文](../netacfilelock-codex-static-crypto-review.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
