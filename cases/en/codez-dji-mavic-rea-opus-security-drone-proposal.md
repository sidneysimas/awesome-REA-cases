# DJI Mavic security drone: Codez proposes REA/Opus phone-side tracking with the official SDK

Category: Hardware and interoperability · REA
Record date: 2026-10-27
Stage: Needs verification

At 00:55:21 Beijing time on October 27, 2026, Codez (@0xCodez) says he reverse-engineered his DJI Mavic with REA and Opus 5.5 and turned it into a home-security drone. An original-post lookup confirms attribution and full text. The context is using a spare phone connected to the remote for visual detection, tracking and control after a home alarm, allegedly without cloud services or GPS on the target.

The text outlines a build proposal: check the DJI Mobile SDK v5 support list and stop without firmware hacks if unsupported; write a small Swift or Kotlin application on the official SDK; send a Home Assistant notification followed by a human tap on Launch; run YOLO on the phone, maintain tracking through occlusion with a Kalman filter, and control through Virtual Stick at 10 Hz. It describes keeping at least 8 m away, stopping at the property boundary and climbing to 30 m, returning to a pad, and saving track, distance and timestamps on the phone. These are proposed parameters and expected behaviors, not measurements, safety certification or directly actionable flight advice.

No specific Mavic model, SDK/operating-system compatibility matrix, protocol recovered by REA, code, flight log, obstacle-avoidance test or return-to-home validation is supplied. Official-SDK development does not itself establish firmware reversing, and the claimed iPhone/Android support is unchecked. Retained as an unverified proposal presented by its author as built, but supported mainly by a step-by-step description; the accompanying video is not treated as proof of the complete workflow. No target code was run, device connected or tracking flight conducted here.

Candidate snapshot: 275 likes, 14,530 views, 24 reposts. Later engagement changes from supplementary lookup are not treated as in-window propagation data.
8 m, 30 m and 10 Hz are author-proposed parameters, not verified safety or compatibility results.
In the October 27, 14:43 candidate, dexx asks whether this is simply DJI SDK development; snapshot: 0 likes, 21 views. Supplementary lookup of the author's full prompt being replied to (pre-window 00:55) explicitly requires only the official SDK, stopping for unsupported models, with no firmware changes or removal of flight limits. This strengthens the methodological boundary, not a proven fraud allegation or evidence that REA recovered a closed protocol. Code and flight logs remain unavailable.

## Sources

- [Candidate and original lookup: Codez's Mavic/REA/Opus proposal, October 27, 2026 Beijing time](https://x.com/i/status/2114762819371680110)
- [dexx asks whether only the official SDK is used, October 27 at 14:43](https://x.com/i/status/2114971107786645923)
- [Supplement: author's 00:55 full prompt, official SDK only and stop if unsupported](https://x.com/i/status/2114762823762952307)

[中文](../codez-dji-mavic-rea-opus-security-drone-proposal.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
