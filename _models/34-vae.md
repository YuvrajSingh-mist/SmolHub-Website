---
title: "VAE"
excerpt: "VAE on CelebA (128×128). 4-layer conv encoder, 32D latent, ConvTranspose decoder. Reconstruction + KL loss over 200 epochs."
collection: models
layout: model-implementation
category: "Generative Models"
framework: "PyTorch"
dataset: "CelebA"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/VAE"
date: 2025-05-01
---

## Overview

From-scratch Variational Autoencoder trained on CelebA face images at 128×128 resolution. Demonstrates reconstruction, novel face generation by sampling from the Gaussian prior, and latent space arithmetic (e.g. adding/subtracting attribute directions). Based on *Auto-Encoding Variational Bayes* (Kingma & Welling, 2014).

## Architecture

**Encoder**: 4× Conv2d (3→128→256→256→256, stride=2) → linear → μ and log σ² (32D latent)

**Decoder**: Linear → 4× ConvTranspose2d → 128×128 RGB image

- Reparameterisation trick for differentiable sampling
- Loss: MSE reconstruction + KL divergence
- Activation: LeakyReLU (slope=0.01)
- WandB tracking

## Training

| Hyperparameter | Value |
|---|---|
| Dataset | CelebA (202,599 images, 80/20 split) |
| Epochs | 200 (checkpoint at epoch 240) |
| Optimizer | Adam, lr=5e-4 |
| Batch size | 32 |

## Paper

[Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114) — Kingma & Welling, 2014
