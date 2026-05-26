---
title: "Attention Mechanisms"
excerpt: "From-scratch implementations of Bahdanau and Luong attention in PyTorch."
collection: models
layout: model-implementation
category: "Attention"
framework: "PyTorch"
dataset: "Custom"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Attention%20Mechanisms"
date: 2025-03-07
stars: 418
---

## Overview

Standalone implementations of the two seminal additive and multiplicative attention mechanisms that preceded the Transformer. These form the conceptual foundation for all modern attention: Bahdanau's additive scoring and Luong's dot-product / general scoring.

## Implemented

**Bahdanau Attention** (*Neural Machine Translation by Jointly Learning to Align and Translate*, Bahdanau et al., 2015)
- Additive (MLP) scoring function: score(s, h) = vᵀ tanh(Ws·s + Wh·h)
- Enables encoder-decoder alignment without fixed-length bottleneck

**Luong Attention** (*Effective Approaches to Attention-based Neural Machine Translation*, Luong et al., 2015)
- Three scoring variants: dot, general, concat
- Global and local attention modes

## Papers

- [Bahdanau et al., 2015](https://arxiv.org/abs/1409.0473)
- [Luong et al., 2015](https://arxiv.org/abs/1508.04025)
