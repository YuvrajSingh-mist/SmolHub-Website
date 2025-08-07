# Deployment to Render.com

This portfolio website is configured for deployment on Render.com. Follow these steps to deploy:

## Prerequisites

1. A GitHub account with this repository
2. A Render.com account (free tier available)

## Deployment Steps

1. **Connect to Render:**
   - Go to [Render.com](https://render.com)
   - Sign up or log in with your GitHub account
   - Click "New +" → "Web Service"

2. **Connect Repository:**
   - Select "Build and deploy from a Git repository"
   - Connect your GitHub account
   - Select this repository: `YuvrajSingh-mist/yuvraj-singh-portfolio.github.io`

3. **Configure Service:**
   - **Name:** `yuvraj-portfolio` (or any name you prefer)
   - **Environment:** `Ruby`
   - **Region:** Choose closest to your target audience
   - **Branch:** `master`
   - **Build Command:** `./build.sh`
   - **Start Command:** `bundle exec jekyll serve --host 0.0.0.0 --port $PORT`

4. **Environment Variables:**
   Add these environment variables in Render dashboard:
   ```
   JEKYLL_ENV=production
   BUNDLE_WITHOUT=development:test
   ```

5. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically build and deploy your site
   - Your site will be available at: `https://yuvraj-portfolio.onrender.com`

## Custom Domain (Optional)

To use your own domain:
1. In your Render dashboard, go to your service settings
2. Add your custom domain in the "Custom Domains" section
3. Update your domain's DNS records as instructed by Render

## Automatic Deployments

Your site will automatically redeploy whenever you push changes to the `master` branch of your GitHub repository.

## Files Added for Render Deployment

- `render.yaml` - Render service configuration
- `build.sh` - Build script for Jekyll
- `.ruby-version` - Ruby version specification
- Updated `Gemfile` with Ruby version

## Troubleshooting

If deployment fails:
1. Check the build logs in Render dashboard
2. Ensure all dependencies are properly specified in `Gemfile`
3. Verify that `build.sh` has execute permissions
4. Check Jekyll configuration in `_config.yml`

## Local Development

To test locally before deploying:
```bash
bundle install
bundle exec jekyll serve
```

Your site will be available at `http://localhost:4000`
