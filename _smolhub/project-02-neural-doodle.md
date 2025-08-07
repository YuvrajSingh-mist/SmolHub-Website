---
title: "Neural Doodle"
excerpt: "Real-time drawing app that completes your sketches using a tiny neural network! Draw half a cat and watch AI complete it magically. 🎨<br/><img src='/images/500x300.png'>"
collection: smolhub
---

## Project Overview
**Neural Doodle** is a fun interactive web app that uses a lightweight neural network to complete your drawings in real-time. Start sketching and watch the AI finish your masterpiece!

### How It Works ✨
1. **Draw**: Start sketching anything on the canvas
2. **Predict**: AI analyzes your partial drawing
3. **Complete**: Neural network fills in the missing parts
4. **Iterate**: Keep drawing to refine the result

### Technical Magic 🧠
- **Model**: Custom lightweight CNN with only 15K parameters
- **Speed**: Real-time inference (<50ms)
- **Training**: Trained on 10K simplified drawings
- **Technology**: TensorFlow.js for browser deployment

### Features
- 🎨 **Real-time completion** as you draw
- 🖱️ **Mouse and touch** support
- 🎭 **Multiple categories**: animals, objects, faces
- 📱 **Mobile friendly** responsive design
- 💾 **Save & share** your AI-completed drawings

### Supported Categories
- Animals (cats, dogs, birds, fish)
- Objects (cars, houses, trees)  
- Faces (human expressions)
- Abstract shapes and patterns

### Performance
- **Model Size**: 127KB compressed
- **Inference**: 30-50ms on modern browsers
- **Accuracy**: 78% completion satisfaction rate
- **Battery**: Optimized for mobile devices

### Try It Live!
The app runs entirely in your browser - no server required! Perfect for:
- 🎮 Creative fun and experimentation
- 📚 Demonstrating AI to non-technical audiences  
- 🧒 Kids learning about AI and creativity
- 🎨 Artists exploring AI-assisted creation

### Code Highlights
```javascript
// Real-time prediction
canvas.on('stroke', async (stroke) => {
  const prediction = await model.predict(stroke);
  canvas.complete(prediction);
});
```
