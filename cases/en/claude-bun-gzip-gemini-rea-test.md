# Claude's Bun single-file build: REA evidence for a Gemini gzip-predicate rewrite

Category: Algorithms and feature recovery · REA
Record date: 2026-10-18
Stage: Analysis test

At 13:15 Beijing time on October 18, @jiangkoumo_ reports investigating Claude's single-file Mach-O program to test what REA can do without Hopper, Ghidra or IDA installed, not to establish automatic reconstruction of the whole client. Only inspect-macho worked, exposing Load Commands and a 175MB __BUN container segment; giving the file directly to the JS analyzer returned unsupported_target. The author calls all three backends commercial, terminology not adopted here because not all three are commercial software.

The author says unbuned extracted the code, after which REA analyzed a 13KB module containing a gzip predicate, producing 2,388 AST nodes and 51 findings. tokenx estimated full Evidence for the 2,451-file directory at 11.43 million tokens; --filter-output reduced the selected key structures to 395 tokens. The scopes differ, so this is not lossless compression. AST evidence and 115 lines of JS were then given to Gemini 3.8 Flash, reportedly rewriting the predicate in one round using 9,352 tokens for about USD 0.0017. The author reports all 69,121 tests constructed against the original logic passed and boundary mutants were killed.

Retrieving the original post confirmed identity and text, not the full fixture, test generator, model trace or bill. Counts, cost and passing results remain the author's self-test claims. The model name is retained as reported, not verified as a service offering. Tests cover only this function and these inputs, not whole-program equivalence, ad removal or recovery of original source. Perplexity credit promotion in the candidate is not evidence of this experiment's cost. No target was downloaded or code run, and no independent reproduction was performed.

October 18 candidate snapshot: 6 likes, 514 views; retrieving the original confirms attribution, not reproduction.
69,121 tests, 9,352 tokens and about USD 0.0017 are author reports; 395 tokens covers only filtered key structures.

## Sources

- [jiangkoumo_'s Mach-O/Bun/gzip experiment account](https://x.com/i/status/2111687633755910612)

[中文](../claude-bun-gzip-gemini-rea-test.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
