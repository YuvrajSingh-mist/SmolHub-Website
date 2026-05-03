---
title: "PaliGemma"
excerpt: "Google's PaliGemma VLM (SigLIP + Gemma) replicated from scratch on Flickr8K."
collection: models
layout: model-implementation
category: "Vision-Language"
framework: "PyTorch"
dataset: "Flickr8K"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/PaliGemma"
date: 2025-05-01
---

## Overview

From-scratch replication of PaliGemma, Google's 3B VLM that combines a SigLIP vision encoder with a Gemma language decoder. PaliGemma is designed as a transfer-ready base model — strong on diverse vision-language tasks after task-specific fine-tuning. Based on *PaliGemma: A versatile 3B VLM for transfer* (Beyer et al., Google 2024).

## Architecture

- **Vision encoder**: SigLIP ViT (patch embeddings with sigmoid-loss pretraining)
- **Language decoder**: Gemma-style decoder-only transformer
- **Connector**: Linear projection from vision to language embedding space
- Full-attention (not cross-attention) — image tokens prepended to text tokens

## Training

- **Dataset**: Flickr8K
- **Framework**: PyTorch

## Paper

[PaliGemma: A versatile 3B VLM for transfer](https://arxiv.org/abs/2407.07726) — Beyer et al., Google 2024
