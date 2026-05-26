---
title: "CycleGANs"
excerpt: "Cycle-consistent unpaired image translation on Cityscapes — two generators, two discriminators, cycle + identity losses."
collection: models
layout: model-implementation
category: "Generative Models"
framework: "PyTorch"
dataset: "Cityscapes"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/CycleGANs"
date: 2025-02-09
stars: 418
---

## Overview

From-scratch replication of CycleGAN for unpaired image-to-image translation. CycleGAN trains two generators (A→B and B→A) and two discriminators simultaneously, with a cycle consistency loss enforcing that translating an image and translating back recovers the original. This enables translation without paired training data. Based on *Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks* (Zhu et al., 2017).

## Architecture

- **Generator G**: Domain A → Domain B (ResNet-based)
- **Generator F**: Domain B → Domain A (ResNet-based)
- **Discriminators D_A, D_B**: PatchGAN discriminators
- **Losses**: Adversarial + cycle consistency (L1) + identity loss

## Training

- **Dataset**: Cityscapes (semantic segmentation maps ↔ street photos)
- **Framework**: PyTorch
- Generated images stored in `output_images_val/`

## Paper

[Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593) — Zhu et al., 2017
