# Series X|S controllers on Xbox 360: a Claude/xone driver account, four pads and float checks unverified

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-28
Stage: Needs verification

At 22:32:23 Beijing time on October 27, 2026, Kreia Notes (@kreia) cites r/ClaudeAI for Claude Code reverse-engineering the Xbox 360 kernel and writing a native driver for Series X|S controllers. The target is cross-generation input interoperability, not original Xbox startup animation or Xbox Labs research.

At 02:25:00 on October 28, current candidate Xiao Tan (@tvytlx) adds a more detailed secondhand account: the newer wireless receiver uses a MediaTek Wi-Fi chip requiring host-side firmware upload, radio setup, pairing, encrypted handshakes and controller protocols. Claude reportedly uses Ghidra to study undocumented Xbox 360 USB internals, ports relevant Linux-community xone logic to the PowerPC console kernel and reads hardware memory through a debug port. The post claims up to four wireless controllers, vibration, Guide support, automatic startup loading and open code. It explicitly requires a modified console and debug access and remains in early testing. A human plugs USB devices, pairs controllers, restarts crashes and reports the screen; this is not an unattended achievement.

The post describes a Guide-triggered self-deadlock from reentering system calls in an input-feeding thread, plus compiler-emitted floating-point instructions in callbacks without a floating-point environment. It says soft float and a build failure on any floating-point instruction address the latter. Driver state/logs in memory are reportedly read by Claude over the network for compile-upload-check cycles. These are reported debugging explanations, not inspected code or guaranteed regressions here.

X lookup confirms Xiao Tan's attribution and full text. Public repository searches did not identify the original developer/source; kernel/firmware versions, receiver revision, pairing logs, four-controller/vibration/Guide tests and reconnect records were not obtained. Existing ID and source URL are preserved and evidence added as unverified, not entire-kernel recovery, support on unmodified retail consoles or universal wired/wireless compatibility. REA is unspecified. The Reddit text was not read, no driver installed and no console operated here.

Original candidate snapshot: 0 likes, 18 views, 0 reposts. Kernel reversing and driver functionality are secondhand claims.
October 28 new-candidate snapshot: 5 likes, 567 views, 0 reposts. Four controllers, deadlock and soft-float checks were not independently verified; later lookup engagement is not substituted.

## Sources

- [Kreia Notes recounts the Xbox 360 controller driver, October 27, 2026](https://x.com/i/status/2115089228220756142)
- [Xiao Tan adds xone, Ghidra, four controllers and floating-point build checks, October 28, 2026](https://x.com/i/status/2115147768780222805)

[中文](../xbox360-series-controller-claude-driver-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
