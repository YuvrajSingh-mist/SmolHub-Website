---
title: "GPT"
excerpt: "Decoder-only transformer trained on TinyShakespeare, replicating the original OpenAI GPT architecture from scratch."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "TinyShakespeare"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/GPT"
date: 2025-02-08
stars: 416
---

## Overview

From-scratch PyTorch replication of the original GPT architecture — a decoder-only transformer trained autoregressively on the TinyShakespeare character dataset. Based on the paper *Improving Language Understanding by Generative Pre-Training* (Radford et al., OpenAI 2018).

## Architecture

Standard decoder-only transformer stack: causal self-attention, feed-forward sublayers, layer norm, and learned positional embeddings. Trained autoregressively with a cross-entropy language modelling objective on character-level tokens.

## Training

- **Dataset**: TinyShakespeare (`/data` folder)
- **Objective**: Next-token prediction (causal LM)
- **Framework**: PyTorch

## Paper

[Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) — Radford et al., OpenAI 2018
