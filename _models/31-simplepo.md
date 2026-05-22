---
title: "SimplePO"
excerpt: "Reference-free preference optimization (SimplePO) on OPT-330M. Batch size 128, lr=2e-5, beta=2 on UltraFeedback."
collection: models
layout: model-implementation
category: "Fine-tuning"
framework: "PyTorch"
dataset: "UltraFeedback"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/SimplePO"
date: 2025-04-04
stars: 417
---

## Overview

From-scratch implementation of SimplePO applied to OPT-330M. SimplePO is a reference-free preference optimisation method that directly maximises the log-likelihood ratio between chosen and rejected responses without a KL penalty or reward model. Based on *SimPO: Simple Preference Optimization with a Reference-Free Reward* (Meng et al., 2024).

## Setup

- **Base model**: OPT-330M
- **Dataset**: UltraFeedback binarized preferences
- **Loss**: Length-normalised log-ratio reward + margin γ

## Training

| Hyperparameter | Value |
|---|---|
| Batch size | 128 |
| Optimizer | Adam, lr=2e-5 |
| Beta (reward scaling) | 2 |
| Gamma (margin) | 1.6 |

## Paper

[SimPO: Simple Preference Optimization with a Reference-Free Reward](https://arxiv.org/abs/2405.14734) — Meng et al., 2024
