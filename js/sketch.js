/*
 * sketch.js — Blueprint × Purple Marker on Cream diagram library.
 *
 * Usage inside any HTML page:
 *
 *   <div class="sketch" data-viewbox="0 0 920 340">
 *     <svg></svg>
 *   </div>
 *   <script>
 *   document.addEventListener('sketch:ready', () => {
 *     const svg = document.querySelector('.sketch svg');
 *     const rc  = sketch.rc(svg);
 *     sketch.box(svg, rc, { x: 40,  y: 90, w: 240, h: 140, title: 'Model',  sub: '(Claude)' });
 *     sketch.box(svg, rc, { x: 340, y: 90, w: 240, h: 140, title: 'Client', sub: '(Claude Code)' });
 *     sketch.box(svg, rc, { x: 640, y: 90, w: 240, h: 140, title: 'Server', sub: '(Gmail MCP)' });
 *     sketch.arrow(svg, rc, { x1: 280, x2: 340, y: 160, label: 'MCP' });
 *     sketch.arrow(svg, rc, { x1: 580, x2: 640, y: 160, label: 'MCP' });
 *   });
 *   </script>
 *
 * The library auto-sets viewBox from the wrapper's data-viewbox attribute,
 * loads rough.js from CDN, and fires `sketch:ready` on document once both
 * are available. Every diagram on every page uses the same visual grammar.
 */
(function() {
  // Inject sketch-wrapper CSS on load so diagrams look right even if the
  // page's main stylesheet is cached, outdated, or fails to load.
  (function injectCss() {
    if (document.getElementById('sketch-css')) return;
    const css = '' +
      '.sketch{position:relative;margin:36px auto;max-width:940px;padding:28px 20px;' +
        'border-radius:18px;background:#faf7f2;' +
        'background-image:linear-gradient(rgba(74,0,224,0.08) 1px, transparent 1px),' +
        'linear-gradient(90deg, rgba(74,0,224,0.08) 1px, transparent 1px);' +
        'background-size:24px 24px;box-shadow:0 4px 20px rgba(0,0,0,0.04);' +
        'box-sizing:border-box;}' +
      '.sketch svg{display:block;width:100%;height:auto;max-width:960px;margin:0 auto;}' +
      '.sketch svg text{fill:#1d1d23;}' +
      '.sketch-caption{text-align:center;font-family:\'Caveat\',\'Kalam\',cursive;' +
        'color:#8b5cf6;font-size:20px;font-weight:700;margin-top:8px;' +
        'letter-spacing:0.02em;}';
    const s = document.createElement('style');
    s.id = 'sketch-css';
    s.textContent = css;
    (document.head || document.documentElement).appendChild(s);
  })();

  const NS = 'http://www.w3.org/2000/svg';
  const COLORS = {
    stroke:     '#4a00e0',
    strokeSoft: '#8b5cf6',
    fill:       '#f1ecff',
    text:       '#4a00e0',
    sub:        '#6b21a8',
    dim:        '#8b5cf6',
    page:       '#faf7f2'
  };

  // ---- Low-level helpers -------------------------------------------------
  function el(tag, attrs) {
    const e = document.createElementNS(NS, tag);
    for (const k in (attrs || {})) e.setAttribute(k, attrs[k]);
    return e;
  }
  function text(svg, x, y, s, opts) {
    opts = opts || {};
    const t = el('text', {
      x, y,
      'text-anchor': opts.anchor || 'middle',
      fill: opts.color || COLORS.text,
      'font-size': opts.size || 20,
      'font-weight': opts.weight || 400,
      'font-family': opts.font || "'Kalam', cursive"
    });
    if (opts.style) t.setAttribute('font-style', opts.style);
    if (opts.transform) t.setAttribute('transform', opts.transform);
    t.textContent = s;
    svg.appendChild(t);
    return t;
  }

  // ---- Crosshair corner marks (blueprint touch) --------------------------
  function crosshair(svg, x, y, color) {
    svg.appendChild(el('circle', {
      cx: x, cy: y, r: 4,
      fill: COLORS.page,
      stroke: color || COLORS.stroke,
      'stroke-width': 1.5
    }));
  }

  // ---- The boxed node (hand-drawn + corner crosshairs + dim label) ------
  function box(svg, rc, b) {
    // Hand-drawn rectangle with lavender fill
    svg.appendChild(rc.rectangle(b.x, b.y, b.w, b.h, {
      roughness: 1.8,
      stroke: b.strokeColor || COLORS.stroke,
      strokeWidth: 2.5,
      fill: b.fillColor || COLORS.fill,
      fillStyle: 'solid'
    }));
    // Corner crosshairs
    [[b.x, b.y], [b.x+b.w, b.y], [b.x, b.y+b.h], [b.x+b.w, b.y+b.h]].forEach(pt => {
      crosshair(svg, pt[0], pt[1], b.strokeColor);
    });
    // Title + subtitle (handwritten)
    if (b.title) {
      text(svg, b.x + b.w/2, b.y + (b.titleY || 68), b.title, {
        size: b.titleSize || 30, weight: 700, color: b.textColor || COLORS.text
      });
    }
    if (b.sub) {
      text(svg, b.x + b.w/2, b.y + (b.subY || 102), b.sub, {
        size: b.subSize || 20, weight: 400, color: b.subColor || COLORS.sub
      });
    }
    // Optional mono dimension label below
    if (b.dim) {
      text(svg, b.x + b.w/2, b.y + b.h + 26, b.dim, {
        size: 11, color: COLORS.dim, font: "'JetBrains Mono', monospace"
      });
    }
  }

  // ---- Circle node (for cases where a box doesn't fit the idea) ---------
  function circle(svg, rc, c) {
    svg.appendChild(rc.circle(c.cx, c.cy, (c.r || 60) * 2, {
      roughness: 1.8,
      stroke: c.strokeColor || COLORS.stroke,
      strokeWidth: 2.5,
      fill: c.fillColor || COLORS.fill,
      fillStyle: 'solid'
    }));
    if (c.title) text(svg, c.cx, c.cy - 2, c.title, { size: 24, weight: 700, color: COLORS.text });
    if (c.sub)   text(svg, c.cx, c.cy + 24, c.sub,   { size: 15, weight: 400, color: COLORS.sub });
  }

  // ---- Arrow between two points (horizontal by default) -----------------
  function arrow(svg, rc, a) {
    // Hand-drawn line
    svg.appendChild(rc.line(a.x1, a.y1 != null ? a.y1 : a.y, a.x2, a.y2 != null ? a.y2 : a.y, {
      roughness: 1.8, stroke: a.color || COLORS.stroke, strokeWidth: 2.5
    }));
    // Arrowhead on the destination side
    const y2 = a.y2 != null ? a.y2 : a.y;
    const y1 = a.y1 != null ? a.y1 : a.y;
    // Simple right-pointing arrowhead
    svg.appendChild(rc.polygon(
      [[a.x2-14, y2-8], [a.x2, y2], [a.x2-14, y2+8]],
      { roughness: 1.4, stroke: a.color || COLORS.stroke, strokeWidth: 2,
        fill: a.color || COLORS.stroke, fillStyle: 'solid' }
    ));
    // Opposite arrowhead if bidirectional
    if (a.bidirectional !== false) {
      svg.appendChild(rc.polygon(
        [[a.x1+14, y1-8], [a.x1, y1], [a.x1+14, y1+8]],
        { roughness: 1.4, stroke: a.color || COLORS.stroke, strokeWidth: 2,
          fill: a.color || COLORS.stroke, fillStyle: 'solid' }
      ));
    }
    // Small handwritten label over the arrow
    if (a.label) {
      const mx = (a.x1 + a.x2) / 2;
      const my = ((y1 + y2) / 2) - 14;
      text(svg, mx, my, a.label, {
        size: 16, color: COLORS.strokeSoft, weight: 700
      });
    }
  }

  // ---- Freehand scribble label (annotation) -----------------------------
  function note(svg, x, y, s, opts) {
    opts = opts || {};
    return text(svg, x, y, s, Object.assign({
      size: 18, color: COLORS.strokeSoft, weight: 700
    }, opts));
  }

  // ---- rough.js convenience ---------------------------------------------
  function rc(svg) {
    if (!window.rough) throw new Error('rough.js not loaded yet');
    return rough.svg(svg);
  }

  // ---- Auto-setup on DOM load -------------------------------------------
  function setupWrappers() {
    document.querySelectorAll('.sketch').forEach(wrap => {
      let svg = wrap.querySelector('svg');
      if (!svg) {
        svg = el('svg');
        wrap.appendChild(svg);
      }
      const vb = wrap.dataset.viewbox || '0 0 920 340';
      svg.setAttribute('viewBox', vb);
      svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
      svg.setAttribute('class', 'sketch-svg');
    });
  }

  function loadRough(cb) {
    if (window.rough) return cb();
    const s = document.createElement('script');
    s.src = 'https://unpkg.com/roughjs@4.6.6/bundled/rough.js';
    s.onload = cb;
    document.head.appendChild(s);
  }

  function ready() {
    setupWrappers();
    loadRough(() => {
      document.dispatchEvent(new Event('sketch:ready'));
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ready);
  } else {
    ready();
  }

  // Expose API
  window.sketch = {
    COLORS, el, text, crosshair, box, circle, arrow, note, rc
  };
})();
