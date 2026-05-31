---
title: "ViT"
excerpt: "ViT-B/16 from scratch on a 3-class Food-101 subset. Train loss 1.20 / test loss 1.52."
collection: models
layout: model-implementation
category: "Computer Vision"
framework: "PyTorch"
dataset: "Food-101 (subset)"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/ViT"
date: 2024-06-20
stars: 419
---

## Overview

From-scratch implementation of ViT-B/16 (Vision Transformer). ViT applies a standard transformer encoder directly to sequences of 16×16 image patches, treating each patch as a token — demonstrating that CNNs are not required for competitive vision performance. Based on *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale* (Dosovitskiy et al., 2021).

## Architecture

- Patch size: 16×16 pixels
- Patch embeddings via linear projection
- Learnable [CLS] token for classification
- Standard transformer encoder (multi-head self-attention, MLP, LayerNorm)
- Classification head on [CLS] token output

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | Food-101 subset (3 classes: 255 train / 75 test images) |
| Variant | ViT-B/16 |

## Results

| Split | Loss |
|---|---|
| Train | 1.20 |
| Test | 1.52 |

## Paper

[An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929) — Dosovitskiy et al., 2021
