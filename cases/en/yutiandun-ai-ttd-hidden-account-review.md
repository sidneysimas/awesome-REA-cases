# YutianDun encrypted USB drives: Xusheng Li's AI-assisted TTD and hidden-account investigation

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-25
Stage: Analysis test

The October 25 candidate at 07:18:48 Beijing time summarizes Xusheng Li's investigation of four USB-protection products. This entry covers only SecZure YutianDun. The supplementary original was read on Binary Ninja's official blog, dated October 22 at 16:00 UTC, or October 23 at 00:00 Beijing time. It is earlier research, not a new experiment within this candidate window.

YutianDun displays encrypted files through bundled readers that attempt to block copying, screenshots and printing. Li had studied its copy protection in 2024. He now describes AI-assisted time-travel debugging that identified NtCreateFile/NtReadFile hooks supplying plaintext inside the reader, followed by cryptosystem analysis. The administrator password unwraps a content identifier from which the file AES key is derived. According to his tests, two built-in accounts hidden from the management interface each hold a wrapped copy of the same identifier; their fixed passwords unwrapped it and decrypted files on both tested drives.

Li calls this a backdoor in the technical sense, explicitly without inferring malicious intent. It is not a break of normal AES, nor proof of practical brute force merely from MD5 or 64-bit key entropy. This collection obtained no samples, ran no tools and decrypted no files; fixed passwords and keys are not reproduced. The model and step-by-step AI contributions are unspecified, and REA is not mentioned. Researcher testing remains distinct from independent reproduction.

Original: October 22 at 16:00 UTC, or October 23 at 00:00 Beijing time. The October 25, 07:18:48 candidate is a secondary account.
Two-drive tests and AI-assisted TTD are researcher reports, not independent testing, proof of malicious intent or confirmation across all versions.

## Sources

- [Window candidate: account of four USB-protection investigations, October 25, 2026](https://x.com/i/status/2114134544836407379)
- [Earlier original by Xusheng Li: Binary Ninja blog, October 22, 2026 UTC](https://binary.ninja/2026/10/22/breaking-more-encrypted-usb-drives-with-ai.html#a-copy-protected-usb-drive)

[中文](../yutiandun-ai-ttd-hidden-account-review.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
