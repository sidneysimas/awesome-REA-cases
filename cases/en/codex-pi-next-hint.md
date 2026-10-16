# Codex next-input prediction recreated for Pi

Category: Applications and clients · REA use unconfirmed
Record date: 2026-10-15
Stage: Needs verification

The author wanted Codex's next-message prediction for Pro users in Pi, reports reverse-engineering its prompt and remote-configuration version 5, and released pi-next-hint. The candidate thread describes a separate prediction request after each turn, high reasoning effort, a 30-second deadline, no automatic retries and only recent messages. Hints appear only when the input is empty and are never sent automatically. The author says the same-version prompt was retained and adapted to Pi's JSON format. Configuration and implementation are author reports, not OpenAI specifications. Code and prediction quality were not independently checked, and REA use is unconfirmed.

Main-post candidate snapshot: 1 like | 16 views; features are author-reported.

## Sources

- [Author's project introduction](https://x.com/i/status/2110631522403512760)
- [Configuration and behavior described in candidate thread](https://x.com/i/status/2110631530683068722)

[中文](../codex-pi-next-hint.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
