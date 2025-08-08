# GitHub Date Integration Documentation

## Overview

This system automatically fetches and displays authentic creation dates for models and datasets from GitHub repositories using the GitHub API. The dates represent actual commit timestamps from when the implementation was first created, providing accurate historical context.

## ✨ Features

### 🎯 **Automatic Date Fetching**
- **Models**: Fetches creation dates from `YuvrajSingh-mist/Paper-Replications` repository
- **Datasets**: Fetches creation dates from `YuvrajSingh-mist/Datasets-Collection` repository
- **Real-time Updates**: GitHub API integration ensures dates stay current

### 🔄 **Multiple Integration Points**
- **JSON Storage**: Dates stored in `_data/models.json` and `_data/datasets.json`
- **Markdown Files**: Individual model markdown files use GitHub dates
- **Card Display**: Model and dataset cards show formatted creation dates
- **GitHub Actions**: Automated workflows keep dates synchronized

### 📅 **Smart Date Display**
- **Format**: User-friendly display (e.g., "Mar 15, 2024")
- **Fallback**: Graceful handling when GitHub data unavailable
- **Live Loading**: JavaScript dynamically loads dates from JSON data

## 🛠️ Components

### Core Scripts

#### `fetch_github_dates.py`
**Purpose**: Main script to fetch GitHub creation dates via API

**Features**:
- Fetches commit dates for both models and datasets
- Updates JSON files with `github_date` and `created_date` fields
- Updates individual markdown files with authentic dates
- Rate limiting protection and error handling
- GitHub token support for higher API limits

**Usage**:
```bash
# Basic usage (anonymous API access)
python fetch_github_dates.py

# With GitHub token (recommended)
GITHUB_TOKEN=your_token_here python fetch_github_dates.py
```

#### `regenerate_models.py` (Updated)
**Enhancement**: Now uses GitHub dates from JSON when generating markdown files

**New Feature**:
```python
# Use GitHub date if available, otherwise fallback
github_date = model_data.get('github_date') or model_data.get('created_date')
model_date = github_date if github_date else datetime.now().strftime('%Y-%m-%d')
```

#### `generate_model_files.py` (Updated)
**Enhancement**: Incorporates GitHub dates into generated frontmatter

### Frontend Integration

#### Models Page (`_pages/models.html`)
**New Features**:
- Hidden JSON data container: `<script id="models-github-data">`
- JavaScript function `loadGitHubDates()` processes GitHub data
- Dynamic date insertion into model cards
- CSS styling for date display

**Implementation**:
```javascript
// Load GitHub dates from JSON data
function loadGitHubDates() {
    const githubData = JSON.parse(githubDataScript.textContent);
    // Map model names to GitHub dates
    // Update cards with formatted dates
}
```

#### Datasets Page (`_pages/datasets.html`)
**New Features**:
- Similar GitHub date loading functionality
- Dedicated JSON data container for datasets
- JavaScript function `loadDatasetGitHubDates()`

#### CSS Styling (`assets/css/models.css`)
**New Styles**:
```css
.model-card__date {
    padding: 8px 20px;
    color: #666;
    font-size: 0.85em;
    border-top: 1px solid #f5f5f5;
    background: #fafafa;
}
```

## 🔄 GitHub Actions Integration

### Updated Workflows

#### `update-models.yml`
**Enhanced Step**:
```yaml
- name: Update models from GitHub API and regenerate markdown files
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    echo "📅 Fetching GitHub creation dates for models and datasets..."
    python fetch_github_dates.py
    # ... rest of workflow
```

#### `standardize-models.yml`
**Enhanced Step**:
```yaml
- name: Run comprehensive standardization
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    echo "📅 Ensuring GitHub creation dates are up to date..."
    python fetch_github_dates.py
    # ... rest of workflow
```

#### `update-datasets.yml` (New)
**Purpose**: Dedicated workflow for updating dataset GitHub dates

**Schedule**: Weekly on Saturdays at 6 AM UTC
**Triggers**: Manual, dataset file changes, script updates

## 📊 Data Structure

### Models JSON Format
```json
{
  "models": [
    {
      "name": "LSTM",
      "display_name": "Lstm",
      "description": "From scratch implementation of lstm",
      "github_url": "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/lstm",
      "created_date": "2025-04-25",
      "github_date": "2025-04-25"
    }
  ],
  "last_updated": "2025-08-08T19:01:30.464938"
}
```

### Datasets JSON Format
```json
{
  "datasets": [
    {
      "name": "QnA-Irrigation-Diseases",
      "display_name": "QnA Irrigation Diseases Dataset",
      "github_url": "https://github.com/YuvrajSingh-mist/Datasets-Collection/tree/main/QnA-Irrigation-Diseases",
      "created_date": "2025-08-08",
      "github_date": "2025-08-08"
    }
  ],
  "last_updated": "2025-08-08T19:01:33.046393"
}
```

## 🎯 User Experience

### Model Cards Display
- **Before**: Generic dates or no dates
- **After**: Authentic creation dates like "📅 Created: Apr 25, 2025"

### Dataset Cards Display
- **Before**: Manual date management
- **After**: Automatic GitHub commit dates

### Live Loading
- JavaScript dynamically fetches dates from JSON
- No page reload required for date updates
- Graceful fallback when data unavailable

## 🛡️ Error Handling

### API Rate Limits
- Anonymous access: 60 requests/hour
- Token access: 5000 requests/hour
- Automatic delay between requests (0.3 seconds)

### Fallback Strategies
- If GitHub API fails: Use existing dates
- If no date available: Use default date (2024-01-01)
- If JSON parsing fails: Skip date loading gracefully

### Logging and Debugging
```python
print(f"✅ Updated {updated_count} model cards with GitHub dates")
print(f"⚠️ No GitHub date found for {filename}")
console.log('📅 Date mapping created:', nameToDate);
```

## 🚀 Deployment

### Manual Update
```bash
# Fetch latest GitHub dates
python fetch_github_dates.py

# Regenerate markdown files with new dates
python regenerate_models.py

# Start Jekyll to see changes
bundle exec jekyll serve
```

### Automated Updates
- **Models**: Updated weekly on Sundays via GitHub Actions
- **Datasets**: Updated weekly on Saturdays via GitHub Actions
- **On-demand**: Manual workflow dispatch available

## 📈 Benefits

### 🎯 **Accuracy**
- Real commit dates instead of arbitrary dates
- Historical context for implementation timeline
- Authentic project evolution tracking

### 🔄 **Automation**
- No manual date management required
- Consistent date format across all content
- Automatic synchronization with GitHub

### 👥 **User Experience**
- Clear creation timeline for models/datasets
- Professional presentation with real dates
- Enhanced credibility and transparency

### 🛠️ **Maintainability**
- Single source of truth (GitHub API)
- Centralized date management
- Easy to update and modify

## 🔧 Configuration

### Environment Variables
```bash
# Optional: GitHub personal access token for higher API limits
export GITHUB_TOKEN=your_token_here
```

### Repository Configuration
- **Models Repository**: `YuvrajSingh-mist/Paper-Replications`
- **Datasets Repository**: `YuvrajSingh-mist/Datasets-Collection`
- **Rate Limiting**: 0.3 second delay between API calls

## 📋 Maintenance

### Regular Tasks
1. **Monitor API Usage**: Check GitHub API rate limits
2. **Verify Dates**: Ensure dates are accurate and updating
3. **Update Scripts**: Keep GitHub API integration current
4. **Test Workflows**: Verify automation is working

### Troubleshooting
- **API Failures**: Check network connectivity and GitHub status
- **Date Mismatches**: Verify repository structure and folder names
- **Display Issues**: Check JavaScript console for errors
- **Workflow Failures**: Review GitHub Actions logs

## 🎉 Result

The GitHub date integration provides a professional, automated system for displaying authentic creation dates across the entire website. Models and datasets now show real commit dates from GitHub, enhancing credibility and providing accurate historical context for the implementation timeline.

### Example Output
- **LSTM Model**: "📅 Created: Apr 25, 2025"
- **Dataset**: "📅 Created: Aug 8, 2025"
- **Automatic Updates**: Weekly synchronization via GitHub Actions
