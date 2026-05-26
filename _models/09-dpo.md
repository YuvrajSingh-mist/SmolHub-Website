---
title: "DPO"
excerpt: "Direct Preference Optimization applied to Qwen0.5B-Instruct on UltraFeedback. Train loss 0.67 in 3,000 iterations."
collection: models
layout: model-implementation
category: "Fine-tuning"
framework: "PyTorch"
dataset: "UltraFeedback"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/DPO"
date: 2025-04-04
stars: 418
---

## Overview

From-scratch implementation of Direct Preference Optimization (DPO), applied to Qwen0.5B-Instruct. DPO eliminates the need for a separate reward model by directly optimising the policy from preference pairs using a closed-form loss derived from RLHF. Based on *Direct Preference Optimization: Your Language Model is Secretly a Reward Model* (Rafailov et al., 2023).

## Setup

- **Base model**: Qwen0.5B-Instruct
- **Dataset**: UltraFeedback binarized (chosen / rejected pairs from HuggingFace)
- **Loss**: DPO contrastive loss with reference model KL penalty (β parameter)

## Training

| Hyperparameter | Value |
|---|---|
| Iterations | 3,000 |
| Optimizer | Adam, lr=1e-6 |
| Batch size | 2 |
| Val frequency | Every 20 steps |

## Results

| Split | Loss |
|---|---|
| Train | 0.67 |
| Validation | 0.68 |

## Paper

[Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — Rafailov et al., Stanford 2023
