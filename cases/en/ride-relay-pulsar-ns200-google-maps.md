# Ride Relay: OpenCode and DeepSeek relay Google Maps turns to a Pulsar NS200 instrument cluster

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-22
Stage: Needs verification

The deferred candidate was originally posted at 15:55:21 Beijing time on October 22, 2026, in the earlier 12:00-16:00 window, not newly collected in the 16:00-20:00 window. Manovikram K (@manov_ik) says he used OpenCode with DeepSeek V4.1 Flash Free to build and debug an Android app combining reverse engineering and Bluetooth protocols, and reports it working on the actual bike.

Supplementary reads of the same thread's 15:55:17 root and 15:55:19 feature explanation identify the Bajaj Pulsar NS200 motorcycle instrument cluster. The official Bajaj app already supports navigation, but he wanted Google Maps, so he had OpenCode help investigate the official app and build a separate Ride Relay solution. It reads Google Maps navigation notifications, extracts turn direction and distance, converts them into the cluster's expected Bluetooth packets and sends them. He says neither root nor a modified official APK is needed. This is a notification-to-cluster bridge, not a full Google Maps port into the bike and not an electric-bicycle project.

The sources provide no packet fields, captures, repository body, firmware version, notification-permission configuration, compatibility list or vehicle-test logs. Free is the reported model name/tier, not a guarantee of permanently free service. The author says to use it at one's own risk, and actual-bike operation remains self-reported. REA is not mentioned. This collection installed no app, connected to no vehicle and did not verify riding safety.

Candidate originally posted 2026-10-22T15:55:21+08:00; supplementary thread posts at 15:55:17 and 15:55:19 that day, all from the earlier window.

## Sources

- [Deferred candidate: DeepSeek, OpenCode and reported actual-bike operation](https://x.com/i/status/2113177372178759943)
- [Supplementary thread root: Bajaj Pulsar NS200 and Google Maps goal](https://x.com/i/status/2113177358220079353)
- [Supplementary thread: Ride Relay notification/Bluetooth bridge](https://x.com/i/status/2113177366969422029)

[中文](../ride-relay-pulsar-ns200-google-maps.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
