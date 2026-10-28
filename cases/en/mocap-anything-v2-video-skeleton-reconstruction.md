# MoCap Anything V2: a report on reconstructing reference-skeleton rotations from video

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-28
Stage: Needs verification

At 23:45 Beijing time on October 28, 2026, a long post introduces MoCap Anything V2: ordinary video plus a reference skeleton/pose yields editable skeletal rotations, with BVH and NumPy joint positions/rotations for humans, animals, fantasy characters and custom FBX rigs. Instead of the earlier mesh reconstruction and analytical IK pipeline, it describes DINOv2 features, direct Video-to-Pose 3D joints, learned Pose-to-Rotation, local/global GL-GMHA skeletal attention and joint training of both stages.

Citing the paper, it claims 120 frames take under a minute instead of over 20 minutes, with about ten seconds of neural prediction excluding shared feature extraction. Roughly 20× refers to offline end-to-end processing, not real-time playback speed. Reported animal rotation error falls from about 17° to 10°; Zoo-Unseen results are 6.54° rotation error and 3.39cm joint-position error. Evaluation mentions 1,038 Truebones Zoo sequences and 1,000 Objaverse samples. Dance Anything reportedly uses SAM2 performer segmentation and retains music. Approximately 464MB weights, a Gradio/ZeroGPU demo and MIT code are likewise report claims; links were not independently checked.

The full post explicitly says the public implementation is a reimplementation whose results may differ from the original paper. Occlusion, unusual cross-species motion, reference-skeleton requirements, FBX preprocessing and a relatively small animal training set remain limitations. This is related AI reconstruction of structured motion from visible behavior, not software decompilation. Original paper, repository and demo were not inspected or run. Performance, errors, licensing and release artifacts are attributed to the report, not independently measured or guaranteed for arbitrary videos. REA is not mentioned.

Candidate snapshot: 0 likes, 129 views, 0 reposts. Full long post read; research benchmarks are not independent measurements here.

## Sources

- [Full MoCap Anything V2 technical account and limitations, October 28, 2026](https://x.com/i/status/2115469893378117928)

[中文](../mocap-anything-v2-video-skeleton-reconstruction.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
