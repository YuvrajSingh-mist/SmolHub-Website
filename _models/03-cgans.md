---
title: "CGANs"
excerpt: "Conditional GAN on MNIST — class-conditioned 64×64 digit generation. 30 epochs, BCE loss, TensorBoard logging."
collection: models
layout: model-implementation
category: "Generative Models"
framework: "PyTorch"
dataset: "MNIST"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/CGANs"
date: 2025-08-06
stars: 418
---

## Overview

From-scratch Conditional GAN (CGAN) on MNIST. CGANs extend vanilla GANs by conditioning both generator and discriminator on class labels, enabling controlled generation of specific digit classes. Based on *Conditional Generative Adversarial Nets* (Mirza & Osindero, 2014).

## Architecture

**Generator**: Noise (100D) concatenated with label embedding → ConvTranspose2d layers → 64×64 grayscale image

**Discriminator**: Image concatenated with label embedding → Conv2d layers → real/fake logit

- InstanceNorm2d, ReLU / LeakyReLU activations
- Weights initialised N(0, 0.02)
- TensorBoard logging

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | MNIST (resized to 64×64) |
| Epochs | 30 |
| Batch size | 128 |
| Optimizer | Adam, lr=0.0002, β=(0.5, 0.999) |
| Loss | Binary Cross-Entropy |

Images saved every 500 iterations.

## Paper

[Conditional Generative Adversarial Nets](https://arxiv.org/abs/1411.1784) — Mirza & Osindero, 2014
