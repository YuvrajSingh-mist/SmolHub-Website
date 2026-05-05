---
title: "Mixtral"
excerpt: "Sparse MoE transformer replicated from scratch on TinyShakespeare. Train loss 2.04 / val loss 2.09 in 1,000 steps on T4."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "TinyShakespeare"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Mixtral"
date: 2025-03-20
stars: 416
---

## Overview

From-scratch replication of Mixtral's Sparse Mixture-of-Experts architecture. Each transformer layer contains multiple expert FFN sub-networks; a learned router selects the top-K experts per token, enabling a larger total parameter count without proportionally increasing compute. Based on *Mixtral of Experts* (Mistral AI, 2024).

## Architecture

- Sparse MoE feed-forward layers with top-K token routing
- Auxiliary load-balancing loss to prevent expert collapse
- Standard multi-head causal self-attention
- RMSNorm, SwiGLU activations

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | TinyShakespeare |
| Steps | 1,000 (val every 50) |
| Hardware | T4 GPU |

## Results

| Split | Loss |
|---|---|
| Train | 2.04 |
| Validation | 2.09 |

## Paper

[Mixtral of Experts](https://arxiv.org/abs/2401.04088) — Mistral AI, 2024
