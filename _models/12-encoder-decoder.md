---
title: "Encoder-Decoder"
excerpt: "LSTM-based Seq2Seq encoder-decoder for German→English translation. Train/val loss ~1.38 in 10 epochs."
collection: models
layout: model-implementation
category: "Sequential Models"
framework: "PyTorch"
dataset: "Multi30k (German–English)"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Encoder-Decoder"
date: 2025-03-01
stars: 419
---

## Overview

From-scratch LSTM-based encoder-decoder (Seq2Seq) for German-to-English translation, replicating the architecture from *Sequence to Sequence Learning with Neural Networks* (Sutskever et al., 2014). This predates attention — the full encoder hidden state is compressed into a single context vector passed to the decoder.

## Architecture

- Deep LSTM encoder and decoder (4 layers each)
- 128 hidden units per layer
- 32-token block size
- No attention — fixed-length context vector bottleneck

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | Multi30k-style German–English |
| Epochs | 10 |
| Optimizer | Adam, lr=1e-4 |
| Batch size | 32 |
| Dropout | 0.2 |

## Results

| Split | Loss |
|---|---|
| Train | 1.38 |
| Validation | 1.39 |

## Paper

[Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) — Sutskever et al., 2014
