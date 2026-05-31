---
title: "Seq2Seq"
excerpt: "GRU-based Seq2Seq with both Bahdanau and Luong attention from scratch. 128 hidden units, 50 epochs."
collection: models
layout: model-implementation
category: "Sequential Models"
framework: "PyTorch"
dataset: "Custom"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Seq2Seq"
date: 2025-04-25
stars: 419
---

## Overview

From-scratch GRU-based Seq2Seq with attention, implementing both Bahdanau (additive) and Luong (multiplicative) attention variants. Extends the vanilla encoder-decoder by letting the decoder dynamically attend to all encoder hidden states at each step, eliminating the fixed-length bottleneck. Based on *Sequence to Sequence Learning with Neural Networks* (Sutskever et al., 2014) plus the attention papers from Bahdanau and Luong.

## Architecture

- GRU encoder and decoder
- 128 hidden units per GRU layer
- FFN hidden = 4× embedding dim
- Sequence length: 32
- **Attention**: Bahdanau (additive) and Luong (dot/general) — both implemented

## Training

| Hyperparameter | Value |
|---|---|
| Epochs | 50 |
| Optimizer | Adam, lr=1e-4 |
| Batch size | 32 |
| Dropout | 0.1 |

## Papers

- [Seq2Seq](https://arxiv.org/abs/1409.3215) — Sutskever et al., 2014
- [Bahdanau Attention](https://arxiv.org/abs/1409.0473) — Bahdanau et al., 2015
- [Luong Attention](https://arxiv.org/abs/1508.04025) — Luong et al., 2015
