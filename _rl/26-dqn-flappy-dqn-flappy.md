---
title: "DQN Flappy"
excerpt: "DQN agent trained on Flappy Bird using pixel observations, experience replay, and epsilon-greedy exploration."
collection: rl
layout: rl-implementation
category: "Value-Based"
categories: ["Value-Based", "Game Environments"]
framework: "PyTorch"
environment: "Flappy Bird"
github_url: "https://github.com/YuvrajSingh-mist/NeatRL/tree/master/DQN-flappy"
date: 2025-03-01
stars: 223
---

## Overview

DQN agent trained on the Flappy Bird game environment from raw pixel observations. The agent learns to navigate through pipes by choosing to flap or do nothing at each timestep.

## Algorithm

Standard DQN with:
- **Experience replay**: transitions stored in a replay buffer, sampled randomly to break correlation
- **Target network**: separate frozen network for computing TD targets, updated periodically
- **Epsilon-greedy**: epsilon decays from 1.0 to a minimum over training to balance exploration/exploitation

## Update Rule

```
TD target = r + gamma * max_a' Q_target(s', a')
Loss = MSE(Q(s, a), TD target)
```

## Features

- Convolutional Q-network processing raw game frames
- Frame preprocessing (grayscale, resize, normalize)
- W&B experiment tracking
- Video recording of agent performance

## References

[Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602) — Mnih et al., DeepMind 2013
