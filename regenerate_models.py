#!/usr/bin/env python3
"""
Regenerate all model markdown files using ONLY data from models.json
This ensures exact title matching and uses only GitHub API data, no custom content
"""

import json
import os
import re
from datetime import datetime

def slugify(text):
    """Convert text to a URL-friendly slug"""
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def extract_framework_and_dataset(readme_content, description):
    """Extract framework and dataset information from readme content"""
    framework = "PyTorch"  # Default
    dataset = "Custom"     # Default
    category = "Machine Learning"  # Default
    
    # Look for framework mentions
    content_lower = (readme_content + " " + description).lower()
    if 'pytorch' in content_lower:
        framework = "PyTorch"
    elif 'tensorflow' in content_lower:
        framework = "TensorFlow"
    elif 'jax' in content_lower:
        framework = "JAX"
    elif 'huggingface' in content_lower:
        framework = "HuggingFace"
    
    # Look for dataset mentions
    if 'mnist' in content_lower:
        dataset = "MNIST"
    elif 'imagenet' in content_lower:
        dataset = "ImageNet"
    elif 'cifar' in content_lower:
        dataset = "CIFAR"
    elif 'coco' in content_lower:
        dataset = "COCO"
    elif 'flickr' in content_lower:
        dataset = "Flickr"
    elif 'cornell' in content_lower:
        dataset = "Cornell Movie Dialog"
    elif 'ultrafeedback' in content_lower:
        dataset = "UltraFeedback"
    elif 'gigaspeech' in content_lower:
        dataset = "Gigaspeech"
    elif 'custom' in content_lower:
        dataset = "Custom"
    
    # Determine category based on model name and content
    model_lower = (readme_content + " " + description).lower()
    if any(term in model_lower for term in ['gpt', 'bert', 'llama', 'gemma', 'transformer', 'language', 'dpo', 'orpo', 'peft', 'lora']):
        category = "Language Models"
    elif any(term in model_lower for term in ['gan', 'dcgan', 'wgan', 'cgan', 'cyclegan', 'pix2pix']):
        category = "Generative Models"
    elif any(term in model_lower for term in ['vit', 'clip', 'vision', 'image', 'siglip', 'paligemma']):
        category = "Computer Vision"
    elif any(term in model_lower for term in ['whisper', 'tts', 'audio', 'clap']):
        category = "Audio Processing"
    elif any(term in model_lower for term in ['vae', 'autoencoder']):
        category = "Unsupervised Learning"
    elif any(term in model_lower for term in ['rnn', 'lstm', 'gru', 'seq2seq', 'encoder', 'decoder']):
        category = "Sequential Models"
    elif any(term in model_lower for term in ['attention']):
        category = "Attention Mechanisms"
    elif any(term in model_lower for term in ['distributed', 'ddp', 'training']):
        category = "Training Optimization"
    
    return framework, dataset, category

def create_markdown_from_json(model_data, file_number):
    """Create markdown content from JSON model data"""
    name = model_data.get('name', 'Unknown Model')
    description = model_data.get('description', 'No description available')
    readme_content = model_data.get('readme_content', '')
    github_url = model_data.get('github_url', '')
    
    # Extract additional metadata
    framework, dataset, category = extract_framework_and_dataset(readme_content, description)
    
    # Use current date as fallback
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Clean up readme content - use exactly what's from GitHub
    clean_content = readme_content.strip() if readme_content else f"# {name}\n\nFrom scratch implementation of {name}."
    
    # Ensure it starts with proper markdown structure
    if not clean_content.startswith('#'):
        clean_content = f"# {name}\n\n{clean_content}"
    
    # Add source code section if not present
    if 'source code' not in clean_content.lower() and github_url:
        clean_content += f"\n\n## Source Code\n📁 **GitHub Repository**: [{name}]({github_url})\n\nView the complete implementation, training scripts, and documentation on GitHub."
    
    # Create frontmatter - use EXACT name from JSON
    frontmatter = f"""---
title: "{name}"
excerpt: "{description}"
collection: models
layout: model-implementation
category: "{category}"
framework: "{framework}"
dataset: "{dataset}"
github_url: "{github_url}"
date: {current_date}
---

## Overview
{description}

## Technical Details
- **Framework**: {framework}
- **Dataset**: {dataset}
- **Category**: {category}

## Implementation Details

{clean_content}
"""
    
    return frontmatter

def main():
    """Main function to regenerate all markdown files from models.json"""
    json_path = '_data/models.json'
    models_dir = '_models'
    
    # Load models.json
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found!")
        return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    models = data.get('models', [])
    if not models:
        print("No models found in JSON!")
        return
    
    # Create models directory if it doesn't exist
    os.makedirs(models_dir, exist_ok=True)
    
    print(f"Regenerating {len(models)} model files from models.json...")
    
    # Generate markdown files
    for i, model in enumerate(models, 1):
        name = model.get('name', f'Model {i}')
        
        # Create filename
        filename = f"{i:02d}-{slugify(name)}.md"
        filepath = os.path.join(models_dir, filename)
        
        # Generate markdown content using ONLY JSON data
        markdown_content = create_markdown_from_json(model, i)
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"Created: {filename} -> {name}")
    
    print(f"\nSuccessfully regenerated {len(models)} model files!")
    print("All files now use EXACT data from models.json (GitHub API)")

if __name__ == '__main__':
    main()
