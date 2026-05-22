---
title: "DCGANs"
excerpt: "Deep Convolutional GAN trained on CelebA and CIFAR-10. ~7,800 steps (CelebA) and ~11,700 steps (CIFAR-10)."
collection: models
layout: model-implementation
category: "Generative Models"
framework: "PyTorch"
dataset: "CelebA / CIFAR-10"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/DCGANs"
date: 2025-08-06
stars: 417
---

## Overview

From-scratch replication of DCGAN (Deep Convolutional GAN). DCGANs introduced convolutional architectures for both generator and discriminator, replacing fully-connected layers and enabling stable GAN training on natural images. Trained on both CelebA (faces) and CIFAR-10 (objects). Based on *Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks* (Radford et al., 2016).

## Architecture

**Generator**: Random noise → ConvTranspose2d upsampling layers → generated image
**Discriminator**: Image → Conv2d downsampling layers → real/fake logit

- BatchNorm in generator, no pooling
- LeakyReLU in discriminator, ReLU in generator
- Tanh output activation

## Training

| Dataset | Steps |
|---|---|
| CelebA (faces) | ~7,800 |
| CIFAR-10 | ~11,700 |

Pretrained weights available on Google Drive.

## Paper

[Unsupervised Representation Learning with DCGANs](https://arxiv.org/abs/1511.06434) — Radford et al., 2016
