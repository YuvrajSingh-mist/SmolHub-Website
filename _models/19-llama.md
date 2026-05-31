---
title: "Llama"
excerpt: "Decoder-only Llama replicated from scratch with RoPE, SwiGLU, RMSNorm and GQA."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "TinyShakespeare"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Llama"
date: 2025-04-20
stars: 419
---

## Overview

From-scratch PyTorch replication of the Llama architecture. Llama improved upon vanilla GPT by replacing LayerNorm with RMSNorm, using SwiGLU activations, and adopting Rotary Positional Embeddings (RoPE) — changes that collectively improve training stability and efficiency. Based on *LLaMA: Open and Efficient Foundation Language Models* (Touvron et al., 2023).

## Architecture

- **Norm**: RMSNorm (pre-norm)
- **Activations**: SwiGLU feed-forward sublayers
- **Position**: Rotary Positional Embeddings (RoPE)
- **Attention**: Grouped-Query Attention (GQA)
- Decoder-only autoregressive stack

## Training

- **Dataset**: TinyShakespeare
- **Objective**: Causal language modelling
- **Framework**: PyTorch

## Paper

[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) — Touvron et al., 2023
