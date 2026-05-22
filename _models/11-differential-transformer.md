---
title: "Differential Transformer"
excerpt: "Differential attention replicated from scratch — two attention maps subtracted to cancel noise. Trained on TinyShakespeare on A100."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "TinyShakespeare"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Differential%20Transformer"
date: 2025-02-09
stars: 417
---

## Overview

From-scratch replication of the Differential Transformer. Standard softmax attention is replaced with *differential attention*: two attention score maps are computed in parallel and their difference is taken. This cancels out attention noise, producing sharper, more focused weights on relevant tokens. Based on *Differential Transformers* (Ye et al., 2024).

## Architecture

- **Differential attention**: Two Q/K projections per head; output = softmax(QK1ᵀ) − λ·softmax(QK2ᵀ)
- Scalar λ per layer, initialised small and learned
- Otherwise standard decoder-only transformer (RMSNorm, SwiGLU)

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | TinyShakespeare |
| Steps | 2,000 (val every 100) |
| Hardware | A100 GPU |

## Results

| Split | Loss |
|---|---|
| Train | 5.95 |
| Validation | 5.98 |

## Paper

[Differential Transformers](https://arxiv.org/abs/2410.05258) — Ye et al., Microsoft Research 2024
