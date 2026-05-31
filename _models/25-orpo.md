---
title: "ORPO"
excerpt: "Odds Ratio Preference Optimization on OPT-330M. Reference-free alignment reaching train loss 1.70 in 3,000 iterations."
collection: models
layout: model-implementation
category: "Fine-tuning"
framework: "PyTorch"
dataset: "UltraFeedback"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/ORPO"
date: 2025-04-10
stars: 419
---

## Overview

From-scratch implementation of ORPO (Odds Ratio Preference Optimization), applied to OPT-330M for instruction following. ORPO unifies SFT and alignment into a single stage by penalising rejected responses via an odds-ratio term added to the NLL loss — no reference model required. Based on *ORPO: Monolithic Preference Optimization without Reference Model* (Hong et al., 2024).

## Setup

- **Base model**: OPT-330M
- **Dataset**: UltraFeedback binarized (argilla cleaned version)
- **Loss**: NLL + log odds-ratio penalty on rejected responses

## Training

| Hyperparameter | Value |
|---|---|
| Iterations | 3,000 |
| Optimizer | Adam, lr=8e-6, betas=(0.95, 0.99) |
| Weight decay | 0.1 |
| Batch size | 2 |
| Val frequency | Every 20 steps |

## Results

| Split | Loss (at 2.5k steps) |
|---|---|
| Train | 1.70 |
| Validation | 1.98 |

## Paper

[ORPO: Monolithic Preference Optimization without Reference Model](https://arxiv.org/abs/2403.07691) — Hong et al., 2024
