# MouseFix: REA and Claude study a 2004 debounce utility and add middle-button and drag-safe modes

Category: Hardware and interoperability · REA
Record date: 2026-10-21
Stage: In progress

At 08:01 Beijing time on October 21, 2026, Felipe Mikeias (felipemikeias) says he used REA and Claude to study the MouseFix double-click utility circulating since 2004, then wrote an open-source replacement from scratch with middle-button support and other improvements. It mitigates worn mice turning one click into two or releasing mid-drag; it does not repair physical switches.

Supplementary repository inspection found commit a7092b4c at 08:02:58 that day, within the candidate window. The original analysis limits its findings by SHA256 to two PE32 files dated January 29, 2004, using objdump headers, imports and disassembly. The original only filters left clicks at a fixed 40 ms, drops presses but passes their unmatched releases, cannot preserve faulty drags and loads a DLL by relative path. The replacement uses an in-process WH_MOUSE_LL hook and one EXE instead of an EXE plus DLL, with five selectable buttons, left-only and 40 ms defaults, and tray controls. Default mode drops a repeated press and its paired release; drag-safe delays every release to absorb bounce, adding release latency. Software-injected events are not filtered.

GitHub Actions run 39518884317 for this exact commit was created at 08:03 and succeeded. That is project build/test evidence, not device reproduction by this collection. The README claims Windows XP through 11 compatibility and describes PE-header/import checks, not demonstrated operation in every system and program. A regular-privilege hook has limits with elevated programs; physical faults still require switch or mouse replacement. No target was executed, real clicks tested or code provenance independently established here. Finding no malicious behavior in the analyzed original files is not a safety guarantee for every downloaded copy.

Evidence boundary: project CI for a7092b4c succeeded; no mouse was tested here, and software debouncing cannot repair physical switches.

## Sources

- [Felipe Mikeias on REA/Claude and the MouseFix replacement](https://x.com/i/status/2112695748374749631)
- [MouseFix README at a7092b4c: modes and limitations](https://github.com/felipemikeias/MouseFix/blob/a7092b4ce524cceab259ccd1c6ca460765f2fed0/README.md)
- [Original-binary analysis and hash scope at the same commit](https://github.com/felipemikeias/MouseFix/blob/a7092b4ce524cceab259ccd1c6ca460765f2fed0/docs/original-analysis.md)
- [Successful project CI for the exact commit](https://github.com/felipemikeias/MouseFix/actions/runs/39518884317)

[中文](../mousefix-rea-claude-middle-button.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
