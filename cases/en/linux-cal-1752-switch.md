# Linux cal: tracing the 1752 calendar switch

Category: Applications and clients · REA
Record date: 2026-10-15

The poster reports inspecting Linux's calendar command with OpenCode, Ghidra and REA, locating a hard-coded 1752-09-02 transition rule in a stripped binary without function names. The post claims the location was found in about 1.5 minutes, says the analysis includes evidence and notes that AI marked untraced portions. The author then reports that changing country or using the Julian calendar restores September's missing dates. This is the post's analysis and manual-test report, without independent retesting; it does not claim reconstruction of the entire program.

Posted: 2026-10-15 (input record time)
REA use, analysis and country/calendar-switch tests are all original-post claims, not independently checked.

## Sources

- [Author's hands-on REA demonstration post (includes video link)](https://x.com/i/status/2110453427209916612)

[中文](../linux-cal-1752-switch.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
