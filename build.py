import base64

with open(r'C:\Users\1553360\nexus-ai\anarock-logo.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()
logo_uri = f'data:image/png;base64,{b64}'

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Anarock — The Growth Loop</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.18/dist/lenis.min.js"></script>
<script type="importmap">
{{
"imports": {{
"three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js"
}}
}}
</script>
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
:root{{--paper:#f7f3ee;--paper2:#f0eae2;--paper3:#e8e0d6;--cream:#faf7f3;--purple:#974e8e;--purple-light:#b86aae;--purple-dim:#5e2f5a;--purple-bright:#d49acb;--text:#1a0f1e;--text-dim:#5d4d69;--text-muted:#8a7a96;--border:rgba(151,78,142,.1);--radius:16px;--pill:60px;--shadow:0 4px 20px rgba(0,0,0,.04);--shadow-hover:0 12px 48px rgba(0,0,0,.06);--ease:cubic-bezier(.22,1,.36,1);--dur:.5s}}
html{{scrollbar-color:var(--purple) var(--paper)}}
::-webkit-scrollbar{{width:4px}}::-webkit-scrollbar-track{{background:var(--paper)}}::-webkit-scrollbar-thumb{{background:var(--purple);border-radius:4px}}
body{{font-family:Inter,sans-serif;background:var(--paper);color:var(--text);line-height:1.6;overflow-x:hidden;-webkit-font-smoothing:antialiased}}
html.lenis,html.lenis body{{height:auto}}.lenis.lenis-smooth{{scroll-behavior:auto!important}}

#cursor{{position:fixed;width:8px;height:8px;border-radius:50%;background:var(--purple);pointer-events:none;z-index:9999;mix-blend-mode:multiply;transition:width .4s,height .4s,background .4s;transform:translate(-50%,-50%)}}
#cursor.hover{{width:56px;height:56px;background:rgba(151,78,142,.08);border:1px solid rgba(151,78,142,.15);backdrop-filter:blur(6px);mix-blend-mode:normal}}

.scroll-progress{{position:fixed;top:0;left:0;height:3px;background:var(--purple);z-index:101;width:0%;transition:width .1s linear}}

/* ─── NAV ─── */
nav{{position:fixed;top:0;left:0;width:100%;z-index:100;padding:24px 48px;display:flex;justify-content:space-between;align-items:center;transition:var(--dur) var(--ease)}}
nav.scrolled{{background:rgba(247,243,238,.92);-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);padding:14px 48px}}
.nav-logo{{display:flex;align-items:center;gap:14px;text-decoration:none}}
.nav-logo img{{height:24px;width:auto;opacity:.9}}
.nav-links{{display:flex;gap:32px;align-items:center;list-style:none}}
.nav-links a{{color:var(--text-dim);text-decoration:none;font-size:12px;font-weight:500;transition:color var(--dur) var(--ease);letter-spacing:.3px;position:relative;padding:2px 0}}
.nav-links a::after{{content:'';position:absolute;bottom:-2px;left:0;width:0;height:2px;background:var(--purple);transition:width var(--dur) var(--ease);border-radius:2px}}
.nav-links a:hover,.nav-links a.active{{color:var(--text)}}
.nav-links a:hover::after,.nav-links a.active::after{{width:100%}}
.nav-cta{{padding:8px 24px;border-radius:var(--pill);background:var(--purple);color:#fff!important;font-weight:600!important;font-size:12px!important;transition:transform var(--dur) var(--ease),box-shadow var(--dur) var(--ease)!important}}
.nav-cta::after{{display:none!important}}.nav-cta:hover{{transform:translateY(-2px)!important;box-shadow:0 8px 32px rgba(151,78,142,.2)!important;color:#fff!important}}

/* ─── HERO ─── */
@keyframes bgLoop{{0%{{background-position:0% 50%}}25%{{background-position:50% 0%}}50%{{background-position:100% 50%}}75%{{background-position:50% 100%}}100%{{background-position:0% 50%}}}}
.hero{{min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:140px 24px 60px;position:relative;overflow:hidden;background:linear-gradient(135deg,#f7f3ee,#ede6f3,#f0eae2,#f5f0ee,#f7f3ee);background-size:400% 400%;animation:bgLoop 20s ease-in-out infinite}}
#three-canvas{{position:absolute;inset:0;z-index:0;pointer-events:none}}

.hero-content{{position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;width:100%}}
.hero-badge{{display:inline-flex;align-items:center;gap:8px;padding:8px 24px;border-radius:var(--pill);background:rgba(255,255,255,.6);border:1px solid var(--border);font-size:11px;font-weight:500;color:var(--purple);letter-spacing:1.5px;margin-bottom:20px;backdrop-filter:blur(10px);opacity:0}}
.hero-badge .pd{{width:6px;height:6px;border-radius:50%;background:var(--purple);animation:pulseDot 2s ease-in-out infinite;display:inline-block}}
@keyframes pulseDot{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:.4;transform:scale(.6)}}}}

.hero h1{{font-size:clamp(36px,7vw,80px);font-weight:900;letter-spacing:-2.5px;line-height:1.04;margin-bottom:16px;opacity:0}}
.hero h1 .gt{{background:linear-gradient(135deg,#974e8e,#d49acb,#b86aae);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;background-size:200% 200%;animation:gradLoop 8s ease-in-out infinite}}
@keyframes gradLoop{{0%,100%{{background-position:0% 50%}}50%{{background-position:100% 50%}}}}

.hero-sub{{font-size:clamp(15px,1.2vw,19px);color:var(--text-dim);font-weight:400;margin-bottom:10px;opacity:0;line-height:1.5}}
.hero-sub strong{{color:var(--text);font-weight:600}}
.hero-desc{{font-size:clamp(13px,1vw,15px);color:var(--text-dim);max-width:520px;margin-bottom:36px;opacity:0;line-height:1.7}}

.hero-actions{{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;opacity:0}}
.btn{{padding:16px 36px;border-radius:var(--pill);font-size:14px;font-weight:600;text-decoration:none;border:none;cursor:none;transition:transform var(--dur) var(--ease),box-shadow var(--dur) var(--ease);display:inline-flex;align-items:center;gap:10px;font-family:inherit;letter-spacing:.2px}}
.btn-primary{{background:var(--purple);color:#fff;box-shadow:0 4px 24px rgba(151,78,142,.2)}}
.btn-primary:hover{{transform:translateY(-3px);box-shadow:0 12px 40px rgba(151,78,142,.3)}}
.btn-secondary{{background:rgba(255,255,255,.7);color:var(--text);border:1px solid var(--border);backdrop-filter:blur(10px)}}
.btn-secondary:hover{{background:rgba(255,255,255,.9);border-color:rgba(151,78,142,.2);transform:translateY(-3px)}}

.hero-platform{{display:flex;align-items:center;gap:32px;padding:24px 40px;margin-top:44px;border-radius:var(--radius);background:rgba(255,255,255,.6);border:1px solid var(--border);opacity:0;backdrop-filter:blur(12px);box-shadow:0 8px 40px rgba(0,0,0,.04),0 2px 8px rgba(151,78,142,.06)}}
.hero-platform .logo-wrap{{display:flex;align-items:center}}
.hero-platform .logo-wrap img{{height:48px;width:auto;filter:drop-shadow(0 2px 4px rgba(0,0,0,.04))}}
.hero-platform .divider{{width:1px;height:40px;background:var(--border)}}
.hero-platform .info{{text-align:left}}
.hero-platform .info .name{{font-size:18px;font-weight:800;letter-spacing:3.5px;color:var(--text);text-transform:uppercase}}
.hero-platform .info .name .accent{{color:var(--purple)}}
.hero-platform .info .role{{font-size:11px;color:var(--text-dim);letter-spacing:2px;text-transform:uppercase;margin-top:2px}}

/* ─── LOOP TICKER ─── */
.loop-ticker{{width:100%;overflow:hidden;padding:18px 0;background:var(--purple);position:relative}}
.loop-track{{display:flex;gap:0;white-space:nowrap;animation:ticker 30s linear infinite}}
.loop-track span{{font-size:11px;color:rgba(255,255,255,.85);font-weight:600;letter-spacing:2px;text-transform:uppercase;padding:0 28px;display:inline-flex;align-items:center;gap:12px}}
.loop-track span em{{font-style:normal;opacity:.5}}span.loop-icon{{font-size:16px;opacity:.6}}
@keyframes ticker{{from{{transform:translateX(0)}}to{{transform:translateX(-50%)}}}}

/* ─── DECORATIVE SERIF ELEMENTS ─── */
.serif-bg{{position:absolute;font-family:'Instrument Serif',serif;font-size:clamp(120px,20vw,300px);font-weight:900;color:rgba(151,78,142,.03);line-height:1;pointer-events:none;user-select:none;z-index:0;top:0;right:0;transform:translate(10%,-20%)}}

/* ─── SECTIONS ─── */
section{{padding:100px 24px;max-width:1100px;margin:0 auto;position:relative}}
.section-label{{font-size:11px;font-weight:500;letter-spacing:3px;color:var(--purple);margin-bottom:10px;opacity:0;text-transform:uppercase}}
.section-title{{font-size:clamp(28px,3.4vw,42px);font-weight:800;letter-spacing:-1.5px;margin-bottom:12px;line-height:1.08;opacity:0}}
.section-title .gt{{background:linear-gradient(135deg,#974e8e,#d49acb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.section-desc{{font-size:15px;color:var(--text-dim);max-width:560px;margin-bottom:48px;line-height:1.7;opacity:0}}

/* ─── STATS ─── */
.stats-wrap{{padding:0 24px;max-width:1100px;margin:0 auto}}
.stats-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--border);border-radius:var(--radius);overflow:hidden;opacity:0;max-width:1000px;margin:0 auto;box-shadow:var(--shadow)}}
.stat-cell{{background:rgba(255,255,255,.7);padding:44px 24px;text-align:center;backdrop-filter:blur(4px);transition:background .3s}}
.stat-cell:hover{{background:rgba(255,255,255,.9)}}
.stat-cell .num{{font-size:clamp(34px,3.8vw,52px);font-weight:900;color:var(--text);letter-spacing:-2px;line-height:1}}
.stat-cell .num .purple{{color:var(--purple)}}
.stat-cell .label{{font-size:12px;color:var(--text-dim);letter-spacing:1px;margin-top:8px;font-weight:500}}

/* ─── CARDS ─── */
.stack-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px}}
.stack-card{{padding:36px 32px;border-radius:var(--radius);background:rgba(255,255,255,.7);border:1px solid var(--border);transition:transform var(--dur) var(--ease),box-shadow var(--dur) var(--ease);position:relative;overflow:hidden;opacity:0;box-shadow:var(--shadow);backdrop-filter:blur(4px)}}
.stack-card::before{{content:'';position:absolute;top:0;left:0;width:100%;height:3px;background:var(--purple);transform:scaleX(0);transform-origin:left;transition:transform .6s var(--ease)}}
.stack-card:hover::before{{transform:scaleX(1)}}
.stack-card:hover{{transform:translateY(-6px);box-shadow:var(--shadow-hover)}}
.stack-icon{{width:48px;height:48px;border-radius:14px;margin-bottom:16px;display:flex;align-items:center;justify-content:center;font-size:22px;background:rgba(151,78,142,.06);border:1px solid rgba(151,78,142,.06)}}
.stack-card h3{{font-size:17px;font-weight:700;margin-bottom:8px}}
.stack-card p{{font-size:13px;color:var(--text-dim);line-height:1.65}}

.strategy-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px}}
.strategy-card{{padding:36px 32px;border-radius:var(--radius);background:rgba(255,255,255,.7);border:1px solid var(--border);transition:transform var(--dur) var(--ease),box-shadow var(--dur) var(--ease);position:relative;opacity:0;box-shadow:var(--shadow);backdrop-filter:blur(4px)}}
.strategy-card::after{{content:'';position:absolute;bottom:0;left:0;width:0;height:3px;background:var(--purple);transition:width .5s var(--ease)}}
.strategy-card:hover::after{{width:100%}}
.strategy-card:hover{{transform:translateY(-4px);box-shadow:var(--shadow-hover)}}
.strategy-card .num{{font-size:48px;font-weight:900;color:rgba(151,78,142,.06);line-height:1;margin-bottom:4px;font-family:'Instrument Serif',serif}}
.strategy-card h3{{font-size:17px;font-weight:700;margin-bottom:8px}}
.strategy-card p{{font-size:13px;color:var(--text-dim);line-height:1.65}}
.strategy-card .metric{{padding:5px 16px;border-radius:var(--pill);background:rgba(151,78,142,.06);border:1px solid rgba(151,78,142,.08);font-size:11px;color:var(--purple);font-weight:500;display:inline-block;margin-top:14px;letter-spacing:.3px}}

/* ─── TABLE ─── */
.table-wrap{{overflow-x:auto;border-radius:var(--radius);border:1px solid var(--border);overflow:hidden;opacity:0;box-shadow:var(--shadow)}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
thead{{background:rgba(255,255,255,.5)}}
th{{padding:18px 24px;text-align:left;font-weight:600;color:var(--purple);font-size:11px;letter-spacing:1px;border-bottom:1px solid var(--border);text-transform:uppercase}}
td{{padding:16px 24px;border-bottom:1px solid rgba(151,78,142,.04);color:var(--text-dim);transition:background .3s}}
tr:hover td{{background:rgba(151,78,142,.02)}}td:first-child{{font-weight:600;color:var(--text)}}tr:last-child td{{border-bottom:none}}

/* ─── ABOUT ─── */
.about-card{{max-width:680px;margin:0 auto;padding:56px 48px;border-radius:var(--radius);background:rgba(255,255,255,.7);border:1px solid var(--border);text-align:center;opacity:0;box-shadow:var(--shadow);backdrop-filter:blur(4px)}}
.about-card .avatar{{width:80px;height:80px;border-radius:50%;background:var(--purple);display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:700;color:#fff;margin:0 auto 22px;font-family:'Instrument Serif',serif}}
.about-card h3{{font-size:22px;font-weight:700;margin-bottom:4px}}
.about-card .role-line{{color:var(--purple);font-size:14px;font-weight:500;margin-bottom:18px}}
.about-card p{{color:var(--text-dim);font-size:14px;line-height:1.7;max-width:500px;margin:0 auto}}

/* ─── FOOTER ─── */
footer{{padding:48px 24px;text-align:center;border-top:1px solid var(--border)}}
footer p{{color:var(--text-muted);font-size:11px}}
footer .fp2{{margin-top:4px;font-size:10px;color:var(--text-muted);letter-spacing:.3px}}

/* ─── REVEALS ─── */
.reveal{{opacity:0!important;transform:translateY(28px)!important;transition:opacity .8s ease,transform .8s var(--ease)!important}}
.reveal.visible{{opacity:1!important;transform:translateY(0)!important}}
.reveal-1{{transition-delay:.08s!important}}.reveal-2{{transition-delay:.16s!important}}
.reveal-3{{transition-delay:.24s!important}}.reveal-4{{transition-delay:.32s!important}}
.reveal-5{{transition-delay:.4s!important}}

/* ─── RESPONSIVE ─── */
@media(max-width:900px){{nav{{padding:16px 24px}}nav.scrolled{{padding:12px 24px}}.nav-links{{gap:24px}}.stats-grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:768px){{#cursor{{display:none}}nav{{padding:12px 16px}}.nav-links{{display:none;position:absolute;top:100%;left:0;width:100%;background:rgba(247,243,238,.98);-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px);flex-direction:column;padding:20px;gap:16px;border-bottom:1px solid var(--border)}}
.nav-links.open{{display:flex}}.nav-toggle{{display:flex;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:4px}}
.nav-toggle span{{width:22px;height:2px;background:var(--text);border-radius:2px;transition:var(--dur)}}
section{{padding:60px 16px}}.hero{{padding:100px 16px 40px;min-height:90vh}}.hero-platform{{flex-direction:column;gap:12px;padding:20px 24px;text-align:center}}
.hero-platform .info{{text-align:center}}.hero-platform .logo-wrap img{{height:36px}}
.stack-grid,.strategy-grid{{grid-template-columns:1fr}}.stats-grid{{grid-template-columns:repeat(2,1fr)}}
.about-card{{padding:36px 24px}}.loop-track span{{font-size:10px;padding:0 18px}}}}
@media(max-width:480px){{body{{cursor:auto}}.btn{{cursor:pointer}}.hero h1{{font-size:30px;letter-spacing:-1.5px}}.hero{{padding:80px 16px 32px;min-height:85vh}}
.hero-platform{{padding:16px 18px;margin-top:28px}}.hero-platform .logo-wrap img{{height:28px}}
.hero-platform .info .name{{font-size:14px;letter-spacing:2px}}.hero-platform .info .role{{font-size:9px}}
.stack-card,.strategy-card{{padding:28px 24px}}.stats-grid{{grid-template-columns:1fr;border-radius:12px}}
.section-title{{font-size:24px;letter-spacing:-1px}}.stat-cell{{padding:32px 16px}}}}
</style>
</head>
<body>

<div id="cursor"></div>
<div class="scroll-progress" id="scrollProgress"></div>

<nav id="nav">
<a class="nav-logo" href="#">
<img src="{logo_uri}" alt="Anarock">
</a>
<button class="nav-toggle" id="navToggle"><span></span><span></span><span></span></button>
<ul class="nav-links" id="navLinks">
<li><a href="#stack" class="nav-link">Stack</a></li>
<li><a href="#strategy" class="nav-link">Strategy</a></li>
<li><a href="#impact" class="nav-link">Impact</a></li>
<li><a href="#about" class="nav-link nav-cta">Shishir Kamble</a></li>
</ul>
</nav>

<!-- HERO -->
<section class="hero">
<canvas id="three-canvas"></canvas>
<div class="hero-content">
<div class="hero-badge" id="heroBadge"><span class="pd"></span> The Growth Loop</div>
<h1 id="heroTitle">The <span class="gt">Infinite Loop</span><br>of AI Growth</h1>
<p class="hero-sub" id="heroSub">Presented by <strong>Shishir Kamble</strong> — Growth Manager, Residential Mandate</p>
<p class="hero-desc" id="heroDesc">Four premium AI engines wired into a continuous loop — each iteration sharper, faster, more effective. Purpose-built for Anarock's BSM team.</p>
<div class="hero-actions" id="heroActions">
<a href="#strategy" class="btn btn-primary">See the Loop →</a>
<a href="#stack" class="btn btn-secondary">The Stack</a>
</div>
<div class="hero-platform" id="heroPlatform">
<div class="logo-wrap"><img src="{logo_uri}" alt="Anarock"></div>
<div class="divider"></div>
<div class="info">
<div class="name">SHISHIR <span class="accent">KAMBLE</span></div>
<div class="role">Growth Manager · Anarock Property Consultants</div>
</div>
</div>
</div>
</section>

<!-- LOOP TICKER -->
<div class="loop-ticker">
<div class="loop-track">
<span>⟳ The Loop Never Stops <em>·</em></span><span>◉ Iterate · Analyze · Improve <em>·</em></span>
<span>⟳ OpenCode Go <em>·</em></span><span>◉ ChatGPT+ <em>·</em></span><span>⟳ Gemini Pro <em>·</em></span><span>◉ Ralph Loop <em>·</em></span>
<span>⟳ AI Growth Engine <em>·</em></span><span>◉ Residential Mandate <em>·</em></span><span>⟳ BSM Team <em>·</em></span>
<span>⟳ The Loop Never Stops <em>·</em></span><span>◉ Iterate · Analyze · Improve <em>·</em></span>
<span>⟳ OpenCode Go <em>·</em></span><span>◉ ChatGPT+ <em>·</em></span><span>⟳ Gemini Pro <em>·</em></span><span>◉ Ralph Loop <em>·</em></span>
</div>
</div>

<!-- STATS -->
<div class="stats-wrap"><div class="stats-grid" id="statsGrid">
<div class="stat-cell"><div class="num"><span class="counter" data-target="40">0</span><span class="purple">+</span></div><div class="label">Hours Saved Per Week</div></div>
<div class="stat-cell"><div class="num"><span class="counter" data-target="8">0</span><span class="purple">x</span></div><div class="label">Lead Processing Speed</div></div>
<div class="stat-cell"><div class="num"><span class="counter" data-target="60">0</span><span class="purple">%</span></div><div class="label">Higher Engagement</div></div>
<div class="stat-cell"><div class="num"><span class="counter" data-target="8">0</span><span class="purple">wks</span></div><div class="label">Full Deployment</div></div>
</div></div>

<!-- STACK -->
<section id="stack">
<div class="serif-bg" style="right:auto;left:-5%;top:-10%;transform:none;font-size:clamp(200px,30vw,400px);color:rgba(151,78,142,.02)">L</div>
<p class="section-label reveal">The Arsenal</p>
<h2 class="section-title reveal reveal-1">Quad-Engine <span class="gt">Loop</span></h2>
<p class="section-desc reveal reveal-2">Four premium engines wired in series — each feeds the next, creating an accelerating growth loop.</p>
<div class="stack-grid">
<div class="stack-card reveal reveal-1"><div class="stack-icon">⚡</div><h3>OpenCode Go</h3><p>AI coding agent that builds automation pipelines, CRM connectors, and custom tools — validated models powering Anarock's infrastructure loop.</p></div>
<div class="stack-card reveal reveal-2"><div class="stack-icon">💬</div><h3>ChatGPT+</h3><p>GPT-4o generates hyper-personalized pitches, marketing copy, and campaign content — each loop improves quality through reinforcement.</p></div>
<div class="stack-card reveal reveal-3"><div class="stack-icon">🧠</div><h3>Gemini Pro</h3><p>1M+ token context window. Analyzes competitors, market trends, and thousands of listings in a single pass — continuous intelligence loop.</p></div>
<div class="stack-card reveal reveal-4"><div class="stack-icon">🔄</div><h3>Ralph Loop</h3><p>Autonomous iterative engine for A/B testing, campaign optimization, and improvement — the loop that runs the loops.</p></div>
</div>
</section>

<!-- STRATEGY -->
<section id="strategy">
<div class="serif-bg">∞</div>
<p class="section-label reveal">Strategy</p>
<h2 class="section-title reveal reveal-1">The <span class="gt">Loop</span> System</h2>
<p class="section-desc reveal reveal-2">Five interconnected loops that transform how Anarock's residential mandate team operates.</p>
<div class="strategy-grid">
<div class="strategy-card reveal reveal-1"><div class="num">01</div><h3>Bullseye Loop</h3><p>Enrich leads with behavioral data. Score and rank by mandate likelihood. Each loop tightens the targeting.</p><div class="metric">25–35% higher conversions</div></div>
<div class="strategy-card reveal reveal-2"><div class="num">02</div><h3>Qualification Loop</h3><p>AI-driven qualification via WhatsApp and email. Intent detection routes hot leads — feedback loop trains the model.</p><div class="metric">3–5x lead processing</div></div>
<div class="strategy-card reveal reveal-3"><div class="num">03</div><h3>Pitch Loop</h3><p>Build prospect profiles from public data. Generate tailored decks — A/B loop finds the winning angle every time.</p><div class="metric">60–80% higher engagement</div></div>
<div class="strategy-card reveal reveal-4"><div class="num">04</div><h3>Intelligence Loop</h3><p>24/7 competitor tracking via Gemini. Ralph Loop manages threshold alerts — intelligence that compounds daily.</p><div class="metric">70% less manual research</div></div>
<div class="strategy-card reveal reveal-5"><div class="num">05</div><h3>Content Loop</h3><p>One source of truth feeds all channels. Performance data cycles back — every iteration improves the output.</p><div class="metric">10–20x content output</div></div>
</div>
</section>

<!-- IMPACT -->
<section id="impact">
<p class="section-label reveal">Impact</p>
<h2 class="section-title reveal reveal-1">Loop <span class="gt">ROI</span></h2>
<p class="section-desc reveal reveal-2">Each loop delivers measurable time savings and revenue impact. Compound returns across the system.</p>
<div class="table-wrap reveal reveal-3">
<table>
<thead><tr><th>Loop</th><th>Time Saved</th><th>Revenue Impact</th><th>Deployment</th></tr></thead>
<tbody>
<tr><td>Lead Qualification</td><td>40 hrs/week</td><td>3–5x capacity</td><td>2–3 weeks</td></tr>
<tr><td>Pitch Generation</td><td>15 hrs/week</td><td>30–40% higher closure</td><td>3–4 weeks</td></tr>
<tr><td>Market Intelligence</td><td>20 hrs/week</td><td>Real-time insights</td><td>2 weeks</td></tr>
<tr><td>Content Pipeline</td><td>30 hrs/week</td><td>10–20x output</td><td>1–2 weeks</td></tr>
<tr><td>CRM Enrichment</td><td>25 hrs/week</td><td>40–50% better targeting</td><td>2 weeks</td></tr>
</tbody>
</table>
</div>
</section>

<!-- ABOUT -->
<section id="about">
<div class="about-card reveal">
<div class="avatar">SK</div>
<h3>Shishir Kamble</h3>
<p class="role-line">Growth Manager · Anarock Property Consultants</p>
<p>Deep expertise across four premium AI engines with a proven ability to wire them into a continuous growth loop for the residential mandate vertical. Purpose-built for Anarock's BSM team.</p>
</div>
</section>

<!-- FOOTER -->
<footer>
<p>AI Growth Loop for Anarock Property Consultants</p>
<p class="fp2">Shishir Kamble — Growth Manager · Residential Mandate Vertical</p>
</footer>

<script>
/* ─── THREE.JS SCENE ─── */
import * as THREE from 'three';

const canvas = document.getElementById('three-canvas');
const scene = new THREE.Scene();
scene.background = null;

const camera = new THREE.PerspectiveCamera(45, canvas.clientWidth / canvas.clientHeight, 0.1, 100);
camera.position.set(0, 2, 8);

const renderer = new THREE.WebGLRenderer({{ canvas, alpha: true, antialias: true }});
renderer.setSize(canvas.clientWidth, canvas.clientHeight);
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.2;

/* Lights */
const ambient = new THREE.AmbientLight(0xffffff, 0.4);
scene.add(ambient);
const hemi = new THREE.HemisphereLight(0xf7f3ee, 0x974e8e, 0.6);
scene.add(hemi);
const dir = new THREE.DirectionalLight(0xffffff, 1.8);
dir.position.set(4, 8, 6);
scene.add(dir);
const rim = new THREE.DirectionalLight(0xd49acb, 0.6);
rim.position.set(-4, -2, -6);
scene.add(rim);

/* Main Torus Knot (The Loop) */
const knotGeo = new THREE.TorusKnotGeometry(1.3, 0.38, 200, 28);
const knotMat = new THREE.MeshPhysicalMaterial({{
color: 0x974e8e,
emissive: 0x974e8e,
emissiveIntensity: 0.06,
metalness: 0.15,
roughness: 0.25,
clearcoat: 0.3,
clearcoatRoughness: 0.3,
transparent: true,
opacity: 0.9
}});
const knot = new THREE.Mesh(knotGeo, knotMat);
knot.position.y = 0.3;
scene.add(knot);

/* Outer glow wireframe */
const glowGeo = new THREE.TorusKnotGeometry(1.45, 0.46, 140, 18);
const glowMat = new THREE.MeshBasicMaterial({{
color: 0xd49acb,
transparent: true,
opacity: 0.06,
wireframe: true
}});
const glow = new THREE.Mesh(glowGeo, glowMat);
glow.position.y = 0.3;
scene.add(glow);

/* Inner dense wireframe */
const wireGeo = new THREE.TorusKnotGeometry(1.3, 0.38, 120, 14);
const wireMat = new THREE.MeshBasicMaterial({{
color: 0xb86aae,
transparent: true,
opacity: 0.08,
wireframe: true
}});
const wire = new THREE.Mesh(wireGeo, wireMat);
wire.position.y = 0.3;
scene.add(wire);

/* Secondary orbiting rings */
for (let r = 0; r < 3; r++) {{
const ringGeo = new THREE.TorusGeometry(2.2 + r * 0.6, 0.015, 16, 60);
const ringMat = new THREE.MeshBasicMaterial({{
color: r === 1 ? 0xd49acb : 0x974e8e,
transparent: true,
opacity: 0.08 - r * 0.02
}});
const ring = new THREE.Mesh(ringGeo, ringMat);
ring.position.y = 0.3;
ring.rotation.x = Math.PI * 0.5 + (r - 1) * 0.15;
ring.userData = {{ speed: 0.1 + r * 0.05, tilt: (r - 1) * 0.15 }};
scene.add(ring);
}}

/* Orbiting Particles */
const particleCount = 800;
const pos = new Float32Array(particleCount * 3);
const colors = new Float32Array(particleCount * 3);
const phases = new Float32Array(particleCount);
const radii = new Float32Array(particleCount);
const speeds = new Float32Array(particleCount);

for (let i = 0; i < particleCount; i++) {{
const theta = Math.random() * Math.PI * 2;
phases[i] = theta;
speeds[i] = 0.15 + Math.random() * 0.5;
radii[i] = 1.8 + Math.random() * 3.5;
pos[i*3] = radii[i] * Math.cos(theta);
pos[i*3+1] = (Math.random() - 0.5) * 1.2 + 0.3;
pos[i*3+2] = radii[i] * Math.sin(theta);
const c = new THREE.Color().setHSL(0.78 + Math.random() * 0.04, 0.4, 0.5 + Math.random() * 0.3);
colors[i*3] = c.r;
colors[i*3+1] = c.g;
colors[i*3+2] = c.b;
}}

const ptGeo = new THREE.BufferGeometry();
ptGeo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
ptGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

const ptMat = new THREE.PointsMaterial({{
size: 0.035,
transparent: true,
opacity: 0.35,
vertexColors: true,
blending: THREE.AdditiveBlending,
sizeAttenuation: true,
depthWrite: false
}});
const particles = new THREE.Points(ptGeo, ptMat);
scene.add(particles);

/* Resize observer (reliable) */
const ro = new ResizeObserver(() => {{
const w = canvas.clientWidth;
const h = canvas.clientHeight;
if (w === 0 || h === 0) return;
renderer.setSize(w, h, false);
camera.aspect = w / h;
camera.updateProjectionMatrix();
}});
ro.observe(canvas.parentElement);

/* Mouse tracking */
let mx = 0, my = 0, tx = 0, ty = 0;
document.addEventListener('mousemove', e => {{
tx = (e.clientX / innerWidth - 0.5) * 2;
ty = (e.clientY / innerHeight - 0.5) * -2;
}});

/* Animation loop */
function animate() {{
requestAnimationFrame(animate);

const t = performance.now() * 0.001;
const float = Math.sin(t * 0.4) * 0.15;

/* Smooth mouse */
mx += (tx - mx) * 0.05;
my += (ty - my) * 0.05;

/* Rotate knot */
knot.rotation.x = t * 0.12 + float * 0.1;
knot.rotation.y = t * 0.18;
knot.position.y = 0.3 + Math.sin(t * 0.3) * 0.08;

glow.rotation.x = t * 0.1 + float * 0.08;
glow.rotation.y = t * 0.15;
glow.position.y = 0.3 + Math.sin(t * 0.3) * 0.08;

wire.rotation.x = t * 0.12 + float * 0.1;
wire.rotation.y = t * 0.18;
wire.position.y = 0.3 + Math.sin(t * 0.3) * 0.08;

/* Animate orbiting rings */
scene.children.forEach(child => {{
if (child.isMesh && child.geometry && child.geometry.type === 'TorusGeometry') {{
child.rotation.z = t * child.userData.speed;
child.position.y = 0.3 + Math.sin(t * 0.2 + child.userData.speed) * 0.06;
}}
}});

/* Orbit particles */
const ppos = particles.geometry.attributes.position.array;
for (let i = 0; i < particleCount; i++) {{
const theta = phases[i] + t * speeds[i];
const r = radii[i];
ppos[i*3] = r * Math.cos(theta);
ppos[i*3+1] = Math.sin(theta * 0.7 + phases[i]) * 0.3 + 0.3 + Math.sin(t * 0.2 + i) * 0.05;
ppos[i*3+2] = r * Math.sin(theta);
}}
particles.geometry.attributes.position.needsUpdate = true;

/* Camera parallax */
camera.position.x += (mx * 1.2 - camera.position.x) * 0.015;
camera.position.y += (my * 0.6 + 2 - camera.position.y) * 0.015;
camera.lookAt(0, 0.3, 0);

renderer.render(scene, camera);
}}

/* Initial resize */
requestAnimationFrame(() => ro.unobserve?.(canvas.parentElement));
ro.observe(canvas.parentElement);
animate();

/* ─── LENIS ─── */
const lenis = new Lenis({{duration:1.15,easing:t=>Math.min(1,1.001-Math.pow(2,-10*t)),orientation:'vertical',smoothWheel:true}});
lenis.on('scroll',ScrollTrigger.update);
gsap.ticker.add(t=>lenis.raf(t*1e3));
gsap.ticker.lagSmoothing(0);

/* ─── CURSOR ─── */
const cu=document.getElementById('cursor');
let cmx=0,cmy=0,cpx=0,cpy=0;
document.addEventListener('mousemove',e=>{{cmx=e.clientX;cmy=e.clientY}});
document.querySelectorAll('a,button').forEach(e=>{{e.addEventListener('mouseenter',()=>cu.classList.add('hover'));e.addEventListener('mouseleave',()=>cu.classList.remove('hover'))}});
(function r(){{cpx+=(cmx-cpx)*.12;cpy+=(cmy-cpy)*.12;cu.style.transform=`translate(${{cpx}}px,${{cpy}}px)`;requestAnimationFrame(r)}})();
if(innerWidth<=768)cu.style.display='none';

/* ─── SCROLL PROGRESS ─── */
const pb=document.getElementById('scrollProgress');
lenis.on('scroll',({{scroll,limit}})=>pb.style.width=`${{(scroll/limit)*100}}%`);

/* ─── NAV ─── */
const nav=document.getElementById('nav');
lenis.on('scroll',({{scroll}})=>nav.classList.toggle('scrolled',scroll>80));
const nt=document.getElementById('navToggle'),nl=document.getElementById('navLinks');
nt?.addEventListener('click',()=>nl.classList.toggle('open'));
nl?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>nl.classList.remove('open')));
document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{{const h=a.getAttribute('href');if(h&&h.startsWith('#')){{e.preventDefault();const t=document.getElementById(h.slice(1));if(t)lenis.scrollTo(t,{{offset:-80}})}}}}));

/* ─── NAV ACTIVE ─── */
const sections=['stack','strategy','impact','about'];
const nls=document.querySelectorAll('.nav-link');
lenis.on('scroll',()=>{{let cur=0;sections.forEach((id,i)=>{{const el=document.getElementById(id);if(el&&el.getBoundingClientRect().top<innerHeight*.3)cur=i}});nls.forEach((l,i)=>l.classList.toggle('active',i===cur))}});

/* ─── REVEALS ─── */
document.querySelectorAll('.reveal').forEach(el=>ScrollTrigger.create({{trigger:el,start:'top 88%',onEnter:()=>el.classList.add('visible'),once:true}}));

/* ─── HERO REVEAL ─── */
const ht=gsap.timeline({{delay:.3}});
ht.set('#heroBadge,#heroTitle,#heroSub,#heroDesc,#heroActions,#heroPlatform',{{opacity:0,y:24}})
.to('#heroBadge',{{opacity:1,y:0,duration:.7,ease:'power3.out'}})
.to('#heroSub',{{opacity:1,y:0,duration:.6,ease:'power3.out'}},'-.5')
.to('#heroTitle',{{opacity:1,y:0,duration:.7,ease:'power3.out'}},'-.45')
.to('#heroDesc',{{opacity:1,y:0,duration:.6,ease:'power3.out'}},'-.4')
.to('#heroActions',{{opacity:1,y:0,duration:.5,ease:'power3.out'}},'-.35')
.to('#heroPlatform',{{opacity:1,y:0,duration:.5,ease:'power3.out'}},'-.25');

/* ─── COUNTERS ─── */
document.querySelectorAll('.counter').forEach(c=>ScrollTrigger.create({{trigger:c,start:'top 92%',onEnter:()=>{{const t=parseInt(c.dataset.target);let n=0;const i=setInterval(()=>{{const s=Math.min(++n/30,1);c.textContent=Math.round((1-Math.pow(1-s,3))*t);if(s>=1)clearInterval(i)}},30)}},once:true}}));

console.log('Anarock — The Growth Loop · Built with Ralph Loop');
</script>
</body>
</html>'''

with open(r'C:\Users\1553360\nexus-ai\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done — {len(b64)//1024}KB logo embedded')
