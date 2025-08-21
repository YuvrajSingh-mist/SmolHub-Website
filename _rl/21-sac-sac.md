---
title: "SAC"
excerpt: "Implementation of SAC reinforcement learning algorithm"
collection: rl
layout: rl-implementation
category: "Actor-Critic Methods"
framework: "PyTorch"
environment: "Gymnasium"
github_url: "https://github.com/YuvrajSingh-mist/Reinforcement-Learning/tree/master/SAC"
date: 2025-08-21
---

Implementation of SAC reinforcement learning algorithm

## Technical Details
- **Framework**: PyTorch
- **Environment**: Gymnasium
- **Category**: Actor-Critic Methods

This directory contains implementations of the Soft Actor-Critic (SAC) algorithm for various continuous control environments.

## Overview

SAC is an off-policy actor-critic algorithm designed for continuous action spaces that optimizes a stochastic policy in an off-policy way. It incorporates several key features:

1. **Maximum Entropy Reinforcement Learning**: Encourages exploration by maximizing the policy entropy along with the expected return.
2. **Actor-Critic Architecture**: Uses a critic to estimate the Q-values and an actor to learn the policy.
3. **Off-Policy Learning**: Can learn from previously collected data, making it sample-efficient.
4. **Soft Policy Updates**: Uses soft updates of the target networks to improve stability.

Key features of this implementation:
- Entropy-regularized reinforcement learning
- Actor-Critic architecture with automatic temperature tuning
- Experience replay buffer for stable learning
- Soft target network updates using Polyak averaging
- Stochastic policy for better exploration
- Support for different continuous control environments

## Environments

This implementation includes support for the following environments:
- **Pendulum-v1**: A classic control problem where the goal is to balance a pendulum in an upright position.
- **BipedalWalker-v3**: A more challenging environment where a 2D biped robot must walk forward without falling.

## Configuration

Each implementation includes a `Config` class that specifies the hyperparameters for training. You can modify these parameters to experiment with different settings:

- `exp_name`: Name of the experiment
- `seed`: Random seed for reproducibility
- `env_id`: ID of the Gymnasium environment
- `total_timesteps`: Total number of training steps
- `learning_rate`: Learning rate for the optimizer
- `buffer_size`: Size of the replay buffer
- `gamma`: Discount factor
- `tau`: Soft update coefficient for target networks
- `batch_size`: Batch size for training
- `exploration_fraction`: Fraction of total timesteps for exploration
- `learning_starts`: Number of timesteps before learning starts
- `train_frequency`: Frequency of updates to the networks

## Architecture

The SAC implementation includes:

1. **Actor Network (Policy)**: Outputs a mean and log standard deviation for each action dimension, defining a Gaussian distribution over actions.
2. **Twin Critic Networks**: Two separate Q-value networks to mitigate overestimation bias.
3. **Temperature Parameter (Alpha)**: Automatically adjusted to maintain a target entropy level.
4. **Target Networks**: Slowly updated copies of the critic networks for stability.
5. **Replay Buffer**: Stores and samples transitions for training.

## Key Advantages of SAC

SAC offers several advantages over other continuous control algorithms:

1. **Sample Efficiency**: Off-policy learning allows SAC to reuse past experiences.
2. **Stability**: The entropy term and soft updates help stabilize training.
3. **Exploration-Exploitation Balance**: The maximum entropy framework naturally balances exploration and exploitation.
4. **Performance**: SAC has shown state-of-the-art performance across many continuous control tasks.
5. **Robustness**: Less sensitive to hyperparameter tuning compared to other algorithms.

## Logging and Monitoring

Training progress is logged using:
- **TensorBoard**: Local visualization of training metrics
- **Weights & Biases (WandB)**: Cloud-based experiment tracking (optional)
- **Video Capture**: Records videos of agent performance at intervals

## Results

### Pendulum

The following image shows the training performance on the Pendulum environment:

![Pendulum Training Results](https://raw.githubusercontent.com/YuvrajSingh-mist/Reinforcement-Learning/master/SAC/images/pendulum.png)

### HalfCheetah

Although not explicitly implemented in the current codebase, we have training results for the HalfCheetah environment using SAC:

![HalfCheetah Training Results](https://raw.githubusercontent.com/YuvrajSingh-mist/Reinforcement-Learning/master/SAC/images/halfcheetah.png)



## Source Code
📁 **GitHub Repository**: [SAC (SAC)](https://github.com/YuvrajSingh-mist/Reinforcement-Learning/tree/master/SAC)

View the complete implementation, training scripts, and documentation on GitHub.
