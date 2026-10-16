# Claude Chrome on remote browsers

Category: Applications and clients · REA use unconfirmed
Record date: 2026-10-12

Paul Klein IV wanted Claude Code to use remote browsers as well as local Chrome. He studied Claude Chrome's native messaging: messages use a four-byte length prefix and JSON to carry navigation, screenshot, click and other tool calls. He then built a service that intercepts browser connections, translates commands into CDP and sends them to Browserbase cloud browsers. The thread provides demonstrations and a plugin entry point. This demonstrates browser interoperability for AI tools, not that AI itself performed all the reverse engineering.

Posted: 2025-12-29 (UTC) | @pk_iv
Engagement snapshot (2026-10-12): 2,263 likes | 395,773 views | 181 reposts

## Sources

- [Author's original post](https://x.com/pk_iv/status/2005694082627297735)
- [Public implementation](https://github.com/browserbase/claude-code-plugin)

[中文](../claude-chrome-remote.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
