---
title: "TTS"
excerpt: "Tacotron-style transformer TTS from scratch — 512-dim phoneme encoder, mel spectrogram decoder, 16kHz on GigaSpeech."
collection: models
layout: model-implementation
category: "Audio/Speech"
framework: "PyTorch"
dataset: "GigaSpeech"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/TTS"
date: 2025-05-01
---

## Overview

From-scratch transformer-based Text-to-Speech model in the style of Tacotron 2. Takes phoneme sequences as input and predicts mel spectrogram frames autoregressively, which a vocoder then converts to audio. A WaveNet vocoder is planned but not yet implemented.

## Architecture

**Encoder**: Phoneme embeddings (512-dim) → transformer encoder
**Decoder**: 8 layers, 4 heads, 256-dim, hidden=2048, 80-token block size

**Audio spec**: 16kHz, 80-channel mel spectrogram, 50ms window, 12.5ms stride, up to 512 time steps

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | GigaSpeech |
| Epochs | 10 (150 steps/epoch) |
| Batch size | 32 |
| Optimizer | AdamW, lr=6e-4, weight decay=0.01 |
| Gradient clipping | 1.0 |
| Val frequency | Every 50 steps |

## Paper

[Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions](https://arxiv.org/abs/1712.05884) — Shen et al. (Tacotron 2), 2018
