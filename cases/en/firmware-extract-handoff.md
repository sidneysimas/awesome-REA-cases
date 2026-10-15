# Layered firmware: extraction to Ghidra

Category: Hardware and interoperability · REA
Record date: 2026-10-12

Device firmware often combines compressed data, file systems and executables in one image. Using self-generated gzip, USTAR and ext4 images and a host ELF, a contributor verified a workflow in which REA calls Binwalk to identify regions, Unblob to extract them, checks exported-file hashes, and hands the extracted ELF to Ghidra to read functions and pseudocode. This bridges a monolithic image and analyzable files. It is a toolchain example with controlled provenance, not evidence that a particular router or unknown device has been cracked.

## Sources

- [Original PR and toolchain validation](https://github.com/morluto/rea/pull/741)

[中文](../firmware-extract-handoff.md) | [Back to editor picks](../../README.en.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/hardware.md)
