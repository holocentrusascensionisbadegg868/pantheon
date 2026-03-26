export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { gem, type, thought, handle } = req.body || {};
  if (!gem || !type || !thought?.trim()) {
    return res.status(400).json({ error: 'gem, type, and thought are required' });
  }

  const token = process.env.GITHUB_TOKEN;
  if (!token) return res.status(500).json({ error: 'Not configured' });

  const snippet = thought.length > 60 ? thought.slice(0, 60) + '…' : thought;
  const title = `[${type}] ${gem}: ${snippet}`;
  const body = [
    `**Gem:** \`${gem}\``,
    `**Type:** ${type}`,
    handle ? `**From:** ${handle}` : null,
    '',
    '---',
    '',
    thought.trim(),
  ].filter(l => l !== null).join('\n');

  const response = await fetch('https://api.github.com/repos/dkschrei/pantheon/issues', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
      Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
    },
    body: JSON.stringify({
      title,
      body,
      labels: ['user-reaction'],
    }),
  });

  if (!response.ok) {
    const err = await response.text();
    console.error('GitHub API error:', err);
    return res.status(502).json({ error: 'Failed to file reaction' });
  }

  return res.status(200).json({ success: true });
}
