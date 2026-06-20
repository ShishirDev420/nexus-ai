with open(r'C:\Users\1553360\nexus-ai\index.html','r',encoding='utf-8') as f:
    h = f.read()

issues = []

if '{logo_uri}' in h:
    issues.append('PLACEHOLDER {logo_uri} still present - f-string not rendered')

if 'NEXUS' in h:
    issues.append('NEXUS text found')

if 'opencode.ai' in h:
    issues.append('OpenCode link found')

if h.count('{') > 50:
    # Check if these are from CSS @keyframes etc
    pass

# Check image src
img_count = h.count('src="')
print(f'Image references: {img_count}')
for i, line in enumerate(h.split('\n'), 1):
    if 'src="' in line and 'http' not in line:
        snippet = line.strip()[:120]
        print(f'  Line {i}: {snippet}')

# Check drum HTML
for term in ['drum-cage', 'spoke-wrap', 'center-platform', 'dot-orbit']:
    if term not in h:
        issues.append(f'Missing drum element: {term}')

# Check key sections
for s in ['id="stack"', 'id="strategy"', 'id="roi"', 'id="about"']:
    if s not in h:
        issues.append(f'Missing section: {s}')

if issues:
    print('ISSUES:')
    for i in issues:
        print(f'  - {i}')
else:
    print('All checks passed!')
