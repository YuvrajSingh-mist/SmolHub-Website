---
title: "RNNs"
excerpt: "Vanilla RNN from scratch. 16 neurons, 50 epochs. Train loss 0.51 / val loss 0.50."
collection: models
layout: model-implementation
category: "Sequential Models"
framework: "PyTorch"
dataset: "Custom"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/RNNs"
date: 2025-03-07
---

## Overview

From-scratch vanilla RNN implementation in PyTorch, establishing the baseline for the sequential model series. Implements the basic recurrent computation hₜ = tanh(Wₓxₜ + Wₕhₜ₋₁ + b) from scratch without using `nn.RNN`, for pedagogical clarity.

## Architecture

- Vanilla RNN cell implemented manually
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
| Validation | 0.50 |
