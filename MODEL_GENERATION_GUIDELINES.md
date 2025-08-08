# Model Generation Guidelines

This document outlines the automated guidelines followed by the GitHub Actions workflows for generating model markdown files.

## 🎯 Core Guidelines

### 1. Layout System
- **Layout Used**: `model-implementation` (NOT `paper-replication`)
- **Location**: `_layouts/model-implementation.html`
- **Features**: Clean header, simplified meta information, no banner, no tags

### 2. Image Handling
- **Approach**: Convert ALL local image references to GitHub hyperlinks
- **Format**: `![Alt Text](local/path.jpg)` → `[📊 View Training Loss Curves](https://github.com/user/repo/blob/master/path.jpg)`
- **Link Text Types**:
  - Loss curves: "📊 View Training Loss Curves"
  - Results: "🖼️ View Results"  
  - Samples: "🎨 View Generated Samples"
  - Architecture: "🏗️ View Model Architecture"
  - Generic: "🔗 View [Alt Text]"

### 3. Data Source
- **Primary Source**: GitHub API data from `_data/models.json`
- **Content**: Use exact README content from GitHub repositories
- **Dates**: Real commit dates from GitHub API (NOT fake dates)
- **Titles**: Exact name matching from models.json

### 4. File Structure
```
_models/
├── 01-attention-mechanisms.md
├── 02-bert.md
├── 03-cgans.md
└── ...
```

### 5. Frontmatter Format
```yaml
---
title: "Exact Name from JSON"
excerpt: "Description from GitHub API"
collection: models
layout: model-implementation  # NOT paper-replication
category: "Auto-detected Category"
framework: "Auto-detected Framework"
dataset: "Auto-detected Dataset"
github_url: "Real GitHub URL from API"
date: 2024-06-20  # Real commit date from GitHub
---
```

## 🔄 Automated Workflows

### Daily Update (update-models.yml)
- **Trigger**: Daily at 6 AM UTC
- **Process**:
  1. Fetch latest GitHub API data
  2. Regenerate ALL markdown files
  3. Convert images to GitHub links
  4. Commit changes automatically

### Weekly Refresh (refresh-models.yml)  
- **Trigger**: Weekly on Sundays
- **Process**:
  1. Full refresh from GitHub API
  2. Regenerate all files with latest guidelines
  3. Ensure all images are converted
  4. Update repository

### Auto-Detection (auto-detect-models.yml)
- **Trigger**: Daily at 8 AM UTC
- **Process**:
  1. Detect new models in repository
  2. Add to models.json automatically
  3. Generate markdown files with all guidelines
  4. Convert images to links

## 🛠️ Scripts Overview

### Core Scripts
- `regenerate_models.py`: Main generation script following all guidelines
- `fix_images_direct.py`: Converts images to GitHub hyperlinks
- `auto_detect_models.py`: Detects and adds new models
- `update_models.py`: Fetches GitHub API data

### Image Conversion Process
1. **Detect**: Find all `![...](...jpg/png/gif)` references
2. **Extract**: Get alt text and image path
3. **Convert**: Create appropriate link text with emoji
4. **Replace**: Replace with `[Link Text](GitHub URL)`

## 📋 Quality Assurance

### Automated Checks
- ✅ All files use `model-implementation` layout
- ✅ No local image references remain
- ✅ All GitHub URLs are valid
- ✅ Real commit dates are used
- ✅ Exact title matching from JSON

### Manual Verification Commands
```bash
# Check layout usage
grep -r "layout:" _models/ | grep -v "model-implementation"

# Check for remaining local images
grep -r "!\[.*\]([^)]*\.(jpg|png|gif))" _models/

# Verify GitHub links
grep -r "github.com.*\.(jpg|png|gif)" _models/
```

## 🔧 Troubleshooting

### Common Issues
1. **Wrong Layout**: Run `find _models -name "*.md" -exec sed -i 's/layout: paper-replication/layout: model-implementation/g' {} \;`
2. **Local Images**: Run `python fix_images_direct.py`
3. **Outdated Content**: Run `python regenerate_models.py`

### Emergency Regeneration
```bash
# Full reset following all guidelines
python update_models.py --fetch --github-token $GITHUB_TOKEN
python regenerate_models.py
python fix_images_direct.py
```

## 📈 Future Enhancements

- [ ] Automatic detection of new frameworks/datasets
- [ ] Enhanced image link text based on context
- [ ] Automatic category classification improvements
- [ ] Integration with more repository hosting platforms

## 🎉 Success Metrics

The system is working correctly when:
- All model files use `model-implementation` layout
- No local image references exist
- All images are clickable GitHub links
- Content matches GitHub repository exactly
- New models are detected and added automatically

---

*This system ensures consistent, automated, and high-quality model documentation following the "From Scratch Implementation" approach.*
