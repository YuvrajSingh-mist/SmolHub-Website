---
title: "NeatRL | Deep Reinforcement Learning Algorithms Library"
collection: projects
excerpt: "Comprehensive implementations of deep RL algorithms including DQN, A2C, PPO, DDPG, TD3, and SAC. Features one-file implementations, experiment tracking with W&B, automatic video recording, and support for Gymnasium environments. Main NeatRL library provides high-quality training utilities with focus on simplicity and performance."
type: "RL Library"
permalink: /rl/
venue: "Personal Project"
date: Feb '25
location: Online
date_iso: 2025-02-01
github_url: https://github.com/YuvrajSingh-mist/NeatRL
website_url: /rl/
stars: 223
---

One-file implementations of deep RL algorithms in PyTorch. Each algorithm is self-contained — readable, runnable, and stripped of unnecessary abstraction.

## NeatRL Library

The `neatrl/` package provides reusable training utilities built on top of the individual implementations. Install via pip:

```bash
pip install neatrl"[classic,box2d,atari]"
```

```python
from neatrl import train_dqn

model = train_dqn(env_id="CartPole-v1", total_timesteps=10000, seed=42)
```

Full source: [github.com/YuvrajSingh-mist/NeatRL/tree/master/neatrl](https://github.com/YuvrajSingh-mist/NeatRL/tree/master/neatrl)

## Implementations

### Value-Based
- [DQN](/rl/07-dqn-dqn/) — Deep Q-Network for CartPole and LunarLander
- [DQN Atari](/rl/06-dqn-atari-dqn-atari/) — DQN with conv nets on Breakout
- [DQN Flappy](/rl/26-dqn-flappy-dqn-flappy/) — DQN on Flappy Bird
- [DQN Lunar](/rl/04-dqn-lunar-dqn-lunar/) — DQN tuned for Lunar Lander
- [DQN Taxi](/rl/05-dqn-taxi-dqn-taxi/) — DQN for discrete Taxi-v3
- [DQN FrozenLake](/rl/03-dqn-frozenlake-dqn-frozenlake/) — DQN on FrozenLake
- [Dueling DQN](/rl/08-duel-dqn-duel-dqn/) — Separate value and advantage streams
- [Q-Learning](/rl/24-q-learning-q-learning/) — Tabular Q-Learning and Value Iteration
- [VizDoom RL](/rl/25-vizdoom-rl-vizdoom-rl/) — DQN in a 3D first-person environment

### Policy-Based
- [REINFORCE](/rl/19-reinforce-reinforce/) — Monte Carlo policy gradient
- [A2C](/rl/01-a2c-a2c/) — Advantage Actor-Critic
- [PPO](/rl/16-ppo-ppo/) — Proximal Policy Optimization
- [FlappyBird PPO](/rl/09-flappybird-ppo-flappybird-ppo/) — PPO on Flappy Bird
- [GRPO](/rl/23-grpo-grpo/) — Group Relative Policy Optimization (DeepSeek-R1)

### Continuous Control
- [DDPG](/rl/02-ddpg-ddpg/) — Deep Deterministic Policy Gradient
- [TD3](/rl/22-td3-td3/) — Twin Delayed DDPG
- [SAC](/rl/21-sac-sac/) — Soft Actor-Critic

### Exploration & Multi-Agent
- [RND](/rl/20-rnd-rnd/) — Random Network Distillation + PPO
- [Imitation Learning](/rl/11-imitation-learning-imitation-learning/) — Behavioral cloning
- [MARL](/rl/12-marl-marl/) — Multi-Agent RL (IPPO, MAPPO, Self-Play)

## References

- [Sutton & Barto — Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html)
- [CleanRL](https://github.com/vwxyzjn/cleanrl) — primary inspiration for the one-file style
