// Local dev server: handles /api/* routes, proxies everything else to Jekyll (port 4000)
// Usage: node dev-server.js
const http = require('http');
const fs = require('fs');

// Load .env.local without any external deps
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

const JEKYLL_PORT = 4000;

// Add Express-style .status().json() to plain Node res so Vercel handlers work locally
function wrap(res) {
  res.status = (code) => { res.statusCode = code; return res; };
  res.json = (obj) => { res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(obj)); };
  return res;
}

const server = http.createServer((req, res) => {
  const path = req.url.split('?')[0];

  if (path === '/api/views') return viewsHandler(req, wrap(res));
  if (path === '/api/likes') return likesHandler(req, wrap(res));

  // Proxy everything else to Jekyll
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
    res.end('Jekyll not running. Start it with: bundle exec jekyll serve');
  });
  req.pipe(proxy, { end: true });
});

server.listen(3000, () => {
  console.log('\n  Dev server ready at http://localhost:3000');
  console.log('  API routes: /api/views  /api/likes');
  console.log('  Proxying everything else to Jekyll on port 4000\n');
});
