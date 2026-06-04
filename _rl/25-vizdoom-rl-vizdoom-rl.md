---
title: "VizDoom RL"
excerpt: "DQN agent trained on VizDoom Basic via Gymnasium wrapper, with grayscale preprocessing, replay buffer, and W&B logging."
collection: rl
layout: rl-implementation
category: "Value-Based"
categories: ["Value-Based", "Game Environments"]
framework: "PyTorch"
environment: "VizDoom"
github_url: "https://github.com/YuvrajSingh-mist/NeatRL/tree/master/VizDoom-RL"
date: 2025-04-01
stars: 223
---

## Overview

DQN agent trained on the VizDoom Basic scenario (`VizdoomBasic-v0`) using Gymnasium's VizDoom wrapper. The agent learns to navigate a 3D first-person environment and eliminate enemies using raw pixel observations.

## Architecture

3-layer CNN + 2 FC layers:

| Layer | Spec |
|---|---|
| Conv 1 | 32 filters, 8×8, stride 4, ReLU |
| Conv 2 | 32 filters, 4×4, stride 2, ReLU |
| Conv 3 | 64 filters, 3×3, stride 3, ReLU |
| FC 1 | 512 units, ReLU |
| FC 2 | 512 units, ReLU |
| Output | Action space dim |

## Image Preprocessing

- RGB → grayscale, channel-first
- Resize to 128×128
- Normalize to [0, 1]
- Handles dict observations (`obs['screen']`)

## Training Config

| Hyperparameter | Value |
|---|---|
| Total timesteps | 1,000,000 |
| Learning rate | 2e-4 |
| Buffer size | 30,000 |
| Batch size | 128 |
| Gamma | 0.99 |
| Epsilon start/end | 1.0 → 0.05 |
| Exploration fraction | 0.5 |
| Target update freq | 50 steps |
| Optimizer | Adam, MSE loss |

## Features

- Target network with polyak averaging (tau)
- SB3 replay buffer for efficient sampling
- W&B logging (episodic return, Q-values, epsilon)
- Periodic evaluation with video export

## References

[Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602) — Mnih et al., DeepMind 2013
