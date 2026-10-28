# PlainMount: REA study of NTFSTool leads to a native Mac utility for an old drive

Category: Applications and clients · REA
Record date: 2026-10-28
Stage: In progress

At 18:03:02 Beijing time on October 28, 2026, Laplaced (@0xlaplaced) reports finding a 512GB Transcend drive from 2008, initially inaccessible and then readable but not writable. An AI agent traced the issue to NTFS support on macOS. Rather than pay for the tools tried, the author had the agent inspect NTFSTool with REA and build the native Mac app PlainMount around existing NTFS components. The author reports reading, writing and reconnecting on that actual drive, with public source and a download, free for personal use without an account or subscription, on Apple Silicon and macOS 14+. Old MEW wallet files explain the interest in the drive, not a key-recovery or recovered-funds result.

Supplementary reading covers the README at 0xlaplaced/PlainMount commit a984a55236f1bd24f344b0adddc5be96644f7c87, committed at 18:11:15 that day, after the post but still within this window. It lists volume information, Finder access, read-only mounting, ejection and bundled-backend writing. The 1.0.5 arm64 download is ad-hoc signed, not Apple-notarized, and writing requires Full Disk Access and administrator approval. The default source build supports inspection and standard read-only operations only. The download additionally bundles NTFS-3G, libfuse and FUSE-T: the application's MIT license does not cover the whole package. The first two retain GPL and LGPL respectively; FUSE-T is free only for non-commercial use and requires separate commercial licensing.

The project says disk identity is revalidated before operations, administrator passwords are not stored, no permanent privileged service is installed, and drives are not formatted or force-unmounted. These are design claims, not a security audit by this collection. Core tests use synthetic data, not live-drive write validation. No NTFSTool revision, REA investigation log, feature-by-feature comparison, data-integrity test or sustained multi-device evidence is provided. Reading, writing and reconnection remain author reports, not a new NTFS driver, full feature equivalence or independent reproduction. This collection only read static material; it downloaded no app, accessed no wallet and operated no disk.

Candidate snapshot: 0 likes, 83 views, 0 reposts. Reading, writing and reconnection are reported on one old 512GB drive only.
MIT application code does not make the writing package MIT; notarization, permissions and third-party non-commercial terms are separate considerations.

## Sources

- [Laplaced's REA/NTFSTool-to-PlainMount report, October 28, 2026](https://x.com/i/status/2115383833570758955)
- [Public PlainMount source repository](https://github.com/0xlaplaced/PlainMount)
- [Pinned same-day 18:11:15 README: builds, licenses and testing limits](https://github.com/0xlaplaced/PlainMount/blob/a984a55236f1bd24f344b0adddc5be96644f7c87/README.md)

[中文](../laplaced-plainmount-rea-ntfstool-macos.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
