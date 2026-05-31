---
title: "WGANs"
excerpt: "Wasserstein GAN and WGAN-GP implemented from scratch on MNIST — gradient penalty for stable training."
collection: models
layout: model-implementation
category: "Generative Models"
framework: "PyTorch"
dataset: "MNIST"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/WGANs"
date: 2025-05-01
stars: 419
---

## Overview

From-scratch implementations of both WGAN and WGAN-GP. Standard GANs suffer from training instability and mode collapse due to the JS divergence loss. WGANs replace this with the Wasserstein-1 (Earth Mover) distance, which provides meaningful gradients even when the real and fake distributions have disjoint support. WGAN-GP further improves this by replacing weight clipping with a gradient penalty. Based on *Wasserstein GAN* (Arjovsky et al., 2017) and *Improved Training of WGANs* (Gulrajani et al., 2017).

## Implemented

**WGAN**: Wasserstein loss + weight clipping to enforce Lipschitz constraint on discriminator (critic)

**WGAN-GP**: Wasserstein loss + gradient penalty — penalises gradients with norm > 1 at interpolated points between real and fake samples

## Training

- **Dataset**: MNIST
- **Framework**: PyTorch

## Papers

- [Wasserstein GAN](https://arxiv.org/abs/1701.07875) — Arjovsky et al., 2017
- [Improved Training of WGANs](https://arxiv.org/abs/1704.00028) — Gulrajani et al., 2017
