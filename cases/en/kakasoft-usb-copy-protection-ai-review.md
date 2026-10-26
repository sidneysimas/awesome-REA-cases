# KakaSoft USB Copy Protection: AI traces custom hashing and a protected test file

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-25
Stage: Analysis test

The October 25 candidate at 07:18:48 Beijing time briefly describes KakaSoft USB Copy Protection. The earlier original by Xusheng Li, dated October 22 at 16:00 UTC, was read in full. On macOS, he asks AI to unpack the Windows installer and analyze version 5.6.0.299. Normal does not encrypt; High XORs at most the first 16,385 bytes with only 256 possible one-byte keys. He selects Highest, advertised as 256-bit Blowfish, and protects his own small text file on a drive.

The original is more specific than the candidate's baked-in-key summary. AI parses raw exFAT directories to locate a hidden 667-byte test file behind unusual names, follows the 32-bit Delphi client's TBlowfishEncryption class, and identifies per-file salt, IV and Blowfish-CBC layout. The failure is an embedded seed transformed by modified MD5 into a fixed internal password, then combined with salt through RIPEMD-128 to derive the file key. AI emulates the relevant client code to recover the internal value; Li reports restoration of the original test-file bytes.

He reports about two minutes unpacking and another seven analyzing cryptography with two prompts. After supplying the protected drive, roughly 26 minutes and six short prompts reportedly extracted the hidden file, recovered the modified hash construction and demonstrated decryption without the user password. These are human-directed author reports, not general timing or all-version results. No sample or drive was independently operated and decryption was not replayed; the internal password is not reproduced. The AI model and REA are unspecified, so Codex is not attributed to every stage.

The original covers version 5.6.0.299 and the author's own test. The 2+7-minute static stage and subsequent 26-minute stage are not conflated into one end-to-end duration.

## Sources

- [Window candidate: KakaSoft protection-flaw account, October 25, 2026](https://x.com/i/status/2114134544836407379)
- [Earlier original: Xusheng Li's full KakaSoft workflow, October 22, 2026 UTC](https://binary.ninja/2026/10/22/breaking-more-encrypted-usb-drives-with-ai.html#kakasoft-usb-copy-protection)

[中文](../kakasoft-usb-copy-protection-ai-review.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
