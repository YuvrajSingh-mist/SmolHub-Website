---
title: "Moonshine"
excerpt: "Compact transformer ASR (288-dim, 6 heads) trained on GigaSpeech for 1,500 steps. Notes on overfitting at ~25 hours."
collection: models
layout: model-implementation
category: "Audio/Speech"
framework: "PyTorch"
dataset: "GigaSpeech"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Moonshine"
date: 2025-05-01
stars: 418
---

## Overview

From-scratch replication of Moonshine, a compact ASR model designed for live transcription and voice commands on edge hardware. The architecture prioritises efficiency over raw capacity. Based on *Moonshine: Speech Recognition for Live Transcription and Voice Commands* (Jeffries et al., 2024).

## Architecture

- 288-dim embeddings, 6 attention heads, 6 decoder layers
- Lightweight design targeting real-time on-device inference
- Encoder processes audio features; decoder generates transcription

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | GigaSpeech |
| Steps | 1,500 |
| Batch size | 128 |
| Optimizer | Adam, lr=6e-4 |
| Val frequency | Every 50 steps |
| Total training time | ~25 hours |

The model began overfitting at this scale — the README notes that 25 hours of training on GigaSpeech xs was insufficient for generalisation at this parameter count.

## Paper

[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://arxiv.org/abs/2410.15608) — Jeffries et al., 2024
