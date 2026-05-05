---
title: "CLiP"
excerpt: "Contrastive vision-language model trained on Flickr8K. Train loss 1.3 / val loss 2.2 in 30 epochs on T4."
collection: models
layout: model-implementation
category: "Vision-Language"
framework: "PyTorch"
dataset: "Flickr8K"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/CLiP"
date: 2025-04-25
stars: 416
---

## Overview

From-scratch PyTorch replication of CLIP (Contrastive Language-Image Pre-training). CLIP jointly trains an image encoder and a text encoder to maximise cosine similarity between matched image-text pairs and minimise it for unmatched pairs — enabling zero-shot image classification by comparing image embeddings to text prompt embeddings. Based on *Learning Transferable Visual Models From Natural Language Supervision* (Radford et al., OpenAI 2021).

## Architecture

- **Image encoder**: Vision Transformer (ViT) or ResNet backbone
- **Text encoder**: Transformer encoder
- **Loss**: Symmetric cross-entropy over cosine similarity matrix (NT-Xent / InfoNCE)
- **Output**: Joint embedding space

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | Flickr8K (image-caption pairs) |
| Epochs | 30 |
| Hardware | T4 GPU |

## Results

| Split | Loss |
|---|---|
| Train | 1.3 |
| Validation | 2.2 |

## Paper

[Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) — Radford et al., OpenAI 2021
