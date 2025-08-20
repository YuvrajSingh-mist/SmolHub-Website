#!/usr/bin/env python3
"""
Script to refresh RL implementations from the Reinforcement-Learning GitHub repository.
This script fetches the folder structure from GitHub API and generates both 
JSON data file and individual Jekyll markdown files.
"""

import os
import json
import requests
import re
from datetime import datetime
from pathlib import Path
import argparse

# Configuration
REPO_OWNER = "YuvrajSingh-mist"
REPO_NAME = "Reinforcement-Learning"
BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
DATA_FILE = "_data/rl.json"
MODELS_DIR = "_rl"
BASE_PATH = Path(__file__).parent

def fetch_github_content(path=""):
    """Fetch repository content from GitHub API."""
    url = f"{BASE_URL}/contents/{path}"
    print(f"🔍 Fetching: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return None

def fetch_readme_content(path):
    """Fetch README content from a specific folder."""
    readme_files = ["README.md", "readme.md", "README.txt"]
    
    for readme_file in readme_files:
        readme_path = f"{path}/{readme_file}" if path else readme_file
        content = fetch_github_content(readme_path)
        
        if content and isinstance(content, dict) and content.get('download_url'):
            try:
                readme_response = requests.get(content['download_url'])
                readme_response.raise_for_status()
                return readme_response.text
            except requests.exceptions.RequestException:
                continue
    
    return ""

def categorize_rl_algorithm(name, path, readme_content=""):
    """Categorize RL algorithms based on name and content."""
    name_lower = name.lower()
    path_lower = path.lower()
    content_lower = readme_content.lower()
    
    # Value-based methods
    if any(term in name_lower for term in ['dqn', 'q-learning', 'duel']):
        return "Value-Based Methods"
    
    # Policy-based methods  
    if any(term in name_lower for term in ['ppo', 'reinforce', 'policy']):
        return "Policy-Based Methods"
    
    # Actor-critic methods
    if any(term in name_lower for term in ['a2c', 'a3c', 'sac', 'td3', 'ddpg', 'actor', 'critic']):
        return "Actor-Critic Methods"
        
    # Multi-agent RL
    if any(term in name_lower for term in ['marl', 'multi-agent', 'ippo', 'mappo', 'self-play']):
        return "Multi-Agent RL"
        
    # Exploration methods
    if any(term in name_lower for term in ['rnd', 'exploration', 'curiosity']):
        return "Exploration Methods"
        
    # Imitation learning
    if any(term in name_lower for term in ['imitation', 'behavioral', 'cloning']):
        return "Imitation Learning"
        
    # Game environments
    if any(term in name_lower for term in ['vizdoom', 'flappybird', 'game']):
        return "Game Environments"
        
    # Unity ML-Agents
    if any(term in name_lower for term in ['ml-agents', 'unity']):
        return "Unity ML-Agents"
    
    return "Other"

def detect_environment(name, readme_content=""):
    """Detect the environment used by the RL algorithm."""
    name_lower = name.lower()
    content_lower = readme_content.lower()
    
    # Specific environments
    if 'atari' in name_lower or 'atari' in content_lower:
        return "Atari"
    elif 'mujoco' in name_lower or 'mujoco' in content_lower:
        return "MuJoCo"
    elif 'lunar' in name_lower or 'lunarlander' in content_lower:
        return "LunarLander"
    elif 'taxi' in name_lower or 'taxi' in content_lower:
        return "Taxi"
    elif 'frozenlake' in name_lower or 'frozen' in content_lower:
        return "Frozenlake"
    elif 'flappybird' in name_lower or 'flappy' in content_lower:
        return "Flappybird"
    elif 'vizdoom' in name_lower or 'vizdoom' in content_lower:
        return "Vizdoom"
    elif 'pong' in content_lower:
        return "Atari"
    elif any(env in content_lower for env in ['gymnasium', 'gym']):
        return "Gymnasium"
    
    return "Custom Environment"

def clean_display_name(name):
    """Clean folder name to create a display name."""
    # Handle special cases
    name = name.replace('-', ' ').replace('_', ' ')
    
    # Capitalize appropriately
    words = name.split()
    cleaned_words = []
    
    for word in words:
        word_lower = word.lower()
        if word_lower in ['dqn', 'ppo', 'a2c', 'sac', 'td3', 'ddpg', 'rnd', 'marl']:
            cleaned_words.append(word.upper())
        elif word_lower == 'rl':
            cleaned_words.append('RL')
        else:
            cleaned_words.append(word.capitalize())
    
    return ' '.join(cleaned_words)

def process_directory(path="", parent_name=""):
    """Process a directory and return RL implementations found."""
    content = fetch_github_content(path)
    if not content:
        return []
    
    implementations = []
    
    for item in content:
        if item['type'] == 'dir':
            item_name = item['name']
            item_path = item['path']
            
            # Skip common non-algorithm directories
            if item_name.lower() in ['.git', '__pycache__', 'node_modules', '.vscode', 'images', 'assets']:
                continue
            
            # Create display name
            if parent_name:
                display_name = f"{clean_display_name(item_name)} ({parent_name})"
            else:
                display_name = clean_display_name(item_name)
            
            # Fetch README content
            readme_content = fetch_readme_content(item_path)
            
            # Determine category and environment
            category = categorize_rl_algorithm(item_name, item_path, readme_content)
            environment = detect_environment(item_name, readme_content)
            
            # Create implementation entry
            implementation = {
                "name": item_name,
                "path": item_path,
                "display_name": display_name,
                "description": f"Implementation of {item_name} reinforcement learning algorithm",
                "readme_content": readme_content[:1000] if readme_content else "",  # Truncate for JSON size
                "github_url": f"https://github.com/{REPO_OWNER}/{REPO_NAME}/tree/master/{item_path}",
                "api_url": item['url'],
                "download_url": item.get('download_url'),
                "created_date": datetime.now().strftime('%Y-%m-%d'),
                "github_date": datetime.now().strftime('%Y-%m-%d'),
                "category": category,
                "framework": "PyTorch",  # Default assumption
                "environment": environment
            }
            
            implementations.append(implementation)
            
            # Recursively process subdirectories (but not too deep)
            if path.count('/') < 2:  # Limit depth
                sub_implementations = process_directory(item_path, clean_display_name(item_name))
                implementations.extend(sub_implementations)
    
    return implementations

def generate_rl_json():
    """Generate the RL JSON data file."""
    print("🚀 Starting RL data generation...")
    
    # Fetch all RL implementations
    implementations = process_directory()
    
    if not implementations:
        print("❌ No RL implementations found!")
        return False
    
    # Create the JSON structure
    rl_data = {
        "rl_implementations": implementations
    }
    
    # Write to JSON file
    data_path = BASE_PATH / DATA_FILE
    data_path.parent.mkdir(exist_ok=True)
    
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(rl_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated {DATA_FILE} with {len(implementations)} RL implementations")
    return True

def generate_markdown_files():
    """Generate individual markdown files for each RL implementation."""
    # Read the JSON data
    data_path = BASE_PATH / DATA_FILE
    if not data_path.exists():
        print("❌ RL JSON data not found. Run JSON generation first.")
        return False
    
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    implementations = data.get('rl_implementations', [])
    if not implementations:
        print("❌ No RL implementations found in JSON data.")
        return False
    
    # Create output directory
    models_path = BASE_PATH / MODELS_DIR
    models_path.mkdir(exist_ok=True)
    
    # Clear existing files
    for existing_file in models_path.glob('*.md'):
        existing_file.unlink()
        print(f"🗑️  Removed old file: {existing_file.name}")
    
    # Filter out image directories and other non-algorithm entries
    main_implementations = []
    for impl in implementations:
        name_lower = impl['name'].lower()
        if not any(skip in name_lower for skip in ['images', 'assets', 'docs', '__pycache__']):
            # Only include main algorithm directories, not sub-directories
            if impl['path'].count('/') <= 1:  # Top-level or one level deep
                main_implementations.append(impl)
    
    # Generate markdown files
    successful_count = 0
    for index, impl in enumerate(main_implementations, 1):
        try:
            name = impl['display_name']
            slug = re.sub(r'[^\w\s-]', '', name.lower())
            slug = re.sub(r'[-\s]+', '-', slug).strip('-')
            
            filename = f"{index:02d}-{slug}.md"
            filepath = models_path / filename
            
            # Generate markdown content
            content = f"""---
title: "{name}"
excerpt: "{impl['description']}"
collection: rl
layout: rl-implementation
category: "{impl['category']}"
framework: "{impl['framework']}"
environment: "{impl['environment']}"
github_url: "{impl['github_url']}"
date: {impl['github_date']}
---

## Overview
{impl['description']}

## Technical Details
- **Framework**: {impl['framework']}
- **Environment**: {impl['environment']}
- **Category**: {impl['category']}

## Implementation Details

{impl['readme_content'] if impl['readme_content'] else f'''
# {name}

This implementation demonstrates {impl['category'].lower()} using {impl['framework']} framework on {impl['environment']} environment.

## Features
- Clean and well-documented code
- Easy to understand implementation
- Comprehensive training and evaluation scripts

## Usage
Please refer to the GitHub repository for detailed usage instructions and training procedures.
'''}

## Source Code
📁 **GitHub Repository**: [{name}]({impl['github_url']})

View the complete implementation, training scripts, and documentation on GitHub.
"""
            
            # Write the file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Generated: {filename}")
            successful_count += 1
            
        except Exception as e:
            print(f"❌ Error generating file for {impl['name']}: {e}")
    
    print(f"\n🎉 Successfully generated {successful_count} RL markdown files")
    return True

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Refresh RL implementations data')
    parser.add_argument('--json-only', action='store_true', help='Only generate JSON data')
    parser.add_argument('--md-only', action='store_true', help='Only generate markdown files')
    args = parser.parse_args()
    
    if args.md_only:
        generate_markdown_files()
    elif args.json_only:
        generate_rl_json()
    else:
        # Generate both
        if generate_rl_json():
            generate_markdown_files()

if __name__ == "__main__":
    main()
