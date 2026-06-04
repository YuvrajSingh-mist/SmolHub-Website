---
title: "GRPO"
excerpt: "Group Relative Policy Optimization — DeepSeek-R1's RL training objective implemented from scratch."
collection: rl
layout: rl-implementation
category: "Policy-Based"
categories: ["Policy-Based"]
framework: "PyTorch"
environment: "Custom"
github_url: "https://github.com/YuvrajSingh-mist/NeatRL/tree/master/GRPO"
date: 2025-06-01
stars: 223
---

## Overview

From-scratch implementation of Group Relative Policy Optimization (GRPO), the RL training objective introduced in DeepSeek-R1. Unlike PPO which uses a value network as baseline, GRPO estimates the baseline from the mean reward of a group of sampled outputs — removing the critic entirely and making RL training of LLMs significantly cheaper.

## Algorithm

For each prompt, sample G outputs from the current policy. The group advantage for output i is:

```
A_i = (r_i - mean(r)) / std(r)
```

The policy is then updated with a clipped surrogate objective identical to PPO's, but using group-relative advantages instead of GAE.

## Key Properties

- **No value network**: baseline is the within-group mean reward
- **Group size G**: controls variance of the advantage estimate
- **KL penalty**: constrains the policy from drifting too far from a reference model
- **Clipped surrogate**: same epsilon-clip as PPO for stability

## Implementation

Implemented as a Jupyter notebook (`train.ipynb`) covering the full GRPO update loop, advantage normalization, and the KL-divergence penalty term.

## References

[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) — DeepSeek-AI, 2025
