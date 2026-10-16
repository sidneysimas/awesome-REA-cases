# jq and Fossify Calculator: REA function identification and early inspection

Category: Algorithms and feature recovery · REA
Record date: 2026-10-17
Stage: Analysis test

At 03:05 Beijing time on October 17, @JohanSlattavik writes in Norwegian that nothing has been reconstructed yet, but REA was tested on a stripped Linux jq 1.8.2 binary, using Ghidra to identify one function and trace it back to original source. jq is a command-line JSON processor; the concrete test concerns locating a known implementation without symbols, not recovering the entire program. The author also says investigation of Android's Fossify Calculator has started, without specific findings for that app. No function name, build parameters, source location, decompiler output or comparison log is supplied for checking. The version is retained as posted without inferring release status. This is an early analysis test, not a completed port or behaviorally equivalent reconstruction.

Explicitly no reconstruction yet; jq 1.8.2 is the author's label, without binary or release-information verification.

## Sources

- [Author's reply about early jq and Fossify tests](https://x.com/i/status/2111171612149985567)

[中文](../rea-jq-fossify-analysis-test.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
