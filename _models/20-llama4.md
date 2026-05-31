---
title: "Llama4"
excerpt: "1.2B-parameter MoE (32×12M experts, top-1 routing) trained on TinyStories. Val loss 1.70 in 20k steps on Kaggle P100."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "TinyStories"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Llama4"
date: 2025-05-01
stars: 419
---

## Overview

From-scratch replication of the Llama 4 Mixture-of-Experts architecture at 1.2B total parameters. Trained to convergence on a Kaggle P100 over 20,000 iterations using Liger kernels for memory efficiency.

## Architecture

- **Experts**: 32 experts (12M params each), top-1 routing, 1 shared expert
- **Load balancing**: Auxiliary-free loss
- **Context window**: 1,024 tokens
- **Config**: 768-dim embeddings, 8 heads, 8 decoder layers
- **Kernels**: Liger kernels for fused ops

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | TinyStories (~4.2B tokens, 1 epoch) |
| Iterations | 20,000 |
| Optimizer | AdamW, lr=6e-4 |
| Batch size | 16 |
| Gradient clipping | 1.0 |
| Hardware | Kaggle P100 |

## Results

| Split | Loss |
|---|---|
| Train | 2.08 |
| Validation | **1.70** |

## Paper

[Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) — Meta AI, 2025
