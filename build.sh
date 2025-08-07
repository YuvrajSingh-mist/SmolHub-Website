#!/bin/bash

# Build script for Render deployment
set -o errexit

echo "Ruby version:"
ruby --version

echo "Bundler version:"
bundler --version

echo "Installing dependencies..."
bundle config set --local deployment 'false'
bundle config set --local without 'development test'
bundle install

echo "Building Jekyll site..."
JEKYLL_ENV=production bundle exec jekyll build --verbose

echo "Build completed successfully!"
echo "Site files:"
ls -la _site/
