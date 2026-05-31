---
title: "LSTM"
excerpt: "LSTM from scratch (~128K params). 128 hidden units, 50 epochs. Train loss 0.49 / val loss 0.48."
collection: models
layout: model-implementation
category: "Sequential Models"
framework: "PyTorch"
dataset: "Custom"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/lstm"
date: 2025-04-25
stars: 419
---

## Overview

From-scratch LSTM implementation, manually implementing all four gates (input, forget, output, cell) without using `nn.LSTM`. LSTMs solve the vanishing gradient problem of vanilla RNNs by introducing a cell state that can carry information over long sequences. Based on *Long Short-Term Memory* (Hochreiter & Schmidhuber, 1997).

## Architecture

- Manual gate implementations: i, f, g, o
- 128 hidden units per layer
- Sequence length: 64
- ~128K parameters

## Training

| Hyperparameter | Value |
|---|---|
| Epochs | 50 |
| Optimizer | Adam, lr=1e-4 |
| Batch size | 32 |
| Dropout | 0.1 |

## Results

| Split | Loss |
|---|---|
| Train | 0.49 |
| Validation | **0.48** |

## Paper

[Long Short-Term Memory](https://www.bioinf.jku.at/publications/older/2604.pdf) — Hochreiter & Schmidhuber, 1997
