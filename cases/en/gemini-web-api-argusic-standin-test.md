# Gemini Web To API: an agent installation test against stand-in services only

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-18
Stage: Analysis test

A candidate posted at 06:30 Beijing time on October 18 introduces ntthanh2603/gemini-web-to-api and reports an Argusic agent testing pinned commit 3633170 on a clean machine without human help: two minutes from installation to first launch, an 18-minute session, no errors encountered and a score of 92/100. The quoted agent conclusion says Go 1.27.2 was installed, the project built, /health on port 4981 returned HTTP 200, all nine test suites with over 85 subtests passed, and Gemini authentication with dummy cookies failed as expected. The post explicitly says every test used stand-in services, never real Gemini.

Reading the public README at that commit confirms a Go project that uses web-session cookies to bridge Gemini's web interface into OpenAI-, Claude- and Gemini-compatible REST endpoints, with explicit warnings about account risks and possible Google terms violations. This supplementary pinned documentation explains intended use; it is not a new in-window live test. The project was not run, its dependencies were not installed and no account was used here. This records an agent's limited inspection of a reverse-engineered interface implementation. Build and stand-in success do not establish real Gemini authentication, generation, quota handling or long-term reliability. Nor does this prove AI performed the original protocol reverse engineering; REA use is unconfirmed. The candidate's 592-star project description was not separately checked as a live statistic.

Two minutes, 18 minutes, 92/100 and nine suites with over 85 subtests are reported values; stand-ins only, no real Gemini acceptance test.
Supplementary documentation commit 3633170 has author and committer timestamps of 2026-09-14 05:07:02 UTC; used only to confirm intended use, not a new October 18 live test.

## Sources

- [Argusic installation and stand-in-service test report](https://x.com/i/status/2111585716195004425)
- [Supplement: project documentation at September 14 pinned commit 3633170](https://github.com/ntthanh2603/gemini-web-to-api/blob/3633170/README.md)

[中文](../gemini-web-api-argusic-standin-test.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
