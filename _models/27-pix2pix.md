---
title: "Pix2Pix"
excerpt: "Conditional GAN for paired image-to-image translation (aerial→map) replicated from scratch. PatchGAN discriminator."
collection: models
layout: model-implementation
category: "Generative Models"
framework: "PyTorch"
dataset: "Aerial2Map"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Pix2Pix"
date: 2025-05-01
---

## Overview

From-scratch replication of Pix2Pix for paired image-to-image translation. Unlike CycleGAN, Pix2Pix requires paired training data and uses a U-Net generator with a PatchGAN discriminator that classifies overlapping 70×70 image patches as real or fake. Based on *Image-to-Image Translation with Conditional Adversarial Networks* (Isola et al., 2017).

## Architecture

**Generator**: U-Net with skip connections (encoder-decoder + lateral connections at each resolution)

**Discriminator**: PatchGAN — classifies 70×70 patches rather than the full image, encouraging sharp local texture

- Combined adversarial + L1 reconstruction loss
- L1 weight encourages low-frequency correctness

## Training

- **Dataset**: Aerial2Map (aerial photography ↔ map tiles)
- **Framework**: PyTorch

## Paper

[Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004) — Isola et al., 2017
