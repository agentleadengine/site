#!/usr/bin/env python3
"""Generate /styles/index.html + 10 standalone style pages under /styles/.

Each standalone page shows one of the ten hand-drawn diagram styles at full
width with the same reference diagram (Model ↔ Client ↔ Server), so it can
be reviewed in isolation. The index page is the picker.
"""
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")
STYLES_DIR = ROOT / "styles"

# Each style: (slug, number, name, description, meta, bg-style, js-config-key)
STYLES = [
    ("pencil-sketch", 1, "Pencil Sketch",
     "Graphite on white. Outline-only, no fills. Quietly confident. Feels like a thought scribbled onto a napkin during a good conversation.",
     "rough: 2.8 · stroke: #2a2a30 · font: Kalam",
     "background:#ffffff;",
     "s1"),
    ("purple-marker", 2, "Purple Marker on Cream",
     "Bold purple strokes on a warm cream background, with soft lavender fills. Matches the site's brand palette most directly. Feels like a sharpie sketch on a designer's notepad.",
     "rough: 1.8 · stroke: #4a00e0 · fill: #f1ecff · font: Kalam Bold",
     "background:#faf7f2;",
     "s2"),
    ("blueprint", 3, "Architect Blueprint",
     "White lines on deep blueprint blue, with a faint grid. Reads as technical and precise even when sketchy. Great for architecture and flow diagrams where the system feels engineered.",
     "rough: 1.6 · stroke: #e0e7ff · bg: #0c2d6b · grid",
     "background:#0c2d6b; background-image: linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px); background-size: 24px 24px;",
     "s3"),
    ("notebook-blue-ink", 4, "Notebook Blue Ink",
     "Blue ballpoint on lined paper. Slightly crooked, like you actually wrote it in a moleskine. Warm, personal, like a first draft somebody later built a company on.",
     "rough: 2.2 · stroke: #1e40af · bg: lined paper · font: Caveat",
     "background:#fefef5; background-image: repeating-linear-gradient(transparent 0 30px, rgba(100,150,200,0.15) 30px 31px);",
     "s4"),
    ("chalkboard", 5, "Chalkboard",
     "Classroom at midnight. White chalk, dark slate, a gold accent. Dramatic for hero diagrams, heavy for inline ones. Makes everything feel like a lesson being taught live.",
     "rough: 2.5 · stroke: #f5f5f5 · bg: #1a1a2e · accent: #ffd700",
     "background:#1a1a2e;",
     "s5"),
    ("highlighter", 6, "Highlighter Multicolor",
     "Dark pencil outlines, each box filled with a different highlighter pastel. Playful without being childish. Great when a diagram has distinct entities you want to differentiate at a glance.",
     "rough: 1.8 · stroke: #1d1d23 · fills: purple/mint/peach · font: Kalam",
     "background:#fafafa;",
     "s6"),
    ("engraving", 7, "Engraving / Crosshatch",
     "Classical etched textbook feel. Crosshatched shadows, aged paper, serif handwriting. Heavy but literary. Fits if you want the site to feel more like a printed manual and less like a web page.",
     "rough: 2.2 · stroke: #1a1a1a · fill: cross-hatch · bg: #fdfbf5",
     "background:#fdfbf5;",
     "s7"),
    ("neon-ink", 8, "Neon Ink (Dark)",
     "Hot magenta strokes on near-black, with soft glow. Feels modern and tech-forward. Pairs with a dark-mode site or dark sections within a light one.",
     "rough: 1.6 · stroke: #c026d3 · bg: #0a0a1a · glow filter",
     "background:#0a0a1a;",
     "s8"),
    ("technical-dots", 9, "Technical Dots",
     "Subtle purple outlines with dotted fills. The most \"designed\" of the ten. Clean enough to ship on a landing page, hand-drawn enough to feel personal. Strong candidate for inline diagrams in deep pages.",
     "rough: 1.2 · stroke: #4a00e0 · fillStyle: dots · minimal",
     "background:#ffffff; background-image: radial-gradient(#4a00e020 1px, transparent 1px); background-size: 18px 18px;",
     "s9"),
    ("ipad-procreate", 10, "iPad Procreate Sketch",
     "My best attempt at \"you drew this on your iPad while thinking out loud.\" Bold dark strokes, soft purple zigzag fills, hand-written labels with a bit of attitude. Most expressive of the ten.",
     "rough: 2 · stroke: #1d1d23 · fill: zigzag purple · font: Kalam Bold",
     "background:#faf8ff;",
     "s10"),
]

# JS config for each style (keyed by svg-id). Mirrors the render() calls in
# the picker. Duplicated here so each standalone page is self-contained.
JS_CONFIGS = {
    "s1":  {"stroke":"#2a2a30","strokeWidth":1.5,"roughness":2.8,"bowing":2,"font":"'Kalam', cursive","textColor":"#1d1d23","subColor":"#525258","fillFn":"() => ({})"},
    "s2":  {"stroke":"#4a00e0","strokeWidth":3,"roughness":1.8,"bowing":1,"font":"'Kalam', cursive","textColor":"#4a00e0","subColor":"#6b21a8","fillFn":"() => ({ fill: '#f1ecff', fillStyle: 'solid' })"},
    "s3":  {"stroke":"#e0e7ff","strokeWidth":2,"roughness":1.6,"font":"'Architects Daughter', 'Kalam', cursive","textColor":"#ffffff","subColor":"#c7d2fe","fillFn":"() => ({ fill: 'rgba(255,255,255,0.05)', fillStyle: 'hachure', hachureGap: 8, hachureAngle: -41 })"},
    "s4":  {"stroke":"#1e40af","strokeWidth":2,"roughness":2.2,"bowing":2,"font":"'Caveat', cursive","textColor":"#1e3a8a","subColor":"#4338ca","fillFn":"() => ({})"},
    "s5":  {"stroke":"#f5f5f5","strokeWidth":2.5,"roughness":2.5,"font":"'Kalam', cursive","textColor":"#ffffff","subColor":"#ffd700","fillFn":"(i) => ({ fill: 'rgba(255,255,255,0.08)', fillStyle: 'hachure', hachureGap: 10, hachureAngle: i * 30 + 20 })"},
    "s6":  {"stroke":"#1d1d23","strokeWidth":2,"roughness":1.8,"font":"'Kalam', cursive","textColor":"#1d1d23","subColor":"#525258","fillFn":"(i) => { const palette = [{ fill: '#e9d5ff', fillStyle: 'solid' },{ fill: '#a7f3d0', fillStyle: 'solid' },{ fill: '#fed7aa', fillStyle: 'solid' }]; return palette[i]; }"},
    "s7":  {"stroke":"#1a1a1a","strokeWidth":1.8,"roughness":2.2,"font":"'Permanent Marker', 'Kalam', cursive","textColor":"#1a1a1a","subColor":"#525258","fillFn":"() => ({ fill: '#1a1a1a', fillStyle: 'cross-hatch', fillWeight: 0.8, hachureGap: 7 })"},
    "s8":  {"stroke":"#c026d3","strokeWidth":2.5,"roughness":1.6,"font":"'Caveat', cursive","textColor":"#f0abfc","subColor":"#c084fc","glow":True,"fillFn":"() => ({ fill: 'rgba(192,38,211,0.12)', fillStyle: 'solid' })"},
    "s9":  {"stroke":"#4a00e0","strokeWidth":1.5,"roughness":1.2,"bowing":0.6,"font":"'Patrick Hand', 'Kalam', cursive","textColor":"#4a00e0","subColor":"#6b21a8","fillFn":"() => ({ fill: '#4a00e0', fillStyle: 'dots', fillWeight: 0.7, hachureGap: 5 })"},
    "s10": {"stroke":"#1d1d23","strokeWidth":2.5,"roughness":2,"bowing":1.5,"font":"'Kalam', cursive","textColor":"#1d1d23","subColor":"#4a00e0","fillFn":"() => ({ fill: '#8b5cf6', fillStyle: 'zigzag', fillWeight: 1.4, hachureGap: 10, hachureAngle: 45 })"},
}

def config_to_js(cfg):
    parts = []
    for k, v in cfg.items():
        if k == "fillFn":
            parts.append(f"    fillFn: {v}")
        elif k == "glow":
            parts.append(f"    glow: {'true' if v else 'false'}")
        elif isinstance(v, str):
            parts.append(f'    {k}: "{v}"')
        else:
            parts.append(f'    {k}: {v}')
    return ",\n".join(parts)


SHARED_JS = r"""
<script src="https://unpkg.com/roughjs@4.6.6/bundled/rough.js"></script>
<script>
(function(){
  if (!window.rough) return;
  const NS = 'http://www.w3.org/2000/svg';
  const LAYOUT = [
    { x: 40,  y: 90, w: 240, h: 140, title: 'Model',  sub: '(Claude)' },
    { x: 340, y: 90, w: 240, h: 140, title: 'Client', sub: '(Claude Code)' },
    { x: 640, y: 90, w: 240, h: 140, title: 'Server', sub: '(Gmail MCP)' }
  ];
  const ARROWS = [
    { x1: 280, x2: 340, y: 160 },
    { x1: 580, x2: 640, y: 160 }
  ];
  function addText(svg, x, y, s, opts) {
    const t = document.createElementNS(NS, 'text');
    t.setAttribute('x', x); t.setAttribute('y', y);
    t.setAttribute('text-anchor', opts.anchor || 'middle');
    t.setAttribute('fill', opts.color || '#1d1d23');
    t.setAttribute('font-size', opts.size || '20');
    t.setAttribute('font-weight', opts.weight || '400');
    if (opts.font) t.setAttribute('font-family', opts.font);
    t.textContent = s;
    svg.appendChild(t);
  }
  function drawArrows(rc, svg, o) {
    ARROWS.forEach(a => {
      svg.appendChild(rc.line(a.x1, a.y, a.x2, a.y, {
        roughness: o.roughness, stroke: o.stroke, strokeWidth: o.strokeWidth
      }));
      svg.appendChild(rc.polygon(
        [[a.x2 - 14, a.y - 8], [a.x2, a.y], [a.x2 - 14, a.y + 8]],
        { roughness: 1.4, stroke: o.stroke, strokeWidth: o.strokeWidth, fill: o.stroke, fillStyle: 'solid' }
      ));
      svg.appendChild(rc.polygon(
        [[a.x1 + 14, a.y - 8], [a.x1, a.y], [a.x1 + 14, a.y + 8]],
        { roughness: 1.4, stroke: o.stroke, strokeWidth: o.strokeWidth, fill: o.stroke, fillStyle: 'solid' }
      ));
    });
  }
  function drawBoxes(rc, svg, s) {
    LAYOUT.forEach((b, i) => {
      const fillOpt = typeof s.fillFn === 'function' ? s.fillFn(i) : {};
      svg.appendChild(rc.rectangle(b.x, b.y, b.w, b.h, Object.assign({
        roughness: s.roughness, stroke: s.stroke, strokeWidth: s.strokeWidth, bowing: s.bowing || 1
      }, fillOpt)));
      addText(svg, b.x + b.w / 2, b.y + 68, b.title, { font: s.font, size: 30, weight: 700, color: s.textColor || s.stroke });
      addText(svg, b.x + b.w / 2, b.y + 106, b.sub, { font: s.font, size: 20, weight: 400, color: s.subColor || s.textColor || s.stroke });
    });
  }
  window.__renderDiagram = function(svgId, style) {
    const svg = document.getElementById(svgId);
    if (!svg) return;
    if (style.glow) {
      const defs = document.createElementNS(NS, 'defs');
      defs.innerHTML = '<filter id="glow-' + svgId + '" x="-50%" y="-50%" width="200%" height="200%">' +
        '<feGaussianBlur stdDeviation="3" result="blur"/>' +
        '<feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>' +
        '</filter>';
      svg.appendChild(defs);
      const g = document.createElementNS(NS, 'g');
      g.setAttribute('filter', 'url(#glow-' + svgId + ')');
      svg.appendChild(g);
      const rc = rough.svg(g);
      drawBoxes(rc, g, style); drawArrows(rc, g, style);
      return;
    }
    const rc = rough.svg(svg);
    drawBoxes(rc, svg, style); drawArrows(rc, svg, style);
  };
})();
</script>
"""

HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Samuel Ochoa</title>
<meta name="description" content="Hand-drawn diagram style: {name}.">
<meta name="author" content="Samuel Ochoa">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&family=Caveat:wght@500;700&family=Kalam:wght@400;700&family=Permanent+Marker&family=Architects+Daughter&family=Patrick+Hand&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css">
<link rel="icon" type="image/png" href="../logo.png">
"""

STANDALONE_CSS = r"""
<style>
  .solo-hero { max-width: 1100px; margin: 0 auto; padding: 40px 24px 16px; }
  .solo-hero h1 { font-size: clamp(32px, 4.5vw, 48px); font-weight: 800; letter-spacing: -0.03em; margin: 0 0 10px; display:flex; align-items:baseline; gap: 16px; flex-wrap: wrap; }
  .solo-num { display:inline-flex; align-items:center; justify-content:center; width: 48px; height: 48px; border-radius: 50%; background: #4a00e0; color: #fff; font-family: 'Kalam', cursive; font-weight: 700; font-size: 24px; }
  .solo-hero p.desc { font-size: 17px; line-height: 1.6; color: #525258; max-width: 760px; margin: 8px 0 0; }
  .solo-meta { font-family: 'JetBrains Mono', monospace; font-size: 12.5px; color: #8b8b93; margin-top: 8px; }
  .solo-stage { max-width: 1100px; margin: 28px auto; padding: 40px 20px 44px; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); }
  .solo-stage svg { display: block; width: 100%; height: auto; max-width: 960px; margin: 0 auto; }
  .solo-stage svg text { font-family: 'Kalam', 'Caveat', cursive; }
  .solo-footer { max-width: 1100px; margin: 0 auto; padding: 0 24px 60px; display:flex; justify-content:space-between; gap: 16px; flex-wrap:wrap; }
  .solo-footer a { color: #4a00e0; font-weight: 600; text-decoration: none; padding: 10px 16px; border: 1px solid #e5e5ea; border-radius: 8px; background: #fff; }
  .solo-footer a:hover { background: #f1ecff; border-color: #4a00e0; }
  .back-link { display: inline-block; padding: 8px 16px; background: #f1ecff; color: #4a00e0; border-radius: 8px; text-decoration: none; font-weight: 600; margin-bottom: 8px; }
</style>
</head>
<body>
<nav class="topbar"><div class="topbar-inner">
<a href="../index.html" class="logo"><img class="brand-logo" src="../logo.png" alt="Samuel Ochoa"></a>
<div class="nav-links"><a href="../index.html">Home</a></div>
</div></nav>
"""

INDEX_CSS = r"""
<style>
  .picker-hero { max-width: 1100px; margin: 0 auto; padding: 48px 24px 16px; }
  .picker-hero h1 { font-size: clamp(32px, 4.5vw, 48px); font-weight: 800; letter-spacing: -0.03em; margin: 0 0 10px; }
  .picker-hero p.lede { font-size: 18px; line-height: 1.6; color: #525258; max-width: 760px; }
  .picker-grid { max-width: 1100px; margin: 24px auto 80px; padding: 0 24px; display: grid; grid-template-columns: 1fr; gap: 32px; }
  .style-card { background: #ffffff; border: 1px solid #e5e5ea; border-radius: 16px; padding: 24px 24px 32px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease; }
  .style-card:hover { border-color: #c7b9ff; box-shadow: 0 10px 28px -8px rgba(74,0,224,0.15); transform: translateY(-2px); }
  .style-header { display:flex; align-items:baseline; gap: 14px; margin-bottom: 6px; flex-wrap: wrap; }
  .style-num { display:inline-flex; align-items:center; justify-content:center; width: 36px; height: 36px; border-radius: 50%; background: #4a00e0; color: #fff; font-family: 'Kalam', cursive; font-weight: 700; font-size: 18px; flex-shrink: 0; }
  .style-name { font-size: 22px; font-weight: 800; letter-spacing: -0.01em; color: #1d1d23; margin: 0; }
  .style-open { margin-left:auto; background: #4a00e0; color:#fff; padding: 6px 14px; border-radius: 999px; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; text-decoration: none; }
  .style-open:hover { background: #7c3aed; }
  .style-desc { font-size: 15px; color: #525258; line-height: 1.55; margin: 6px 0 18px 50px; }
  .style-stage { margin-top: 8px; border-radius: 12px; overflow: hidden; padding: 20px 12px; }
  .style-stage svg { display: block; width: 100%; height: auto; max-width: 860px; margin: 0 auto; }
  .style-stage svg text { font-family: 'Kalam', 'Caveat', cursive; }
  .style-meta { font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #8b8b93; margin: 12px 0 0 50px; }
  .back-link { display: inline-block; padding: 8px 16px; background: #f1ecff; color: #4a00e0; border-radius: 8px; text-decoration: none; font-weight: 600; margin-bottom: 20px; }
</style>
</head>
<body>
<nav class="topbar"><div class="topbar-inner">
<a href="../index.html" class="logo"><img class="brand-logo" src="../logo.png" alt="Samuel Ochoa"></a>
<div class="nav-links"><a href="../index.html">Home</a></div>
</div></nav>
"""


def build_standalone(slug, num, name, description, meta, bg_style, js_key):
    cfg = JS_CONFIGS[js_key]
    cfg_js = config_to_js(cfg)
    # Navigation: prev/next slugs
    prev_idx = num - 2 if num > 1 else None
    next_idx = num if num < 10 else None
    prev_link = f'<a href="{STYLES[prev_idx][1]:02d}-{STYLES[prev_idx][0]}.html">← {STYLES[prev_idx][2]}</a>' if prev_idx is not None else '<span></span>'
    next_link = f'<a href="{STYLES[next_idx][1]:02d}-{STYLES[next_idx][0]}.html">{STYLES[next_idx][2]} →</a>' if next_idx is not None else '<span></span>'

    body = f"""
<div class="solo-hero">
  <a href="index.html" class="back-link">← All 10 styles</a>
  <h1><span class="solo-num">{num}</span>{name}.</h1>
  <p class="desc">{description}</p>
  <p class="solo-meta">{meta}</p>
</div>

<div class="solo-stage" style="{bg_style}">
  <svg id="{js_key}" viewBox="0 0 920 300" preserveAspectRatio="xMidYMid meet"></svg>
</div>

<div class="solo-footer">
  {prev_link}
  {next_link}
</div>

{SHARED_JS}
<script>
window.__renderDiagram && window.__renderDiagram("{js_key}", {{
{cfg_js}
}});
</script>

</body>
</html>
"""
    head = HEAD.format(title=f"Style {num}: {name}", name=name)
    return head + STANDALONE_CSS + body


def build_index():
    cards = []
    for slug, num, name, description, meta, bg_style, js_key in STYLES:
        cards.append(f"""
  <div class="style-card">
    <div class="style-header">
      <span class="style-num">{num}</span>
      <h2 class="style-name">{name}</h2>
      <a href="{num:02d}-{slug}.html" class="style-open">Open full-size</a>
    </div>
    <p class="style-desc">{description}</p>
    <div class="style-meta">{meta}</div>
    <div class="style-stage" style="{bg_style}"><svg id="{js_key}" viewBox="0 0 860 280"></svg></div>
  </div>
""")

    init_calls = []
    for slug, num, name, description, meta, bg_style, js_key in STYLES:
        cfg = JS_CONFIGS[js_key]
        cfg_js = config_to_js(cfg)
        init_calls.append(f'window.__renderDiagram && window.__renderDiagram("{js_key}", {{\n{cfg_js}\n}});')
    init_js = "\n".join(init_calls)

    body = f"""
<div class="picker-hero">
  <a href="../index.html" class="back-link">← Back home</a>
  <h1>Diagram style picker.</h1>
  <p class="lede">Ten different hand-drawn looks, each rendering the same tiny reference diagram (Model ↔ Client ↔ Server) so you can compare cleanly. Click "Open full-size" on any card to see that style on its own page.</p>
</div>

<div class="picker-grid">
{"".join(cards)}
</div>

<footer><div class="container" style="max-width:1100px; padding:20px 24px 40px;">
<p>&copy; 2026 Samuel Ochoa. <a href="../index.html">Home</a> . <a href="../framework/index.html">Framework</a></p>
</div></footer>

{SHARED_JS}
<script>
{init_js}
</script>

</body>
</html>
"""
    head = HEAD.format(title="Diagram style picker", name="all")
    # Patch the CSS href since index.html is 1 level deep
    return head + INDEX_CSS + body


# Build
for slug, num, name, description, meta, bg_style, js_key in STYLES:
    out = STYLES_DIR / f"{num:02d}-{slug}.html"
    out.write_text(build_standalone(slug, num, name, description, meta, bg_style, js_key), encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}")

idx = STYLES_DIR / "index.html"
idx.write_text(build_index(), encoding="utf-8")
print(f"wrote {idx.relative_to(ROOT)}")

# Delete the old root-level diagram-styles.html
old = ROOT / "diagram-styles.html"
if old.exists():
    old.unlink()
    print(f"removed {old.relative_to(ROOT)}")
