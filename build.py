import base64

with open(r'C:\Users\1553360\nexus-ai\anarock-logo.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()

uri = f'data:image/png;base64,{b64}'

# Read existing HTML
with open(r'C:\Users\1553360\nexus-ai\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all PNG references with base64
html = html.replace('src="anarock-logo.png"', f'src="{uri}"')
html = html.replace('src="anarock-logo.png?v=2"', f'src="{uri}"')

# Remove NEXUS text from nav
html = html.replace('<span>NEXUS<em>·</em>AI</span>', '')
html = html.replace('NEXUS — AI', 'AI')
html = html.replace('NEXUS —', '')
html = html.replace('NEXUS', '')

# Remove OpenCode from footer links
html = html.replace('<a href="https://opencode.ai">OpenCode</a>\n', '')
html = html.replace('<a href="https://opencode.ai">OpenCode</a>', '')

# Remove any remaining "NEXUS" in footer
html = html.replace('NEXUS — AI Growth Engine for', 'AI Growth Engine for')
html = html.replace('NEXUS · AI', 'AI')

# Fix title
html = html.replace('<title>NEXUS — Anarock AI Growth Engine</title>', '<title>Anarock — AI Growth Engine</title>')

with open(r'C:\Users\1553360\nexus-ai\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done - all fixes applied')
