# 🔐 Secure Models Data Generator

This tool securely fetches your models data from the Paper-Replications repository using your GitHub Personal Access Token.

## 🚨 Security Notice

**Your GitHub token is kept secure and never exposed in client-side code!** This script runs locally on your machine and only generates static data files.

## 📋 Prerequisites

1. **Node.js** installed on your system
2. **GitHub Personal Access Token** with `repo` scope

## 🎫 Creating a GitHub Token

1. Go to [GitHub Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a name like "Portfolio Models Generator"
4. Select the `repo` scope (full control of private repositories)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again!)

## 🚀 Usage

### Windows (Command Prompt)
```cmd
set GITHUB_TOKEN=your_token_here
update-models.bat
```

### Windows (PowerShell)
```powershell
$env:GITHUB_TOKEN="your_token_here"
./update-models.bat
```

### Linux/Mac (Terminal)
```bash
export GITHUB_TOKEN=your_token_here
./update-models.sh
```

### One-liner (any system)
```bash
GITHUB_TOKEN=your_token_here node generate-models-data.js
```

## 📊 What It Does

1. 🔍 Fetches all directories from your Paper-Replications repository
2. 📄 Downloads README content for each model (if available)
3. 🏷️ Generates clean display names and descriptions
4. 💾 Creates `_data/models.json` with all the data
5. ✨ Your Jekyll site automatically uses this data

## 🔄 Workflow

1. **Run the script** with your token
2. **Review** the generated `_data/models.json` file
3. **Commit and push** the changes to GitHub
4. **GitHub Pages rebuilds** your site automatically
5. **Visitors see** all your models instantly!

## 🎯 Benefits

- ✅ **5,000 requests/hour** (vs 60 unauthenticated)
- ✅ **Secure token handling** (never exposed publicly)
- ✅ **Fast page loads** (pre-built static data)
- ✅ **Automatic descriptions** from README files
- ✅ **Sorted by name** for better organization

## 🔒 Security Features

- Token is only used locally on your machine
- Token is never stored in files or committed to Git
- Generated data contains no sensitive information
- Works offline after data is generated

## 🐛 Troubleshooting

### "Node.js not found"
Install Node.js from https://nodejs.org/

### "GITHUB_TOKEN required"
Make sure you set the environment variable with your token

### "GitHub API error: 403"
Your token might be expired or lack proper permissions

### "No models found"
Check that your Paper-Replications repository has directories

## 📁 Generated File Structure

The script creates `_data/models.json` with this structure:
```json
{
  "last_updated": "2025-08-06T12:00:00.000Z",
  "total_models": 41,
  "models": [
    {
      "name": "BERT",
      "display_name": "Bert",
      "description": "Bidirectional Encoder Representations from Transformers implementation",
      "readme_content": "# BERT\n\n...",
      "github_url": "https://github.com/YuvrajSingh-mist/Paper-Replications/tree/master/BERT"
    }
  ]
}
```

## 🔄 Regular Updates

Run this script whenever you:
- Add new models to your repository
- Update README files
- Want to refresh the descriptions

The Jekyll site will automatically rebuild and show the latest data!
