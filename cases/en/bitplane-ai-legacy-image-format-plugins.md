# Amiga .info and legacy image formats: bitplane reports adding readers to Pillow and other tools

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-24
Stage: Needs verification

In his October 24, 2026 AI project list at 17:05:27 Beijing time, davidsong (@bitplane) reports adding Amiga .info support to Pillow, MediaInfo, ImageMagick and other tools. Further Pillow plugins cover Windows MetaFiles, loading screens from ZX Spectrum dumps, Atari DEGAS, AMOS abk and more than forty netpbm formats. The purpose is reading historical files in existing image tools, not generating new pictures.

He explicitly excludes EMF from the Windows MetaFiles work; support must not be broadened beyond that. The post provides no samples, parsing rules, test results or upstream pull requests. AI attribution applies to the overall list without a named model or evidence of REA use. Supplementary reading of amigainfo's README, last changed March 16, 2026 before this window, identifies a separate Python package for loading, saving and converting five generations of icons, including a Pillow plugin. This does not establish an upstream merge.

This records reported format-compatibility work, not confirmation of integration in all three upstream projects, coverage of every file variant or security testing against malicious input. No plugin was installed or target file opened.

EMF is explicitly unsupported; more than forty netpbm formats and upstream support are author claims without inspected pull requests or samples. Supplementary amigainfo documentation lists five icon generations and a Pillow plugin in a separate package, not proof of upstream integration.

## Sources

- [bitplane's legacy-image-format and Pillow-plugin list, October 24, 2026](https://x.com/i/status/2113919789886218477)
- [Supplementary amigainfo README, last changed March 16, 2026](https://github.com/bitplane/amigainfo/blob/627948384e2cc47e7f36477c91fb9aafd3abec0a/README.md)

[中文](../bitplane-ai-legacy-image-format-plugins.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
