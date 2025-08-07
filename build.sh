#!/bin/bash

# Build script for Render deployment
set -o errexit

echo "Ruby version:"
ruby --version

echo "Bundler version:"
bundler --version

echo "Node.js version:"
node --version

echo "Installing Ruby dependencies..."
bundle config set --local deployment 'false'
bundle config set --local without 'development test'
bundle install

echo "Updating bundle..."
bundle update

echo "Installing Node.js dependencies..."
npm install

echo "Generating models data..."
if [ -n "$GITHUB_TOKEN" ]; then
    echo "✅ GitHub token found, generating models data..."
    node generate-models-data.js
else
    echo "⚠️ No GitHub token found, using existing models data..."
fi

echo "Building Jekyll site..."
JEKYLL_ENV=production bundle exec jekyll build --verbose

echo "Build completed successfully!"
echo "Site files:"
ls -la _site/
