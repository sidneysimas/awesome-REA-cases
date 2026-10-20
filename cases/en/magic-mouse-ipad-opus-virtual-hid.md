# MagicSwipe: Opus-assisted Magic Mouse gestures for iPad Universal Control

Category: Hardware and interoperability · Other AI-assisted work
Record date: 2026-10-20
Stage: In progress

At 07:46 Beijing time on October 20, saikumar (@saikumar2729) says Opus 5.5 investigated missing two-finger Magic Mouse gestures when controlling an iPad through Universal Control in one session. It reads touches through Apple's private MultitouchSupport framework and sends Globe shortcuts through Karabiner's open-source virtual HID driver. The author reports left/right swipes switching apps, an upward swipe or two-finger double-tap opening the App Switcher, and a downward swipe going home, enabled only while the pointer is on the iPad. A hashtag mentions REA, but the narrative gives no explicit REA steps; this is classified as other AI-assisted work.

Supplementary reading covered the public MagicSwipe README and app/main.m at commit f8379a0e6f2aa3af9d22f0846f482321b3417876 (October 19, 09:45 Beijing time, before this window). Code shows private touch callbacks, Universal Control notify-state bits 0x2/0x1, gesture recognition and commands sent to keyd. The README explains that ordinary CGEvent or AppleScript keystrokes are not forwarded, requiring HID-level input and, when necessary, virtual mouse button 4 to move keyboard focus. This substitutes keyboard shortcuts; it does not restore continuous, draggable native trackpad gestures.

The project reports testing macOS 27, a Magic Mouse with Bluetooth product ID 0x0269 and an iPad. Installation requires administrator privileges and Karabiner DriverKit 8.5.0 (protocol 7); some helpers run as root. Private interfaces may break after OS updates. Swipes slightly scroll the underlying page, whereas double-taps do not. The commit credits Claude Opus 5.5 as co-author, which is not independent execution evidence. This collection read public documentation and source only, without installing drivers, executing target code or testing devices.

Candidate snapshot: 2 likes, 17 views and 0 reposts; very early circulation, not compatibility verification.

## Sources

- [saikumar's Opus gesture investigation and demo post](https://x.com/i/status/2112329554731630682)
- [Earlier fixed-commit README: test setup, privileges and limitations](https://github.com/sai2729/MagicSwipe/blob/f8379a0e6f2aa3af9d22f0846f482321b3417876/README.md)
- [Same-commit gesture recognition and Universal Control state source](https://github.com/sai2729/MagicSwipe/blob/f8379a0e6f2aa3af9d22f0846f482321b3417876/app/main.m)

[中文](../magic-mouse-ipad-opus-virtual-hid.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
