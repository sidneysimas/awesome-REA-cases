# Chrome: Anthropic reports its internal model chaining browser bugs and sandbox escape

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-29
Stage: Analysis test

At 09:33:04 Beijing time on October 29, 2026, a report signed Ummon cites Anthropic's 'Discovering and exploiting vulnerabilities in critical, real-world software with Claude,' describing months of browser/OS research with an unreleased, unnamed internal model. The Chrome target is execution outside the sandbox from webpage input, involving V8 memory corruption, a V8 memory-region boundary bypass, a CacheStorage race and a FedCM use-after-free. This records the research shape without reproduction payloads.

Supplementary reading obtained the official article, dated October 27, before the candidate, not newly published that day as the retelling suggests. The official text reports launching Calculator seconds after page load in default-configuration Chrome on macOS without further interaction. It says Google assigned 62 high/critical CVEs patched by Chrome 156, including 13 sandbox escapes and 21 renderer-compromise opportunities. The subcategories are not arbitrarily added together; 62 is not the flaw count of this single chain.

This collection confirmed consistency with the official project report, without reading vendor advisories or running the demonstration. The official account starts with initial human prompting; 'little human involvement' does not mean full autonomy, and the internal model is not equated with named models in the access program. It describes 90 days to patch plus 45 days before detailed disclosure. No in-the-wild exploitation or victims are reported, which is not proof that none exist. CVEs and patching remain Anthropic's characterization of Google's response, not safety certification here. REA is unspecified.

Shared candidate snapshot: 0 likes, 157 views, 0 reposts. Five independent targets in one post are recorded separately.
The October 27 official research was read; Google advisories, PoCs and CVEs were not independently checked. No attack payloads included.

## Sources

- [The Chrome investigation in Ummon's full report, October 29, 2026](https://x.com/i/status/2115617884533907835)
- [Supplementary original research: Anthropic's Chrome section, published October 27](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude#1-one-click-remote-code-execution-in-chrome)

[中文](../anthropic-internal-claude-chrome-chain-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
