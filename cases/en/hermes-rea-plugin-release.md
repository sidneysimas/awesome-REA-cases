# Hermes REA plugin: a reported MCP and adapted Skill release

Category: Applications and clients · REA
Record date: 2026-10-17
Stage: Related project

An earlier circulating post says an official Hermes REA plugin installs REA MCP and an adapted reverse-engineer-anything Skill together, with roughly 170 tools discoverable through tool search for native binaries, .NET, Electron, Android packages, firmware, browser captures and live process activity. It names hermes plugins install rea, Hermes 0.22.1 and Node, with Ghidra, Hopper or IDA separately required for native decompilation, and says the Skill asks before running programs or changing devices. That poster only planned to install that night: official attribution, versions, counts and permission guidance remain secondhand, not installation tests by this collection. At 13:44 Beijing time on October 16, @wyant_dalto says REA and MCP were added to their own Hermes a day or two earlier, reports inadequate Python reverse engineering, mentions jadx 1.5.6, pycdc-rapid and Ghidra, and says these were also added locally. This is user integration experience and a request, not an official Python compatibility matrix or proof that all software can be reverse engineered. No configuration, target sample, log or acceptance test is provided. This collection did not install or execute anything, and the user's additional tools are not presented as official plugin features. This remains distinct from the Hermes/WinSCP import test and implies neither universal version support nor enforced interception of every sensitive operation.

An engineering digest at 02:50 Beijing time on October 17 says the plugin needs Node.js 22.19 or newer, still with Ghidra, Hopper or IDA separately needed for native analysis. Some tools can run commands, drive apps, change Android devices or overwrite files without a Hermes prompt: Skill instructions to ask first are not enforced runtime approval. The digest also says the first pin could not install on 0.22.2 because of a newer manifest key, was re-pinned that day, and main now warns on newer keys. These are version and repair accounts, not commit, catalog or installation checks here. Main changes or re-pinning do not establish fixes in every installed version.

Earlier October 16 candidate snapshot: 6 likes, 549 views; plugin scope and roughly 170 tools are post claims, not tests by this collection.
13:44 user candidate snapshot: 0 likes, 19 views; the Python gap and extra integrations are user reports, not official support conclusions.
The October 17, 02:50 digest's 0.22.2 compatibility and re-pinning claims were not checked against commits or installation; Skill guidance is not enforced approval for all tools.

## Sources

- [Secondhand Hermes REA plugin release and usage-boundary introduction](https://x.com/i/status/2110805485939249561)
- [October 16 user report of REA MCP and additional tool integration](https://x.com/i/status/2110970183372116411)
- [October 17 engineering digest: pin compatibility and side-effect prompt limits](https://x.com/i/status/2111167832037954013)

[中文](../hermes-rea-plugin-release.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/apps.md)
