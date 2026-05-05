---
title: "DeepSeekV3"
excerpt: "16×4 MoE with Multi-head Latent Attention and auxiliary-free load balancing, trained on TinyStories on Kaggle P100."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "TinyStories"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/DeepSeekV3"
date: 2025-08-06
stars: 416
---

## Overview

From-scratch replication of DeepSeek-V3. Two key innovations: Multi-head Latent Attention (MLA) which compresses KV-cache via a low-rank bottleneck, and auxiliary-free load balancing that avoids gradient interference from explicit balancing losses. Also implements multi-token prediction. Based on *DeepSeek-V3 Technical Report* (DeepSeek-AI, 2024).

## Architecture

- **MoE**: 16 experts, top-4 routing, 1 shared expert
- **Load balancing**: Auxiliary-free (bias-based routing)
- **Attention**: MLA with 64-dim KV latent, 8 heads
- **MTP**: 1 auxiliary multi-token prediction head
- **Config**: 512-dim, 8 decoder layers, 256-token context

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | TinyStories (~300M tokens via grad accumulation) |
| Optimizer | AdamW, lr=6e-4 |
| Batch size | 32, loss scale=0.3 |
| Hardware | Kaggle P100 |

## Paper

[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) — DeepSeek-AI, 2024
