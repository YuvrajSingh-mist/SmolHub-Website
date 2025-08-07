---
title: "Seq2Seq"
excerpt: "Implementation of Seq2Seq from the Paper Replications repository"
collection: paper_replications
layout: paper-replication
category: "Attention Mechanisms"
framework: "PyTorch"
dataset: "Custom"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Seq2Seq"
date: 2025-08-07
---

## Overview
Implementation of Seq2Seq from the Paper Replications repository

## Key Features
- Attention Mechanism

## Technical Details
- **Framework**: PyTorch
- **Dataset**: Custom
- **Category**: Attention Mechanisms

## Implementation Details

# Seq2Seq with Bahdanau and Luong Attention in Pytorch from scratch implementation

Trained a Seq2Seq model with the said attention mechanism  coded from scratch in Pytorch 

[Effective Approaches to Attention-based Neural Machine Translation](https://arxiv.org/abs/1508.04025)

[Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.0473)

## ModelArgs Hyperparameters

| Parameter    | Value    | Description                                                                 
|--------------|----------|-----------------------------------------------------------------------------|
| `batch_size` | 32       | The number of samples processed before the model is updated.                |
| `max_lr`     | 1e-4     | Maximum learning rate.                                                      |
| `dropout`    | 0.1      | Dropout.                                                                    |
| `epochs`     | 50       | Epochs                                                                      |           
| `block_size` | 32      | Seq Len                                                                      |
| `No of neurons`| 128      | No of neurons in an GRU per layer                                         |    
| `hidden_dim`| 4*embedding_dims      | No of neurons in FFN                                            |  
| `No of neurons`| 128      | No of neurons in an GRU per layer                                         |  

### Frameworks:
**Pytorch**

### Epochs/Steps
Epochs (train) = 50

Val iterations = every epoch

### Loss Curves

![Train and Val loss curves](img/loss_curves.jpg)

## Source Code
📁 **GitHub Repository**: [Seq2Seq](https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/Seq2Seq)

View the complete implementation, training scripts, and documentation on GitHub.
