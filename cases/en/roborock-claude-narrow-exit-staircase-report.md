# A Roborock under the stairs: reported Claude-assisted remote-command research to escape a narrow opening

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-24
Stage: Needs verification

At 20:17:00 Beijing time on October 24, 2026, Xiao Tan (@tvytlx) relays a user's problem with a Roborock stored under stairs. Its opening is only a few centimeters wider than the robot, requiring manual steering with the official app's joystick before each cleaning. The user reportedly spent one evening having Claude Code investigate and automate the exit and return while a human observed collisions and Claude wrote code, read logs and tested.

The retelling describes undocumented remote commands used by the app, commands silently ignored for about the first five seconds in remote mode, and an automatic 180-degree turn after undocking. An initial move-right-on-obstruction rule hits a stair pillar. Localization drift is comparable to the clearance, so a fixed path is unreliable. The eventual strategy reverses a few centimeters when stuck and alternates left/right attempts from the nearest angle. Ten consecutive exit-and-dock trials reportedly succeed. Home Assistant on a Raspberry Pi connects to Google Home to start an automatic exit and cleaning, abandoning the attempt and returning to charge on failure.

This is Xiao Tan's secondhand report; the original researcher and research link were not located. The model, firmware, protocol records, source, logs and conditions for the ten trials are unspecified. About five seconds, 180 degrees, one evening and 10/10 all come from the retelling, not evidence for every Roborock or general safety; failure-return behavior is unverified too. REA is not mentioned. The target is narrow-opening maneuver automation, distinct from the existing Roborock home-cloud reconstruction. No device was connected, remote command sent or implementation run here; status remains unverified.

Candidate at 20:17:00 Beijing time; original researcher and research date unknown. One evening, about five seconds, 180 degrees and 10/10 are secondhand reports, not independently reproduced.

## Sources

- [Xiao Tan relays Claude Code-assisted Roborock narrow-exit automation, October 24, 2026](https://x.com/i/status/2113967994909184367)

[中文](../roborock-claude-narrow-exit-staircase-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
