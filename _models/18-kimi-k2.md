---
title: "Kimi-K2"
excerpt: "DeepSeekV3-inspired MoE with latent attention trained with Muon optimizer. Pre-trained weights on HuggingFace."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "TinyStories"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Kimi-K2"
date: 2025-08-01
stars: 416
---

## Overview

DeepSeekV3-inspired architecture trained with the Muon optimizer. Pre-trained weights are published on HuggingFace. Includes DDP multi-GPU support and a Gradio inference interface.

## Architecture

- **MoE**: 8 experts, top-2 routing, 1 shared expert
- **Attention**: Latent (compressed KV) attention, latent dim=64
- **Activation**: SwiGLU
- **Config**: 384-dim, 6 layers, 8 heads, 128-token block, ~32K vocab (Llama-2 tokenizer)

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | TinyStories (default); FineWeb / TinyShakespeare also supported |
| Optimizer | Muon + auxiliary Adam |
| LR schedule | Cosine decay with warmup |
| Iterations | 10,000 |
| Tracking | WandB |

- Gradient accumulation and DDP multi-GPU supported

## Published Model

[HuggingFace — YuvrajSingh9886/StoryKimi](https://huggingface.co/YuvrajSingh9886/StoryKimi)

## Paper

[Kimi K2](https://github.com/MoonshotAI/Kimi-K2) — Moonshot AI, 2025
