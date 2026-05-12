// Local dev server — single command, starts Jekyll watch build, serves _site on port 3000
// Usage: node dev-server.js
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

// Load .env.local
try {
  fs.readFileSync('.env.local', 'utf8').split('\n').forEach(line => {
    const eq = line.indexOf('=');
    if (eq < 1 || line.startsWith('#')) return;
    const k = line.slice(0, eq).trim();
    const v = line.slice(eq + 1).trim().replace(/^["']|["']$/g, '');
    process.env[k] = v;
  });
} catch {}

const viewsHandler = require('./api/views');
const likesHandler = require('./api/likes');

const PUBLIC_PORT = 3000;
const SITE_DIR = path.join(__dirname, '_site');

// MIME types for static file serving
const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css':  'text/css',
  '.js':   'application/javascript',
  '.json': 'application/json',
  '.png':  'image/png',
  '.jpg':  'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif':  'image/gif',
  '.svg':  'image/svg+xml',
  '.ico':  'image/x-icon',
  '.woff': 'font/woff',
  '.woff2':'font/woff2',
  '.ttf':  'font/ttf',
  '.webp': 'image/webp',
  '.xml':  'application/xml',
  '.txt':  'text/plain',
  '.webmanifest': 'application/manifest+json',
};

function serveFile(filePath, res) {
  const ext = path.extname(filePath).toLowerCase();
  const ct = MIME[ext] || 'application/octet-stream';
  const stream = fs.createReadStream(filePath);
  res.writeHead(200, { 'Content-Type': ct });
  stream.pipe(res);
  stream.on('error', () => { res.end(); });
}

function serveStatic(reqUrl, res) {
  const urlPath = decodeURIComponent(reqUrl.split('?')[0]);
  let candidate = path.join(SITE_DIR, urlPath);

  // Security: stay inside _site
  if (!candidate.startsWith(SITE_DIR)) {
    res.writeHead(403); res.end('Forbidden'); return;
  }

  try {
    const stat = fs.statSync(candidate);
    if (stat.isFile()) { serveFile(candidate, res); return; }
    if (stat.isDirectory()) {
      const idx = path.join(candidate, 'index.html');
      if (fs.existsSync(idx)) { serveFile(idx, res); return; }
    }
  } catch {}

  const notFound = path.join(SITE_DIR, '404.html');
  if (fs.existsSync(notFound)) {
    res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
    fs.createReadStream(notFound).pipe(res);
  } else {
    res.writeHead(404); res.end('Not Found');
  }
}

// Start Jekyll in --watch mode (build only, no Jekyll serve)
// Prepend rbenv shims so the correct Ruby/bundler is used
const rbenvShims = (process.env.HOME || '') + '/.rbenv/shims';
const spawnEnv = { ...process.env, PATH: rbenvShims + ':' + process.env.PATH };
const jekyll = spawn('bundle', ['exec', 'jekyll', 'build', '--watch', '--incremental'], {
  stdio: ['ignore', 'pipe', 'pipe'],
  env: spawnEnv,
});

jekyll.stdout.on('data', d => {
  const line = d.toString().trim();
  if (line.includes('done in') || line.includes('Regenerating')) {
    console.log('  Jekyll:', line);
  }
});
jekyll.stderr.on('data', d => {
  const line = d.toString().trim();
  if (line && !line.includes('GitHub Metadata')) console.error('  Jekyll err:', line);
});
jekyll.on('exit', code => { if (code) console.error('Jekyll exited with code', code); });
process.on('exit', () => jekyll.kill());
process.on('SIGINT', () => { jekyll.kill(); process.exit(); });

// Add Express-style .status().json() to plain Node res
function wrap(res) {
  res.status = (code) => { res.statusCode = code; return res; };
  res.json = (obj) => { res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(obj)); };
  return res;
}

const server = http.createServer((req, res) => {
  const urlPath = req.url.split('?')[0];

  if (urlPath === '/api/views') return viewsHandler(req, wrap(res));
  if (urlPath === '/api/likes') return likesHandler(req, wrap(res));

  serveStatic(req.url, res);
});

server.listen(PUBLIC_PORT, () => {
  console.log(`\n  Dev server: http://localhost:${PUBLIC_PORT}`);
  console.log('  Jekyll is watching for changes...\n');
});
