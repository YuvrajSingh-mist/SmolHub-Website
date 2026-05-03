---
title: "Llava"
excerpt: "Visual instruction tuning replicated from scratch on Flickr8K. Train loss 0.23 / val loss 0.22 in 5 epochs on T4."
collection: models
layout: model-implementation
category: "Vision-Language"
framework: "PyTorch"
dataset: "Flickr8K"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Llava"
date: 2025-04-25
---

## Overview

From-scratch replication of LLaVA (Large Language and Vision Assistant). LLaVA connects a vision encoder to a language model decoder via a trainable projection layer, enabling visual instruction following. The projection maps image patch embeddings into the LLM's token embedding space. Based on *Visual Instruction Tuning* (Liu et al., 2023).

## Architecture

- **Vision encoder**: CLIP ViT (image patch embeddings)
- **Projection**: Linear layer mapping image embeddings → LLM input space
- **Language decoder**: LLM (instruction-following)
- Two-stage training: (1) train projection with frozen encoders; (2) fine-tune full model

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | Flickr8K (image-caption pairs as instruction-following data) |
| Epochs | 5 |
| Hardware | T4 GPU |

## Results

| Split | Loss |
|---|---|
| Train | **0.23** |
| Validation | **0.22** |

## Paper

[Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) — Liu et al., 2023
