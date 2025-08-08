#!/usr/bin/env python3
"""
Convert local image references to GitHub hyperlinks in all model markdown files
"""

import os
import re
import json

def get_model_github_urls():
    """Get the GitHub URLs for each model from models.json"""
    models_file = "_data/models.json"
    github_urls = {}
    
    if os.path.exists(models_file):
        with open(models_file, 'r') as f:
            data = json.load(f)
        
        # Handle both old and new JSON structures
        models_list = data.get('models', data) if isinstance(data, dict) else data
        
        for model in models_list:
            if isinstance(model, dict):
                name = model.get('name', '')
                github_url = model.get('github_url', '')
                if name and github_url:
                    # Convert tree/master to blob/master for direct file access
                    base_url = github_url.replace('/tree/master/', '/blob/master/')
                    github_urls[name] = base_url
    
    return github_urls

def convert_image_to_link(match, github_base_url):
    """Convert an image markdown to a hyperlink"""
    alt_text = match.group(1)
    image_path = match.group(2)
    
    # Create appropriate link text based on alt text
    if 'loss' in alt_text.lower():
        link_text = "📊 View Training Loss Curves"
    elif 'train' in alt_text.lower() and 'val' in alt_text.lower():
        link_text = "📈 View Train and Validation Loss"
    elif 'result' in alt_text.lower():
        link_text = "🖼️ View Results"
    elif 'sample' in alt_text.lower():
        link_text = "🎨 View Generated Samples"
    elif 'architecture' in alt_text.lower():
        link_text = "🏗️ View Model Architecture"
    elif 'output' in alt_text.lower():
        link_text = "📋 View Model Output"
    else:
        link_text = f"🔗 View {alt_text}"
    
    # Create GitHub URL
    github_image_url = f"{github_base_url}/{image_path}"
    
    # Return as hyperlink
    return f"[{link_text}]({github_image_url})"

def update_markdown_file(filepath, github_urls):
    """Update a single markdown file"""
    print(f"Processing {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract model folder name from frontmatter
    github_url_match = re.search(r'github_url:\s*"([^"]+)"', content)
    if not github_url_match:
        print(f"  ⚠️  No github_url found in {filepath}")
        return False
    
    github_url = github_url_match.group(1)
    github_base_url = github_url.replace('/tree/master/', '/blob/master/')
    
    # Find all image references
    image_pattern = r'!\[([^\]]*)\]\(([^)]+\.(jpg|jpeg|png|gif|svg))\)'
    images_found = re.findall(image_pattern, content)
    
    if not images_found:
        print(f"  ✅ No images found in {filepath}")
        return False
    
    print(f"  🖼️  Found {len(images_found)} images in {filepath}")
    
    # Replace all image references with hyperlinks
    def replace_image(match):
        return convert_image_to_link(match, github_base_url)
    
    updated_content = re.sub(image_pattern, replace_image, content)
    
    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"  ✅ Updated {len(images_found)} image references in {filepath}")
    return True

def main():
    """Main function to update all markdown files"""
    models_dir = "_models"
    
    if not os.path.exists(models_dir):
        print(f"❌ Models directory {models_dir} not found")
        return
    
    # Get all markdown files
    markdown_files = []
    for filename in os.listdir(models_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(models_dir, filename)
            markdown_files.append(filepath)
    
    print(f"🔍 Found {len(markdown_files)} markdown files to process")
    
    # Get GitHub URLs
    github_urls = get_model_github_urls()
    print(f"📚 Loaded GitHub URLs for {len(github_urls)} models")
    
    # Process each file
    updated_count = 0
    for filepath in sorted(markdown_files):
        if update_markdown_file(filepath, github_urls):
            updated_count += 1
    
    print(f"\n🎉 Successfully updated {updated_count} markdown files!")
    print("📝 All local image references have been converted to GitHub hyperlinks")

if __name__ == "__main__":
    main()
