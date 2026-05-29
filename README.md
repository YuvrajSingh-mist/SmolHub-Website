# SmolHub — Yuvraj Singh's AI Portfolio & Playground

Live at **[smolhub.com](https://www.smolhub.com)**

A Jekyll-based portfolio and AI playground showcasing from-scratch implementations of 38+ research papers, curated datasets, RL experiments, and the SmolHub model playground. Deployed on Vercel; uses Upstash Redis for per-post view counts and likes.

---

## What's inside

| Section | URL | Description |
|---|---|---|
| SmolHub Playground | `/smolhub` | Experimental AI models and proofs-of-concept |
| From-Scratch Models | `/models` | 38+ paper re-implementations (Transformers, LLMs, GANs, ViT…) |
| Datasets | `/datasets` | Curated datasets with preprocessing scripts |
| RL Experiments | `/rl` | Reinforcement learning implementations |
| Blog / Posts | `/posts` | Technical write-ups and benchmarks |
| CV | `/cv` | Résumé |

---

## Running locally

### 1. Prerequisites

Install [Homebrew](https://brew.sh) if you don't have it, then:

```bash
brew install ruby@3.3 node
```

Add Ruby 3.3 to your PATH (add this line to `~/.zshrc` or `~/.bashrc` so it persists):

```bash
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
```

Then reload your shell:

```bash
source ~/.zshrc   # or source ~/.bashrc
```

### 2. Clone and install gems

```bash
git clone https://github.com/YuvrajSingh-mist/SmolHub-Website.git
cd SmolHub-Website

bundle install
bundle update github-pages   # ensures compatible Liquid version — required
```

> **Why `bundle update github-pages`?** The github-pages gem must be on v232+ which ships with a Liquid version compatible with Ruby 3.3. Skipping this step causes a `tainted?` error on build.

### 3. Set up environment variables

Create a `.env.local` file in the project root for the views/likes API (Upstash Redis):

```
UPSTASH_REDIS_REST_URL=your_upstash_url
UPSTASH_REDIS_REST_TOKEN=your_upstash_token
```

Without these, the dev server still works — view/like counts just won't persist.

### 4. Start the dev server

```bash
node dev-server.js
```

Open **[http://localhost:3000](http://localhost:3000)**

The dev server:
- Runs `jekyll build --watch --incremental` in the background (auto-rebuilds on file changes)
- Serves the built `_site/` directory on port 3000
- Proxies `/api/views` and `/api/likes` to the local Node handlers

---

## Deployment

The site is deployed to Vercel. Push to `master` triggers an automatic build via:

```
buildCommand: bundle exec jekyll build
outputDirectory: _site
```

The `/api/views` and `/api/likes` routes are Vercel serverless functions in `/api/`.

---

## Project structure

```
_posts/          Blog posts (Markdown)
_models/         From-scratch model pages
_datasets/       Dataset pages
_smolhub/        SmolHub playground entries
_rl/             RL experiment pages
_layouts/        Jekyll layouts (single.html is the main post layout)
_includes/       Partials (seo.html, social-share.html, …)
_data/           Navigation, UI text
api/             Vercel serverless functions (views.js, likes.js)
assets/          CSS, JS, images
dev-server.js    Local dev server (Node)
vercel.json      Vercel config (redirects, cleanUrls)
```

---

## Contact

- Email: yuvraj.mist@gmail.com
- GitHub: [YuvrajSingh-mist](https://github.com/YuvrajSingh-mist)
- X: [@YuvrajS9886](https://x.com/YuvrajS9886)
