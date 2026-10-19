# Kestrel: studying MuMuPlayer Pro for a native Apple Silicon Android gaming player

Category: Applications and clients · REA
Record date: 2026-10-19
Stage: In progress

At 07:59 Beijing time on October 19, @ColateAi retells @iamthehimansh_'s Kestrel work: to play BGMI on a Mac, parts of MuMuPlayer Pro's architecture were investigated with Colate Desktop's REA mod, then a native player, input and keymapping were implemented on Google's Android Emulator. The public iamthehimansh/kestrel README instead names Cana.build's REA mod and explicitly credits the open-source REA toolkit. This preserves the naming difference between the candidate and repository without inferring a product rename. The project says it includes no proprietary emulator binaries, decompiled source or restricted Android images. It is not a complete Android emulator implemented from scratch.

Public commit 5250e2ba, dated October 19 at 06:46:09 Beijing time, and its experiment ledger provide summaries from one Apple Silicon development machine and public reproduction methods. Historical figures were transcribed from retained private assessment files; they are not public raw datasets or independent reproductions. Two boots per transport and three samples per boot did not establish a meaningful frame-time benefit for pipe versus ASG, so no performance toggle was added. MuMu's Android 12/API 32 and Kestrel's Android 16/API 36, drawable sizes and workloads differ, preventing a general speed multiplier. Shared memory reduced measured CPU cost and frame age but lacked a demonstrated producer fence; the product uses complete copied frames and a single-slot latest-frame mailbox. Its Metal display path bounds in-flight rendering and preserves aspect ratio.

The author documents a requested 4 GiB capacity versus an existing 6 GiB QCOW2 disk invalidating snapshots. Preserving actual capacity led to three resumes of about 6.36 seconds; a setup-inclusive cold boot is not a valid speedup denominator. A 120 Hz virtual display does not establish 120 FPS gameplay. BGMI initially crashed in EGL; disabling asynchronous swaps removed the crash but left a black screen. Selecting built-in ANGLE while retaining that condition produced rendering, and the maintainer supplied gameplay screenshots and reported playing. This does not prove other settings irrelevant. Keymapping, held-touch release on focus loss, fullscreen hints, instance management and a CLI have public implementations; preset keymaps are not individually tested game support.

Repository limits include macOS 15 and Apple Silicon for the native player, first-run SDK downloads, ad-hoc signing without notarization, ASCII-only input and unverified real microphone/voice-chat behavior. No anti-cheat acceptance or commercial-emulator performance parity is promised. Public CI run 39173792442, running from 06:48 to 07:01 Beijing time on October 19, shows a successful Swift Build step, failed Test step and successful packaging-script test job, not an entirely green CI suite. No target code, installer or game was executed here; this collection only read public material.

07:59 candidate snapshot: 0 likes and 3 views; GitHub showed 1 star when checked. Little circulation is not evidence of maturity.

## Sources

- [Colate's account of Kestrel research, experiments and preview limits](https://x.com/i/status/2111970389983142116)
- [Kestrel public repository and README](https://github.com/iamthehimansh/kestrel)
- [Experiment ledger at the October 19 06:46 commit](https://github.com/iamthehimansh/kestrel/blob/5250e2ba2ca5d9fbcbb8ad94e7aa1cc7534f6809/docs/research/experiment-ledger.md)
- [Compatibility and evidence notes at the same commit](https://github.com/iamthehimansh/kestrel/blob/5250e2ba2ca5d9fbcbb8ad94e7aa1cc7534f6809/docs/guide/compatibility.md)
- [Public CI: failed Swift tests, successful packaging-script tests](https://github.com/iamthehimansh/kestrel/actions/runs/39173792442)

[中文](../kestrel-colate-rea-mac-android-player.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
