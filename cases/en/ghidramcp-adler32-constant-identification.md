# GhidraMCP: identifying Adler-32 in a stripped binary through constant fingerprints

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-20
Stage: Analysis test

At 21:33 Beijing time on October 20, 2026, the poster describes Claude Code using GhidraMCP on a stripped binary to associate anonymous functions with known checksums and format handling, not reconstruct the whole application. The account claims access through 28 MCP tools, batch decompilation of 170 functions and a 46.7-second search yielding ten candidates. Search clues are the Adler-32 modulus 65521, CRC-32 polynomial 0xEDB88320 and gzip magic 1f 8b. The block size 5552, zlib's NMAX, is then used to support the adler32 identification.

The post supplies short constant-search code over decompiled text and a connection example, but no sample identity, function addresses, exported pseudocode or runtime comparison. Constants are identification clues, not independent proof of function; hitting CRC or gzip constants does not establish recovery of a complete decompressor. Timing, function counts and accuracy remain source claims, not rerun here. REA is not explicit.

## Sources

- [Candidate: GhidraMCP constant screening and Adler-32 identification demonstration](https://x.com/i/status/2112537569800163717)

[中文](../ghidramcp-adler32-constant-identification.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
