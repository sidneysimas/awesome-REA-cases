# Kaggle code embeddings: GNN imitation of an undisclosed generator for Gemma 4 post-training

Category: Algorithms and feature recovery · Other AI-assisted work
Record date: 2026-10-19
Stage: In progress

At 19:29 Beijing time on October 19, @vbnakrani (Vaibhav) reports investigating official code graphs and embeddings while post-training Gemma 4 for a Kaggle competition. External tasks such as SWE-Gym and SWE-smith need graphs and 256-dimensional per-node vectors resembling the official tasks, supporting three agent tools: similar-code search, neighbor lookup and local-subgraph retrieval. The author says an e2b A/B solved more with these tools, but provides no task count or score.

The call graph represents functions, methods and classes as nodes and calls as edges. The author reports an AST parser exactly matching all 127 official graphs, approximately 368k nodes and 226k edges. The harder target is about 368k official vectors whose source is undisclosed. From identical text changing vectors when neighbors differ, the author infers a GNN using raw node and neighbor code. That is an experimental inference, not organizer confirmation. Testing about 30 public encoders, including EmbeddingGemma, CodeGemma, Qwen3-Embedding, UniXcoder, CodeBERT, CodeT5+, BGE, E5 and nomic, reportedly identified none as the source. Reported R² values are 0.28–0.42, compared with 0.40 for character TF-IDF.

A small GNN is therefore being trained to imitate official vectors. Untuned ranking agreement is reported as 0.84 within a repository but only 0.08–0.24 on unseen repositories, precisely the intended external-data use. A 60-configuration sweep over loss, input features and depth/width is ongoing; dropping similar-code search remains a fallback. No verifiable competition name, public code, vectors, raw measurements or holdout split was obtained. This collection neither trained a model nor reran experiments. Exact graph matches and all figures remain the author's report, not successful recovery of the official embedding generator or cross-repository generalization. REA use is unconfirmed.

October 19 candidate snapshot: 0 likes, 9 views and 0 reposts; low engagement does not preclude collecting a concrete ongoing experiment.

## Sources

- [Vaibhav's report on Kaggle code graphs, vector imitation and cross-repository failure](https://x.com/i/status/2112144008856375798)

[中文](../kaggle-code-graph-embedding-gnn-imitation.md) | [Back to editor picks](../../README.md) | [Full index](../../INDEX.en.md) | [Category](../../categories/en/algorithms.md)
