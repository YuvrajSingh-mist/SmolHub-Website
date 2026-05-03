---
title: "BERT"
excerpt: "Bidirectional encoder pre-trained with masked language modelling on the Cornell Movie Dialogs corpus."
collection: models
layout: model-implementation
category: "Language Models"
framework: "PyTorch"
dataset: "Cornell Movie Dialogs"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/BERT"
date: 2025-02-09
---

## Overview

From-scratch PyTorch replication of BERT. Unlike decoder-only models, BERT conditions on both left and right context via masked language modelling (MLM), making it a strong encoder backbone for classification and retrieval. Based on *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* (Devlin et al., 2019).

## Architecture

Full bidirectional transformer encoder — no causal mask, tokens attend to the full sequence. Trained with the MLM objective where 15% of tokens are masked and the model reconstructs them from surrounding context.

## Training

- **Dataset**: Cornell Movie Dialog Corpus
- **Objective**: Masked Language Modelling (MLM)
- **Framework**: PyTorch

## Paper

[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) — Devlin et al., 2019
