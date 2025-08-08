# Dataset Automation System

## Overview

The dataset automation system automatically detects new datasets from GitHub repositories and generates corresponding Jekyll markdown files for the website. This system ensures that all datasets are properly formatted, validated, and integrated into the site structure.

## System Components

### Core Scripts

1. **`auto_detect_datasets.py`** - Main detection script
   - Monitors GitHub repositories for new dataset folders
   - Extracts metadata from README files
   - Updates `_data/datasets.json` with new entries
   - Handles date extraction and formatting

2. **`generate_dataset_files.py`** - Markdown generation script
   - Creates Jekyll-compatible markdown files from JSON data
   - Generates proper frontmatter with all required fields
   - Handles image link conversion and content formatting
   - Uses standardized templates for consistency

3. **`validate_datasets.py`** - Validation script
   - Checks frontmatter structure and required fields
   - Validates content sections and formatting
   - Ensures JSON-markdown file consistency
   - Reports issues and compliance status

### Supporting Files

- **`_templates/dataset_template.md`** - Template for new dataset files
- **`refresh_datasets.sh`** - Manual refresh script
- **`.github/workflows/auto-update-datasets.yml`** - GitHub Actions automation

## How It Works

### Automatic Detection Process

1. **Repository Scanning**: The system scans configured GitHub repositories for new folders
2. **Metadata Extraction**: Extracts dataset information from README files and repository structure
3. **JSON Update**: Updates the `_data/datasets.json` file with new dataset entries
4. **Markdown Generation**: Creates individual markdown files in the `_datasets/` directory
5. **Validation**: Ensures all files meet quality standards

### GitHub Integration

- **Token Authentication**: Uses GitHub API tokens for repository access
- **Rate Limiting**: Respects API rate limits and handles errors gracefully
- **Date Integration**: Automatically fetches creation and update dates from Git history

## Configuration

### Environment Variables

```bash
GITHUB_TOKEN=your_github_token_here
```

### Repository Configuration

The system can monitor multiple repositories by configuring the repository list in `auto_detect_datasets.py`:

```python
REPOSITORIES = [
    'owner/repo-name-1',
    'owner/repo-name-2'
]
```

## File Structure

```
_data/
  datasets.json          # Central dataset registry
_datasets/
  *.md                   # Individual dataset pages
_templates/
  dataset_template.md    # Template for new datasets
```

### Dataset JSON Schema

```json
{
  "datasets": [
    {
      "name": "dataset-name",
      "title": "Human Readable Title",
      "description": "Brief description",
      "github_url": "https://github.com/owner/repo",
      "created_date": "2024-01-01",
      "updated_date": "2024-01-01",
      "tags": ["tag1", "tag2"],
      "tasks": ["task1", "task2"],
      "size": "1000 samples",
      "format": "JSON/CSV/etc"
    }
  ]
}
```

### Markdown Frontmatter

```yaml
---
title: "Dataset Title"
excerpt: "Brief description"
collection: datasets
github_url: "https://github.com/owner/repo"
date: 2024-01-01
tags:
  - tag1
  - tag2
tasks:
  - task1
  - task2
size: "1000 samples"
format: "JSON"
---
```

## Usage

### Manual Operations

1. **Full Refresh**:
   ```bash
   ./refresh_datasets.sh
   ```

2. **Detection Only**:
   ```bash
   python3 auto_detect_datasets.py
   ```

3. **Generation Only**:
   ```bash
   python3 generate_dataset_files.py
   ```

4. **Validation Only**:
   ```bash
   python3 validate_datasets.py
   ```

### Automated Operations

The system runs automatically via GitHub Actions:
- **Schedule**: Every 30 minutes
- **Manual Trigger**: Via workflow dispatch
- **Auto-commit**: Changes are automatically committed and pushed

## Error Handling

### Common Issues

1. **Missing README Files**: Datasets without README files will use default metadata
2. **API Rate Limits**: System implements exponential backoff for rate limit handling
3. **Malformed YAML**: Validation catches and reports frontmatter syntax errors
4. **Missing Images**: Automatic conversion from local to GitHub-hosted images

### Recovery Procedures

1. **Backup System**: Automatic backups of JSON files before major updates
2. **Rollback**: Git history allows reverting to previous states
3. **Manual Override**: All scripts support manual configuration and forced updates

## Quality Assurance

### Validation Rules

- **Required Fields**: All datasets must have title, description, and GitHub URL
- **URL Validation**: GitHub URLs must be valid and accessible
- **Content Structure**: Markdown files must follow standardized section structure
- **Image Links**: All images must use GitHub raw URLs, not local references

### Consistency Checks

- **JSON-Markdown Sync**: Ensures datasets.json entries match markdown files
- **Duplicate Detection**: Prevents duplicate dataset entries
- **Naming Conventions**: Enforces consistent file naming patterns

## Maintenance

### Regular Tasks

1. **Monthly Review**: Check for orphaned files or inconsistencies
2. **Token Renewal**: Update GitHub tokens before expiration
3. **Dependency Updates**: Keep Python packages current
4. **Performance Monitoring**: Monitor API usage and script execution times

### Troubleshooting

1. **Check Logs**: GitHub Actions provide detailed execution logs
2. **Validate Manually**: Run validation script to identify issues
3. **Test Locally**: Run scripts locally before deploying changes
4. **Backup Recovery**: Use Git history to recover from errors

## Integration with Existing Systems

### Models System Compatibility

The dataset automation mirrors the models automation system:
- Same directory structure patterns
- Compatible script naming conventions  
- Shared validation patterns
- Unified GitHub Actions approach

### Jekyll Integration

- **Collections**: Datasets are part of Jekyll collections system
- **Layouts**: Uses existing layout templates
- **Navigation**: Integrates with site navigation structure
- **Search**: Datasets are included in site search functionality

## Future Enhancements

### Planned Features

1. **Multi-language Support**: Support for datasets in multiple languages
2. **Advanced Metadata**: Enhanced metadata extraction from various file formats
3. **Quality Scoring**: Automatic quality assessment for datasets
4. **Version Tracking**: Track dataset versions and changes over time

### Extension Points

- **Custom Templates**: Support for dataset-type-specific templates
- **External APIs**: Integration with dataset registries and APIs
- **Notification System**: Alerts for new datasets or issues
- **Analytics Integration**: Usage tracking and popularity metrics
