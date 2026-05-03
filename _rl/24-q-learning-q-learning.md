---
title: "Q-Learning"
excerpt: "Tabular Q-Learning and Value Iteration implemented from scratch as educational notebooks."
collection: rl
layout: rl-implementation
category: "Value-Based"
categories: ["Value-Based"]
framework: "NumPy"
environment: "FrozenLake / GridWorld"
github_url: "https://github.com/YuvrajSingh-mist/NeatRL/tree/master/Q-Learning"
date: 2025-01-01
---

## Overview

Two foundational RL algorithms implemented as clean notebooks:

- **`q_values.ipynb`** — Tabular Q-Learning: an off-policy TD method that learns the action-value function Q(s,a) directly from experience using the Bellman optimality equation.
- **`v_iteration.ipynb`** — Value Iteration: a dynamic programming algorithm that computes the optimal value function V*(s) by iterating the Bellman optimality operator to convergence.

## Q-Learning Update

```
Q(s, a) <- Q(s, a) + alpha * [r + gamma * max_a' Q(s', a') - Q(s, a)]
```

Off-policy — learns from greedy target regardless of the behavior policy used to collect data.

## Value Iteration Update

```
V(s) <- max_a [ R(s,a) + gamma * sum_s' P(s'|s,a) * V(s') ]
```

Requires full model of the environment (transition probabilities and rewards). Converges to V* when run to convergence.

## Key Concepts

- **Exploration**: epsilon-greedy policy for Q-Learning
- **Convergence**: Value Iteration converges in finite MDPs; Q-Learning converges under sufficient exploration
- **Tabular vs. function approximation**: these are the tabular foundations that DQN later extends with neural networks
