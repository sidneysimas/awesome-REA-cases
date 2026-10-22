# Building-doorbell live view: Mattia investigates firmware with REA/Ghidra and replaces the indoor monitor with a Pi

Category: Hardware and interoperability · REA
Record date: 2026-10-22
Stage: Needs verification

At 21:37:29 Beijing time on October 22, 2026, Mattia Righetti (@matttrighetti) reports examining his building door station's ARM firmware with REA and Ghidra, finding UDP send/receive paths and XML templates including Call, CallAck, Accpet, HangUp and Tick. Accpet preserves his exact identifier rather than silently correcting it. The goal is to understand communication between his building's camera doorbell and indoor intercom monitor and display the camera feed directly in a browser.

Supplementary reads of the thread root (October 21 at 20:47:05) and an early result (October 22 at 00:13:37) establish the background: he used Raspberry Pi GPIO with an existing UART root shell and says Codex luna 5.6 medium created a webpage displaying live doorbell data. Both precede this 20:00-24:00 window and serve only as background, AI-role and early-result evidence, not new candidates.

Further posts in the same thread at 21:35-21:53 on October 22 describe inspecting monitor/station communications and observing 12 UDP/6600 packets during a call. He says firmware-derived protocol details let him decode encrypted messages and associate them with application call commands. After disconnecting the indoor monitor and attaching a Pi to the same Ethernet cable, he reports establishing and maintaining the session and receiving UDP multicast video. His decoded video reportedly has a small header carrying sequence numbers, timestamps and frame-boundary flags, followed by H.264. He reports building a Rust service and using FFmpeg to package H.264 into short HLS segments for browser live view, with a result image attached. This entry summarizes interoperability research and reported results without decryption material or attack instructions.

This review obtained the author's narrative, not a device brand/model, firmware version, repository, packet-capture body, source code, latency or stability tests. It did not independently verify video, wiring or access-control safety. The account is not generalized to all building doorbells and does not establish door unlocking, two-way audio or security hardening. REA, Ghidra and Codex roles are attributed to the author; the case remains unverified.

Candidate originally posted 2026-10-22T21:37:29+08:00; supplementary root at 2026-10-21T20:47:05+08:00 and early result at 2026-10-22T00:13:37+08:00 predate this window.
12 packets, UDP/6600, H.264 and HLS are author-reported; no packet capture or independent reproduction was obtained.

## Sources

- [Candidate: ARM door-station firmware investigation with REA and Ghidra](https://x.com/i/status/2113263472486051899)
- [Supplementary earlier root: building camera doorbell and indoor monitor](https://x.com/i/status/2112888402496659861)
- [Supplementary earlier result: Codex luna 5.6 medium and a live webpage](https://x.com/i/status/2112940379670483416)
- [Supplementary thread: UDP/6600 capture observation](https://x.com/i/status/2113263382677815675)
- [Supplementary thread: Pi maintaining the session in place of the indoor monitor](https://x.com/i/status/2113264163514732695)
- [Supplementary thread: video header and H.264](https://x.com/i/status/2113264571054211570)
- [Supplementary thread: Rust, FFmpeg and browser HLS output](https://x.com/i/status/2113266775060263326)

[中文](../mattia-doorbell-rea-ghidra-rust-live-view.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
