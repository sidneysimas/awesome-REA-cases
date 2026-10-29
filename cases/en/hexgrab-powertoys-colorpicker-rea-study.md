# hexgrab: Claude/REA studies PowerToys Color Picker, with one of nine claims only partly right

Category: Applications and clients · REA
Record date: 2026-10-29
Stage: Analysis test

At 16:50:03 Beijing time on October 29, 2026, Mukesh Murugan (@iammukeshm) reports spending a day investigating Microsoft PowerToys Color Picker with Claude Code and REA before reading its source, then building his own .NET 10 picker, hexgrab. Supplementary reading obtained the same author's README and docs/rea-findings.md at commit 511c58078776af4fb0d2e3601e098f98e9f90c9a, timestamped October 12, 22:35:07Z. The investigation document is dated October 12. These are pre-window evidence, not a claim that development happened on the announcement date.

The investigation targets the managed ColorPickerUI.dll and native ColorPicker.dll from PowerToys 0.98.0, documenting REA 6.4.0 and Ghidra 12.1.4. It inspects managed types and call boundaries, then native strings, cross-references and pseudocode, exporting evidence. The first string hit was a logging wrapper, requiring examination of its caller; Ghidra's library-prefixed import names also caused a name-based reference query to fail. The author later grades nine claims against public source: eight fully correct, one partial. The native module handles hotkeys but the runner registers them; that runner was outside the analyzed binaries. This is an author's finite scorecard, not general accuracy or this collection's independent comparison.

The public hexgrab implementation samples screen pixels with Win+Shift+H and copies HEX. Timer polling captures changing content under a still cursor, and clipboard writes retry. It deliberately avoids PowerToys' system cursor-scheme changes. The project reports no NuGet packages and fewer than 750 C# lines including comments, with HEX only and no history, magnifier or settings yet. A public end-to-end script describes checks for hotkeys, swallowed clicks, cancellation, Enter, hook removal and changing colors, but was not run here.

The README reports testing on one monitor at 125% scale; mixed-DPI multiple monitors are not hardware-tested. Release executables are unsigned; a download does not establish safety. The author says no PowerToys code was copied and public source was only used for grading. That is attribution and a licensing statement, not a legal guarantee. This collection did not download executables, install target dependencies or reproduce desktop tests.

Candidate snapshot: 12 likes, 630 views, 2 reposts. One day is the author's time claim; source commit and investigation predate the window.
Eight of nine fully correct, one partly correct. Source grading and desktop tests were not independently rerun; releases are unsigned and mixed-DPI multi-monitor use untested.

## Sources

- [Mukesh reports the PowerToys investigation and hexgrab, October 29, 2026](https://x.com/i/status/2115727855669641216)
- [Supplementary: October 12 pinned hexgrab README, implementation scope and limitations](https://github.com/iammukeshm/hexgrab/blob/511c58078776af4fb0d2e3601e098f98e9f90c9a/README.md)
- [Supplementary: October 12 REA investigation and nine-claim author scorecard for PowerToys 0.98.0](https://github.com/iammukeshm/hexgrab/blob/511c58078776af4fb0d2e3601e098f98e9f90c9a/docs/rea-findings.md)

[中文](../hexgrab-powertoys-colorpicker-rea-study.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
