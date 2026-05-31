---
title: "Whisper"
excerpt: "Whisper ASR from scratch — CNN on 80-channel mel spectrograms + 6-layer transformer decoder. Trained on GigaSpeech."
collection: models
layout: model-implementation
category: "Audio/Speech"
framework: "PyTorch"
dataset: "GigaSpeech"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Whisper"
date: 2025-04-25
stars: 419
---

## Overview

From-scratch replication of OpenAI Whisper, a sequence-to-sequence ASR model. The audio encoder processes mel spectrograms with 1D convolutions before feeding into transformer layers; the decoder autoregressively generates transcription tokens. Based on *Robust Speech Recognition via Large-Scale Weak Supervision* (Radford et al., OpenAI 2022).

## Architecture

**Audio Encoder**:
- 80-channel mel spectrogram (16kHz, 25ms window, 10ms stride, up to 500 time steps)
- Two 1D Conv layers (kernel=3, stride=2) for downsampling
- Transformer encoder on top

**Decoder**:
- 6 layers, 6 heads, 384-dim embeddings
- Vocab size: 50,262
- Cross-attention to encoder outputs

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | GigaSpeech ('xs' snapshot, HuggingFace) |
| Epochs | 10 |
| Optimizer | Adam, lr=2e-4 |
| Batch size | 64 |
| Sequence length | 64 |
| Dropout | 0.1 |

## Paper

[Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356) — Radford et al., OpenAI 2022
