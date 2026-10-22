# Private-source NuGet eval: Aaron Stannard tests whether agents choose ILSpy without prompting

Category: Applications and clients · Other AI-assisted work
Record date: 2026-10-22
Stage: In progress

At 22:35:50 Beijing time on October 22, 2026, Aaron Stannard (@Aaronontheweb) says he is adding a fourth agent evaluation using a package available on NuGet but with private source. He wants the agent to decide on decompilation itself rather than receiving that suggestion in the prompt. NuGet distributes .NET packages and ILSpy decompiles .NET assemblies; the experiment concerns tool choice, not complete source recovery of a particular app.

A supplementary read of the 22:35:08 thread root finds his observation that Anthropic models usually search for GitHub source first, with ILSpy their fourth preference. Subsequent posts warn that eval design can skew results. He proposes comparing token efficiency of GitHub source fetching with ILSpy but explicitly says the necessary infrastructure has not been added. He also identifies Claude SDK versus his DSpy harness as a potential variable. At 22:43:11 he says he raised the eval token budget to 200k and observes that Opus prefers writing small reproduction programs, making it the least token-efficient model in his experiment.

The fourth private-package evaluation was still being added when the candidate was posted; the root's observations are not results of a completed fourth test. The retrieved text gives no package name, model versions, sample count, prompts, detailed preference-ranking table or inspectable eval logs. 200k is a budget, not actual consumption per run, and establishes neither cost nor general model superiority. This collection read only the author's text and attachment information and ran no evaluations. REA is not mentioned. The project remains in progress.

Candidate originally posted 2026-10-22T22:35:50+08:00; supplementary thread at 22:35-22:43 that day. Adding an evaluation is not passing it.

## Sources

- [Candidate: adding a private-source NuGet eval without suggesting decompilation](https://x.com/i/status/2113278157549711521)
- [Supplementary thread root: reported GitHub-first behavior and ILSpy fourth preference](https://x.com/i/status/2113277981955346792)
- [Supplementary thread: token-efficiency measurement infrastructure not yet added](https://x.com/i/status/2113278992975597665)
- [Supplementary thread: 200k budget and observations of Opus reproduction programs](https://x.com/i/status/2113280008794075202)

[中文](../aaron-stannard-nuget-ilspy-agent-evals.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
