#!/usr/bin/env python3

"""
SmolHub Playground Markdown Generator
This script generates markdown files for SmolHub playground projects from the JSON data.
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime

def load_smolhub_data():
    """Load SmolHub data from JSON file"""
    data_file = Path(__file__).parent / '_data' / 'smolhub_playground.json'
    
    if not data_file.exists():
        print("❌ SmolHub data file not found. Please run generate-smolhub-data.js first.")
        return None
    
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_content(content):
    """Clean and format content for Jekyll"""
    if not content:
        return ""
    
    # Convert Windows line endings to Unix
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    
    # Remove any triple quotes that might break frontmatter
    content = content.replace('"""', '"')
    content = content.replace("'''", "'")
    
    # Escape any YAML special characters in content
    content = content.replace('{{', '{{ "{{" }}')
    content = content.replace('}}', '{{ "}}" }}')
    
    return content

def convert_images_to_links(content, github_url):
    """Convert local image references to GitHub links"""
    if not content or not github_url:
        return content
    
    # Pattern to match image markdown: ![alt](path) or ![alt](./path) or images/file
    image_patterns = [
        (r'!\[([^\]]*)\]\(([^)]+\.(?:png|jpg|jpeg|gif|svg|webp))\)', True),  # ![alt](image.png)
        (r'(images/[^)\s]+\.(?:png|jpg|jpeg|gif|svg|webp))', False),          # images/file.png
    ]
    
    for pattern, is_markdown in image_patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            if is_markdown and isinstance(match, tuple) and len(match) == 2:
                # For ![alt](image) pattern
                alt_text, image_path = match
                # Create GitHub raw URL
                github_image_url = f"{github_url.replace('/tree/', '/raw/')}/{image_path}"
                # Replace in content
                content = content.replace(f'![{alt_text}]({image_path})', f'![{alt_text}]({github_image_url})')
            elif not is_markdown:
                # For images/file.png pattern (standalone)
                image_path = match
                github_image_url = f"{github_url.replace('/tree/', '/raw/')}/{image_path}"
                # Only replace if it's not already part of a markdown link
                if f']({image_path})' not in content and f'[{image_path}]' not in content:
                    content = content.replace(image_path, f'[🖼️ {image_path}]({github_image_url})')
    
    return content

def create_markdown_from_json(project_data, file_number):
    """Create markdown content from JSON project data"""
    name = project_data.get('name', 'Unknown Project')
    display_name = project_data.get('display_name', name)
    description = project_data.get('description', 'SmolHub playground project')
    github_url = project_data.get('github_url', '')
    readme_content = project_data.get('readme_content', '')
    tags = project_data.get('tags', ['playground'])
    project_date = project_data.get('created_date', '2025-08-08')
    
    # Clean and process content
    clean_readme = clean_content(readme_content)
    
    # Remove title if it already exists in README to avoid duplication
    if clean_readme.startswith(f'# {name}'):
        lines = clean_readme.split('\n')
        clean_readme = '\n'.join(lines[1:]).strip()
    elif clean_readme.startswith(f'# {display_name}'):
        lines = clean_readme.split('\n')
        clean_readme = '\n'.join(lines[1:]).strip()
    
    # Ensure content starts with a proper title
    if clean_readme and not clean_readme.startswith('#'):
        clean_readme = f"# {display_name}\n\n{clean_readme}"
    
    # Convert images to GitHub hyperlinks
    if github_url:
        clean_readme = convert_images_to_links(clean_readme, github_url)
    
    # Add source code section if not present
    if 'source code' not in clean_readme.lower() and github_url:
        clean_readme += f"\n\n## Source Code\n📁 **GitHub Repository**: [{display_name}]({github_url})\n\nView the complete implementation, documentation, and examples on GitHub."
    
    # Add interactive features section
    if 'gradio' in clean_readme.lower() or 'interactive' in clean_readme.lower():
        if 'interactive features' not in clean_readme.lower():
            clean_readme += f"\n\n## Interactive Features\n🎮 **Web Interface**: This project includes a Gradio-based web interface for easy interaction and experimentation.\n\n📱 **User-Friendly**: Simple, intuitive interface perfect for testing and learning."
    
    # Create comprehensive frontmatter
    tags_str = ', '.join(tags) if tags else 'playground'
    
    frontmatter = f"""---
title: "{display_name}"
excerpt: "{description[:200]}{'...' if len(description) > 200 else ''} 🎮<br/><img src='/images/500x300.png'>"
collection: smolhub
github_url: "{github_url}"
date: {project_date}
tags: [{', '.join([f'"{tag}"' for tag in tags])}]
---

## Project Overview
{description}

## Technical Details
- **Type**: SmolHub Playground Project
- **Framework**: PyTorch
- **Category**: Experimental AI/ML
- **Repository**: [{display_name}]({github_url})

## Implementation Details

{clean_readme}

---

*This project is part of the SmolHub Playground collection - a space for experimental AI models and proof-of-concept implementations.*"""

    return frontmatter

def generate_smolhub_markdowns():
    """Main function to generate SmolHub markdown files"""
    print("🚀 Starting SmolHub playground markdown generation...")
    
    # Load SmolHub data
    smolhub_data = load_smolhub_data()
    if not smolhub_data:
        return
    
    projects = smolhub_data.get('projects', [])
    print(f"📊 Found {len(projects)} playground projects")
    
    # Create _smolhub directory if it doesn't exist
    smolhub_dir = Path(__file__).parent / '_smolhub'
    smolhub_dir.mkdir(exist_ok=True)
    
    # Clear existing auto-generated files (keep manual ones)
    print("🧹 Cleaning up old auto-generated files...")
    existing_files = list(smolhub_dir.glob('project-*.md'))
    manual_files = len(existing_files)
    
    generated_count = 0
    updated_count = 0
    
    # Generate markdown files
    for i, project in enumerate(projects, 1):
        project_name = project.get('name', f'project-{i}')
        filename = f"playground-{i:02d}-{project_name.lower().replace(' ', '-')}.md"
        file_path = smolhub_dir / filename
        
        # Generate markdown content
        try:
            markdown_content = create_markdown_from_json(project, i)
            
            # Check if file exists and has changed
            file_exists = file_path.exists()
            needs_update = True
            
            if file_exists:
                with open(file_path, 'r', encoding='utf-8') as f:
                    existing_content = f.read()
                needs_update = existing_content != markdown_content
            
            if needs_update:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                
                if file_exists:
                    print(f"✏️  Updated: {filename}")
                    updated_count += 1
                else:
                    print(f"✅ Generated: {filename}")
                    generated_count += 1
            else:
                print(f"⏭️  Skipped: {filename} (no changes)")
                
        except Exception as e:
            print(f"❌ Error generating {filename}: {e}")
            continue
    
    # Summary
    print(f"\n📋 Summary:")
    print(f"   📄 Manual files preserved: {manual_files}")
    print(f"   ✅ New files generated: {generated_count}")
    print(f"   ✏️  Files updated: {updated_count}")
    print(f"   📊 Total playground projects: {len(projects)}")
    
    print(f"\n🎉 SmolHub playground markdown generation complete!")
    print(f"📁 Files are ready in: {smolhub_dir}")

if __name__ == "__main__":
    generate_smolhub_markdowns()
