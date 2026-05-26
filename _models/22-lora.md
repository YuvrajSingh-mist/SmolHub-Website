---
title: "LoRA"
excerpt: "Low-rank adaptation implemented from scratch in PyTorch. Train/val loss ~3.5 in 1,000 steps on A100."
collection: models
layout: model-implementation
category: "Fine-tuning"
framework: "PyTorch"
dataset: "TinyShakespeare"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/LoRA"
date: 2025-04-05
stars: 418
---

## Overview

From-scratch PyTorch implementation of LoRA (Low-Rank Adaptation). Rather than fine-tuning all parameters, LoRA freezes the pre-trained weights and injects trainable low-rank decomposition matrices (A and B) into each attention projection. The update ΔW = BA where B ∈ Rᵈˣʳ and A ∈ Rʳˣᵏ, with rank r ≪ d. Based on *LoRA: Low-Rank Adaptation of Large Language Models* (Hu et al., 2022).

## Architecture

- LoRA adapters injected into Q, V projections
- Rank r configurable; original weights frozen
- Zero-initialised B, random Gaussian A — ensures ΔW=0 at start

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | TinyShakespeare |
| Steps | 1,000 (val every 100) |
| Hardware | A100 GPU |

## Results

| Split | Loss |
|---|---|
| Train | 3.51 |
| Validation | 3.50 |

## Paper

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) — Hu et al., 2022
