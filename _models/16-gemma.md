---
title: "Gemma"
excerpt: "Google's Gemma architecture replicated from scratch — multi-query attention and GeGLU activations on TinyShakespeare."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "TinyShakespeare"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Gemma"
date: 2025-04-20
stars: 416
---

## Overview

PyTorch replication of Google's Gemma decoder-only architecture. Gemma builds on the Llama recipe with multi-query attention and GeGLU activations, offering better efficiency at comparable quality. Based on *Gemma: Open Models Based on Gemini Research and Technology* (Gemma Team, Google DeepMind, 2024).

## Architecture

- Multi-query attention (MQA)
- GeGLU feed-forward sublayers
- RMSNorm (pre-norm)
- Rotary Positional Embeddings (RoPE)
- Decoder-only autoregressive stack

## Training

- **Dataset**: TinyShakespeare
- **Objective**: Causal language modelling
- **Framework**: PyTorch

## Paper

[Gemma: Open Models Based on Gemini Research and Technology](https://arxiv.org/abs/2403.08295) — Gemma Team, Google DeepMind 2024
