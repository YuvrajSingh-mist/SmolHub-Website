---
title: "DDP"
excerpt: "From scratch implementation of DDP"
collection: models
layout: model-implementation
category: "Training Methods"
framework: "PyTorch"
dataset: "Custom"
github_url: "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/DDP"
date: 2025-04-25
---

## Overview
From scratch implementation of DDP

## Key Features
- Attention Mechanism
- Distributed Training

## Technical Details
- **Framework**: PyTorch
- **Dataset**: Custom
- **Category**: Training Methods

## Implementation Details


I implemented a training loop and trained a Llama made from scratch using Data Distributed Parallel and torchrun.

##  ModelArgs Hyperparameters

| Parameter              | Value         | Description                                                                 |
|------------------------|---------------|-----------------------------------------------------------------------------|
| `block_size`           | 128           | The size of each block.                                                     |
| `batch_size`           | 64            | The number of samples processed before the model is updated.                |
| `embeddings_dims`      | 384           | The dimensionality of the embeddings.                                       |
| `attn_dropout`         | 0.1           | Dropout rate for attention layers.                                          |
| `no_of_heads`          | 6             | Number of attention heads (needs thorough calculation).                     |
| `dropout`              | 0.1           | Dropout rate for the model.                                                 |
| `max_lr`               | 1e-4          | Maximum learning rate.                                                      |
| `no_of_decoder_layers` | 6             | Number of decoder layers (needs thorough calculation).                      |
| `weight_decay_optim`   | 0.1           | Weight decay for the optimizer.                                             |
| `beta_1`               | 0.9           | Exponential decay rate for the first moment estimates in the optimizer.     |
| `beta_2`               | 0.95          | Exponential decay rate for the second moment estimates in the optimizer.    |
| `clip`                 | 1.0           | Gradient clipping value.                                                    |
| `device`               | 'cuda:0'      | The device to run the model on (e.g., 'cuda:0' for GPU).                    |
| `no_kv_heads`          | 2             | Number of key-value heads.                                                 

### Datasets

**Tineshakespeare**: in the /data folder

### Frameworks:
**Pytorch**

### Epochs/Steps
Iterations (train) = 8000

Val iterations = every 100

### Losses
Train loss - 1.5

Val loss - 1.1

### Local setup

### Requirements

```python
pip install torchtune
pip install torchao
pip install torchrun
pip install wandb

```

If you want to use your dataset, please take a look at the dataset provided in data/.
If you have one, move your dataset to the data/ folder and then change the following line to point to your dataset in the data/ (currently only .txt is supported) in the llama_multi_gpu_train.py
Also please change 'device' to any of your available cuda gpus.

```python
'data/input.txt' -> 'data/{YPU_FILE_NAME_HERE}' line  66

```
To run:

```python
torchrun --standalone --nproc_per_node=gpu llama_multi_gpu_train.py
```
--standalone - if all the gpu are on one server
--npro_per_node - number of gpus available and use the keyword gpu to use all


## Source Code
📁 **GitHub Repository**: [DDP](https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/DDP)

View the complete implementation, training scripts, and documentation on GitHub.
