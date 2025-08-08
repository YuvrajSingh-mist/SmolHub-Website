# SmolHub Automation System

This document explains the complete automation system for maintaining consistent model markdown files in the SmolHub website.

## 🤖 Automation Overview

The system ensures all model markdown files follow consistent standards and automatically fixes common issues.

### Key Components

1. **Standardization Scripts** - Ensure consistent format
2. **Validation Scripts** - Check compliance with guidelines  
3. **Templates** - For creating new model files
4. **GitHub Actions** - Automated workflows

## 📁 File Structure

```
SmolHub-Website/
├── _models/                      # Model markdown files
├── _templates/                   # Templates for new models
│   └── model_template.md
├── _data/
│   └── models.json              # Canonical model data
├── .github/workflows/           # GitHub Actions
│   ├── auto-detect-models.yml   # Auto-detect new models
│   ├── refresh-models.yml       # Weekly refresh
│   ├── update-models.yml        # Daily updates
│   └── standardize-models.yml   # Standardization workflow
└── Scripts:
    ├── standardize_markdowns.py # Main standardization script
    ├── validate_guidelines.py   # Validation script
    ├── fix_image_links.py       # Fix image URLs
    ├── create_new_model.py      # Create new model files
    └── auto_detect_models.py    # Auto-detection script
```

## 🔧 Scripts and Their Purpose

### Core Scripts

#### `standardize_markdowns.py`
**Purpose**: Comprehensive standardization of all markdown files
- Fixes frontmatter format
- Ensures proper layout (`model-implementation`)
- Converts image URLs to `raw.githubusercontent.com`
- Standardizes content structure
- Creates templates and automation tools

**Usage**: `python standardize_markdowns.py`

#### `validate_guidelines.py`
**Purpose**: Validates that all files follow guidelines
- Checks layout usage
- Validates no local image references
- Verifies proper GitHub image links
- Confirms title consistency with models.json
- Validates file count matches JSON entries
- Checks automation setup

**Usage**: `python validate_guidelines.py`

#### `create_new_model.py`
**Purpose**: Creates new model markdown files from template
**Usage**: 
```bash
python create_new_model.py "Model Name" "Category" "Dataset" "GitHub URL"
```

**Example**:
```bash
python create_new_model.py "ResNet" "Computer Vision" "ImageNet" "https://github.com/user/repo"
```

### Legacy Scripts (still used by workflows)

- `fix_image_links.py` - Fixes image URLs (now integrated into standardization)
- `auto_detect_models.py` - Auto-detects new models from repositories
- `regenerate_models.py` - Regenerates all markdown files
- `update_models.py` - Updates models.json from GitHub API

## 📋 Standards Enforced

### Frontmatter Format
```yaml
---
title: "Model Name"
excerpt: "From scratch implementation of Model Name"
collection: models
layout: model-implementation
category: "Category"
framework: "PyTorch"
dataset: "Dataset"
github_url: "https://github.com/user/repo"
date: YYYY-MM-DD
---
```

### Content Structure
```markdown
## Overview
From scratch implementation of [Model Name]

## Technical Details
- **Framework**: PyTorch
- **Dataset**: [Dataset]
- **Category**: [Category]

## Implementation Details
[Detailed content...]

## Source Code
📁 **GitHub Repository**: [Model Name](github_url)
```

### Image Links
✅ **Correct**: `![Description](https://raw.githubusercontent.com/user/repo/branch/path/image.jpg)`
❌ **Incorrect**: `![Description](https://github.com/user/repo/blob/branch/path/image.jpg)`
❌ **Incorrect**: `<img src="local/path/image.jpg">`

## 🔄 GitHub Actions Workflows

### 1. `auto-detect-models.yml`
- **Trigger**: Daily at 8 AM UTC, manual, repository dispatch
- **Purpose**: Auto-detect new models from repositories
- **Actions**: 
  - Runs `auto_detect_models.py`
  - Applies standardization
  - Validates results
  - Commits changes

### 2. `refresh-models.yml`
- **Trigger**: Weekly on Sundays, manual, repository dispatch
- **Purpose**: Full refresh of all model data
- **Actions**:
  - Updates from GitHub API
  - Regenerates all markdown files
  - Applies standardization
  - Validates results

### 3. `update-models.yml`
- **Trigger**: Daily at 6 AM UTC, manual, file changes
- **Purpose**: Regular updates and validation
- **Actions**:
  - Updates models.json
  - Regenerates markdown files
  - Applies standardization
  - Validates guidelines

### 4. `standardize-models.yml`
- **Trigger**: Manual, markdown file changes, PR changes
- **Purpose**: Ensure all files follow standards
- **Actions**:
  - Runs comprehensive standardization
  - Validates all guidelines
  - Commits any fixes needed

## 🎯 Workflow Integration

### When you add a new model manually:
1. Use: `python create_new_model.py "Name" "Category" "Dataset" "URL"`
2. The standardization workflow will automatically run
3. Validation ensures compliance

### When GitHub Actions detect new models:
1. Auto-detection runs daily
2. New models are added using standardized format
3. All existing models are validated
4. Changes are committed automatically

### When making bulk changes:
1. Run: `python standardize_markdowns.py`
2. Run: `python validate_guidelines.py`
3. Commit changes
4. GitHub Actions will validate on push

## 🔍 Validation Checks

The system performs these validation checks:

1. **Layout Usage** ✅ All files use `layout: model-implementation`
2. **Local Images** ✅ No local image references found
3. **GitHub Links** ✅ Proper `raw.githubusercontent.com` image URLs
4. **Title Consistency** ✅ All titles match models.json
5. **File Count** ✅ Markdown files count matches JSON entries
6. **Automation Setup** ✅ Templates and scripts are available

## 🚀 Benefits

### Consistency
- All model files follow the same format
- Standardized frontmatter and content structure
- Consistent image handling

### Automation
- New models are automatically detected and added
- Regular updates keep content fresh
- Manual intervention only needed for special cases

### Quality
- Validation ensures no broken images or links
- Guidelines prevent common formatting issues
- Templates ensure new files start with correct format

### Maintenance
- Easy to update all files at once
- Clear documentation of standards
- Automated testing of compliance

## 📝 Creating New Models

### Option 1: Use the automation script (Recommended)
```bash
python create_new_model.py "BERT" "Language Models" "BookCorpus" "https://github.com/user/bert"
```

### Option 2: Copy template manually
1. Copy `_templates/model_template.md`
2. Replace all `{PLACEHOLDER}` values
3. Save as `XX-modelname.md` in `_models/`
4. Run standardization: `python standardize_markdowns.py`

### Option 3: Let auto-detection handle it
- Add model to your implementation repository
- Wait for daily auto-detection (8 AM UTC)
- Or trigger manually via GitHub Actions

## 🔧 Troubleshooting

### If validation fails:
1. Run: `python standardize_markdowns.py`
2. Run: `python validate_guidelines.py`
3. Check the output for specific issues
4. Fix manually if needed

### If images don't load:
1. Check that URLs use `raw.githubusercontent.com`
2. Run: `python fix_image_links.py`
3. Verify the image exists in the repository

### If new models aren't detected:
1. Check that the source repository is accessible
2. Verify the model has proper structure
3. Run auto-detection manually: `python auto_detect_models.py`

## 📈 Future Enhancements

- [ ] Automatic image optimization
- [ ] Markdown linting integration
- [ ] Performance metrics tracking
- [ ] SEO optimization automation
- [ ] Multi-language support templates
