import base64

with open(r'C:\Users\1553360\nexus-ai\anarock-logo.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()

logo_uri = f'data:image/png;base64,{b64}'

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Anarock — AI Growth Engine</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.18/dist/lenis.min.js"></script>
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#050308;--bg2:#0a0612;--surface:#0f081c;--card:#140d24;--border:rgba(151,78,142,.08);--purple:#974e8e;--purple-light:#b86aae;--purple-dim:#5e2f5a;--purple-bright:#d49acb;--text:#e2d8ea;--text-dim:#8a7a96;--text-muted:#5d4d69;--glass:rgba(151,78,142,.05);--radius:16px;--ease:cubic-bezier(.22,1,.36,1);--dur:.5s}}
html{{scrollbar-color:var(--purple) var(--bg)}}
::-webkit-scrollbar{{width:3px}}::-webkit-scrollbar-track{{background:var(--bg)}}::-webkit-scrollbar-thumb{{background:var(--purple);border-radius:2px}}
body{{font-family:Inter,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;overflow-x:hidden;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}}
html.lenis,html.lenis body{{height:auto}}.lenis.lenis-smooth{{scroll-behavior:auto!important}}.lenis.lenis-smooth[data-lenis-prevent]{{overscroll-behavior:contain}}.lenis.lenis-stopped{{overflow:hidden}}

#cursor{{position:fixed;width:6px;height:6px;border-radius:50%;background:var(--purple-bright);pointer-events:none;z-index:9999;mix-blend-mode:difference;transition:width .4s,height .4s,background .4s;transform:translate(-50%,-50%)}}
#cursor.hover{{width:48px;height:48px;background:rgba(151,78,142,.06);border:1px solid rgba(151,78,142,.12);backdrop-filter:blur(6px);mix-blend-mode:normal}}

.noise{{position:fixed;inset:0;z-index:1;pointer-events:none;opacity:.015;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.65' numOctaves='4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");background-size:256px}}
.vignette{{position:fixed;inset:0;z-index:1;pointer-events:none;background:radial-gradient(ellipse at center,transparent 50%,rgba(5,3,8,.85) 100%)}}
.glow-orb{{position:fixed;border-radius:50%;filter:blur(120px);pointer-events:none;z-index:0}}
.g1{{width:600px;height:600px;background:rgba(151,78,142,.05);top:-200px;right:-200px;animation:float 30s ease-in-out infinite}}
.g2{{width:500px;height:500px;background:rgba(94,47,90,.06);bottom:-150px;left:-150px;animation:float 35s ease-in-out infinite reverse}}
@keyframes float{{0%,100%{{transform:translate(0,0)}}33%{{transform:translate(40px,-20px)}}66%{{transform:translate(-20px,30px)}}}}
.scroll-progress{{position:fixed;top:0;left:0;height:2px;background:var(--purple);z-index:101;width:0%;transition:width .1s linear}}
.wrap{{position:relative;z-index:2}}

/* ─── NAV ─── */
nav{{position:fixed;top:0;left:0;width:100%;z-index:100;padding:24px 48px;display:flex;justify-content:space-between;align-items:center;transition:var(--dur) var(--ease);mix-blend-mode:exclusion}}
nav.scrolled{{background:rgba(5,3,8,.92);-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);padding:14px 48px;mix-blend-mode:normal}}
.nav-logo{{display:flex;align-items:center;gap:14px;text-decoration:none}}
.nav-logo img{{height:22px;width:auto;opacity:.95;filter:brightness(1.15)}}
.nav-links{{display:flex;gap:32px;align-items:center;list-style:none}}
.nav-links a{{color:var(--text-dim);text-decoration:none;font-size:12px;font-weight:500;transition:color var(--dur) var(--ease);letter-spacing:.3px;position:relative;padding:2px 0}}
.nav-links a::after{{content:'';position:absolute;bottom:-2px;left:0;width:0;height:1px;background:var(--purple-light);transition:width var(--dur) var(--ease)}}
.nav-links a:hover,.nav-links a.active{{color:var(--text)}}
.nav-links a:hover::after,.nav-links a.active::after{{width:100%}}
.nav-cta{{padding:8px 24px;border-radius:100px;background:var(--purple);color:#fff!important;font-weight:600!important;font-size:12px!important;transition:transform var(--dur) var(--ease),box-shadow var(--dur) var(--ease)!important}}
.nav-cta::after{{display:none!important}}.nav-cta:hover{{transform:translateY(-2px)!important;box-shadow:0 8px 32px rgba(151,78,142,.25)!important;color:#fff!important}}

/* ─── HERO ─── */
.hero{{min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:160px 24px 60px;position:relative;perspective:1600px;overflow:hidden}}
.hero-glow{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(151,78,142,.035) 0%,transparent 65%);pointer-events:none;z-index:0}}

/* Drum*/
.drum-scene{{width:440px;height:440px;position:relative;margin-bottom:36px;transform-style:preserve-3d;z-index:1}}
.drum-cage{{position:absolute;inset:0;border-radius:50%;transform-style:preserve-3d;animation:spin 20s linear infinite}}
@keyframes spin{{from{{transform:rotateX(72deg) rotateZ(0deg)}}to{{transform:rotateX(72deg) rotateZ(360deg)}}}}
.drum-cage::before{{content:'';position:absolute;inset:0;border-radius:50%;border:1.5px solid transparent;border-top-color:rgba(151,78,142,.4);border-right-color:rgba(184,106,174,.12);border-bottom-color:rgba(151,78,142,.06);border-left-color:var(--purple-dim);box-shadow:0 0 60px rgba(151,78,142,.06),inset 0 0 60px rgba(151,78,142,.02)}}
.spoke-wrap{{position:absolute;inset:0;border-radius:50%;transform-style:preserve-3d;animation:spin 20s linear infinite}}
.spoke{{position:absolute;width:1px;height:46%;top:4%;left:50%;transform-origin:bottom center;background:linear-gradient(to top,rgba(151,78,142,.2),transparent)}}
.spoke:nth-child(1){{transform:translateX(-50%) rotate(0deg)}}.spoke:nth-child(2){{transform:translateX(-50%) rotate(22.5deg)}}
.spoke:nth-child(3){{transform:translateX(-50%) rotate(45deg)}}.spoke:nth-child(4){{transform:translateX(-50%) rotate(67.5deg)}}
.spoke:nth-child(5){{transform:translateX(-50%) rotate(90deg)}}.spoke:nth-child(6){{transform:translateX(-50%) rotate(112.5deg)}}
.spoke:nth-child(7){{transform:translateX(-50%) rotate(135deg)}}.spoke:nth-child(8){{transform:translateX(-50%) rotate(157.5deg)}}
.spoke:nth-child(9){{transform:translateX(-50%) rotate(180deg)}}.spoke:nth-child(10){{transform:translateX(-50%) rotate(202.5deg)}}
.spoke:nth-child(11){{transform:translateX(-50%) rotate(225deg)}}.spoke:nth-child(12){{transform:translateX(-50%) rotate(247.5deg)}}
.spoke:nth-child(13){{transform:translateX(-50%) rotate(270deg)}}.spoke:nth-child(14){{transform:translateX(-50%) rotate(292.5deg)}}
.spoke:nth-child(15){{transform:translateX(-50%) rotate(315deg)}}.spoke:nth-child(16){{transform:translateX(-50%) rotate(337.5deg)}}
.rib{{position:absolute;border-radius:50%;border:1px solid transparent;border-left-color:rgba(151,78,142,.1);border-right-color:rgba(184,106,174,.06);transform-style:preserve-3d}}
.rib1{{inset:50px;animation:spin 15s linear infinite reverse}}
.rib2{{inset:100px;animation:spin 25s linear infinite}}
.rib3{{inset:150px;animation:spin 10s linear infinite reverse}}
.node{{position:absolute;width:4px;height:4px;border-radius:50%;background:var(--purple-bright);box-shadow:0 0 10px rgba(151,78,142,.3);transform-style:preserve-3d}}
.no1{{top:50%;left:-2px;animation:spin 20s linear infinite}}.no2{{top:-2px;left:50%;animation:spin 20s linear infinite}}
.no3{{top:50%;right:-2px;animation:spin 20s linear infinite}}.no4{{bottom:-2px;left:50%;animation:spin 20s linear infinite}}
.dot-orbit{{position:absolute;width:6px;height:6px;border-radius:50%;transform-style:preserve-3d}}
.dot-orbit::before{{content:'';position:absolute;inset:-1px;border-radius:50%;background:var(--purple-bright);box-shadow:0 0 16px rgba(151,78,142,.4),0 0 50px rgba(151,78,142,.1)}}
.do1{{animation:spin 20s linear infinite}}.do2{{animation:spin 15s linear infinite reverse}}.do3{{animation:spin 25s linear infinite}}
.do2::before{{background:var(--purple-light);box-shadow:0 0 16px rgba(184,106,174,.35),0 0 40px rgba(184,106,174,.08)}}
.do3::before{{background:var(--purple);width:4px;height:4px;box-shadow:0 0 10px rgba(151,78,142,.35)}}
.center-glow{{position:absolute;inset:55px;border-radius:50%;background:radial-gradient(circle,rgba(151,78,142,.1) 0%,rgba(184,106,174,.04) 35%,transparent 65%);animation:pulse 5s ease-in-out infinite;transform-style:preserve-3d;transform:rotateX(72deg)}}
@keyframes pulse{{0%,100%{{opacity:.5;transform:rotateX(72deg) scale(1)}}50%{{opacity:1;transform:rotateX(72deg) scale(1.08)}}}}
.center-platform{{position:absolute;inset:80px;border-radius:50%;background:rgba(5,3,8,.96);border:1px solid var(--border);display:flex;flex-direction:column;align-items:center;justify-content:center;transform-style:preserve-3d;backdrop-filter:blur(20px);box-shadow:0 24px 80px rgba(0,0,0,.6),0 0 60px rgba(151,78,142,.04)}}
.center-platform .logo-frame{{width:200px;height:auto;margin-bottom:4px;display:flex;align-items:center;justify-content:center;filter:drop-shadow(0 4px 16px rgba(151,78,142,.06))}}
.center-platform .logo-frame img{{width:100%;height:auto;object-fit:contain;filter:brightness(1.08) contrast(1.02)}}
.center-platform .divider{{width:40px;height:1px;background:var(--purple);margin:6px 0;border-radius:2px;opacity:.4}}
.center-platform .name{{font-size:14px;font-weight:800;color:var(--text);letter-spacing:3.5px;text-transform:uppercase}}
.center-platform .name .accent{{color:var(--purple-bright);font-weight:900}}
.center-platform .role{{font-size:8px;color:var(--text-muted);letter-spacing:2.5px;text-transform:uppercase;margin-top:2px;font-weight:400}}

.hero-badge{{display:inline-flex;align-items:center;gap:8px;padding:6px 18px;border-radius:100px;background:var(--glass);border:1px solid var(--border);font-size:11px;font-weight:500;color:var(--purple-bright);letter-spacing:1.5px;margin-bottom:20px;opacity:0;z-index:2;position:relative}}
.hero h1{{font-size:clamp(32px,6.5vw,72px);font-weight:900;letter-spacing:-2.5px;line-height:1.04;margin-bottom:14px;opacity:0;z-index:2;position:relative}}
.hero h1 .gt{{background:linear-gradient(135deg,#974e8e,#d49acb,#b86aae);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.hero-sub{{font-size:clamp(14px,1.1vw,17px);color:var(--text-dim);font-weight:400;margin-bottom:8px;opacity:0;z-index:2;position:relative;line-height:1.5}}
.hero-sub strong{{color:var(--text);font-weight:600}}
.hero-desc{{font-size:clamp(12px,1vw,14px);color:var(--text-dim);max-width:540px;margin-bottom:32px;opacity:0;line-height:1.7;z-index:2;position:relative}}
.hero-actions{{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;opacity:0;z-index:2;position:relative}}
.btn{{padding:14px 32px;border-radius:100px;font-size:13px;font-weight:600;text-decoration:none;border:none;cursor:none;transition:transform var(--dur) var(--ease),box-shadow var(--dur) var(--ease);display:inline-flex;align-items:center;gap:10px;font-family:inherit;letter-spacing:.2px}}
.btn-primary{{background:var(--purple);color:#fff;box-shadow:0 4px 24px rgba(151,78,142,.2)}}
.btn-primary:hover{{transform:translateY(-3px);box-shadow:0 12px 40px rgba(151,78,142,.3)}}
.btn-secondary{{background:var(--glass);color:var(--text);border:1px solid var(--border)}}
.btn-secondary:hover{{background:rgba(151,78,142,.08);border-color:rgba(151,78,142,.15);transform:translateY(-3px)}}

.hero-strip{{display:flex;align-items:center;gap:20px;padding:14px 28px;margin-top:36px;border-radius:var(--radius);background:rgba(15,8,28,.5);border:1px solid var(--border);opacity:0;z-index:2;position:relative;backdrop-filter:blur(12px)}}
.hero-strip .sep{{width:1px;height:28px;background:var(--border)}}
.hero-strip .l{{font-size:10px;color:var(--text-muted);letter-spacing:1.5px;font-weight:500}}
.hero-strip .v{{font-size:12px;font-weight:500;color:var(--text)}}
.hero-strip .tag{{font-size:11px;color:var(--purple-bright);font-weight:600;letter-spacing:.3px}}

/* ─── STATS ─── */
.stats-row{{display:grid;grid-template-columns:repeat(4,1fr);max-width:1000px;margin:0 auto;padding:80px 24px;gap:1px;background:var(--border)}}
.stat-cell{{background:var(--bg);padding:40px 24px;text-align:center}}
.stat-cell .num{{font-size:clamp(32px,3.5vw,48px);font-weight:900;color:var(--text);letter-spacing:-1.5px;line-height:1}}
.stat-cell .num .purple{{color:var(--purple-bright)}}
.stat-cell .label{{font-size:11px;color:var(--text-dim);letter-spacing:1px;margin-top:8px;font-weight:500}}

/* ─── SECTIONS ─── */
section{{padding:100px 24px;max-width:1100px;margin:0 auto;position:relative}}
.section-label{{font-size:11px;font-weight:500;letter-spacing:2.5px;color:var(--purple-bright);margin-bottom:10px;opacity:0}}
.section-title{{font-size:clamp(26px,3.2vw,40px);font-weight:800;letter-spacing:-1.5px;margin-bottom:12px;line-height:1.08;opacity:0}}
.section-title .gt{{background:linear-gradient(135deg,#974e8e,#d49acb);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.section-desc{{font-size:14px;color:var(--text-dim);max-width:540px;margin-bottom:48px;line-height:1.7;opacity:0}}

/* ─── STACK CARDS ─── */
.stack-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px}}
.stack-card{{padding:32px;border-radius:var(--radius);background:var(--surface);border:1px solid var(--border);transition:transform var(--dur) var(--ease),border-color var(--dur) var(--ease),box-shadow var(--dur) var(--ease);position:relative;overflow:hidden;opacity:0}}
.stack-card::before{{content:'';position:absolute;top:0;left:0;width:3px;height:0;background:var(--purple);transition:height .6s var(--ease)}}
.stack-card:hover::before{{height:100%}}
.stack-card:hover{{transform:translateY(-6px);border-color:rgba(151,78,142,.12);box-shadow:0 20px 60px rgba(0,0,0,.4)}}
.stack-icon{{width:48px;height:48px;border-radius:14px;margin-bottom:16px;display:flex;align-items:center;justify-content:center;font-size:22px;background:rgba(151,78,142,.08)}}
.stack-card h3{{font-size:16px;font-weight:700;margin-bottom:8px}}
.stack-card p{{font-size:13px;color:var(--text-dim);line-height:1.65}}

/* ─── STRATEGY ─── */
.strategy-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}}
.strategy-card{{padding:32px;border-radius:var(--radius);background:var(--surface);border:1px solid var(--border);transition:transform var(--dur) var(--ease),border-color var(--dur) var(--ease);position:relative;opacity:0}}
.strategy-card::after{{content:'';position:absolute;top:0;left:0;width:0;height:3px;background:var(--purple);transition:width .5s var(--ease)}}
.strategy-card:hover::after{{width:100%}}
.strategy-card:hover{{transform:translateY(-4px);border-color:rgba(151,78,142,.1)}}
.strategy-card .num{{font-size:40px;font-weight:900;color:rgba(151,78,142,.05);line-height:1;margin-bottom:4px;font-family:'Instrument Serif',serif}}
.strategy-card h3{{font-size:16px;font-weight:700;margin-bottom:8px}}
.strategy-card p{{font-size:13px;color:var(--text-dim);line-height:1.65}}
.strategy-card .metric{{padding:4px 14px;border-radius:100px;background:rgba(151,78,142,.06);border:1px solid rgba(151,78,142,.08);font-size:11px;color:var(--purple-bright);font-weight:500;display:inline-block;margin-top:12px;letter-spacing:.3px}}

/* ─── TABLE ─── */
.table-wrap{{overflow-x:auto;border-radius:var(--radius);border:1px solid var(--border);overflow:hidden;opacity:0}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
thead{{background:rgba(20,13,36,.5)}}
th{{padding:16px 20px;text-align:left;font-weight:600;color:var(--purple-bright);font-size:11px;letter-spacing:1px;border-bottom:1px solid var(--border)}}
td{{padding:14px 20px;border-bottom:1px solid rgba(151,78,142,.04);color:var(--text-dim);transition:background .3s}}
tr:hover td{{background:rgba(151,78,142,.02)}}td:first-child{{font-weight:600;color:var(--text)}}tr:last-child td{{border-bottom:none}}

/* ─── ABOUT ─── */
.about-card{{max-width:700px;margin:0 auto;padding:48px;border-radius:var(--radius);background:var(--surface);border:1px solid var(--border);text-align:center;opacity:0}}
.about-card .avatar{{width:72px;height:72px;border-radius:50%;background:var(--purple);display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:700;color:#fff;margin:0 auto 20px;font-family:'Instrument Serif',serif}}
.about-card h3{{font-size:20px;font-weight:700;margin-bottom:4px}}
.about-card .role-line{{color:var(--purple-bright);font-size:13px;font-weight:500;margin-bottom:16px}}
.about-card p{{color:var(--text-dim);font-size:13px;line-height:1.7;max-width:480px;margin:0 auto}}

/* ─── FOOTER ─── */
footer{{padding:40px 24px;text-align:center;border-top:1px solid var(--border)}}
footer p{{color:var(--text-muted);font-size:11px}}
footer .fp2{{margin-top:4px;font-size:10px;color:var(--text-muted);letter-spacing:.3px}}

/* ─── REVEALS ─── */
.reveal{{opacity:0!important;transform:translateY(24px)!important;transition:opacity .8s ease,transform .8s var(--ease)!important}}
.reveal.visible{{opacity:1!important;transform:translateY(0)!important}}
.reveal-0{{transition-delay:0s!important}}.reveal-1{{transition-delay:.1s!important}}
.reveal-2{{transition-delay:.2s!important}}.reveal-3{{transition-delay:.3s!important}}
.reveal-4{{transition-delay:.4s!important}}.reveal-5{{transition-delay:.5s!important}}

/* ─── RESPONSIVE ─── */
@media(max-width:900px){{nav{{padding:16px 24px}}nav.scrolled{{padding:12px 24px}}.nav-links{{gap:24px}}.stats-row{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:768px){{#cursor{{display:none}}nav{{padding:12px 16px}}.nav-links{{display:none;position:absolute;top:100%;left:0;width:100%;background:rgba(5,3,8,.98);-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px);flex-direction:column;padding:20px;gap:16px;border-bottom:1px solid var(--border)}}
.nav-links.open{{display:flex}}.nav-toggle{{display:flex;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:4px}}
.nav-toggle span{{width:22px;height:1.5px;background:var(--text);border-radius:2px;transition:var(--dur)}}
section{{padding:60px 16px}}.drum-scene{{width:300px;height:300px}}.center-platform{{inset:55px}}.center-platform .logo-frame{{width:140px}}.center-platform .name{{font-size:12px;letter-spacing:2.5px}}
.hero-strip{{flex-direction:column;gap:8px;padding:16px 20px;align-items:flex-start}}.hero-strip .sep{{display:none}}
.stack-grid,.strategy-grid{{grid-template-columns:1fr}}.stats-row{{grid-template-columns:repeat(2,1fr)}}.about-card{{padding:32px 20px}}}}
@media(max-width:480px){{body{{cursor:auto}}.btn{{cursor:pointer}}.hero h1{{font-size:28px;letter-spacing:-1px}}.drum-scene{{width:240px;height:240px}}.center-platform{{inset:44px}}.center-platform .logo-frame{{width:110px}}.center-platform .name{{font-size:10px;letter-spacing:2px}}.stats-row{{grid-template-columns:1fr}}}}
</style>
</head>
<body>

<div id="cursor"></div>
<div class="noise"></div>
<div class="vignette"></div>
<div class="glow-orb g1"></div>
<div class="glow-orb g2"></div>
<div class="scroll-progress" id="scrollProgress"></div>

<div class="wrap">

<!-- NAV -->
<nav id="nav">
<a class="nav-logo" href="#">
<img src="{logo_uri}" alt="Anarock">
</a>
<button class="nav-toggle" id="navToggle"><span></span><span></span><span></span></button>
<ul class="nav-links" id="navLinks">
<li><a href="#stack" class="nav-link">Stack</a></li>
<li><a href="#strategy" class="nav-link">Strategy</a></li>
<li><a href="#roi" class="nav-link">Impact</a></li>
<li><a href="#about" class="nav-link nav-cta">Shishir Kamble</a></li>
</ul>
</nav>

<!-- HERO -->
<section class="hero">
<div class="hero-glow"></div>
<div class="drum-scene" id="drumScene">
<div class="drum-cage"></div>
<div class="spoke-wrap">
<div class="spoke"></div><div class="spoke"></div><div class="spoke"></div><div class="spoke"></div>
<div class="spoke"></div><div class="spoke"></div><div class="spoke"></div><div class="spoke"></div>
<div class="spoke"></div><div class="spoke"></div><div class="spoke"></div><div class="spoke"></div>
<div class="spoke"></div><div class="spoke"></div><div class="spoke"></div><div class="spoke"></div>
</div>
<div class="rib rib1"></div>
<div class="rib rib2"></div>
<div class="rib rib3"></div>
<div class="node no1"></div><div class="node no2"></div><div class="node no3"></div><div class="node no4"></div>
<div class="dot-orbit do1"></div>
<div class="dot-orbit do2"></div>
<div class="dot-orbit do3"></div>
<div class="center-glow"></div>
<div class="center-platform">
<div class="logo-frame">
<img src="{logo_uri}" alt="Anarock">
</div>
<div class="divider"></div>
<div class="name">SHISHIR <span class="accent">KAMBLE</span></div>
<div class="role">Growth Manager · Anarock</div>
</div>
</div>

<div class="hero-badge" id="heroBadge">AI Growth Strategy</div>
<h1 id="heroTitle">The <span class="gt">AI-Powered</span><br>Growth Engine</h1>
<p class="hero-sub" id="heroSub">Presented by <strong>Shishir Kamble</strong> — Growth Manager, Residential Mandate Vertical</p>
<p class="hero-desc" id="heroDesc">Four premium AI engines unified into one growth machine purpose-built for Anarock's BSM team and the residential mandate vertical.</p>
<div class="hero-actions" id="heroActions">
<a href="#strategy" class="btn btn-primary">See the Strategy →</a>
<a href="#stack" class="btn btn-secondary">The Stack</a>
</div>
<div class="hero-strip" id="heroStrip">
<span class="tag">Shishir Kamble</span><span class="sep"></span>
<span class="l">Role</span><span class="v">Growth Manager</span><span class="sep"></span>
<span class="l">Vertical</span><span class="v">Residential Mandate</span><span class="sep"></span>
<span class="l">Stack</span><span class="v">OpenCode Go · ChatGPT+ · Gemini Pro · Ralph Loop</span>
</div>
</section>

<!-- STATS -->
<div class="stats-row" id="statsRow">
<div class="stat-cell"><div class="num"><span class="counter" data-target="40">0</span><span class="purple">+</span></div><div class="label">Hours Saved Per Week</div></div>
<div class="stat-cell"><div class="num"><span class="counter" data-target="8">0</span><span class="purple">x</span></div><div class="label">Lead Processing Speed</div></div>
<div class="stat-cell"><div class="num"><span class="counter" data-target="60">0</span><span class="purple">%</span></div><div class="label">Higher Engagement Rate</div></div>
<div class="stat-cell"><div class="num"><span class="counter" data-target="8">0</span><span class="purple">wks</span></div><div class="label">Full Deployment</div></div>
</div>

<!-- STACK -->
<section id="stack">
<p class="section-label reveal">The Arsenal</p>
<h2 class="section-title reveal reveal-1">Quad-Engine <span class="gt">Stack</span></h2>
<p class="section-desc reveal reveal-2">Four premium subscriptions woven into one unified workflow. Each engine delivers a distinct advantage.</p>
<div class="stack-grid">
<div class="stack-card reveal reveal-1"><div class="stack-icon">⚡</div><h3>OpenCode Go</h3><p>AI coding agent that builds automation pipelines, CRM connectors, and custom tools — validated models powering Anarock's infrastructure.</p></div>
<div class="stack-card reveal reveal-2"><div class="stack-icon">💬</div><h3>ChatGPT+</h3><p>GPT-4o generates hyper-personalized pitches, marketing copy, and campaign content with human-level quality at machine speed.</p></div>
<div class="stack-card reveal reveal-3"><div class="stack-icon">🧠</div><h3>Gemini Pro</h3><p>1M+ token context window. Analyzes competitors, market trends, and thousands of listings in a single pass.</p></div>
<div class="stack-card reveal reveal-4"><div class="stack-icon">🔄</div><h3>Ralph Loop</h3><p>Autonomous iterative loops for A/B testing, campaign optimization, and continuous improvement — no manual supervision needed.</p></div>
</div>
</section>

<section id="strategy">
<p class="section-label reveal">Strategy</p>
<h2 class="section-title reveal reveal-1">Residential <span class="gt">Bullseye</span></h2>
<p class="section-desc reveal reveal-2">Five strategic plays that transform how the sales and marketing team operates at ground level.</p>
<div class="strategy-grid">
<div class="strategy-card reveal reveal-1"><div class="num">01</div><h3>Bullseye Targeting</h3><p>Enrich leads with demographic and behavioral data. Score and rank by mandate likelihood. Eliminate wasted effort.</p><div class="metric">25–35% higher conversions</div></div>
<div class="strategy-card reveal reveal-2"><div class="num">02</div><h3>Automated Qualification</h3><p>AI-driven qualification via WhatsApp and email. Intent detection routes hot leads to the right salesperson in minutes.</p><div class="metric">3–5x lead processing speed</div></div>
<div class="strategy-card reveal reveal-3"><div class="num">03</div><h3>Personalized Pitches</h3><p>Build prospect profiles from public data. Generate tailored decks, proposals, and scripts for every unique buyer.</p><div class="metric">60–80% higher engagement</div></div>
<div class="strategy-card reveal reveal-4"><div class="num">04</div><h3>Market Intelligence</h3><p>24/7 competitor tracking. Gemini processes daily feeds. Ralph Loop manages threshold alerts automatically.</p><div class="metric">70% less manual research</div></div>
<div class="strategy-card reveal reveal-5"><div class="num">05</div><h3>Content at Scale</h3><p>One source of truth feeds all channels. Localized, quality-validated, continuously optimized through performance loops.</p><div class="metric">10–20x content output</div></div>
</div>
</section>

<section id="roi">
<p class="section-label reveal">Impact</p>
<h2 class="section-title reveal reveal-1">Measurable <span class="gt">Results</span></h2>
<p class="section-desc reveal reveal-2">Concrete time savings, revenue impact, and implementation timelines for every use case.</p>
<div class="table-wrap reveal reveal-3">
<table>
<thead><tr><th>Use Case</th><th>Time Saved</th><th>Revenue Impact</th><th>Deployment</th></tr></thead>
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

<section id="about">
<div class="about-card reveal">
<div class="avatar">SK</div>
<h3>Shishir Kamble</h3>
<p class="role-line">Growth Manager · Anarock Property Consultants</p>
<p>Deep expertise across four premium AI engines with a proven ability to deploy them into a unified growth machine for the residential mandate vertical. Purpose-built for Anarock's BSM team.</p>
</div>
</section>

<!-- FOOTER -->
<footer>
<p>AI Growth Engine for Anarock Property Consultants</p>
<p class="fp2">Shishir Kamble — Growth Manager · Residential Mandate Vertical</p>
</footer>

</div>

<script>
const lenis = new Lenis({{duration:1.15,easing:t=>Math.min(1,1.001-Math.pow(2,-10*t)),orientation:'vertical',smoothWheel:true}});
lenis.on('scroll',ScrollTrigger.update);
gsap.ticker.add(t=>lenis.raf(t*1e3));
gsap.ticker.lagSmoothing(0);

const cu=document.getElementById('cursor');
let mx=0,my=0,px=0,py=0;
document.addEventListener('mousemove',e=>{{mx=e.clientX;my=e.clientY}});
document.querySelectorAll('a,button').forEach(e=>{{e.addEventListener('mouseenter',()=>cu.classList.add('hover'));e.addEventListener('mouseleave',()=>cu.classList.remove('hover'))}});
(function r(){{px+=(mx-px)*.15;py+=(my-py)*.15;cu.style.transform=`translate(${{px}}px,${{py}}px)`;requestAnimationFrame(r)}})();
if(innerWidth<=768)cu.style.display='none';

const pb=document.getElementById('scrollProgress');
lenis.on('scroll',({{scroll,limit}})=>pb.style.width=`${{(scroll/limit)*100}}%`);

const nav=document.getElementById('nav');
lenis.on('scroll',({{scroll}})=>nav.classList.toggle('scrolled',scroll>80));

const nt=document.getElementById('navToggle'),nl=document.getElementById('navLinks');
nt?.addEventListener('click',()=>nl.classList.toggle('open'));
nl?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>nl.classList.remove('open')));

document.querySelectorAll('a[href^="#"]').forEach(a=>{{
a.addEventListener('click',e=>{{const h=a.getAttribute('href');if(h&&h.startsWith('#')){{e.preventDefault();const t=document.getElementById(h.slice(1));if(t)lenis.scrollTo(t,{{offset:-80}})}}}})
}});

const sections=['stack','strategy','roi','about'];
const nls=document.querySelectorAll('.nav-link');
lenis.on('scroll',()=>{{let cur=0;sections.forEach((id,i)=>{{const el=document.getElementById(id);if(el&&el.getBoundingClientRect().top<innerHeight*.3)cur=i}});nls.forEach((l,i)=>l.classList.toggle('active',i===cur))}});

const reveals=document.querySelectorAll('.reveal');
reveals.forEach(el=>ScrollTrigger.create({{trigger:el,start:'top 88%',onEnter:()=>el.classList.add('visible'),once:true}}));

const ht=gsap.timeline({{delay:.3}});
ht.set('#heroBadge,#heroTitle,#heroSub,#heroDesc,#heroActions,#heroStrip',{{opacity:0,y:24}})
.to('#heroBadge',{{opacity:1,y:0,duration:.7,ease:'power3.out'}})
.to('#heroSub',{{opacity:1,y:0,duration:.6,ease:'power3.out'}},'-=.45')
.to('#heroTitle',{{opacity:1,y:0,duration:.7,ease:'power3.out'}},'-=.45')
.to('#heroDesc',{{opacity:1,y:0,duration:.6,ease:'power3.out'}},'-=.35')
.to('#heroActions',{{opacity:1,y:0,duration:.5,ease:'power3.out'}},'-=.3')
.to('#heroStrip',{{opacity:1,y:0,duration:.5,ease:'power3.out'}},'-=.2');

const ds=document.getElementById('drumScene');
document.addEventListener('mousemove',e=>{{const x=(e.clientX/innerWidth-.5)*12;const y=(e.clientY/innerHeight-.5)*-12;ds.style.transform=`rotateY(${{x}}deg) rotateX(${{y}}deg)`}});

const counters=document.querySelectorAll('.counter');
counters.forEach(c=>ScrollTrigger.create({{trigger:c,start:'top 92%',onEnter:()=>{{const t=parseInt(c.dataset.target);let n=0;const i=setInterval(()=>{{const s=Math.min(++n/30,1);const v=1-Math.pow(1-s,3);c.textContent=Math.round(v*t);if(s>=1)clearInterval(i)}},30)}},once:true}}));

console.log('Anarock AI Growth Engine · Built with Ralph Loop');
</script>
</body>
</html>'''

with open(r'C:\Users\1553360\nexus-ai\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done — index.html written with logo base64 ({len(b64)//1024}KB)')
