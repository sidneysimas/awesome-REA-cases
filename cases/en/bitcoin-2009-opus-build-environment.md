# Bitcoin 2009: Opus-assisted build-environment archaeology, not source recovery

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-20
Stage: Analysis test

At 02:42 Beijing time on October 20, @itsarcvale relays @t4t5's Opus 5.5 reconstruction of the 2009 bitcoin.exe and suggests checking personal wallet builds. Supplementary reading of the author's October 19 original at 03:12 and same-second continuation confirms the task: recover an unknown historical build environment for already-public source, not recover unpublished source by decompilation. The author reports an EXE matching the historical release's SHA256.

The README at t4t5/bitcoin-0.1-rebuilt commit 344f88083abf301af107fb9de120ee9350f1415b (October 19, 14:36 Beijing time, before this window) describes reconstructing Windows XP/MinGW gcc 3.4.5, different binutils versions for different stages, wxWidgets and Berkeley DB, using Docker/Wine and WinRAR 3.51. It reports a 6,440,960-byte EXE and 2,132,686-byte RAR matching historical hashes. These are project results, not hashes calculated or builds run by this collection.

The archive named bitcoin-0.1.0 is the January 10, 0.1.1-era update, not the January 8 launch file; the author knows of no verified surviving launch copy. Three original timestamps are build inputs; without them 335 bytes differ. RAR timestamps and NTFS Compressed attributes also come from the original archive; a script patches the latter and recalculates header checksums. Neither libeay32.dll nor mingwm10.dll is rebuilt from source; execution uses Wine rather than XP. This collection ran no build, downloaded no historical target and accessed no wallets. This does not establish reproducibility for every wallet or eliminate all supply-chain risks.

Candidate snapshot: 11 likes, 357 views, 2 reposts. Supplementary retrieval of the earlier author's post returned 2,084 likes, 271,269 views and 119 reposts. Both are circulation snapshots observed October 20, not technical reproduction.

## Sources

- [Window candidate: Arcvale's retelling and wallet-build checking proposal](https://x.com/i/status/2112252966971301962)
- [Earlier original: author reports Opus-assisted environment reconstruction](https://x.com/i/status/2111898332658544835)
- [Earlier author continuation: version identity and build archaeology](https://x.com/i/status/2111898334893842717)
- [Earlier pinned README: results, inputs and DLL exclusions](https://github.com/t4t5/bitcoin-0.1-rebuilt/blob/344f88083abf301af107fb9de120ee9350f1415b/README.md)

[中文](../bitcoin-2009-opus-build-environment.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
