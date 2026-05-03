---
title: "GRU"
excerpt: "GRU from scratch. 16 hidden units, 50 epochs. Train loss 0.51 / val loss 0.48."
collection: models
layout: model-implementation
category: "Sequential Models"
framework: "PyTorch"
dataset: "Custom"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/GRU"
date: 2025-03-05
---

## Overview

From-scratch GRU (Gated Recurrent Unit) implementation. GRU simplifies the LSTM by merging the cell and hidden state into one and using just two gates (reset and update), achieving comparable performance with fewer parameters. Based on *Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation* (Cho et al., 2014).

## Architecture

- Manual gate implementations: reset gate r, update gate z
- New hidden state: h̃ = tanh(Wx + r ⊙ Uh_{t-1})
- 16 hidden units per layer
- Sequence length: 16

## Training

| Hyperparameter | Value |
|---|---|
| Epochs | 50 |
| Optimizer | Adam, lr=1e-4 |
| Batch size | 16 |
| Dropout | 0.2 |

## Results

| Split | Loss |
|---|---|
| Train | 0.51 |
| Validation | 0.48 |

## Paper

[Learning Phrase Representations using RNN Encoder-Decoder](https://arxiv.org/abs/1406.1078) — Cho et al., 2014
