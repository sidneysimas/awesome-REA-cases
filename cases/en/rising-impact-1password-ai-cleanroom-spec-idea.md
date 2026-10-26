# 1Password's public design: Rising Impact proposes AI-assisted observation, specification and testing

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-25
Stage: Needs verification

At 18:11:56 Beijing time on October 25, 2026, Rising Impact (@KrEarthMilkyway) published a Korean design-research proposal targeting the 1Password password manager. It advocates observing product behavior and public documentation, then expressing requirements, architecture and data flow in one's own words rather than obtaining original code. Its six steps are recording signup/login/save/autofill journeys; consulting whitepapers and official documentation; extracting requirements; hypothesizing components and sequences; black-box testing public features through one's own account; and drafting an isolated reconstruction specification.

The proposed AI roles are document search and sourced summaries, browser-based workflow recording, and requirements/mermaid-diagram drafting, with unsupported claims explicitly marked unconfirmed. As discussion material, the post describes password-plus-Secret-Key 2SKD, 650,000 rounds of PBKDF2-HMAC-SHA256 XORed with an HKDF result to obtain the AUK, differently salted SRP authentication secrets, AES-256-GCM vault data, RSA-OAEP private-key protection, and Watchtower, Travel Mode and Passkeys. These are the poster's design summaries. This collection did not check every cryptographic detail, iteration parameter or assertion about where a feature runs, and does not present them as independently validated 1Password specifications.

The proposal also calls for checking service terms, separating specification authors from implementers, and avoiding protection bypass, secret extraction or copying code, UI or trademarks. This entry records a specific AI-assisted design-recovery idea: no completed specification, implementation, test or security assessment is supplied, and there is no evidence of actually running morluto/rea. Reading public design is not breaking the password manager and does not establish legal approval of the proposed isolation method.

A specific teaching idea without execution or implementation; REA is used as a method concept, with use of the namesake tool unconfirmed.
Cryptographic details are the poster's summary, not a product specification or legal conclusion verified by this collection.

## Sources

- [Rising Impact's proposal for studying 1Password's public design, October 25, 2026](https://x.com/i/status/2114298908964729320)

[中文](../rising-impact-1password-ai-cleanroom-spec-idea.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
