# CF632BLE: a local Web Bluetooth scale client

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-12
Stage: Needs verification

guyru wanted direct use of a personally owned smart body-fat scale and reports using Claude Code connected to ghidra-rpc to study its BLE (Bluetooth Low Energy) protocol, first writing Python and then switching to Web Bluetooth. The corresponding CF632BLE repository says the protocol and body-composition algorithm came from analysis of the Unique Health Android app. The webpage calculates locally and stores measurement history without the manufacturer's backend. Source is public, and the author reports good results. This collection did not connect a device or verify health-metric accuracy. Web Bluetooth requires Chromium and is unsupported on Safari/iOS.

Posted: 2026-10-12T16:48:02+08:00 (Beijing time)
Engagement snapshot (2026-10-12): 2 likes | 94 views | 0 reposts

## Sources

- [Author report from this review](https://x.com/guyru_/status/2109566754540392730)
- [Public implementation and device limitations](https://github.com/guyru/cf632ble)

[中文](../cf632ble-web-bluetooth.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
