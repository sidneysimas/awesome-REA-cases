# PSP/Allegrex analysis

Category: Hardware and interoperability · REA
Record date: 2026-10-12

Sony's PlayStation Portable (PSP) handheld uses a processor called Allegrex. A user wanted REA to analyze programs for this platform, so a contributor integrated Ghidra's Allegrex extension, allowing agents to retrieve functions, assembly and pseudocode. Validation used a self-compiled PSP test program to check known functions and call relationships. This addresses a platform unsupported by a general reverse-engineering workflow, rather than demonstrating a reconstruction of a commercial PSP game.

## Sources

- [Use-case request](https://github.com/morluto/rea/issues/1330)
- [Integration implementation](https://github.com/morluto/rea/pull/1599)

[中文](../psp-allegrex.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
