---
title: "Fine Tuning using PEFT"
excerpt: "QLoRA fine-tuning scripts using PEFT + BitsAndBytes for both decoder and encoder-type models."
collection: models
layout: model-implementation
category: "Fine-tuning"
framework: "PyTorch"
dataset: "Custom"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Fine%20Tuning%20using%20PEFT"
date: 2025-03-01
---

## Overview

Practical fine-tuning scripts using HuggingFace PEFT with QLoRA and BitsAndBytes 4-bit quantisation. Covers both decoder-only (causal LM) and encoder-type models. Useful as a reference for parameter-efficient adaptation of large pre-trained models on consumer hardware.

## What's Included

- **QLoRA + BitsAndBytes 4-bit quantisation** — load large models on limited VRAM
- **PEFT LoRA adapter injection** — target Q/V projections, configurable rank and alpha
- **Separate script for encoder-type models** — e.g. BERT-class architectures

## Key Concepts

- 4-bit NormalFloat (NF4) quantisation for base weights
- Double quantisation to further reduce memory
- LoRA adapters trained in full precision on top of quantised base

## Papers

- [LoRA](https://arxiv.org/abs/2106.09685) — Hu et al., 2022
- [QLoRA](https://arxiv.org/abs/2305.14314) — Dettmers et al., 2023
