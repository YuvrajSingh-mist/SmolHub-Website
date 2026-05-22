---
title: "CLAP"
excerpt: "Contrastive Language-Audio Pretraining from scratch on GigaSpeech. 768D text / 2048D audio → 1024D shared space."
collection: models
layout: model-implementation
category: "Audio/Speech"
framework: "PyTorch"
dataset: "GigaSpeech"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/CLAP"
date: 2025-08-06
stars: 417
---

## Overview

From-scratch replication of CLAP (Contrastive Language-Audio Pretraining) — the audio equivalent of CLIP. A text encoder and an audio encoder are jointly trained with contrastive loss to align audio clips with natural language descriptions in a shared embedding space. Based on *Large-Scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation* (Wu et al., 2023).

## Architecture

- **Text embeddings**: 768-dim
- **Audio embeddings**: 2048-dim
- **Output space**: 1024-dim shared embedding
- **Audio features**: 44.1kHz, 64 mel bins, 1024 FFT window, 320 hop length, 50–8000 Hz
- **Learning rates**: Differentiated by component — head (1e-3), audio encoder (1e-4), text encoder (1e-5)

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | GigaSpeech ('xs' snapshot) |
| Epochs | 30 |
| Batch size | 32 |
| LR | 4e-4 |

**Known issue**: Loss plateaued at 2.079 (≈ −log(1/8)), indicating the logit scale wasn't large enough for the softmax to assign high probability to correct pairs. Documented as an unresolved training instability.

## Paper

[CLAP: Learning Audio Concepts from Natural Language Supervision](https://arxiv.org/abs/2206.04769) — Wu et al., 2023
