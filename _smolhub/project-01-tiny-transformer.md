---
title: "Tiny Transformer"
excerpt: "A miniature transformer implementation in just 200 lines of code! Perfect for understanding attention mechanisms and transformer architecture.<br/><img src='/images/500x300.png'>"
collection: smolhub
---

## Project Overview
**Tiny Transformer** is a minimalist implementation of the transformer architecture that fits in just 200 lines of clean, readable code. Perfect for learning and experimentation!

### Features 🚀
- **Ultra-compact**: Complete transformer in <200 lines
- **Educational**: Heavily commented for learning
- **Functional**: Actually works for small tasks
- **Customizable**: Easy to modify and experiment with

### What's Included
- Multi-head attention mechanism
- Position encoding
- Layer normalization
- Feed-forward networks
- Training loop with toy data

### Code Stats
- **Lines of Code**: 187
- **Dependencies**: Only PyTorch + NumPy
- **Model Size**: ~50K parameters
- **Training Time**: <5 minutes on CPU

### Perfect For
- 📚 Learning transformer internals
- 🧪 Quick prototyping
- 🎯 Algorithm understanding
- 🔬 Research experiments
- 👨‍🏫 Teaching AI concepts

### Quick Start
```python
from tiny_transformer import TinyTransformer

model = TinyTransformer(
    vocab_size=1000,
    d_model=128,
    nhead=8,
    num_layers=2
)

# Train on your data
model.train(data)
```

### Fun Facts
- Trained on emoji sequences for text generation
- Can learn simple patterns in under 100 iterations
- Implements core transformer concepts without bloat
- Great for understanding attention visualization
