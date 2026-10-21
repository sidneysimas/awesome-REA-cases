# Meta glasses putting coach: unverified HCI/jadx research and an AR proposal

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-20
Stage: Needs verification

At 22:25 Beijing time on October 20, 2026, a post attributed to 0xCodez claims Opus 5.5 turned Meta Ray-Ban glasses into a putting coach with one prompt in twenty minutes. It describes Bluetooth HCI capture and jadx analysis of Meta AI, then four tmux agents for video, vision, physics and UI, claiming whatever the phone renders appears in the lens. The immediately following full prompt specifies Ray-Ban Meta 2 and Android, calls for tshark log parsing and checking Meta's Device Access Toolkit, and requires recorded-footage tests before connecting glasses.

The proposal combines monocular SLAM, Depth Anything V2 and metric calibration using a 42.67 mm ball and 108 mm cup to create a 5 cm grid. It requests 1 cm elevation contours, YOLO target detection and RK4 integration in 1 ms steps to search for a putt finishing 17 inches beyond the cup, plus MediaPipe fingertip menus. Sub-100 ms end-to-end latency is a requested acceptance target, not a measurement. The author calls the video a practice green and says slope readers are prohibited in competition. A Chinese account at 22:46 on October 20 repeats the same promotion, not a reproduction.

Supplementary reading of Meta's official Android DAT README at a commit dated October 10 at 02:23 Beijing time explicitly scopes Display features to Meta Ray-Ban Display glasses. The prompt's Ray-Ban Meta 2 cannot be assumed to have in-lens display capability merely from Bluetooth access or decompilation. No confirmed hardware identity, source, overlay transport protocol, depth accuracy or device-latency tests were obtained. This remains a concrete target and unverified proposal, not confirmation of a twenty-minute implementation or working AR projection, and is distinct from voice-assistant replacement clients.

## Sources

- [0xCodez's putting-coach feature and twenty-minute claim](https://x.com/i/status/2112550881950396884)
- [Full prompt in the same thread: HCI, vision, physics and UI acceptance targets](https://x.com/i/status/2112550885452623952)
- [Supplementary technical boundary: Display device scope in Meta's official DAT README](https://github.com/facebook/meta-wearables-dat-android/blob/f4371bc9f90249d51eb07d7f8a61e8d829294f16/README.md)

[中文](../meta-rayban-golf-coach-claim.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
