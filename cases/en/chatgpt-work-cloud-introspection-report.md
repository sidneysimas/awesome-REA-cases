# ChatGPT Work Cloud: probing a cloud agent's tools through introspection

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-16
Stage: Needs verification

An October 16 Chinese-language post recounts Simon Willison's investigation of ChatGPT Work Cloud. He reportedly asked the system to find London locations featuring the Pelican in her piety symbol, organize JSON and build a website, with search, cleaning and publication reportedly completed. Introspective prompts then reportedly exposed 44 Skills and 223 miniature Tools, together with networking, code execution, headless Chrome, a cross-session workspace and deployment through Cloudflare Workers, D1 and R2. The goal is to understand how a cloud agent links research to delivery and what data and networks it can access, not to recover the service's source code. This entry records the post's secondhand account of Willison; the original test records were not obtained and the figures were not reproduced. Introspective output does not itself prove backend permissions. Its discussion of prompt-injection risk when private data, untrusted content and outbound access coexist does not establish an actual leak. Codex-like review and sandboxing are speculation in the post, not confirmed public Work Cloud mechanisms. REA is not mentioned.

Source published: 2026-10-16 16:22 Beijing time; secondhand report, tool inventory and deployment test not independently verified.

## Sources

- [October 16 account of Willison's Work Cloud investigation](https://x.com/i/status/2111009945865097386)

[中文](../chatgpt-work-cloud-introspection-report.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
