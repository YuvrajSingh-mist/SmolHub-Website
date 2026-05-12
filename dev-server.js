// Local dev server — single command, starts Jekyll internally, exposes only port 3000
// Usage: node dev-server.js
const http = require('http');
const fs = require('fs');
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

const JEKYLL_PORT = 14000; // internal only — never visit this directly
const PUBLIC_PORT = 3000;

// Start Jekyll as a child process on the internal port
// Prepend rbenv shims so the correct Ruby/bundler is used instead of /usr/bin/bundle
const rbenvShims = (process.env.HOME || '') + '/.rbenv/shims';
const spawnEnv = { ...process.env, PATH: rbenvShims + ':' + process.env.PATH };
const jekyll = spawn('bundle', ['exec', 'jekyll', 'serve', '--port', String(JEKYLL_PORT)], {
  stdio: ['ignore', 'pipe', 'pipe'],
  env: spawnEnv,
});

jekyll.stdout.on('data', d => {
  const line = d.toString();
  if (line.includes('Server running') || line.includes('done in')) {
    console.log('  Jekyll ready');
  }
});
jekyll.stderr.on('data', () => {});
jekyll.on('exit', code => { if (code) console.error('Jekyll exited', code); });
process.on('exit', () => jekyll.kill());
process.on('SIGINT', () => { jekyll.kill(); process.exit(); });

// Add Express-style .status().json() to plain Node res
function wrap(res) {
  res.status = (code) => { res.statusCode = code; return res; };
  res.json = (obj) => { res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(obj)); };
  return res;
}

const server = http.createServer((req, res) => {
  const path = req.url.split('?')[0];

  if (path === '/api/views') return viewsHandler(req, wrap(res));
  if (path === '/api/likes') return likesHandler(req, wrap(res));

  // Proxy to Jekyll
  const opts = {
    hostname: 'localhost',
    port: JEKYLL_PORT,
    path: req.url,
    method: req.method,
    headers: { ...req.headers, host: `localhost:${JEKYLL_PORT}` },
  };
  const proxy = http.request(opts, proxyRes => {
    res.writeHead(proxyRes.statusCode, proxyRes.headers);
    proxyRes.pipe(res, { end: true });
  });
  proxy.on('error', () => {
    res.writeHead(502);
    res.end('Jekyll is still starting up, refresh in a few seconds...');
  });
  req.pipe(proxy, { end: true });
});

server.listen(PUBLIC_PORT, () => {
  console.log(`\n  Starting Jekyll (takes ~10s)...`);
  console.log(`  Dev server will be ready at http://localhost:${PUBLIC_PORT}\n`);
});
