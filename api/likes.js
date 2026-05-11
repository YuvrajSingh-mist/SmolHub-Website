const crypto = require('crypto');
const https = require('https');

function redis(cmd) {
  const url = new URL(process.env.UPSTASH_REDIS_REST_URL);
  const body = JSON.stringify(cmd);
  return new Promise((resolve, reject) => {
    const req = https.request({
      hostname: url.hostname,
      path: '/',
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.UPSTASH_REDIS_REST_TOKEN}`,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(body),
      },
    }, (res) => {
      let data = '';
      res.on('data', chunk => { data += chunk; });
      res.on('end', () => {
        try { resolve(JSON.parse(data).result); } catch { reject(new Error('bad json')); }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

function readBody(req) {
  return new Promise((resolve) => {
    let raw = '';
    req.on('data', chunk => { raw += chunk; });
    req.on('end', () => { try { resolve(JSON.parse(raw)); } catch { resolve({}); } });
    req.on('error', () => resolve({}));
  });
}

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(200).end();

  let slug;
  if (req.method === 'POST') {
    const body = await readBody(req);
    slug = body.slug;
  } else {
    slug = new URL(req.url, 'http://localhost').searchParams.get('slug');
  }

  if (!slug) return res.status(400).json({ error: 'slug required' });

  const likesKey = `likes:${slug}`;

  if (req.method === 'POST') {
    const rawIp = (req.headers['x-forwarded-for'] || req.socket?.remoteAddress || 'unknown')
      .split(',')[0].trim();
    const ipHash = crypto.createHash('sha256').update(rawIp).digest('hex').slice(0, 16);

    const added = await redis(['SADD', likesKey, ipHash]);
    const count = await redis(['SCARD', likesKey]);
    return res.status(200).json({ count: parseInt(count) || 0, added: added === 1 });
  }

  const count = parseInt(await redis(['SCARD', likesKey])) || 0;
  return res.status(200).json({ count });
};
