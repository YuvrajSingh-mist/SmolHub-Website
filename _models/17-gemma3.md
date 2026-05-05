---
title: "Gemma3"
excerpt: "90M-parameter Gemma 3 with local sliding-window attention (128-token blocks). Val loss 1.77 in 25k steps on TinyStories."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "TinyStories"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Gemma3"
date: 2025-05-01
stars: 416
---

## Overview

From-scratch 90M-parameter replication of Gemma 3 trained on TinyStories. The key change from Gemma 2 is local sliding-window attention with fixed block sizes, which reduces memory for long sequences without sacrificing context quality.

## Architecture

- **Parameters**: ~90M
- **Layers**: 6 decoder layers
- **Attention**: 8 heads, 2 KV heads (MQA), 128-token sliding window
- **Embedding dim**: 512, vocab size 32,768
- **Regularisation**: Dropout 0.1

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | TinyStories |
| Steps | 25,000 (val every 500) |
| Optimizer | Adam, lr=2.5e-4, weight decay=0.1 |
| Sequence length | 256 |

## Results

| Split | Loss |
|---|---|
| Train | 2.08 |
| Validation | **1.77** |

## Paper

[Gemma 3 Technical Report](https://arxiv.org/abs/2503.19786) — Gemma Team, Google DeepMind 2025
