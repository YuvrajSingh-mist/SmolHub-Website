---
title: "DDP"
excerpt: "Llama trained with PyTorch DistributedDataParallel (torchrun). Val loss 1.1 in 8,000 iterations on TinyShakespeare."
collection: models
layout: model-implementation
category: "Training Methods"
framework: "PyTorch"
dataset: "TinyShakespeare"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/DDP"
date: 2025-04-25
stars: 416
---

## Overview

Experiments with PyTorch DistributedDataParallel (DDP) via `torchrun` for multi-GPU training. The base model is a small Llama variant. Focus is on the DDP training loop: process-group init, gradient synchronisation across ranks, and checkpoint management.

## Architecture (base model)

- Llama-style decoder-only transformer
- 6 attention heads, 6 decoder layers, 384-dim, 2 KV heads (GQA)
- 128-token block size

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | TinyShakespeare |
| Iterations | 8,000 (val every 100) |
| Optimizer | AdamW, lr=1e-4 |
| Batch size | 64 |

## Results

| Split | Loss |
|---|---|
| Train | 1.5 |
| Validation | **1.1** |
