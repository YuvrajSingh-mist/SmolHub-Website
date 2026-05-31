---
title: "Transformer"
excerpt: "Encoder-decoder transformer for English→Hindi translation on Samanantar (~25M params). Published on HuggingFace."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "Samanantar"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Transformer"
date: 2025-03-10
stars: 419
---

## Overview

Full encoder-decoder transformer for English-to-Hindi neural machine translation, dubbed **SmolTransformer**. Replicates *Attention Is All You Need* (Vaswani et al., 2017) and is published on HuggingFace.

## Architecture

- 6-layer encoder + 6-layer decoder
- Multi-head self-attention + cross-attention
- Sinusoidal positional embeddings
- ~25M parameters, 512-token context window
- IndicBARTSS tokenizer (~30K vocab)
- Supports top-K sampling and beam search at inference

## Training

- **Dataset**: Samanantar (large-scale English–Hindi parallel corpus)
- **Techniques**: Automatic mixed precision, gradient accumulation
- **Tracking**: WandB (loss, perplexity, gradient norms)

## Published Model

[HuggingFace — YuvrajSingh9886/SmolTransformer](https://huggingface.co/YuvrajSingh9886/SmolTransformer)

## Paper

[Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Vaswani et al., 2017
