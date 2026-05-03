---
title: "SigLip"
excerpt: "Sigmoid-loss vision-language pretraining replicated from scratch on Flickr8K — avoids global softmax normalisation."
collection: models
layout: model-implementation
category: "Vision-Language"
framework: "PyTorch"
dataset: "Flickr8K"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/SigLip"
date: 2025-05-01
---

## Overview

From-scratch replication of SigLIP (Sigmoid Loss for Language Image Pre-Training). SigLIP replaces CLIP's softmax-based contrastive loss with a pairwise sigmoid loss, treating the problem as independent binary classification for each image-text pair. This removes the dependency on global batch normalisation and improves scalability. Based on *Sigmoid Loss for Language Image Pre-Training* (Zhai et al., 2023).

## Architecture

- Image encoder + text encoder (same backbone structure as CLIP)
- **Loss**: Pairwise sigmoid cross-entropy — no global softmax over the batch
- Each (image, text) pair independently classified as matching or not

## Training

- **Dataset**: Flickr8K
- **Framework**: PyTorch

## Paper

[Sigmoid Loss for Language Image Pre-Training](https://arxiv.org/abs/2303.15343) — Zhai et al., Google 2023
