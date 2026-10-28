# tolpo: Tapo protocol research, MCP device control and a live 3D home

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-29
Stage: In progress

At 01:50:01 Beijing time on October 29, 2026, beamnxw recounts research into the Tapo smart-home app, attributing most development and protocol work to Claude Code. tolpo exposes lights, plugs, sensors and cameras through MCP. Device names suggest rooms; a person corrects the layout before a 3D home displays live states, sensor-driven doors and click-to-view camera video. AI's research contribution is attributed by that post, not established by a development-process audit here.

A project-name lookup found signerless/tolpo. Pinned commit 07fdd5c81f1f6dc7326cd1cfdc67dc64ba7543a1 dates to October 15 at 04:28:53 Beijing time; this earlier source supplements the new report, not new development in this window. Its README explains reuse of python-kasa's KLAP/SSL-AES communications plus a C465 certificate compatibility fix and independent analysis of the official app and devices. This is not Claude discovering every Tapo protocol from scratch. MCP and HTTP share a core, authenticating with the owning Tapo account and contacting devices over LAN; that does not mean the model runs locally or images never reach a model.

The project lists L430C, P115, H200, T110/T310/T300, C225/C610/C465 and D230 as hardware-tested. home_plan documentation reports a home test on October 12 involving nine rooms, 18 devices, two camera streams, light toggling and layout saving, solely a project test. Most extended writes were simulated only. Vacuums, locks, radiator valves and firewall providers were not hardware-tested; locks are not usable, and cloud accounts/sharing/Tapo Care are outside local scope. English, German and Spanish device names suggest rooms needing human correction, not automatic house surveying.

Camera images are off by default and privacy mode is checked. Advanced security/lifecycle actions require extra permissions and confirmation phrases, but a phrase does not prove human consent. The thread's read-only-first and permission rules are deployment advice, not a security certification. No code was run, devices connected or video/full functionality independently verified.

Candidate snapshot: 51 likes, 1,037 views, 3 reposts. An MIT source label does not replace device or cloud-service authorization.

## Sources

- [beamnxw's Claude protocol-research and 3D-home account, October 29, 2026](https://x.com/i/status/2115501353594404870)
- [Same author's read-only-first, consent and privacy supplement](https://x.com/i/status/2115501358539223415)
- [Earlier pinned README: reused protocol library, hardware and simulation boundaries](https://github.com/signerless/tolpo/blob/07fdd5c81f1f6dc7326cd1cfdc67dc64ba7543a1/README.md)
- [Earlier home_plan documentation: October 12 project test and room inference](https://github.com/signerless/tolpo/blob/07fdd5c81f1f6dc7326cd1cfdc67dc64ba7543a1/docs/areas/home_plan.md)

[中文](../tolpo-tapo-claude-lan-3d-home-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
