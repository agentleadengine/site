#!/usr/bin/env python3
"""Generate 100 diagram styles under /styles/.

Each style renders the same reference diagram (Model ↔ Client ↔ Server).
Uses a shared JS helper library so each style's config stays tight.

Groups shown on the index:
  Hand-drawn family          (1–10)
  Designed / professional    (11–30)
  Color & palette variations (31–40)
  Shape variations           (41–50)
  Artistic rendering         (51–60)
  Pattern & texture fills    (61–70)
  Era & aesthetic            (71–80)
  Effects                    (81–90)
  Utility & special          (91–100)
"""
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")
STYLES_DIR = ROOT / "styles"
STYLES_DIR.mkdir(exist_ok=True)

# =============================================================================
# HELPERS LIBRARY (injected into every page)
# =============================================================================
HELPERS_JS = r"""
<script>
(function(){
  const NS = 'http://www.w3.org/2000/svg';
  const LAYOUT = [
    { x: 40,  y: 90,  w: 240, h: 140, title: 'Model',  sub: '(Claude)' },
    { x: 340, y: 90,  w: 240, h: 140, title: 'Client', sub: '(Claude Code)' },
    { x: 640, y: 90,  w: 240, h: 140, title: 'Server', sub: '(Gmail MCP)' }
  ];
  const ARROWS = [
    { x1: 280, x2: 340, y: 160 },
    { x1: 580, x2: 640, y: 160 }
  ];
  function el(name, attrs) {
    const e = document.createElementNS(NS, name);
    for (const k in (attrs||{})) e.setAttribute(k, attrs[k]);
    return e;
  }
  function text(svg, x, y, s, opts) {
    opts = opts || {};
    const t = el('text', {
      x, y, 'text-anchor': opts.anchor || 'middle',
      fill: opts.color || '#111',
      'font-size': opts.size || 22,
      'font-weight': opts.weight || 400,
      'font-family': opts.font || "'Inter', sans-serif"
    });
    if (opts.style) t.setAttribute('font-style', opts.style);
    if (opts.transform) t.setAttribute('transform', opts.transform);
    t.textContent = s;
    svg.appendChild(t);
    return t;
  }
  function rect(svg, b, opts) {
    opts = opts || {};
    const r = el('rect', {
      x: b.x, y: b.y, width: b.w, height: b.h,
      rx: opts.rx || 0, ry: opts.ry || opts.rx || 0,
      fill: opts.fill || 'none',
      stroke: opts.stroke || 'none',
      'stroke-width': opts.strokeWidth || 0
    });
    if (opts.filter) r.setAttribute('filter', opts.filter);
    if (opts.dash) r.setAttribute('stroke-dasharray', opts.dash);
    svg.appendChild(r);
    return r;
  }
  function circle(svg, cx, cy, r, opts) {
    opts = opts || {};
    const c = el('circle', {
      cx, cy, r,
      fill: opts.fill || 'none',
      stroke: opts.stroke || 'none',
      'stroke-width': opts.strokeWidth || 0
    });
    if (opts.filter) c.setAttribute('filter', opts.filter);
    svg.appendChild(c);
    return c;
  }
  function poly(svg, points, opts) {
    opts = opts || {};
    const p = el('polygon', {
      points: points.map(pt => pt.join(',')).join(' '),
      fill: opts.fill || 'none',
      stroke: opts.stroke || 'none',
      'stroke-width': opts.strokeWidth || 0
    });
    svg.appendChild(p);
    return p;
  }
  function line(svg, x1, y1, x2, y2, opts) {
    opts = opts || {};
    const l = el('line', {
      x1, y1, x2, y2,
      stroke: opts.stroke || '#000',
      'stroke-width': opts.strokeWidth || 1
    });
    if (opts.dash) l.setAttribute('stroke-dasharray', opts.dash);
    if (opts.linecap) l.setAttribute('stroke-linecap', opts.linecap);
    if (opts.filter) l.setAttribute('filter', opts.filter);
    svg.appendChild(l);
    return l;
  }
  function arrowhead(svg, x, y, dir, opts) {
    opts = opts || {};
    const s = 8;
    const pts = dir === 'right'
      ? [[x-s-4, y-s/1.5], [x, y], [x-s-4, y+s/1.5]]
      : [[x+s+4, y-s/1.5], [x, y], [x+s+4, y+s/1.5]];
    poly(svg, pts, { fill: opts.color || '#000' });
  }
  function hexPath(cx, cy, r) {
    const pts = [];
    for (let i = 0; i < 6; i++) {
      const a = Math.PI / 3 * i - Math.PI/2;
      pts.push([cx + r * Math.cos(a), cy + r * Math.sin(a)]);
    }
    return pts;
  }
  function addDefs(svg, innerHTML) {
    let defs = svg.querySelector('defs');
    if (!defs) { defs = el('defs'); svg.appendChild(defs); }
    const tmp = el('defs'); tmp.innerHTML = innerHTML;
    while (tmp.firstChild) defs.appendChild(tmp.firstChild);
    return defs;
  }

  // Standard diagram: 3 rect boxes with text and arrows
  function drawStandard(svg, cfg) {
    cfg = cfg || {};
    const boxColors = Array.isArray(cfg.fills) ? cfg.fills : [cfg.fill, cfg.fill, cfg.fill];
    const strokeColors = Array.isArray(cfg.strokes) ? cfg.strokes : [cfg.stroke, cfg.stroke, cfg.stroke];
    LAYOUT.forEach((b, i) => {
      rect(svg, b, {
        rx: cfg.rx != null ? cfg.rx : 8,
        fill: boxColors[i] || 'none',
        stroke: strokeColors[i] || 'none',
        strokeWidth: cfg.strokeWidth != null ? cfg.strokeWidth : 1,
        filter: cfg.boxFilter,
        dash: cfg.dash
      });
      const tc = Array.isArray(cfg.textColors) ? cfg.textColors[i] : (cfg.textColor || '#111');
      const sc = Array.isArray(cfg.subColors) ? cfg.subColors[i] : (cfg.subColor || cfg.textColor || '#555');
      text(svg, b.x + b.w/2, b.y + 66, b.title, {
        size: cfg.titleSize || 26, weight: cfg.titleWeight || 700,
        color: tc, font: cfg.font
      });
      text(svg, b.x + b.w/2, b.y + 100, b.sub, {
        size: cfg.subSize || 14, weight: cfg.subWeight || 500,
        color: sc, font: cfg.subFont || cfg.font, style: cfg.subStyle
      });
    });
    ARROWS.forEach(a => {
      line(svg, a.x1, a.y, a.x2, a.y, {
        stroke: cfg.arrowColor || '#111',
        strokeWidth: cfg.arrowWidth || 1.5,
        dash: cfg.arrowDash, filter: cfg.arrowFilter, linecap: cfg.arrowCap
      });
      if (cfg.arrowHeads !== false) {
        arrowhead(svg, a.x2, a.y, 'right', { color: cfg.arrowColor || '#111' });
        arrowhead(svg, a.x1, a.y, 'left', { color: cfg.arrowColor || '#111' });
      }
    });
  }

  // Circle variant
  function drawCircles(svg, cfg) {
    cfg = cfg || {};
    const fills = cfg.fills || [cfg.fill, cfg.fill, cfg.fill];
    const strokes = cfg.strokes || [cfg.stroke, cfg.stroke, cfg.stroke];
    LAYOUT.forEach((b, i) => {
      const cx = b.x + b.w/2, cy = b.y + b.h/2;
      circle(svg, cx, cy, 78, {
        fill: fills[i] || 'none',
        stroke: strokes[i] || 'none',
        strokeWidth: cfg.strokeWidth || 2
      });
      const tc = Array.isArray(cfg.textColors) ? cfg.textColors[i] : cfg.textColor || '#fff';
      const sc = Array.isArray(cfg.subColors) ? cfg.subColors[i] : cfg.subColor || 'rgba(255,255,255,.85)';
      text(svg, cx, cy - 2, b.title, { size: 24, weight: 700, color: tc, font: cfg.font });
      text(svg, cx, cy + 24, b.sub, { size: 13, weight: 500, color: sc, font: cfg.subFont || cfg.font });
    });
    ARROWS.forEach(a => {
      const p = el('path', {
        d: `M ${a.x1} ${a.y} Q ${(a.x1+a.x2)/2} ${a.y-20} ${a.x2} ${a.y}`,
        stroke: cfg.arrowColor || '#333', 'stroke-width': cfg.arrowWidth || 2,
        fill: 'none'
      });
      if (cfg.arrowDash) p.setAttribute('stroke-dasharray', cfg.arrowDash);
      svg.appendChild(p);
    });
  }

  // Hexagon variant
  function drawHexes(svg, cfg) {
    cfg = cfg || {};
    const fills = cfg.fills || [cfg.fill, cfg.fill, cfg.fill];
    const strokes = cfg.strokes || [cfg.stroke, cfg.stroke, cfg.stroke];
    LAYOUT.forEach((b, i) => {
      const cx = b.x + b.w/2, cy = b.y + b.h/2;
      const pts = hexPath(cx, cy, 80);
      poly(svg, pts, {
        fill: fills[i] || 'none',
        stroke: strokes[i] || 'none',
        strokeWidth: cfg.strokeWidth || 2
      });
      const tc = Array.isArray(cfg.textColors) ? cfg.textColors[i] : cfg.textColor || '#fff';
      text(svg, cx, cy - 2, b.title, { size: 22, weight: 700, color: tc, font: cfg.font });
      text(svg, cx, cy + 22, b.sub, { size: 12, weight: 500, color: tc, font: cfg.font });
    });
    ARROWS.forEach(a => {
      line(svg, a.x1, a.y, a.x2, a.y, { stroke: cfg.arrowColor || '#333', strokeWidth: 2 });
    });
  }

  // Diamond variant
  function drawDiamonds(svg, cfg) {
    cfg = cfg || {};
    const fills = cfg.fills || [cfg.fill];
    const strokes = cfg.strokes || [cfg.stroke];
    LAYOUT.forEach((b, i) => {
      const cx = b.x + b.w/2, cy = b.y + b.h/2;
      const pts = [[cx, b.y], [b.x + b.w, cy], [cx, b.y + b.h], [b.x, cy]];
      poly(svg, pts, {
        fill: fills[i % fills.length], stroke: strokes[i % strokes.length],
        strokeWidth: cfg.strokeWidth || 2
      });
      text(svg, cx, cy - 2, b.title, { size: 22, weight: 700, color: cfg.textColor || '#fff', font: cfg.font });
      text(svg, cx, cy + 22, b.sub, { size: 12, weight: 500, color: cfg.subColor || 'rgba(255,255,255,.85)', font: cfg.font });
    });
    ARROWS.forEach(a => {
      line(svg, a.x1, a.y, a.x2, a.y, { stroke: cfg.arrowColor || '#333', strokeWidth: 2 });
    });
  }

  // Expose
  window.__dg = {
    NS, LAYOUT, ARROWS,
    el, text, rect, circle, poly, line, arrowhead, hexPath, addDefs,
    drawStandard, drawCircles, drawHexes, drawDiamonds
  };
})();
</script>
"""

# Rough.js shared renderer (for 1-10)
SHARED_ROUGH = r"""
<script src="https://unpkg.com/roughjs@4.6.6/bundled/rough.js"></script>
<script>
(function(){
  if (!window.rough) return;
  const NS='http://www.w3.org/2000/svg';
  const LAYOUT=[{x:40,y:90,w:240,h:140,title:'Model',sub:'(Claude)'},{x:340,y:90,w:240,h:140,title:'Client',sub:'(Claude Code)'},{x:640,y:90,w:240,h:140,title:'Server',sub:'(Gmail MCP)'}];
  const ARROWS=[{x1:280,x2:340,y:160},{x1:580,x2:640,y:160}];
  function addText(svg,x,y,s,o){const t=document.createElementNS(NS,'text');t.setAttribute('x',x);t.setAttribute('y',y);t.setAttribute('text-anchor',o.anchor||'middle');t.setAttribute('fill',o.color||'#1d1d23');t.setAttribute('font-size',o.size||'20');t.setAttribute('font-weight',o.weight||'400');if(o.font)t.setAttribute('font-family',o.font);t.textContent=s;svg.appendChild(t);}
  window.__renderRough=function(svgId,s){const svg=document.getElementById(svgId);if(!svg)return;let g=svg;if(s.glow){const defs=document.createElementNS(NS,'defs');defs.innerHTML='<filter id="glow-'+svgId+'" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>';svg.appendChild(defs);g=document.createElementNS(NS,'g');g.setAttribute('filter','url(#glow-'+svgId+')');svg.appendChild(g);}const rc=rough.svg(g);LAYOUT.forEach((b,i)=>{const fo=typeof s.fillFn==='function'?s.fillFn(i):{};g.appendChild(rc.rectangle(b.x,b.y,b.w,b.h,Object.assign({roughness:s.roughness,stroke:s.stroke,strokeWidth:s.strokeWidth,bowing:s.bowing||1},fo)));addText(g,b.x+b.w/2,b.y+68,b.title,{font:s.font,size:30,weight:700,color:s.textColor||s.stroke});addText(g,b.x+b.w/2,b.y+106,b.sub,{font:s.font,size:20,weight:400,color:s.subColor||s.textColor||s.stroke});});ARROWS.forEach(a=>{g.appendChild(rc.line(a.x1,a.y,a.x2,a.y,{roughness:s.roughness,stroke:s.stroke,strokeWidth:s.strokeWidth}));g.appendChild(rc.polygon([[a.x2-14,a.y-8],[a.x2,a.y],[a.x2-14,a.y+8]],{roughness:1.4,stroke:s.stroke,strokeWidth:s.strokeWidth,fill:s.stroke,fillStyle:'solid'}));g.appendChild(rc.polygon([[a.x1+14,a.y-8],[a.x1,a.y],[a.x1+14,a.y+8]],{roughness:1.4,stroke:s.stroke,strokeWidth:s.strokeWidth,fill:s.stroke,fillStyle:'solid'}));});}
})();
</script>
"""

# =============================================================================
# STYLES DATA — 100 entries
# Each tuple: (kind, slug, num, name, description, meta, bg_css, render_spec)
#   kind: 'rough' | 'custom'
#   render_spec for 'rough' is a dict passed to __renderRough
#   render_spec for 'custom' is JS string that executes inside the SVG scope
# =============================================================================

def rough(stroke, sw, r, font, tc, sc, fillFn=None, bowing=None, glow=False):
    d = {"stroke":stroke, "strokeWidth":sw, "roughness":r, "font":font,
         "textColor":tc, "subColor":sc}
    if fillFn: d["fillFn"] = fillFn
    if bowing is not None: d["bowing"] = bowing
    if glow: d["glow"] = True
    return d

def std(**kw):
    """Emit JS that calls drawStandard with the given kwargs (as JS literals)."""
    return "__dg.drawStandard(SVG, " + js_obj(kw) + ");"

def call(fn, **kw):
    """Emit JS calling __dg.fn(SVG, {...})."""
    return f"__dg.{fn}(SVG, " + js_obj(kw) + ");"

def js_obj(d):
    """Shallow JS object literal from python dict (values must be pre-JSONable or JS-string)."""
    parts = []
    for k, v in d.items():
        parts.append(f'"{k}": {v}' if isinstance(v, str) and v.startswith(('[', '{', 'function', '(', '"', "'")) else f'"{k}": {js_value(v)}')
    return "{" + ", ".join(parts) + "}"

def js_value(v):
    if isinstance(v, bool): return 'true' if v else 'false'
    if isinstance(v, (int, float)): return str(v)
    if v is None: return 'null'
    if isinstance(v, list):
        return '[' + ', '.join(js_value(x) for x in v) + ']'
    # assume string — if it looks like a JS literal already, emit as-is
    s = str(v)
    if s.startswith(('[', '{', '(')) or s.startswith('function') or s in ('true','false','null'):
        return s
    return '"' + s.replace('"', '\\"') + '"'

# Shorthand for plain SVG background styles
W, D = "background:#ffffff;", "background:#0c0c14;"

STYLES = [
    # ---- 1-10: original hand-drawn ----
    ('rough','pencil-sketch',1,'Pencil Sketch',
     'Graphite on white. Outline-only. Quietly confident.',
     'rough: 2.8 · stroke: #2a2a30',
     W,
     rough("#2a2a30",1.5,2.8,"'Kalam', cursive","#1d1d23","#525258","() => ({})",bowing=2)),
    ('rough','purple-marker',2,'Purple Marker on Cream',
     'Bold purple strokes on cream with soft lavender fills. Brand-aligned.',
     'rough: 1.8 · stroke: #4a00e0',
     'background:#faf7f2;',
     rough("#4a00e0",3,1.8,"'Kalam', cursive","#4a00e0","#6b21a8","() => ({ fill: '#f1ecff', fillStyle: 'solid' })",bowing=1)),
    ('rough','blueprint',3,'Architect Blueprint (sketchy)',
     'White lines on blueprint blue with a faint grid.',
     'rough: 1.6 · bg: #0c2d6b',
     'background:#0c2d6b; background-image: linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px); background-size: 24px 24px;',
     rough("#e0e7ff",2,1.6,"'Architects Daughter', 'Kalam', cursive","#ffffff","#c7d2fe","() => ({ fill: 'rgba(255,255,255,0.05)', fillStyle: 'hachure', hachureGap: 8, hachureAngle: -41 })")),
    ('rough','notebook-blue-ink',4,'Notebook Blue Ink',
     'Blue ballpoint on lined paper. Slightly crooked, personal.',
     'rough: 2.2 · bg: lined paper',
     'background:#fefef5; background-image: repeating-linear-gradient(transparent 0 30px, rgba(100,150,200,0.15) 30px 31px);',
     rough("#1e40af",2,2.2,"'Caveat', cursive","#1e3a8a","#4338ca","() => ({})",bowing=2)),
    ('rough','chalkboard',5,'Chalkboard',
     'White chalk on slate. Dramatic for heros.',
     'rough: 2.5 · bg: #1a1a2e',
     'background:#1a1a2e;',
     rough("#f5f5f5",2.5,2.5,"'Kalam', cursive","#ffffff","#ffd700","(i) => ({ fill: 'rgba(255,255,255,0.08)', fillStyle: 'hachure', hachureGap: 10, hachureAngle: i * 30 + 20 })")),
    ('rough','highlighter',6,'Highlighter Multicolor',
     'Dark outlines, pastel highlighter fills per box.',
     'rough: 1.8 · fills: purple/mint/peach',
     'background:#fafafa;',
     rough("#1d1d23",2,1.8,"'Kalam', cursive","#1d1d23","#525258","(i) => { const p = [{ fill: '#e9d5ff', fillStyle: 'solid' },{ fill: '#a7f3d0', fillStyle: 'solid' },{ fill: '#fed7aa', fillStyle: 'solid' }]; return p[i]; }")),
    ('rough','engraving',7,'Engraving / Crosshatch',
     'Cross-hatched shadows, aged paper, literary feel.',
     'rough: 2.2 · fill: cross-hatch',
     'background:#fdfbf5;',
     rough("#1a1a1a",1.8,2.2,"'Permanent Marker', 'Kalam', cursive","#1a1a1a","#525258","() => ({ fill: '#1a1a1a', fillStyle: 'cross-hatch', fillWeight: 0.8, hachureGap: 7 })")),
    ('rough','neon-ink',8,'Neon Ink (Dark)',
     'Hot magenta on near-black, soft glow.',
     'rough: 1.6 · bg: #0a0a1a',
     'background:#0a0a1a;',
     rough("#c026d3",2.5,1.6,"'Caveat', cursive","#f0abfc","#c084fc","() => ({ fill: 'rgba(192,38,211,0.12)', fillStyle: 'solid' })",glow=True)),
    ('rough','technical-dots',9,'Technical Dots (sketchy)',
     'Subtle purple outlines with dotted fills.',
     'rough: 1.2 · fillStyle: dots',
     'background:#ffffff; background-image: radial-gradient(#4a00e020 1px, transparent 1px); background-size: 18px 18px;',
     rough("#4a00e0",1.5,1.2,"'Patrick Hand', 'Kalam', cursive","#4a00e0","#6b21a8","() => ({ fill: '#4a00e0', fillStyle: 'dots', fillWeight: 0.7, hachureGap: 5 })",bowing=0.6)),
    ('rough','ipad-procreate',10,'iPad Procreate Sketch',
     'Bold dark strokes, zigzag purple fills, most expressive.',
     'rough: 2 · fill: zigzag purple',
     'background:#faf8ff;',
     rough("#1d1d23",2.5,2,"'Kalam', cursive","#1d1d23","#4a00e0","() => ({ fill: '#8b5cf6', fillStyle: 'zigzag', fillWeight: 1.4, hachureGap: 10, hachureAngle: 45 })",bowing=1.5)),
]

# ---- 11-30: designed / professional ----
DESIGNED = [
    (11,'stripe-docs','Stripe Docs Clean',
     'Crisp solid boxes with thin purple borders, soft shadow, sans typography.',
     'fill: #faf5ff · stroke: #7c3aed',
     W,
     """__dg.addDefs(SVG, '<filter id="ss" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#7c3aed" flood-opacity="0.12"/></filter>');
        __dg.drawStandard(SVG, { rx: 10, fill: '#faf5ff', stroke: '#7c3aed', strokeWidth: 1.5, boxFilter: 'url(#ss)', textColor: '#3b0764', subColor: '#7c3aed', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#7c3aed', arrowWidth: 1.8 });"""),
    (12,'linear-dark','Linear Interface Dark',
     'Dark mode with gradient border + soft glow. Modern SaaS.',
     'dark · gradient border · glow',
     'background:#0c0c14;',
     """__dg.addDefs(SVG, '<linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6366f1"/><stop offset="1" stop-color="#ec4899"/></linearGradient><filter id="lgf" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>');
        __dg.LAYOUT.forEach(b => {
          __dg.rect(SVG, {x:b.x-1,y:b.y-1,w:b.w+2,h:b.h+2}, { rx: 14, fill: 'url(#lg)' });
          __dg.rect(SVG, b, { rx: 13, fill: '#17171f' });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 28, weight: 700, color: '#fafafa', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, weight: 500, color: '#a5b4fc', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => {
          __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#a5b4fc', strokeWidth: 2, filter: 'url(#lgf)' });
        });"""),
    (13,'notion-minimal','Notion Minimal',
     'Off-white, rounded cards, thin dividers. Clean writing-first.',
     'fill: #fff · stroke: #e5e5ea',
     'background:#fdfcfa;',
     """__dg.drawStandard(SVG, { rx: 8, fill: '#ffffff', stroke: '#e5e5ea', strokeWidth: 1, textColor: '#1f1f1f', subColor: '#8a8a8a', titleSize: 24, titleWeight: 600, font: "'Inter', sans-serif", arrowColor: '#8a8a8a', arrowWidth: 1 });"""),
    (14,'apple-glass','Apple Glass',
     'Translucent cards on a soft gradient mesh. Premium, layered.',
     'glass · blur · gradient mesh',
     'background: linear-gradient(135deg, #fecaca 0%, #e9d5ff 50%, #bae6fd 100%);',
     """__dg.drawStandard(SVG, { rx: 18, fill: 'rgba(255,255,255,0.35)', stroke: 'rgba(255,255,255,0.7)', strokeWidth: 1.5, textColor: '#1d1d1f', subColor: '#4a4a52', titleSize: 28, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: 'rgba(29,29,31,0.6)', arrowWidth: 2 });"""),
    (15,'vercel-minimal','Vercel Minimal',
     'Black, thin borders, monospaced labels. Stark.',
     'minimal · mono',
     W,
     """__dg.drawStandard(SVG, { rx: 0, fill: 'none', stroke: '#000', strokeWidth: 1, textColor: '#000', subColor: '#666', titleSize: 26, titleWeight: 600, subSize: 13, font: "'JetBrains Mono', monospace", arrowColor: '#000', arrowWidth: 1 });"""),
    (16,'swiss-grotesk','Swiss Grotesk',
     'Helvetica-feel precision, one accent color, asymmetric.',
     'red accent · precise',
     'background:#f5f3ee;',
     """__dg.drawStandard(SVG, { rx: 0, fills: ['#fff','#dc2626','#fff'], stroke: '#000', strokeWidth: 2, textColors: ['#000','#fff','#000'], subColors: ['#666','#fecaca','#666'], titleSize: 30, titleWeight: 800, font: "'Inter', sans-serif", arrowColor: '#000', arrowWidth: 2 });"""),
    (17,'brutalist','Brutalist Block',
     'Thick black strokes, raw yellow/red, offset shadow. Heavy.',
     'thick · bold colors',
     'background:#fcd34d;',
     """__dg.LAYOUT.forEach((b, i) => {
          __dg.rect(SVG, {x:b.x+6,y:b.y+6,w:b.w,h:b.h}, { fill: '#000' });
          __dg.rect(SVG, b, { fill: ['#fde047','#fff','#f87171'][i], stroke: '#000', strokeWidth: 4 });
          __dg.text(SVG, b.x+b.w/2, b.y+68, b.title.toUpperCase(), { size: 32, weight: 900, color: '#000', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+104, b.sub, { size: 15, weight: 600, color: '#000', font: "'JetBrains Mono', monospace" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#000', strokeWidth: 4 }));"""),
    (18,'neumorphic','Neumorphic Soft',
     'Dual light/shadow. Tactile and plush.',
     'embossed · dual shadow',
     'background:#e8e8ef;',
     """__dg.addDefs(SVG, '<filter id="neu" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="-5" dy="-5" stdDeviation="6" flood-color="#ffffff" flood-opacity="1"/><feDropShadow dx="5" dy="5" stdDeviation="6" flood-color="#a3a3b5" flood-opacity="0.7"/></filter>');
        __dg.drawStandard(SVG, { rx: 20, fill: '#e8e8ef', boxFilter: 'url(#neu)', textColor: '#4a4a5c', subColor: '#8b8ba3', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#8b8ba3', arrowWidth: 2, arrowCap: 'round' });"""),
    (19,'glassmorphism-mesh','Glassmorphism on Mesh',
     'Frosted glass on a gradient mesh. Dreamy, vibrant.',
     'mesh gradient · frosted',
     'background: radial-gradient(at 20% 30%, #f472b6 0, transparent 50%), radial-gradient(at 80% 70%, #60a5fa 0, transparent 50%), radial-gradient(at 50% 90%, #c084fc 0, transparent 50%), #1e1b4b;',
     """__dg.drawStandard(SVG, { rx: 20, fill: 'rgba(255,255,255,0.15)', stroke: 'rgba(255,255,255,0.4)', strokeWidth: 1.5, textColor: '#fff', subColor: 'rgba(255,255,255,0.8)', titleSize: 28, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: 'rgba(255,255,255,0.7)', arrowWidth: 2 });"""),
    (20,'cyberpunk','Cyberpunk Neon Grid',
     'Neon cyan/magenta on pure black, scanline grid.',
     'neon · grid · dual glow',
     'background:#000510;',
     """__dg.addDefs(SVG, '<filter id="cy" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3"/><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>');
        for (let i = 0; i <= 12; i++) __dg.line(SVG, i*75, 0, i*75, 300, { stroke: '#ec4899', strokeWidth: 0.5 }).setAttribute('opacity', 0.2);
        __dg.LAYOUT.forEach((b, i) => {
          const c = i%2===0?'#06b6d4':'#ec4899';
          __dg.rect(SVG, b, { fill: 'transparent', stroke: c, strokeWidth: 2, filter: 'url(#cy)' });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title.toUpperCase(), { size: 26, weight: 700, color: c, font: "'JetBrains Mono', monospace" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 13, weight: 500, color: '#94a3b8', font: "'JetBrains Mono', monospace" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#06b6d4', strokeWidth: 2, filter: 'url(#cy)' }));"""),
    (21,'isometric-3d','Isometric 3D',
     'Axonometric projection with shaded faces. Real depth.',
     '30° · 3 faces · depth',
     'background:#f1f5f9;',
     """const D=18; const cs=[{t:'#c4b5fd',f:'#8b5cf6',s:'#6d28d9'},{t:'#fde68a',f:'#f59e0b',s:'#b45309'},{t:'#a7f3d0',f:'#10b981',s:'#065f46'}];
        __dg.LAYOUT.forEach((b, i) => {
          __dg.poly(SVG, [[b.x,b.y],[b.x+b.w,b.y],[b.x+b.w+D,b.y-D],[b.x+D,b.y-D]], { fill: cs[i].t, stroke: '#1e293b', strokeWidth: 1 });
          __dg.poly(SVG, [[b.x+b.w,b.y],[b.x+b.w+D,b.y-D],[b.x+b.w+D,b.y+b.h-D],[b.x+b.w,b.y+b.h]], { fill: cs[i].s, stroke: '#1e293b', strokeWidth: 1 });
          __dg.rect(SVG, b, { fill: cs[i].f, stroke: '#1e293b', strokeWidth: 1 });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 26, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+98, b.sub, { size: 14, weight: 500, color: 'rgba(255,255,255,0.85)', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#1e293b', strokeWidth: 2 }));"""),
    (22,'monochrome-editorial','Monochrome Editorial',
     'Pure black/white, serif display, figure caption.',
     'b/w · serif · essay',
     'background:#fafaf7;',
     """__dg.drawStandard(SVG, { rx: 0, fill: '#fafaf7', stroke: '#000', strokeWidth: 1.5, textColor: '#000', subColor: '#555', titleSize: 32, titleWeight: 400, subSize: 14, font: "'Instrument Serif', serif", subFont: "'Instrument Serif', serif", subStyle: 'italic', arrowColor: '#000', arrowWidth: 1.5 });
        __dg.text(SVG, 470, 280, 'Fig. 1  The MCP traffic pattern.', { size: 14, color: '#666', font: "'Instrument Serif', serif", style: 'italic' });"""),
    (23,'material-elevation','Material Elevation',
     'Flat color cards with layered Material shadows.',
     'flat · elevation · rounded',
     'background:#f4f4f6;',
     """__dg.addDefs(SVG, '<filter id="mat" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.12"/><feDropShadow dx="0" dy="1" stdDeviation="1" flood-opacity="0.24"/></filter>');
        __dg.drawStandard(SVG, { rx: 6, fills: ['#5b6bfa','#fb7185','#34d399'], boxFilter: 'url(#mat)', textColor: '#fff', subColor: 'rgba(255,255,255,.85)', titleSize: 28, titleWeight: 600, font: "'Inter', sans-serif", arrowColor: '#5b6bfa', arrowWidth: 2 });"""),
    (24,'duotone-gradient','Duotone Gradient',
     'Bold two-tone gradient fills, no borders.',
     'gradients · vivid',
     'background:#fef3f9;',
     """__dg.addDefs(SVG, '<linearGradient id="dg1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a855f7"/><stop offset="1" stop-color="#ec4899"/></linearGradient><linearGradient id="dg2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8b5cf6"/><stop offset="1" stop-color="#f472b6"/></linearGradient><linearGradient id="dg3" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6366f1"/><stop offset="1" stop-color="#db2777"/></linearGradient>');
        __dg.drawStandard(SVG, { rx: 16, fills: ['url(#dg1)','url(#dg2)','url(#dg3)'], textColor: '#fff', subColor: 'rgba(255,255,255,.9)', titleSize: 28, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#a855f7', arrowWidth: 2.5 });"""),
    (25,'wire-schematic','Wire Schematic',
     'Electronic schematic: pin dots, bracketed labels, precise.',
     'pins · brackets · mono',
     'background:#f9fafb;',
     """__dg.LAYOUT.forEach(b => {
          __dg.line(SVG, b.x+15, b.y, b.x, b.y, { stroke: '#111', strokeWidth: 1.2 });
          __dg.line(SVG, b.x, b.y, b.x, b.y+b.h, { stroke: '#111', strokeWidth: 1.2 });
          __dg.line(SVG, b.x, b.y+b.h, b.x+15, b.y+b.h, { stroke: '#111', strokeWidth: 1.2 });
          __dg.line(SVG, b.x+b.w-15, b.y, b.x+b.w, b.y, { stroke: '#111', strokeWidth: 1.2 });
          __dg.line(SVG, b.x+b.w, b.y, b.x+b.w, b.y+b.h, { stroke: '#111', strokeWidth: 1.2 });
          __dg.line(SVG, b.x+b.w, b.y+b.h, b.x+b.w-15, b.y+b.h, { stroke: '#111', strokeWidth: 1.2 });
          __dg.circle(SVG, b.x, b.y+b.h/2, 3.5, { fill: '#111' });
          __dg.circle(SVG, b.x+b.w, b.y+b.h/2, 3.5, { fill: '#111' });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 24, weight: 500, color: '#111', font: "'JetBrains Mono', monospace" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, '[ '+b.sub.replace(/[()]/g,'')+' ]', { size: 13, weight: 400, color: '#666', font: "'JetBrains Mono', monospace" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#111', strokeWidth: 1 }));"""),
    (26,'blueprint-precise','Blueprint Precise',
     'Refined blueprint: corner crosshairs, dashed arrows, dimension labels.',
     'corner marks · dashed',
     'background:#0f3a7e; background-image: linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px); background-size: 30px 30px;',
     """__dg.LAYOUT.forEach(b => {
          __dg.rect(SVG, b, { fill: 'rgba(255,255,255,0.04)', stroke: '#dbeafe', strokeWidth: 1 });
          [[b.x,b.y],[b.x+b.w,b.y],[b.x,b.y+b.h],[b.x+b.w,b.y+b.h]].forEach(pt => __dg.circle(SVG, pt[0], pt[1], 4, { fill: 'none', stroke: '#dbeafe', strokeWidth: 1 }));
          __dg.text(SVG, b.x+b.w/2, b.y+68, b.title.toUpperCase(), { size: 22, weight: 500, color: '#fff', font: "'JetBrains Mono', monospace" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 12, weight: 400, color: '#93c5fd', font: "'JetBrains Mono', monospace" });
          __dg.text(SVG, b.x+b.w/2, b.y+b.h+22, '240 × 140', { size: 11, color: '#93c5fd', font: "'JetBrains Mono', monospace" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#dbeafe', strokeWidth: 1, dash: '4 3' }));"""),
    (27,'retro-terminal','Retro Terminal',
     'Phosphor green on black, ASCII corners, scanlines.',
     'green · mono · scanlines',
     'background:#000; background-image: repeating-linear-gradient(transparent 0 2px, rgba(0,255,70,0.04) 2px 3px);',
     """__dg.LAYOUT.forEach(b => {
          __dg.rect(SVG, b, { fill: 'rgba(0,255,70,0.03)', stroke: '#00ff46', strokeWidth: 1 });
          [[b.x-2,b.y+4],[b.x+b.w+2,b.y+4],[b.x-2,b.y+b.h-2],[b.x+b.w+2,b.y+b.h-2]].forEach(c => __dg.text(SVG, c[0], c[1], '+', { size: 16, color: '#00ff46', font: "'JetBrains Mono', monospace" }));
          __dg.text(SVG, b.x+b.w/2, b.y+66, '> '+b.title.toUpperCase(), { size: 24, weight: 500, color: '#00ff46', font: "'JetBrains Mono', monospace" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 13, color: '#0de060', font: "'JetBrains Mono', monospace" });
        });
        __dg.ARROWS.forEach(a => { __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#00ff46', strokeWidth: 1, dash: '3 2' }); __dg.text(SVG, (a.x1+a.x2)/2, a.y-6, '<->', { size: 14, color: '#00ff46', font: "'JetBrains Mono', monospace" }); });"""),
    (28,'editorial-serif','Editorial Serif',
     'Large serif, generous whitespace, hairline boxes.',
     'serif · hairline · essay',
     'background:#f9f5ea;',
     """__dg.LAYOUT.forEach((b, i) => {
          __dg.rect(SVG, b, { fill: 'none', stroke: '#1f1611', strokeWidth: 0.75 });
          __dg.text(SVG, b.x+b.w-14, b.y+22, '0'+(i+1), { size: 14, color: '#8b7355', font: "'Instrument Serif', serif", anchor: 'end' });
          __dg.text(SVG, b.x+b.w/2, b.y+72, b.title, { size: 34, weight: 400, color: '#1f1611', font: "'Instrument Serif', serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+106, b.sub, { size: 14, color: '#7a6a5a', font: "'Instrument Serif', serif", style: 'italic' });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#1f1611', strokeWidth: 0.75 }));"""),
    (29,'bauhaus','Bauhaus Geometric',
     'Primary colors, geometric primitives (square/circle/triangle).',
     'primary · geometry',
     'background:#f5f1e8;',
     """const pal=['#e23e2b','#205fd9','#fcb813']; const sh=['square','circle','triangle'];
        __dg.LAYOUT.forEach((b, i) => {
          const cx=b.x+b.w/2, cy=b.y+b.h/2;
          if (sh[i]==='square') __dg.rect(SVG, b, { fill: pal[i], stroke: '#000', strokeWidth: 3 });
          else if (sh[i]==='circle') __dg.circle(SVG, cx, cy, Math.min(b.w,b.h)/2, { fill: pal[i], stroke: '#000', strokeWidth: 3 });
          else __dg.poly(SVG, [[cx,b.y],[b.x+b.w,b.y+b.h],[b.x,b.y+b.h]], { fill: pal[i], stroke: '#000', strokeWidth: 3 });
          __dg.text(SVG, cx, cy-4, b.title, { size: 22, weight: 700, color: sh[i]==='triangle'?'#000':'#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, cx, cy+24, b.sub, { size: 13, weight: 500, color: sh[i]==='triangle'?'#333':'rgba(255,255,255,.85)', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#000', strokeWidth: 3 }));"""),
    (30,'infographic-circles','Infographic Circles',
     'Circular nodes with curved dashed connectors.',
     'circles · curves',
     'background:#fff7f0;',
     """__dg.drawCircles(SVG, { fills: ['#a78bfa','#fb923c','#2dd4bf'], strokes: ['#6d28d9','#c2410c','#0f766e'], strokeWidth: 3, textColor: '#fff', subColor: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif", arrowColor: '#8b5cf6', arrowWidth: 2.5, arrowDash: '6 4' });"""),
]

# ---- 31-40: color variations ----
COLOR_VARS = [
    (31,'midnight-purple','Midnight Purple',
     'Deep purple background, cream cards, gold accent.',
     'dark purple · cream',
     'background:#1e1b4b;',
     """__dg.drawStandard(SVG, { rx: 10, fill: '#fef3c7', stroke: '#fbbf24', strokeWidth: 1.5, textColor: '#1e1b4b', subColor: '#4338ca', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#fbbf24', arrowWidth: 2 });"""),
    (32,'forest-green','Forest Green',
     'Deep forest background, soft cream cards.',
     'green · cream',
     'background:#052e16;',
     """__dg.drawStandard(SVG, { rx: 10, fill: '#f7f3e9', stroke: '#84cc16', strokeWidth: 1.5, textColor: '#052e16', subColor: '#15803d', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#84cc16', arrowWidth: 2 });"""),
    (33,'rose-gold','Rose Gold',
     'Soft pink background, metallic gold boxes.',
     'rose · gold · soft',
     'background:#fdf2f8;',
     """__dg.addDefs(SVG, '<linearGradient id="gld" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fef3c7"/><stop offset="0.5" stop-color="#f59e0b"/><stop offset="1" stop-color="#b45309"/></linearGradient>');
        __dg.drawStandard(SVG, { rx: 12, fill: 'url(#gld)', stroke: '#be185d', strokeWidth: 1.5, textColor: '#78350f', subColor: '#9d174d', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#be185d', arrowWidth: 2 });"""),
    (34,'mono-slate','Mono Slate',
     'Pure grayscale, different slate tones per box.',
     'grayscale · slate',
     'background:#f8fafc;',
     """__dg.drawStandard(SVG, { rx: 4, fills: ['#1e293b','#475569','#94a3b8'], strokeWidth: 0, textColor: '#fff', subColor: 'rgba(255,255,255,.8)', titleSize: 26, titleWeight: 600, font: "'Inter', sans-serif", arrowColor: '#334155', arrowWidth: 2 });"""),
    (35,'coral-pop','Coral Pop',
     'Coral background, white cards with coral accents.',
     'coral · warm',
     'background:#fb7185;',
     """__dg.drawStandard(SVG, { rx: 14, fill: '#fff', stroke: '#e11d48', strokeWidth: 2, textColor: '#881337', subColor: '#e11d48', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#fff', arrowWidth: 2.5 });"""),
    (36,'deep-navy','Deep Navy',
     'Navy with white text, minimalist.',
     'navy · white text',
     'background:#0f172a;',
     """__dg.drawStandard(SVG, { rx: 6, fill: '#1e293b', stroke: '#334155', strokeWidth: 1, textColor: '#f8fafc', subColor: '#94a3b8', titleSize: 26, titleWeight: 600, font: "'Inter', sans-serif", arrowColor: '#60a5fa', arrowWidth: 2 });"""),
    (37,'sage-linen','Sage & Linen',
     'Sage green on warm linen, calming earth tones.',
     'sage · linen · calm',
     'background:#f5f5f0;',
     """__dg.drawStandard(SVG, { rx: 10, fill: '#d3e4cd', stroke: '#4a7c59', strokeWidth: 1.5, textColor: '#1a4027', subColor: '#4a7c59', titleSize: 26, titleWeight: 600, font: "'Inter', sans-serif", arrowColor: '#4a7c59', arrowWidth: 2 });"""),
    (38,'electric-lime','Electric Lime',
     'Black cards with bright lime accents. Energetic.',
     'black · lime',
     'background:#0a0a0a;',
     """__dg.drawStandard(SVG, { rx: 8, fill: '#1a1a1a', stroke: '#a3e635', strokeWidth: 2, textColor: '#a3e635', subColor: '#ecfccb', titleSize: 26, titleWeight: 700, font: "'JetBrains Mono', monospace", arrowColor: '#a3e635', arrowWidth: 2 });"""),
    (39,'terracotta','Terracotta Earth',
     'Warm terracotta palette, clay cards on sand.',
     'earthy · warm',
     'background:#fef3c7;',
     """__dg.drawStandard(SVG, { rx: 10, fill: '#c2410c', stroke: '#7c2d12', strokeWidth: 2, textColor: '#fef3c7', subColor: '#fed7aa', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#7c2d12', arrowWidth: 2 });"""),
    (40,'midnight-ocean','Midnight Ocean',
     'Deep teal gradient, luminous cards.',
     'teal · deep · luminous',
     'background: linear-gradient(135deg, #042f2e 0%, #0f766e 100%);',
     """__dg.addDefs(SVG, '<filter id="oce"><feGaussianBlur stdDeviation="0.3"/></filter>');
        __dg.drawStandard(SVG, { rx: 16, fill: 'rgba(20,184,166,0.2)', stroke: '#5eead4', strokeWidth: 1.5, textColor: '#f0fdfa', subColor: '#99f6e4', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#5eead4', arrowWidth: 2 });"""),
]

# ---- 41-50: shape variations ----
SHAPE_VARS = [
    (41,'hexagonal','Hexagonal Nodes',
     'Hexagons instead of rectangles, honeycomb-tech feel.',
     'hex · honeycomb',
     'background:#fffbeb;',
     """__dg.drawHexes(SVG, { fills: ['#f59e0b','#fbbf24','#fcd34d'], strokes: ['#92400e','#92400e','#92400e'], strokeWidth: 3, textColor: '#78350f', subColor: '#92400e', font: "'Inter', sans-serif", arrowColor: '#92400e' });"""),
    (42,'pills','Pill Buttons',
     'Rounded-pill shapes. Friendly, touch-target feel.',
     'pills · rounded',
     'background:#f0f9ff;',
     """__dg.drawStandard(SVG, { rx: 70, fills: ['#0ea5e9','#06b6d4','#10b981'], strokeWidth: 0, textColor: '#fff', subColor: 'rgba(255,255,255,.9)', titleSize: 26, titleWeight: 600, font: "'Inter', sans-serif", arrowColor: '#0284c7', arrowWidth: 2.5 });"""),
    (43,'tag-shape','Tag / Index Card',
     'Corner-cut tag shapes, like library index cards.',
     'tag · index card',
     'background:#fafaf9;',
     """__dg.LAYOUT.forEach((b, i) => {
          const notch = 15;
          __dg.poly(SVG, [[b.x+notch,b.y],[b.x+b.w,b.y],[b.x+b.w,b.y+b.h],[b.x,b.y+b.h],[b.x,b.y+notch]], { fill: ['#fef3c7','#fde68a','#fcd34d'][i], stroke: '#78350f', strokeWidth: 1.5 });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 26, weight: 700, color: '#78350f', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: '#92400e', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#78350f', strokeWidth: 2 }));"""),
    (44,'stacked-cards','Stacked Cards',
     'Each box is 3 overlapping cards, depth illusion.',
     'stacked · overlap',
     'background:#f5f3ff;',
     """__dg.LAYOUT.forEach((b, i) => {
          for (let k = 2; k >= 0; k--) {
            __dg.rect(SVG, {x:b.x+k*3, y:b.y+k*3, w:b.w, h:b.h}, { rx: 10, fill: k===0?'#fff':'#ede9fe', stroke: '#8b5cf6', strokeWidth: 1 });
          }
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 26, weight: 700, color: '#4c1d95', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: '#6b21a8', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#8b5cf6', strokeWidth: 2 }));"""),
    (45,'network-nodes','Network Nodes',
     'Small circular nodes with thick connecting links.',
     'nodes · network graph',
     'background:#f1f5f9;',
     """__dg.LAYOUT.forEach(b => {
          const cx = b.x+b.w/2, cy = b.y+b.h/2;
          __dg.circle(SVG, cx, cy, 40, { fill: '#6366f1', stroke: '#4338ca', strokeWidth: 3 });
          __dg.circle(SVG, cx, cy, 6, { fill: '#fff' });
          __dg.text(SVG, cx, cy+68, b.title, { size: 18, weight: 700, color: '#1e1b4b', font: "'Inter', sans-serif" });
          __dg.text(SVG, cx, cy+90, b.sub, { size: 12, color: '#4338ca', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1-20, a.y, a.x2+20, a.y, { stroke: '#6366f1', strokeWidth: 4 }));"""),
    (46,'diamond-flow','Flow Diamonds',
     'Diamond decision-shapes, classic flowchart.',
     'diamonds · flowchart',
     'background:#fefce8;',
     """__dg.drawDiamonds(SVG, { fills: ['#facc15','#fbbf24','#f59e0b'], strokes: ['#713f12','#713f12','#713f12'], strokeWidth: 3, textColor: '#713f12', subColor: '#78350f', font: "'Inter', sans-serif", arrowColor: '#713f12' });"""),
    (47,'squircle','Squircle',
     'Superellipse shapes (softer than rounded rect).',
     'squircle · smooth',
     'background:#f0fdf4;',
     """__dg.LAYOUT.forEach(b => {
          const p = __dg.el('path', { d: `M ${b.x+20} ${b.y} Q ${b.x} ${b.y} ${b.x} ${b.y+20} L ${b.x} ${b.y+b.h-20} Q ${b.x} ${b.y+b.h} ${b.x+20} ${b.y+b.h} L ${b.x+b.w-20} ${b.y+b.h} Q ${b.x+b.w} ${b.y+b.h} ${b.x+b.w} ${b.y+b.h-20} L ${b.x+b.w} ${b.y+20} Q ${b.x+b.w} ${b.y} ${b.x+b.w-20} ${b.y} Z`, fill: '#10b981', stroke: '#047857', 'stroke-width': 2 });
          SVG.appendChild(p);
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 26, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#047857', strokeWidth: 2 }));"""),
    (48,'hub-spoke','Hub & Spoke',
     'Central client as hub, model/server as satellites.',
     'hub · radial',
     'background:#fafaf9;',
     """const hub = __dg.LAYOUT[1];
        const hcx = hub.x+hub.w/2, hcy = hub.y+hub.h/2;
        __dg.circle(SVG, hcx, hcy, 95, { fill: '#8b5cf6', stroke: '#4c1d95', strokeWidth: 3 });
        __dg.text(SVG, hcx, hcy-4, 'Client', { size: 22, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
        __dg.text(SVG, hcx, hcy+20, '(Claude Code)', { size: 12, color: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif" });
        [__dg.LAYOUT[0], __dg.LAYOUT[2]].forEach((b, idx) => {
          const cx = b.x+b.w/2, cy = b.y+b.h/2;
          __dg.circle(SVG, cx, cy, 55, { fill: idx===0?'#a78bfa':'#c084fc', stroke: '#4c1d95', strokeWidth: 2 });
          __dg.text(SVG, cx, cy-2, b.title, { size: 18, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, cx, cy+20, b.sub, { size: 11, color: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif" });
          __dg.line(SVG, cx + (idx===0?55:-55)*(idx===0?1:-1), cy, hcx + (idx===0?-95:95)*(idx===0?1:-1), hcy, { stroke: '#8b5cf6', strokeWidth: 3 });
        });"""),
    (49,'tree-branches','Tree Branches',
     'Hierarchical tree: model parent, client child, server grandchild.',
     'tree · hierarchy',
     'background:#ecfdf5;',
     """// Model at top, client middle, server bottom
        const nodes = [
          { ...__dg.LAYOUT[0], x: 340, y: 30 },
          { ...__dg.LAYOUT[1], x: 340, y: 150 },
          { ...__dg.LAYOUT[2], x: 340, y: 270 }
        ];
        // Simplified: use standard layout but vertically
        __dg.LAYOUT.forEach((b, i) => {
          const nb = { x: 340, y: 30 + i*110, w: 240, h: 80 };
          __dg.rect(SVG, nb, { rx: 8, fill: ['#34d399','#10b981','#059669'][i], strokeWidth: 0 });
          __dg.text(SVG, nb.x+nb.w/2, nb.y+34, b.title, { size: 22, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, nb.x+nb.w/2, nb.y+56, b.sub, { size: 12, color: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif" });
        });
        __dg.line(SVG, 460, 110, 460, 140, { stroke: '#047857', strokeWidth: 2 });
        __dg.line(SVG, 460, 220, 460, 250, { stroke: '#047857', strokeWidth: 2 });"""),
    (50,'cloud-shapes','Cloud Shapes',
     'Fluffy cloud outlines. Whimsical, abstract.',
     'clouds · soft',
     'background:#dbeafe;',
     """__dg.LAYOUT.forEach((b, i) => {
          const cx = b.x+b.w/2, cy = b.y+b.h/2;
          // Simple cloud: 4 overlapping circles
          __dg.circle(SVG, cx-45, cy+5, 40, { fill: '#fff', stroke: '#3b82f6', strokeWidth: 2 });
          __dg.circle(SVG, cx+45, cy+5, 40, { fill: '#fff', stroke: '#3b82f6', strokeWidth: 2 });
          __dg.circle(SVG, cx, cy-15, 50, { fill: '#fff', stroke: '#3b82f6', strokeWidth: 2 });
          __dg.circle(SVG, cx, cy+15, 45, { fill: '#fff', stroke: '#3b82f6', strokeWidth: 2 });
          __dg.text(SVG, cx, cy-4, b.title, { size: 20, weight: 700, color: '#1e3a8a', font: "'Inter', sans-serif" });
          __dg.text(SVG, cx, cy+20, b.sub, { size: 11, color: '#3b82f6', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#3b82f6', strokeWidth: 2 }));"""),
]

# ---- 51-60: artistic rendering ----
ARTISTIC = [
    (51,'watercolor','Watercolor Splash',
     'Soft watercolor washes as box backgrounds.',
     'watercolor · soft',
     'background:#fef7f7;',
     """__dg.addDefs(SVG, '<filter id="wc" x="-20%" y="-20%" width="140%" height="140%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2"/><feDisplacementMap in="SourceGraphic" scale="8"/></filter>');
        __dg.drawStandard(SVG, { rx: 30, fills: ['rgba(244,114,182,0.4)','rgba(139,92,246,0.4)','rgba(96,165,250,0.4)'], strokeWidth: 0, boxFilter: 'url(#wc)', textColor: '#1e1b4b', subColor: '#4338ca', titleSize: 26, titleWeight: 600, font: "'Inter', sans-serif", arrowColor: '#6366f1', arrowWidth: 2.5 });"""),
    (52,'ink-wash','Ink Wash / Sumi-e',
     'Soft black ink on rice paper, East Asian calligraphy feel.',
     'ink · sumi-e',
     'background:#fdfcf7;',
     """__dg.addDefs(SVG, '<filter id="ink" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="3"/><feDisplacementMap in="SourceGraphic" scale="3"/></filter>');
        __dg.drawStandard(SVG, { rx: 0, fill: 'rgba(0,0,0,0.05)', stroke: '#1a1a1a', strokeWidth: 3, boxFilter: 'url(#ink)', textColor: '#1a1a1a', subColor: '#555', titleSize: 28, titleWeight: 400, font: "'Instrument Serif', serif", subStyle: 'italic', arrowColor: '#1a1a1a', arrowWidth: 3 });"""),
    (53,'oil-pastel','Oil Pastel',
     'Textured soft brush, rich color, artistic.',
     'pastel · textured',
     'background:#fef9f3;',
     """__dg.addDefs(SVG, '<filter id="op"><feTurbulence baseFrequency="0.3" numOctaves="2"/><feComposite in2="SourceAlpha" operator="in"/><feComponentTransfer><feFuncA type="linear" slope="0.3"/></feComponentTransfer><feComposite in="SourceGraphic" operator="over"/></filter>');
        __dg.drawStandard(SVG, { rx: 20, fills: ['#f97316','#eab308','#22c55e'], strokeWidth: 0, boxFilter: 'url(#op)', textColor: '#fff', subColor: 'rgba(255,255,255,.9)', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#ea580c', arrowWidth: 3 });"""),
    (54,'charcoal','Charcoal',
     'Smudgy dark texture on cream, drawing-board feel.',
     'charcoal · smudgy',
     'background:#f5f1e8;',
     """__dg.addDefs(SVG, '<filter id="ch"><feTurbulence baseFrequency="0.8" numOctaves="2" seed="5"/><feComposite in2="SourceAlpha" operator="in"/></filter>');
        __dg.drawStandard(SVG, { rx: 4, fill: '#2a2a2a', stroke: '#1a1a1a', strokeWidth: 2, boxFilter: 'url(#ch)', textColor: '#f5f1e8', subColor: '#c0b8a8', titleSize: 26, titleWeight: 600, font: "'Inter', sans-serif", arrowColor: '#1a1a1a', arrowWidth: 3 });"""),
    (55,'pixel-art','Pixel Art 8-bit',
     'Chunky pixel borders, limited palette, retro game feel.',
     'pixels · 8-bit',
     'background:#1e1b4b;',
     """__dg.LAYOUT.forEach((b, i) => {
          const c = ['#10b981','#f59e0b','#ef4444'][i];
          // Chunky border via 4 thick edges
          [4,8,12].forEach(s => __dg.rect(SVG, {x:b.x-s+s, y:b.y-s+s, w:b.w, h:b.h}, { fill: c, strokeWidth: 0 }));
          __dg.rect(SVG, b, { fill: c, stroke: '#000', strokeWidth: 4 });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title.toUpperCase(), { size: 24, weight: 700, color: '#fff', font: "'JetBrains Mono', monospace" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 13, color: '#fff', font: "'JetBrains Mono', monospace" });
        });
        __dg.ARROWS.forEach(a => {
          for (let x=a.x1; x<a.x2; x+=10) __dg.rect(SVG, {x, y:a.y-3, w:6, h:6}, { fill: '#fff' });
        });"""),
    (56,'low-poly','Low Poly',
     'Triangulated faceted surface, geometric 3D feel.',
     'triangulated · faceted',
     'background:#1f2937;',
     """__dg.LAYOUT.forEach((b, i) => {
          const pal = [['#3b82f6','#60a5fa','#93c5fd'],['#ec4899','#f472b6','#fbcfe8'],['#10b981','#34d399','#6ee7b7']][i];
          // Four triangles making a rect
          __dg.poly(SVG, [[b.x,b.y],[b.x+b.w,b.y],[b.x+b.w/2,b.y+b.h/2]], { fill: pal[0] });
          __dg.poly(SVG, [[b.x+b.w,b.y],[b.x+b.w,b.y+b.h],[b.x+b.w/2,b.y+b.h/2]], { fill: pal[1] });
          __dg.poly(SVG, [[b.x+b.w,b.y+b.h],[b.x,b.y+b.h],[b.x+b.w/2,b.y+b.h/2]], { fill: pal[2] });
          __dg.poly(SVG, [[b.x,b.y+b.h],[b.x,b.y],[b.x+b.w/2,b.y+b.h/2]], { fill: pal[0] });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 24, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 13, color: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#fff', strokeWidth: 2 }));"""),
    (57,'paper-cut','Paper Cut Layers',
     'Layered cut-paper with heavy drop shadows.',
     'paper · layered · shadow',
     'background:#e0f2fe;',
     """__dg.addDefs(SVG, '<filter id="pc" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="3" dy="6" stdDeviation="3" flood-opacity="0.3"/></filter>');
        __dg.drawStandard(SVG, { rx: 2, fills: ['#fef3c7','#fed7aa','#fecaca'], strokeWidth: 0, boxFilter: 'url(#pc)', textColor: '#78350f', subColor: '#92400e', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#78350f', arrowWidth: 2.5 });"""),
    (58,'mosaic','Mosaic Tiles',
     'Box made of many small tile squares, mosaic texture.',
     'mosaic · tiles',
     'background:#0f172a;',
     """__dg.LAYOUT.forEach((b, i) => {
          const ts = 10; // tile size
          const pal = ['#3b82f6','#8b5cf6','#ec4899'];
          for (let x = 0; x < b.w; x += ts) {
            for (let y = 0; y < b.h; y += ts) {
              const jitter = (Math.random() - 0.5) * 30;
              __dg.rect(SVG, {x: b.x+x+1, y: b.y+y+1, w: ts-2, h: ts-2}, { fill: pal[i], strokeWidth: 0 }).setAttribute('opacity', 0.4 + Math.random() * 0.6);
            }
          }
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 26, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#fff', strokeWidth: 2 }));"""),
    (59,'stained-glass','Stained Glass',
     'Leaded glass panels, jeweled colors, dark lead lines.',
     'stained glass · jewel tones',
     'background:#1e293b;',
     """__dg.LAYOUT.forEach((b, i) => {
          __dg.rect(SVG, b, { fill: ['#7c3aed','#dc2626','#0891b2'][i], stroke: '#000', strokeWidth: 5 });
          // Internal lead lines
          __dg.line(SVG, b.x, b.y+b.h/2, b.x+b.w, b.y+b.h/2, { stroke: '#000', strokeWidth: 3 });
          __dg.line(SVG, b.x+b.w/2, b.y, b.x+b.w/2, b.y+b.h, { stroke: '#000', strokeWidth: 3 });
          __dg.text(SVG, b.x+b.w/2, b.y+50, b.title, { size: 22, weight: 700, color: '#fff', font: "'Instrument Serif', serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+120, b.sub, { size: 13, color: '#fff', font: "'Instrument Serif', serif", style: 'italic' });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#000', strokeWidth: 4 }));"""),
    (60,'origami','Origami Fold',
     'Folded paper planes with shaded faces.',
     'folded · paper',
     'background:#fef3c7;',
     """__dg.LAYOUT.forEach((b, i) => {
          const c = ['#8b5cf6','#ec4899','#06b6d4'][i];
          __dg.poly(SVG, [[b.x, b.y],[b.x+b.w, b.y+20],[b.x+b.w, b.y+b.h],[b.x, b.y+b.h-20]], { fill: c, strokeWidth: 0 });
          __dg.poly(SVG, [[b.x, b.y],[b.x+b.w, b.y+20],[b.x+b.w/2, b.y+40]], { fill: c, strokeWidth: 0 }).setAttribute('opacity', 0.7);
          __dg.poly(SVG, [[b.x, b.y+b.h-20],[b.x+b.w, b.y+b.h],[b.x+b.w/2, b.y+b.h-40]], { fill: c, strokeWidth: 0 }).setAttribute('opacity', 0.6);
          __dg.text(SVG, b.x+b.w/2, b.y+70, b.title, { size: 24, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 13, color: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#111', strokeWidth: 2 }));"""),
]

# ---- 61-70: pattern & texture fills ----
PATTERNS = [
    (61,'polka-dots','Polka Dots',
     'Polka-dot pattern fills, playful retro.',
     'dots · playful',
     'background:#fef3c7;',
     """__dg.addDefs(SVG, '<pattern id="pd" x="0" y="0" width="15" height="15" patternUnits="userSpaceOnUse"><circle cx="7.5" cy="7.5" r="3" fill="#7c3aed"/></pattern>');
        __dg.drawStandard(SVG, { rx: 10, fill: 'url(#pd)', stroke: '#4c1d95', strokeWidth: 2, textColor: '#4c1d95', subColor: '#6b21a8', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#7c3aed', arrowWidth: 2 });"""),
    (62,'stripes-bold','Bold Stripes',
     'Diagonal bold stripes, zesty.',
     'stripes · diagonal',
     'background:#fff1f2;',
     """__dg.addDefs(SVG, '<pattern id="st" x="0" y="0" width="20" height="20" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><rect x="0" y="0" width="10" height="20" fill="#f43f5e"/></pattern>');
        __dg.drawStandard(SVG, { rx: 8, fill: 'url(#st)', stroke: '#881337', strokeWidth: 2, textColor: '#fff', subColor: '#fff', titleSize: 26, titleWeight: 800, font: "'Inter', sans-serif", arrowColor: '#881337', arrowWidth: 3 });"""),
    (63,'checkerboard','Checkerboard',
     'Checker fill, old-school retro.',
     'checker · retro',
     'background:#fafaf9;',
     """__dg.addDefs(SVG, '<pattern id="ck" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse"><rect x="0" y="0" width="10" height="10" fill="#111"/><rect x="10" y="10" width="10" height="10" fill="#111"/></pattern>');
        __dg.drawStandard(SVG, { rx: 0, fill: 'url(#ck)', stroke: '#111', strokeWidth: 3, textColor: '#fff', subColor: '#fff', titleSize: 26, titleWeight: 800, font: "'JetBrains Mono', monospace", arrowColor: '#111', arrowWidth: 3 });"""),
    (64,'noise-grain','Noise Grain',
     'Gritty film-grain texture inside colored cards.',
     'grain · gritty',
     'background:#fafaf9;',
     """__dg.addDefs(SVG, '<filter id="ng"><feTurbulence baseFrequency="0.9" numOctaves="2"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.3 0"/><feComposite in2="SourceAlpha" operator="in"/></filter>');
        __dg.drawStandard(SVG, { rx: 12, fills: ['#6366f1','#8b5cf6','#a855f7'], strokeWidth: 0, textColor: '#fff', subColor: 'rgba(255,255,255,.9)', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#6366f1', arrowWidth: 2 });
        __dg.LAYOUT.forEach(b => __dg.rect(SVG, b, { rx: 12, fill: '#000', strokeWidth: 0, filter: 'url(#ng)' }));"""),
    (65,'paper-texture','Paper Texture',
     'Fibrous paper texture, organic feel.',
     'paper · fibrous',
     'background:#fdf6e3;',
     """__dg.addDefs(SVG, '<filter id="pt"><feTurbulence baseFrequency="0.04" numOctaves="5"/><feColorMatrix values="0 0 0 0 0.96  0 0 0 0 0.94  0 0 0 0 0.87  0 0 0 0.3 0"/><feComposite in2="SourceAlpha" operator="in"/><feComposite in="SourceGraphic" operator="over"/></filter>');
        __dg.drawStandard(SVG, { rx: 2, fill: '#faf4e1', stroke: '#8b7355', strokeWidth: 1, boxFilter: 'url(#pt)', textColor: '#3e2f1f', subColor: '#7a6345', titleSize: 26, titleWeight: 600, font: "'Instrument Serif', serif", arrowColor: '#8b7355', arrowWidth: 1.5 });"""),
    (66,'wood-grain','Wood Grain',
     'Wood panel texture, natural warm.',
     'wood · natural',
     'background:#78350f;',
     """__dg.addDefs(SVG, '<pattern id="wd" x="0" y="0" width="100" height="30" patternUnits="userSpaceOnUse"><rect fill="#d4a574" width="100" height="30"/><path d="M 0 15 Q 25 10 50 15 T 100 15" stroke="#92400e" fill="none" stroke-width="1" opacity="0.4"/><path d="M 0 8 Q 25 5 50 8 T 100 8" stroke="#92400e" fill="none" stroke-width="0.5" opacity="0.3"/><path d="M 0 22 Q 25 26 50 22 T 100 22" stroke="#92400e" fill="none" stroke-width="0.5" opacity="0.3"/></pattern>');
        __dg.drawStandard(SVG, { rx: 6, fill: 'url(#wd)', stroke: '#78350f', strokeWidth: 2, textColor: '#3e2f1f', subColor: '#78350f', titleSize: 26, titleWeight: 700, font: "'Instrument Serif', serif", arrowColor: '#78350f', arrowWidth: 2.5 });"""),
    (67,'concrete','Concrete',
     'Rough concrete texture, industrial.',
     'concrete · industrial',
     'background:#f1f5f9;',
     """__dg.addDefs(SVG, '<filter id="cn"><feTurbulence baseFrequency="0.9" numOctaves="4"/><feColorMatrix values="0 0 0 0 0.6  0 0 0 0 0.6  0 0 0 0 0.62  0 0 0 0.4 0"/><feComposite in2="SourceAlpha" operator="in"/><feComposite in="SourceGraphic" operator="over"/></filter>');
        __dg.drawStandard(SVG, { rx: 0, fill: '#94a3b8', stroke: '#334155', strokeWidth: 1, boxFilter: 'url(#cn)', textColor: '#0f172a', subColor: '#334155', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#334155', arrowWidth: 2 });"""),
    (68,'fabric-weave','Fabric Weave',
     'Cross-woven thread pattern, textile feel.',
     'weave · textile',
     'background:#faf5ff;',
     """__dg.addDefs(SVG, '<pattern id="fw" x="0" y="0" width="8" height="8" patternUnits="userSpaceOnUse"><rect fill="#a78bfa" width="8" height="8"/><rect fill="#c4b5fd" width="4" height="4"/><rect x="4" y="4" fill="#c4b5fd" width="4" height="4"/></pattern>');
        __dg.drawStandard(SVG, { rx: 12, fill: 'url(#fw)', stroke: '#6d28d9', strokeWidth: 2, textColor: '#fff', subColor: 'rgba(255,255,255,.9)', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#6d28d9', arrowWidth: 2 });"""),
    (69,'marble','Marble Veins',
     'Marble veining, luxury/stone feel.',
     'marble · luxury',
     'background:#fff;',
     """__dg.addDefs(SVG, '<filter id="mb"><feTurbulence baseFrequency="0.01" numOctaves="3" seed="3"/><feColorMatrix values="0 0 0 0 0.8  0 0 0 0 0.8  0 0 0 0 0.85  0 0 0 0.3 0"/><feComposite in2="SourceAlpha" operator="in"/><feComposite in="SourceGraphic" operator="over"/></filter>');
        __dg.drawStandard(SVG, { rx: 4, fill: '#f5f5f7', stroke: '#1a1a1a', strokeWidth: 1, boxFilter: 'url(#mb)', textColor: '#1a1a1a', subColor: '#444', titleSize: 28, titleWeight: 400, font: "'Instrument Serif', serif", arrowColor: '#1a1a1a', arrowWidth: 2 });"""),
    (70,'leather','Leather Grain',
     'Soft leather texture, premium dark.',
     'leather · premium',
     'background:#1c1917;',
     """__dg.addDefs(SVG, '<filter id="lt"><feTurbulence baseFrequency="0.4" numOctaves="3"/><feColorMatrix values="0 0 0 0 0.2  0 0 0 0 0.1  0 0 0 0 0.05  0 0 0 0.3 0"/><feComposite in2="SourceAlpha" operator="in"/><feComposite in="SourceGraphic" operator="over"/></filter>');
        __dg.drawStandard(SVG, { rx: 10, fill: '#78350f', stroke: '#451a03', strokeWidth: 2, boxFilter: 'url(#lt)', textColor: '#fef3c7', subColor: '#fde68a', titleSize: 26, titleWeight: 600, font: "'Instrument Serif', serif", arrowColor: '#fde68a', arrowWidth: 2 });"""),
]

# ---- 71-80: era & aesthetic ----
ERA = [
    (71,'memphis-80s','Memphis 80s',
     'Squiggles, confetti, primary-on-pastel, 1980s design.',
     'memphis · squiggles',
     'background:#fef3c7;',
     """// Confetti background
        for (let i = 0; i < 30; i++) {
          const x = Math.random() * 920, y = Math.random() * 300;
          const c = ['#f472b6','#60a5fa','#fbbf24','#34d399'][i%4];
          __dg.rect(SVG, {x, y, w: 8, h: 8}, { fill: c, strokeWidth: 0 });
        }
        __dg.drawStandard(SVG, { rx: 4, fills: ['#fbbf24','#f472b6','#60a5fa'], stroke: '#000', strokeWidth: 3, textColor: '#000', subColor: '#000', titleSize: 26, titleWeight: 800, font: "'Inter', sans-serif", arrowColor: '#000', arrowWidth: 3 });"""),
    (72,'vaporwave','Vaporwave',
     'Neon pink/cyan gradient, chrome, retro-futuristic.',
     'vapor · chrome · gradient',
     'background: linear-gradient(180deg, #fb7185 0%, #a855f7 50%, #06b6d4 100%);',
     """__dg.addDefs(SVG, '<linearGradient id="vw" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="0.5" stop-color="#fce7f3"/><stop offset="1" stop-color="#bae6fd"/></linearGradient>');
        __dg.drawStandard(SVG, { rx: 0, fill: 'url(#vw)', stroke: '#fff', strokeWidth: 2, textColor: '#500d68', subColor: '#1e1b4b', titleSize: 26, titleWeight: 700, font: "'JetBrains Mono', monospace", arrowColor: '#fff', arrowWidth: 3 });"""),
    (73,'art-deco','Art Deco',
     'Gold on black, angular ornamentation, 1920s.',
     'deco · gold · angular',
     'background:#0f0f0f;',
     """__dg.drawStandard(SVG, { rx: 0, fill: '#1a1a1a', stroke: '#d4af37', strokeWidth: 2, textColor: '#d4af37', subColor: '#d4af37', titleSize: 28, titleWeight: 800, font: "'Inter', sans-serif", arrowColor: '#d4af37', arrowWidth: 2 });
        // Corner ornaments
        __dg.LAYOUT.forEach(b => {
          [[b.x+8, b.y+8],[b.x+b.w-8, b.y+8],[b.x+8, b.y+b.h-8],[b.x+b.w-8, b.y+b.h-8]].forEach(pt => {
            __dg.poly(SVG, [[pt[0]-4,pt[1]],[pt[0],pt[1]-4],[pt[0]+4,pt[1]],[pt[0],pt[1]+4]], { fill: '#d4af37' });
          });
        });"""),
    (74,'y2k-cyber','Y2K Cyber',
     'Translucent chrome and bubble gum. Early-2000s tech.',
     'Y2K · chrome · bubbles',
     'background: linear-gradient(135deg, #fbcfe8 0%, #e0f2fe 100%);',
     """__dg.addDefs(SVG, '<linearGradient id="y2k" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0.9"/><stop offset="0.5" stop-color="#bae6fd"/><stop offset="1" stop-color="#60a5fa" stop-opacity="0.7"/></linearGradient>');
        __dg.drawStandard(SVG, { rx: 100, fill: 'url(#y2k)', stroke: '#fff', strokeWidth: 2, textColor: '#075985', subColor: '#0369a1', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#0ea5e9', arrowWidth: 3 });"""),
    (75,'brutalist-concrete','Brutalist Concrete',
     'Raw concrete, harsh typography, bunker-architecture feel.',
     'concrete · brutal',
     'background:#737373;',
     """__dg.addDefs(SVG, '<filter id="br"><feTurbulence baseFrequency="0.9" numOctaves="4"/><feColorMatrix values="0 0 0 0 0.3  0 0 0 0 0.3  0 0 0 0 0.3  0 0 0 0.35 0"/><feComposite in2="SourceAlpha" operator="in"/><feComposite in="SourceGraphic" operator="over"/></filter>');
        __dg.drawStandard(SVG, { rx: 0, fill: '#525252', stroke: '#171717', strokeWidth: 4, boxFilter: 'url(#br)', textColor: '#fff', subColor: '#d4d4d4', titleSize: 30, titleWeight: 900, font: "'Inter', sans-serif", arrowColor: '#171717', arrowWidth: 4 });"""),
    (76,'risograph','Risograph Print',
     'Offset layered print, dual-ink overlap, screenprint feel.',
     'riso · offset layers',
     'background:#fef9c3;',
     """__dg.LAYOUT.forEach((b, i) => {
          // Pink layer offset
          __dg.rect(SVG, {x: b.x+4, y: b.y+4, w: b.w, h: b.h}, { rx: 2, fill: '#f472b6', strokeWidth: 0 }).setAttribute('opacity', 0.7);
          // Blue layer offset
          __dg.rect(SVG, {x: b.x-4, y: b.y-2, w: b.w, h: b.h}, { rx: 2, fill: '#60a5fa', strokeWidth: 0 }).setAttribute('opacity', 0.7);
          __dg.rect(SVG, b, { rx: 2, fill: '#fef9c3', stroke: '#1a1a1a', strokeWidth: 1.5 });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 26, weight: 700, color: '#1a1a1a', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: '#525252', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#1a1a1a', strokeWidth: 2 }));"""),
    (77,'newspaper','Newspaper Print',
     'Halftone pattern, serif headlines, old-newspaper feel.',
     'halftone · serif',
     'background:#faf8f3;',
     """__dg.addDefs(SVG, '<pattern id="ht" x="0" y="0" width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.2" fill="#111"/></pattern>');
        __dg.drawStandard(SVG, { rx: 0, fill: 'url(#ht)', stroke: '#111', strokeWidth: 2, textColor: '#fff', subColor: '#f5f5f5', titleSize: 32, titleWeight: 800, font: "'Instrument Serif', serif", arrowColor: '#111', arrowWidth: 2 });"""),
    (78,'sticker-pack','Sticker Pack',
     'Outlined playful stickers with white borders, rounded.',
     'stickers · playful',
     'background:#ddd6fe;',
     """__dg.LAYOUT.forEach((b, i) => {
          // White border ring
          __dg.rect(SVG, {x: b.x-4, y: b.y-4, w: b.w+8, h: b.h+8}, { rx: 22, fill: '#fff', strokeWidth: 0 });
          __dg.rect(SVG, b, { rx: 18, fill: ['#fbbf24','#f472b6','#34d399'][i], stroke: '#111', strokeWidth: 3 });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 28, weight: 800, color: '#111', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, weight: 600, color: '#111', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#111', strokeWidth: 3 }));"""),
    (79,'polaroid','Polaroid Photo',
     'Photo with thick white border, slight tilt, scrapbook.',
     'polaroid · white frame',
     'background: linear-gradient(135deg, #f0e5d0 0%, #e5d3b3 100%);',
     """__dg.addDefs(SVG, '<filter id="po" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="2" dy="4" stdDeviation="3" flood-opacity="0.25"/></filter>');
        __dg.LAYOUT.forEach((b, i) => {
          // White border extends below the "photo"
          const r = i === 1 ? -2 : (i === 0 ? -3 : 3); // tilt
          const g = __dg.el('g', { transform: `rotate(${r} ${b.x+b.w/2} ${b.y+b.h/2})` });
          SVG.appendChild(g);
          const outer = { x: b.x-10, y: b.y-10, w: b.w+20, h: b.h+50 };
          const ol = __dg.el('rect', { x: outer.x, y: outer.y, width: outer.w, height: outer.h, fill: '#fff', filter: 'url(#po)' });
          g.appendChild(ol);
          const inner = { x: b.x, y: b.y, w: b.w, h: b.h };
          const il = __dg.el('rect', { x: inner.x, y: inner.y, width: inner.w, height: inner.h, fill: ['#fbbf24','#a78bfa','#06b6d4'][i] });
          g.appendChild(il);
          // Text inside photo
          const t1 = __dg.el('text', { x: b.x+b.w/2, y: b.y+66, 'text-anchor': 'middle', fill: '#fff', 'font-size': 26, 'font-weight': 700, 'font-family': "'Inter', sans-serif" });
          t1.textContent = b.title; g.appendChild(t1);
          // Caption in bottom margin
          const t2 = __dg.el('text', { x: b.x+b.w/2, y: b.y+b.h+30, 'text-anchor': 'middle', fill: '#111', 'font-size': 16, 'font-family': "'Caveat', cursive" });
          t2.textContent = b.sub; g.appendChild(t2);
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#111', strokeWidth: 2 }));"""),
    (80,'comic-halftone','Comic Halftone',
     'Black outlines, flat fills, halftone dot shading.',
     'comic · halftone',
     'background:#fef3c7;',
     """__dg.addDefs(SVG, '<pattern id="cht" x="0" y="0" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="1.5" fill="#000" opacity="0.3"/></pattern>');
        __dg.LAYOUT.forEach((b, i) => {
          __dg.rect(SVG, b, { rx: 2, fill: ['#ef4444','#3b82f6','#10b981'][i], stroke: '#000', strokeWidth: 4 });
          __dg.rect(SVG, b, { rx: 2, fill: 'url(#cht)' });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title.toUpperCase() + '!', { size: 30, weight: 900, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#000', strokeWidth: 4 }));"""),
]

# ---- 81-90: effects ----
EFFECTS = [
    (81,'long-shadow','Long Shadow',
     'Flat cards with dramatic long shadows in 45° angle.',
     'flat · long shadow',
     'background:#fef2f2;',
     """__dg.LAYOUT.forEach((b, i) => {
          const c = ['#ef4444','#f97316','#eab308'][i];
          const sc = ['#991b1b','#9a3412','#854d0e'][i];
          // Long shadow polygon
          __dg.poly(SVG, [[b.x+b.w, b.y],[b.x+b.w+80, b.y+80],[b.x+b.w+80, b.y+b.h+80],[b.x+b.w, b.y+b.h]], { fill: sc });
          __dg.poly(SVG, [[b.x, b.y+b.h],[b.x+b.w, b.y+b.h],[b.x+b.w+80, b.y+b.h+80],[b.x+80, b.y+b.h+80]], { fill: sc });
          __dg.rect(SVG, b, { fill: c, strokeWidth: 0 });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 28, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#111', strokeWidth: 2 }));"""),
    (82,'pure-outline','Pure Outline',
     'Monochrome line art only, no fills, clean minimal.',
     'outline · minimal',
     'background:#f9f5eb;',
     """__dg.drawStandard(SVG, { rx: 0, fill: 'none', stroke: '#1a1a1a', strokeWidth: 1.5, textColor: '#1a1a1a', subColor: '#666', titleSize: 26, titleWeight: 400, font: "'Instrument Serif', serif", arrowColor: '#1a1a1a', arrowWidth: 1 });"""),
    (83,'mesh-gradient','Mesh Gradient Fill',
     'Each box has its own gradient mesh, painterly.',
     'mesh · gradient',
     'background:#f1f5f9;',
     """__dg.addDefs(SVG, '<radialGradient id="mg1" cx="0.3" cy="0.3"><stop offset="0" stop-color="#f472b6"/><stop offset="1" stop-color="#6366f1"/></radialGradient><radialGradient id="mg2" cx="0.7" cy="0.3"><stop offset="0" stop-color="#fbbf24"/><stop offset="1" stop-color="#ef4444"/></radialGradient><radialGradient id="mg3" cx="0.5" cy="0.7"><stop offset="0" stop-color="#34d399"/><stop offset="1" stop-color="#0891b2"/></radialGradient>');
        __dg.drawStandard(SVG, { rx: 18, fills: ['url(#mg1)','url(#mg2)','url(#mg3)'], strokeWidth: 0, textColor: '#fff', subColor: 'rgba(255,255,255,.9)', titleSize: 26, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#6366f1', arrowWidth: 2.5 });"""),
    (84,'tilted-3d','Tilted 3D',
     'Slight perspective tilt, all boxes leaning into view.',
     'perspective · tilt',
     'background:#ede9fe;',
     """__dg.LAYOUT.forEach((b, i) => {
          const g = __dg.el('g', { transform: `translate(${b.x+b.w/2} ${b.y+b.h/2}) skewY(-5) translate(${-(b.x+b.w/2)} ${-(b.y+b.h/2)})` });
          SVG.appendChild(g);
          const r = __dg.el('rect', { x: b.x, y: b.y, width: b.w, height: b.h, rx: 10, fill: ['#8b5cf6','#6366f1','#a855f7'][i], 'stroke-width': 0 });
          g.appendChild(r);
          const t1 = __dg.el('text', { x: b.x+b.w/2, y: b.y+66, 'text-anchor': 'middle', fill: '#fff', 'font-size': 26, 'font-weight': 700, 'font-family': "'Inter', sans-serif" });
          t1.textContent = b.title; g.appendChild(t1);
          const t2 = __dg.el('text', { x: b.x+b.w/2, y: b.y+100, 'text-anchor': 'middle', fill: 'rgba(255,255,255,.9)', 'font-size': 14, 'font-family': "'Inter', sans-serif" });
          t2.textContent = b.sub; g.appendChild(t2);
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#6366f1', strokeWidth: 2 }));"""),
    (85,'double-outline','Double Outline',
     'Two-tone nested outlines, retro label feel.',
     'double border · nested',
     'background:#fef3c7;',
     """__dg.LAYOUT.forEach((b, i) => {
          __dg.rect(SVG, b, { fill: '#fef3c7', stroke: '#000', strokeWidth: 3 });
          __dg.rect(SVG, {x: b.x+6, y: b.y+6, w: b.w-12, h: b.h-12}, { fill: 'none', stroke: '#000', strokeWidth: 1 });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title.toUpperCase(), { size: 26, weight: 800, color: '#000', font: "'Instrument Serif', serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 13, color: '#666', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#000', strokeWidth: 2 }));"""),
    (86,'soft-blur','Soft Focus',
     'Dreamy feathered edges, soft focus photography.',
     'blur · dreamy',
     'background: linear-gradient(135deg, #fce7f3 0%, #ede9fe 100%);',
     """__dg.addDefs(SVG, '<filter id="sf" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="1.5"/></filter>');
        __dg.drawStandard(SVG, { rx: 20, fills: ['#ec4899','#8b5cf6','#3b82f6'], strokeWidth: 0, boxFilter: 'url(#sf)', textColor: '#fff', subColor: 'rgba(255,255,255,.9)', titleSize: 28, titleWeight: 700, font: "'Inter', sans-serif", arrowColor: '#6366f1', arrowWidth: 2 });"""),
    (87,'neon-tube','Neon Tube',
     'Bright glowing tube lights, sign-shop aesthetic.',
     'neon tube · sign',
     'background:#0a0a0a;',
     """__dg.addDefs(SVG, '<filter id="nt" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>');
        __dg.LAYOUT.forEach((b, i) => {
          const c = ['#10b981','#f59e0b','#ec4899'][i];
          __dg.rect(SVG, b, { rx: 12, fill: 'none', stroke: c, strokeWidth: 3, filter: 'url(#nt)' });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title.toUpperCase(), { size: 28, weight: 800, color: c, font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: c, font: "'JetBrains Mono', monospace" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#10b981', strokeWidth: 3, filter: 'url(#nt)' }));"""),
    (88,'chrome-metallic','Chrome Metallic',
     'Polished metal gradient, reflective sheen.',
     'chrome · metal',
     'background:#0f172a;',
     """__dg.addDefs(SVG, '<linearGradient id="cm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1f5f9"/><stop offset="0.3" stop-color="#94a3b8"/><stop offset="0.5" stop-color="#475569"/><stop offset="0.7" stop-color="#94a3b8"/><stop offset="1" stop-color="#cbd5e1"/></linearGradient>');
        __dg.drawStandard(SVG, { rx: 8, fill: 'url(#cm)', stroke: '#1e293b', strokeWidth: 1.5, textColor: '#0f172a', subColor: '#334155', titleSize: 28, titleWeight: 800, font: "'Inter', sans-serif", arrowColor: '#94a3b8', arrowWidth: 2.5 });"""),
    (89,'holographic','Holographic Foil',
     'Iridescent rainbow gradient, holo-sticker look.',
     'holo · iridescent',
     'background:#000;',
     """__dg.addDefs(SVG, '<linearGradient id="ho" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f472b6"/><stop offset="0.3" stop-color="#fbbf24"/><stop offset="0.6" stop-color="#34d399"/><stop offset="1" stop-color="#60a5fa"/></linearGradient>');
        __dg.drawStandard(SVG, { rx: 12, fill: 'url(#ho)', strokeWidth: 0, textColor: '#000', subColor: '#333', titleSize: 28, titleWeight: 800, font: "'Inter', sans-serif", arrowColor: '#fff', arrowWidth: 2.5 });"""),
    (90,'embossed-deep','Embossed Deep',
     'Deep raised surface, carved-from-stone feel.',
     'embossed · carved',
     'background:#475569;',
     """__dg.addDefs(SVG, '<filter id="ed" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="-3" dy="-3" stdDeviation="4" flood-color="#64748b" flood-opacity="1"/><feDropShadow dx="3" dy="3" stdDeviation="4" flood-color="#1e293b" flood-opacity="0.8"/></filter>');
        __dg.drawStandard(SVG, { rx: 12, fill: '#475569', boxFilter: 'url(#ed)', textColor: '#f1f5f9', subColor: '#cbd5e1', titleSize: 26, titleWeight: 600, font: "'Inter', sans-serif", arrowColor: '#cbd5e1', arrowWidth: 2 });"""),
]

# ---- 91-100: utility & special ----
SPECIAL = [
    (91,'flip-card','Flip Card',
     'Two-tone card, front face with subtle back peek.',
     'flip · two-tone',
     'background:#eff6ff;',
     """__dg.LAYOUT.forEach((b, i) => {
          // "back" offset slightly
          __dg.rect(SVG, {x:b.x+8, y:b.y+8, w:b.w, h:b.h}, { rx: 10, fill: '#3b82f6', strokeWidth: 0 });
          __dg.rect(SVG, b, { rx: 10, fill: '#dbeafe', stroke: '#1d4ed8', strokeWidth: 1.5 });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 26, weight: 700, color: '#1e3a8a', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: '#1e40af', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#1d4ed8', strokeWidth: 2 }));"""),
    (92,'badge-ribbon','Badge Ribbon',
     'Award-ribbon shape with tail at the bottom.',
     'ribbon · award',
     'background:#fef3c7;',
     """__dg.LAYOUT.forEach((b, i) => {
          // Main badge body
          __dg.rect(SVG, {x:b.x, y:b.y, w:b.w, h:b.h-20}, { rx: 8, fill: ['#dc2626','#2563eb','#059669'][i], strokeWidth: 0 });
          // Ribbon tails
          __dg.poly(SVG, [[b.x+20, b.y+b.h-20],[b.x+60, b.y+b.h-20],[b.x+45, b.y+b.h+10],[b.x+35, b.y+b.h+10]], { fill: ['#991b1b','#1e40af','#047857'][i] });
          __dg.poly(SVG, [[b.x+b.w-60, b.y+b.h-20],[b.x+b.w-20, b.y+b.h-20],[b.x+b.w-35, b.y+b.h+10],[b.x+b.w-45, b.y+b.h+10]], { fill: ['#991b1b','#1e40af','#047857'][i] });
          __dg.text(SVG, b.x+b.w/2, b.y+56, b.title, { size: 24, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+88, b.sub, { size: 13, color: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#111', strokeWidth: 2 }));"""),
    (93,'speech-bubble','Speech Bubble',
     'Chat-bubble shapes, conversational.',
     'bubble · chat',
     'background:#fafaf9;',
     """__dg.LAYOUT.forEach((b, i) => {
          const c = ['#8b5cf6','#ec4899','#06b6d4'][i];
          __dg.rect(SVG, b, { rx: 18, fill: c, strokeWidth: 0 });
          // Tail pointing down
          __dg.poly(SVG, [[b.x+30, b.y+b.h],[b.x+50, b.y+b.h+15],[b.x+70, b.y+b.h]], { fill: c });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 26, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: 'rgba(255,255,255,.9)', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y+8, a.x2, a.y+8, { stroke: '#475569', strokeWidth: 2, dash: '4 3' }));"""),
    (94,'torn-paper','Torn Paper Edge',
     'Jagged torn-paper edges, scrapbook.',
     'torn · scrapbook',
     'background:#1a1a1a;',
     """__dg.LAYOUT.forEach((b, i) => {
          // Approximate torn edge with zigzag path at top + bottom
          const p = [];
          p.push(`M ${b.x} ${b.y}`);
          for (let x = b.x+10; x < b.x+b.w; x += 10) p.push(`L ${x} ${b.y + (Math.random()-0.5)*8}`);
          p.push(`L ${b.x+b.w} ${b.y}`);
          p.push(`L ${b.x+b.w} ${b.y+b.h}`);
          for (let x = b.x+b.w-10; x > b.x; x -= 10) p.push(`L ${x} ${b.y+b.h + (Math.random()-0.5)*8}`);
          p.push(`L ${b.x} ${b.y+b.h} Z`);
          const pth = __dg.el('path', { d: p.join(' '), fill: ['#fef3c7','#fed7aa','#fecaca'][i], 'stroke-width': 0 });
          SVG.appendChild(pth);
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 26, weight: 700, color: '#78350f', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: '#92400e', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#fff', strokeWidth: 2 }));"""),
    (95,'sticky-note','Sticky Note',
     'Yellow Post-it notes with slight folded corner.',
     'sticky · post-it',
     'background:#f3f4f6;',
     """__dg.addDefs(SVG, '<filter id="sn" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="1" dy="3" stdDeviation="2" flood-opacity="0.2"/></filter>');
        __dg.LAYOUT.forEach((b, i) => {
          const tilt = [-2, 1, -1][i];
          const g = __dg.el('g', { transform: `rotate(${tilt} ${b.x+b.w/2} ${b.y+b.h/2})` });
          SVG.appendChild(g);
          const r = __dg.el('rect', { x: b.x, y: b.y, width: b.w, height: b.h, fill: '#fde047', 'stroke-width': 0, filter: 'url(#sn)' });
          g.appendChild(r);
          // Folded corner
          const fc = __dg.el('polygon', { points: `${b.x+b.w-15},${b.y+b.h} ${b.x+b.w},${b.y+b.h} ${b.x+b.w},${b.y+b.h-15}`, fill: '#facc15' });
          g.appendChild(fc);
          const t1 = __dg.el('text', { x: b.x+b.w/2, y: b.y+66, 'text-anchor': 'middle', fill: '#713f12', 'font-size': 26, 'font-weight': 700, 'font-family': "'Caveat', cursive" });
          t1.textContent = b.title; g.appendChild(t1);
          const t2 = __dg.el('text', { x: b.x+b.w/2, y: b.y+102, 'text-anchor': 'middle', fill: '#713f12', 'font-size': 18, 'font-family': "'Caveat', cursive" });
          t2.textContent = b.sub; g.appendChild(t2);
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#111', strokeWidth: 2 }));"""),
    (96,'ticket-stub','Ticket Stub',
     'Perforated-edge ticket strip, event pass.',
     'ticket · perforated',
     'background:#ecfdf5;',
     """__dg.LAYOUT.forEach((b, i) => {
          __dg.rect(SVG, b, { rx: 0, fill: '#fff', stroke: '#065f46', strokeWidth: 2 });
          // Perforations (dashed vertical line at end)
          __dg.line(SVG, b.x+b.w-40, b.y, b.x+b.w-40, b.y+b.h, { stroke: '#065f46', strokeWidth: 2, dash: '4 4' });
          // Color bar on left
          __dg.rect(SVG, {x: b.x, y: b.y, w: 12, h: b.h}, { fill: ['#10b981','#059669','#047857'][i], strokeWidth: 0 });
          __dg.text(SVG, b.x+(b.w-40)/2+6, b.y+66, b.title, { size: 26, weight: 700, color: '#065f46', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+(b.w-40)/2+6, b.y+100, b.sub, { size: 13, color: '#047857', font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w-20, b.y+b.h/2, '#' + (i+1), { size: 20, weight: 700, color: '#065f46', font: "'JetBrains Mono', monospace", transform: `rotate(-90 ${b.x+b.w-20} ${b.y+b.h/2})` });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#065f46', strokeWidth: 2 }));"""),
    (97,'index-tab','Index Tab Cards',
     'Tabbed filing cards, with a labeled tab at the top.',
     'tabs · file cards',
     'background:#fafaf9;',
     """__dg.LAYOUT.forEach((b, i) => {
          const c = ['#ea580c','#2563eb','#059669'][i];
          // Tab
          __dg.rect(SVG, {x: b.x+20, y: b.y-18, w: 100, h: 20}, { rx: 4, fill: c, strokeWidth: 0 });
          __dg.text(SVG, b.x+70, b.y-4, ['M','C','S'][i], { size: 14, weight: 700, color: '#fff', font: "'Inter', sans-serif" });
          // Card body
          __dg.rect(SVG, b, { rx: 4, fill: '#fff', stroke: c, strokeWidth: 2 });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 26, weight: 700, color: c, font: "'Inter', sans-serif" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 14, color: '#525258', font: "'Inter', sans-serif" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#525258', strokeWidth: 2 }));"""),
    (98,'blueprint-light','Blueprint Light',
     'Light grid on white, crisp engineering feel without dark blue.',
     'grid · engineering light',
     'background:#fff; background-image: linear-gradient(rgba(148,163,184,0.2) 1px, transparent 1px), linear-gradient(90deg, rgba(148,163,184,0.2) 1px, transparent 1px); background-size: 20px 20px;',
     """__dg.LAYOUT.forEach((b, i) => {
          __dg.rect(SVG, b, { fill: '#fff', stroke: '#4a00e0', strokeWidth: 1.5 });
          [[b.x,b.y],[b.x+b.w,b.y],[b.x,b.y+b.h],[b.x+b.w,b.y+b.h]].forEach(pt => {
            __dg.circle(SVG, pt[0], pt[1], 4, { fill: '#fff', stroke: '#4a00e0', strokeWidth: 1 });
          });
          __dg.text(SVG, b.x+b.w/2, b.y+66, b.title, { size: 24, weight: 500, color: '#1e293b', font: "'JetBrains Mono', monospace" });
          __dg.text(SVG, b.x+b.w/2, b.y+100, b.sub, { size: 12, color: '#64748b', font: "'JetBrains Mono', monospace" });
        });
        __dg.ARROWS.forEach(a => __dg.line(SVG, a.x1, a.y, a.x2, a.y, { stroke: '#4a00e0', strokeWidth: 1.2, dash: '3 3' }));"""),
    (99,'graph-paper','Graph Paper',
     'Fine grid on mint paper, engineering-student aesthetic.',
     'graph · mint',
     'background:#ecfdf5; background-image: linear-gradient(rgba(16,185,129,0.2) 1px, transparent 1px), linear-gradient(90deg, rgba(16,185,129,0.2) 1px, transparent 1px); background-size: 10px 10px;',
     """__dg.drawStandard(SVG, { rx: 0, fill: 'rgba(255,255,255,0.8)', stroke: '#059669', strokeWidth: 1.5, textColor: '#065f46', subColor: '#047857', titleSize: 26, titleWeight: 600, font: "'JetBrains Mono', monospace", arrowColor: '#065f46', arrowWidth: 1.5 });"""),
    (100,'clean-notebook','Clean Notebook',
     'Lined page with clean simple boxes, minimalist study.',
     'notebook · clean',
     'background:#fefcf3; background-image: repeating-linear-gradient(transparent 0 36px, rgba(168,162,158,0.25) 36px 37px);',
     """__dg.drawStandard(SVG, { rx: 8, fill: '#fff', stroke: '#a8a29e', strokeWidth: 1.2, textColor: '#1c1917', subColor: '#78716c', titleSize: 26, titleWeight: 500, font: "'Inter', sans-serif", arrowColor: '#57534e', arrowWidth: 1.5 });"""),
]

# Merge all
ALL_ENTRIES = []
# Rough (1-10)
for e in STYLES:
    ALL_ENTRIES.append(e)  # already has kind
# Custom (11-100)
for num_tup in DESIGNED + COLOR_VARS + SHAPE_VARS + ARTISTIC + PATTERNS + ERA + EFFECTS + SPECIAL:
    num, slug, name, desc, meta, bg, js = num_tup
    ALL_ENTRIES.append(('custom', slug, num, name, desc, meta, bg, js))

# Sort by number
ALL_ENTRIES.sort(key=lambda x: x[2])

# =============================================================================
# HTML GENERATION
# =============================================================================

def config_to_js(cfg):
    parts = []
    for k, v in cfg.items():
        if k == "fillFn":
            parts.append(f'    "{k}": {v}')
        elif k == "glow":
            parts.append(f'    "{k}": {"true" if v else "false"}')
        elif isinstance(v, str):
            parts.append(f'    "{k}": "{v}"')
        else:
            parts.append(f'    "{k}": {v}')
    return ",\n".join(parts)


HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Samuel Ochoa</title>
<meta name="description" content="Diagram style: {name}.">
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
  .solo-num { display:inline-flex; align-items:center; justify-content:center; width: 48px; height: 48px; border-radius: 50%; background: #4a00e0; color: #fff; font-weight: 700; font-size: 22px; }
  .solo-hero p.desc { font-size: 17px; line-height: 1.6; color: #525258; max-width: 760px; margin: 8px 0 0; }
  .solo-meta { font-family: 'JetBrains Mono', monospace; font-size: 12.5px; color: #8b8b93; margin-top: 8px; }
  .solo-stage { max-width: 1100px; margin: 28px auto; padding: 40px 20px 44px; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); }
  .solo-stage svg { display: block; width: 100%; height: auto; max-width: 960px; margin: 0 auto; }
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
  .picker-hero { max-width: 1200px; margin: 0 auto; padding: 48px 24px 16px; }
  .picker-hero h1 { font-size: clamp(32px, 4.5vw, 48px); font-weight: 800; letter-spacing: -0.03em; margin: 0 0 10px; }
  .picker-hero p.lede { font-size: 18px; line-height: 1.6; color: #525258; max-width: 800px; }
  .picker-section { max-width: 1200px; margin: 8px auto; padding: 0 24px; }
  .picker-section h2 { font-size: 20px; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; color: #4a00e0; margin: 48px 0 16px; }
  .picker-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(420px, 1fr)); gap: 20px; padding: 0 24px; max-width: 1200px; margin: 0 auto 40px; }
  .style-card { background: #ffffff; border: 1px solid #e5e5ea; border-radius: 14px; padding: 18px 20px 22px; transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease; }
  .style-card:hover { border-color: #c7b9ff; box-shadow: 0 10px 28px -8px rgba(74,0,224,0.15); transform: translateY(-2px); }
  .style-header { display:flex; align-items:baseline; gap: 10px; margin-bottom: 4px; flex-wrap: wrap; }
  .style-num { display:inline-flex; align-items:center; justify-content:center; width: 28px; height: 28px; border-radius: 50%; background: #4a00e0; color: #fff; font-weight: 700; font-size: 13px; flex-shrink: 0; }
  .style-name { font-size: 17px; font-weight: 700; color: #1d1d23; margin: 0; }
  .style-open { margin-left:auto; background: transparent; color: #4a00e0; padding: 4px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; text-decoration: none; border: 1px solid #4a00e0; }
  .style-open:hover { background: #4a00e0; color: #fff; }
  .style-desc { font-size: 13px; color: #525258; line-height: 1.5; margin: 4px 0 10px 38px; }
  .style-stage { margin-top: 4px; border-radius: 10px; overflow: hidden; padding: 10px 8px; }
  .style-stage svg { display: block; width: 100%; height: auto; }
  .style-meta { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #8b8b93; margin: 8px 0 0 38px; }
  .back-link { display: inline-block; padding: 8px 16px; background: #f1ecff; color: #4a00e0; border-radius: 8px; text-decoration: none; font-weight: 600; margin-bottom: 20px; }
</style>
</head>
<body>
<nav class="topbar"><div class="topbar-inner">
<a href="../index.html" class="logo"><img class="brand-logo" src="../logo.png" alt="Samuel Ochoa"></a>
<div class="nav-links"><a href="../index.html">Home</a></div>
</div></nav>
"""


def write_standalone(entry):
    kind = entry[0]
    if kind == 'rough':
        _, slug, num, name, desc, meta, bg, cfg = entry
        render_html = f"""
{SHARED_ROUGH}
<script>
window.__renderRough && window.__renderRough("stage", {{
{config_to_js(cfg)}
}});
</script>"""
    else:
        _, slug, num, name, desc, meta, bg, js = entry
        render_html = f"""
{HELPERS_JS}
<script>
(function(){{
  const SVG = document.getElementById('stage');
  if (!SVG) return;
{js}
}})();
</script>"""

    # prev/next
    prev_e = next_e = None
    for e in ALL_ENTRIES:
        if e[2] == num - 1: prev_e = e
        if e[2] == num + 1: next_e = e
    prev_link = f'<a href="{prev_e[2]:03d}-{prev_e[1]}.html">← {prev_e[3]}</a>' if prev_e else '<span></span>'
    next_link = f'<a href="{next_e[2]:03d}-{next_e[1]}.html">{next_e[3]} →</a>' if next_e else '<span></span>'

    body = f"""
<div class="solo-hero">
  <a href="index.html" class="back-link">← All 100 styles</a>
  <h1><span class="solo-num">{num}</span>{name}.</h1>
  <p class="desc">{desc}</p>
  <p class="solo-meta">{meta}</p>
</div>

<div class="solo-stage" style="{bg}">
  <svg id="stage" viewBox="0 0 920 320" preserveAspectRatio="xMidYMid meet"></svg>
</div>

<div class="solo-footer">{prev_link}{next_link}</div>

{render_html}

</body>
</html>
"""
    head = HEAD.format(title=f"Style {num}: {name}", name=name)
    (STYLES_DIR / f"{num:03d}-{slug}.html").write_text(head + STANDALONE_CSS + body, encoding="utf-8")


def write_index():
    # Group by section
    sections = [
        ("Hand-drawn (1–10)", list(range(1, 11))),
        ("Designed / professional (11–30)", list(range(11, 31))),
        ("Color & palette (31–40)", list(range(31, 41))),
        ("Shape variations (41–50)", list(range(41, 51))),
        ("Artistic rendering (51–60)", list(range(51, 61))),
        ("Pattern & texture (61–70)", list(range(61, 71))),
        ("Era & aesthetic (71–80)", list(range(71, 81))),
        ("Effects (81–90)", list(range(81, 91))),
        ("Utility & special (91–100)", list(range(91, 101))),
    ]

    by_num = {e[2]: e for e in ALL_ENTRIES}

    html_parts = []
    init_parts = []

    for section_name, nums in sections:
        html_parts.append(f'<div class="picker-section"><h2>{section_name}</h2></div>\n<div class="picker-grid">\n')
        for n in nums:
            if n not in by_num: continue
            e = by_num[n]
            kind = e[0]
            slug, num, name, desc, meta, bg = e[1], e[2], e[3], e[4], e[5], e[6]
            stage_id = f"idx{num}"

            card = f"""
<div class="style-card">
  <div class="style-header">
    <span class="style-num">{num}</span>
    <h3 class="style-name">{name}</h3>
    <a href="{num:03d}-{slug}.html" class="style-open">Full size</a>
  </div>
  <p class="style-desc">{desc}</p>
  <div class="style-meta">{meta}</div>
  <div class="style-stage" style="{bg}"><svg id="{stage_id}" viewBox="0 0 920 320"></svg></div>
</div>
"""
            html_parts.append(card)

            if kind == 'rough':
                init_parts.append(f'window.__renderRough && window.__renderRough("{stage_id}", {{\n{config_to_js(e[7])}\n}});')
            else:
                init_parts.append(f"""
(function(){{
  const SVG = document.getElementById('{stage_id}');
  if (!SVG) return;
{e[7]}
}})();
""")
        html_parts.append('</div>\n')

    body = f"""
<div class="picker-hero">
  <a href="../index.html" class="back-link">← Back home</a>
  <h1>Diagram style picker. 100 options.</h1>
  <p class="lede">Every card renders the same reference diagram (Model ↔ Client ↔ Server) in a different style. Click "Full size" on any card to see it on its own page. Browse by section, or scroll through all hundred.</p>
</div>

{"".join(html_parts)}

<footer><div class="container" style="max-width:1200px; padding:20px 24px 40px;">
<p>&copy; 2026 Samuel Ochoa. <a href="../index.html">Home</a> . <a href="../framework/index.html">Framework</a></p>
</div></footer>

{HELPERS_JS}
{SHARED_ROUGH}
<script>
{chr(10).join(init_parts)}
</script>

</body>
</html>
"""
    head = HEAD.format(title="Diagram style picker (100 styles)", name="all")
    (STYLES_DIR / "index.html").write_text(head + INDEX_CSS + body, encoding="utf-8")


# Remove old style files (keep directory)
for f in list(STYLES_DIR.glob("*.html")):
    f.unlink()
# Also remove old 2-digit files
for f in list(STYLES_DIR.glob("??-*.html")):
    if f.exists(): f.unlink()

# Generate
for entry in ALL_ENTRIES:
    write_standalone(entry)
    print(f"wrote {entry[2]:03d}-{entry[1]}.html")

write_index()
print("wrote index.html")
print(f"TOTAL: {len(ALL_ENTRIES)} styles")
