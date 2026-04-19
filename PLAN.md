# samuelochoa.com — 50-Page Site Plan

**Purpose:** personal brand site anchored by a deep, evergreen knowledge base on **AI autonomy** — Claude, MCPs, plugins, Claude Code, agent patterns, and going fully autonomous. The content repo is the *credibility engine*. Personal brand pages are the "who's the author" layer on top.

**Positioning:** "Samuel Ochoa — AI researcher who writes the handbook on autonomous AI."

**Shape:** static HTML, no build step. Each page self-contained (HTML + inline CSS OR shared stylesheet).

---

## 1. Total page count: 50

| Section | Pages | Purpose |
|---|---|---|
| Personal brand | 8 | Who Samuel is, what he does, how to reach him |
| Framework hub + foundations | 4 | Intro to the autonomy framework |
| Claude + foundation models | 4 | How the model layer works |
| MCP (Model Context Protocol) | 8 | The core of autonomy |
| Plugins | 3 | Extension layer |
| Claude Code (the harness) | 6 | Where most agents run |
| Agent patterns | 6 | Architectures and design |
| Going autonomous | 5 | Headless, scheduling, safety |
| Practical build guides | 4 | First-agent step-by-step |
| Tools + ecosystem | 2 | Adjacent tech |
| **Total** | **50** | |

---

## 2. Site tree

```
samuelochoa.com/
├── index.html                              (1)  Home / hero
├── about.html                              (2)  Longer bio
├── work.html                               (3)  3 pillars of what he does
├── background.html                         (4)  Education + career snapshot
├── now.html                                (5)  What he's focused on this quarter
├── uses.html                               (6)  Personal stack (credibility shorthand)
├── writing.html                            (7)  Index of essays / framework entry point
├── contact.html                            (8)  Contact + LinkedIn
│
├── framework/
│   ├── index.html                          (9)  Framework hub — the "start here" page
│   ├── what-is-autonomous-ai.html         (10)  Foundations: definitions
│   ├── the-autonomy-spectrum.html         (11)  Chatbot → Assistant → Agent → Autonomous
│   ├── glossary.html                      (12)  Every term explained in plain English
│   │
│   ├── claude/
│   │   ├── overview.html                  (13)  What Claude is and why it matters for agents
│   │   ├── prompting-for-agents.html      (14)  Prompting patterns specifically for agentic work
│   │   ├── extended-thinking.html         (15)  Reasoning budgets, tradeoffs, when to use
│   │   └── tool-use.html                  (16)  Tool use mechanics, JSON schemas, errors
│   │
│   ├── mcp/
│   │   ├── index.html                     (17)  MCP section hub
│   │   ├── what-is-mcp.html               (18)  The elevator pitch for MCP
│   │   ├── anatomy.html                   (19)  Tools, resources, prompts, servers, clients
│   │   ├── transports.html                (20)  stdio, SSE, HTTP — when to use each
│   │   ├── servers.html                   (21)  Building your own MCP server
│   │   ├── clients.html                   (22)  Clients that speak MCP (Claude Code, Claude.ai, IDEs, etc.)
│   │   ├── security.html                  (23)  Permissions, sandboxing, prompt injection defense
│   │   └── directory.html                 (24)  Curated MCPs worth trying (with categories)
│   │
│   ├── plugins/
│   │   ├── index.html                     (25)  Plugins section hub
│   │   ├── vs-mcp.html                    (26)  Plugins vs MCPs — what's the difference
│   │   └── marketplace.html               (27)  Official + community plugin marketplaces
│   │
│   ├── claude-code/
│   │   ├── index.html                     (28)  What Claude Code is and why it's the right harness
│   │   ├── settings.html                  (29)  settings.json — the whole config model
│   │   ├── permissions.html               (30)  Allow/deny lists, auto mode, skip-permission
│   │   ├── hooks.html                     (31)  Hooks: automating on events
│   │   ├── skills.html                    (32)  What skills are and how to write one
│   │   └── memory.html                    (33)  The persistent memory system
│   │
│   ├── patterns/
│   │   ├── index.html                     (34)  Agent pattern hub
│   │   ├── react-loop.html                (35)  ReAct: reason → act → observe
│   │   ├── plan-execute.html              (36)  Plan-then-execute agents
│   │   ├── multi-agent.html               (37)  Sub-agents, delegation, orchestration
│   │   ├── evaluation.html                (38)  How to actually test an agent
│   │   └── prompt-caching.html            (39)  Prompt caching, cost + latency wins
│   │
│   ├── autonomous/
│   │   ├── index.html                     (40)  "Fully autonomous" — what it means
│   │   ├── headless.html                  (41)  Headless mode (Claude Code running without a human)
│   │   ├── scheduling.html                (42)  Crons, triggers, event-driven agents
│   │   ├── self-monitoring.html           (43)  Agents watching themselves
│   │   └── safety.html                    (44)  Boundaries, guardrails, kill-switches
│   │
│   ├── build/
│   │   ├── index.html                     (45)  Build-guides hub
│   │   ├── first-agent.html               (46)  Your first autonomous agent in 60 minutes
│   │   ├── voice-agent.html               (47)  Building a voice agent
│   │   └── research-agent.html            (48)  Building a research agent
│   │
│   └── tools/
│       ├── browser-automation.html        (49)  Controlling browsers autonomously
│       └── desktop-control.html           (50)  Controlling the desktop / native apps
```

---

## 3. Page-by-page content brief

### Personal brand (1–8)

1. **index.html** — current single-page hero transformed into a landing: name, tagline, "what I work on" 3-card preview, latest-writing strip, LinkedIn CTA. Links to `about` and `framework`.
2. **about.html** — longer bio: origin story, why AI autonomy, current obsessions, personal beliefs about shipping AI.
3. **work.html** — expanded "what I do": applied products, LLM integration, advisory. Each with 2–3 paragraphs (no client names).
4. **background.html** — education, career snapshot, skills matrix, languages/tools.
5. **now.html** — "What I'm focused on *this quarter*." Classic personal-site /now page. Living doc, updated monthly.
6. **uses.html** — his daily stack: hardware, software, shell, editor, AI tools, note-taking, etc. Credibility-by-proxy.
7. **writing.html** — index of essays + the framework. Entry point to everything under `/framework/`.
8. **contact.html** — LinkedIn, availability for advisory, "how to reach me" with expectations.

### Framework foundations (9–12)

9. **framework/index.html** — the hub. Explains the whole framework, links to every section, says "start here."
10. **framework/what-is-autonomous-ai.html** — definition: "Autonomous AI = model + tools + harness + permissions + loop." Breaks down each piece.
11. **framework/the-autonomy-spectrum.html** — 5 levels: (1) Chatbot, (2) Assistant, (3) Agent with human-in-the-loop, (4) Agent with auto mode, (5) Fully autonomous (scheduled, headless). Visual spectrum.
12. **framework/glossary.html** — alphabetical glossary: Agent, Auto Mode, Claude Code, Context Window, Extended Thinking, Harness, Hook, LLM, MCP, Memory, Plugin, Prompt Caching, ReAct, Skill, Tool Use, etc. 40+ terms.

### Claude / foundation models (13–16)

13. **framework/claude/overview.html** — what Claude is, the Claude families (Opus/Sonnet/Haiku), context windows, pricing tiers, how it compares to GPT/Gemini for agents. Vendor-neutral-ish.
14. **framework/claude/prompting-for-agents.html** — prompting patterns for agentic work: XML tags, reasoning scaffolds, output format constraints, error-recovery instructions, anti-patterns.
15. **framework/claude/extended-thinking.html** — what extended thinking is, when the reasoning budget pays off, when it's overkill, observable patterns.
16. **framework/claude/tool-use.html** — tool-use mechanics: JSON schemas, parallel tool calls, error messages, retry logic, multi-turn tool loops.

### MCP section (17–24)

17. **framework/mcp/index.html** — MCP hub. What's in this section, why MCP matters, reading order.
18. **framework/mcp/what-is-mcp.html** — plain-English pitch: MCP is the USB-C port of AI — a standard for connecting tools to models. Who built it, who uses it, what it replaces.
19. **framework/mcp/anatomy.html** — the 5 primitives: Tools (functions), Resources (data), Prompts (templates), Servers (providers), Clients (consumers). Diagrams for each.
20. **framework/mcp/transports.html** — stdio (local subprocess), SSE (streaming over HTTP), HTTP (request/response). Decision matrix: when to use each.
21. **framework/mcp/servers.html** — how to build an MCP server. TypeScript + Python examples (pseudocode, conceptual). Lifecycle: initialize, list tools, call tool, shutdown.
22. **framework/mcp/clients.html** — what "MCP client" means; list the major ones (Claude Code, Claude.ai, IDEs, third-party agent frameworks). How to configure one.
23. **framework/mcp/security.html** — the real security model: tool approvals, sandboxing, trust boundaries, prompt injection through tool outputs, audit logging, deny-by-default patterns.
24. **framework/mcp/directory.html** — curated MCPs organized by category: productivity (Notion, Gmail, Calendar), dev tools (GitHub, Linear), design (Figma, Canva), voice (phone/SMS), browser (claude-in-chrome), desktop (computer-use), finance, CRM, etc. One-line description per entry.

### Plugins (25–27)

25. **framework/plugins/index.html** — what plugins are in the context of AI agents. How they differ from MCPs. When to use each.
26. **framework/plugins/vs-mcp.html** — deeper comparison: scope, packaging, install path, distribution model. Table + decision tree.
27. **framework/plugins/marketplace.html** — official plugin marketplaces (Anthropic, community). How to install, vet, publish.

### Claude Code harness (28–33)

28. **framework/claude-code/index.html** — what Claude Code is, why it's the canonical harness for autonomous agents (vs raw API, vs other frameworks). Install + first run.
29. **framework/claude-code/settings.html** — deep dive on settings.json: permissions, default mode, environment, hooks, plugins, every key explained.
30. **framework/claude-code/permissions.html** — allow lists, deny lists, auto mode, skipAutoPermissionPrompt. How to design a permission model for autonomous work.
31. **framework/claude-code/hooks.html** — hooks trigger on events: tool-pre, tool-post, session-start, session-end, prompt-submit, etc. Use cases + examples.
32. **framework/claude-code/skills.html** — what Skills are (named slash-command invokable bundles of instructions). Anatomy of a skill. How to write your own. Examples.
33. **framework/claude-code/memory.html** — the persistent memory system: structure (`~/.claude/...`), types of memories (user, feedback, project, reference), retention patterns, pitfalls.

### Agent patterns (34–39)

34. **framework/patterns/index.html** — hub: 5 patterns every agent builder should know. When to pick which.
35. **framework/patterns/react-loop.html** — ReAct: reason → act → observe → loop. The default agent pattern. Strengths, failure modes.
36. **framework/patterns/plan-execute.html** — plan-then-execute: generate a plan, approve, then run. Better for long tasks, worse for adaptive ones.
37. **framework/patterns/multi-agent.html** — sub-agents, delegation, orchestrator-worker, peer-to-peer. Context isolation benefits. When it backfires.
38. **framework/patterns/evaluation.html** — how to actually test an agent. Eval harnesses, regression tests, offline vs live eval, human feedback loops.
39. **framework/patterns/prompt-caching.html** — prompt caching: what it is, how to structure prompts to maximize cache hits, cost savings math, latency wins.

### Going autonomous (40–44)

40. **framework/autonomous/index.html** — "fully autonomous" defined. The autonomy stack (model + tools + harness + scheduler + safety). When autonomy is worth it.
41. **framework/autonomous/headless.html** — running Claude Code without a human terminal. stdin/stdout patterns, CI/CD integrations, background tasks.
42. **framework/autonomous/scheduling.html** — crons, triggers, event queues. How to run agents on a schedule or on an event. Recurring work vs one-shot.
43. **framework/autonomous/self-monitoring.html** — agents that watch themselves: health checks, self-reported metrics, anomaly detection, auto-restart.
44. **framework/autonomous/safety.html** — the safety model: permission scopes, kill switches, escape hatches, approval workflows for risky actions, audit logs, "never do X" guardrails.

### Practical build guides (45–48)

45. **framework/build/index.html** — hub. List of buildable agents with difficulty ratings.
46. **framework/build/first-agent.html** — "your first autonomous agent in 60 minutes." Install Claude Code, configure one MCP, write a skill, run it headless. Fully walkthrough.
47. **framework/build/voice-agent.html** — building a voice agent: STT → LLM → TTS pipeline, routing, state machines.
48. **framework/build/research-agent.html** — research agent: web search + content extraction + synthesis + report. Multi-step reasoning, fact-checking.

### Tools (49–50)

49. **framework/tools/browser-automation.html** — controlling a browser autonomously. Chrome-extension-based (Claude-in-Chrome pattern), Playwright/Puppeteer, DOM-awareness vs pixel-based.
50. **framework/tools/desktop-control.html** — controlling the OS / native apps. Computer-use APIs, screen reasoning, click-and-type patterns, per-app permission tiers.

---

## 4. Shared components (built once, used everywhere)

- **Top nav** — sticky header with sections: Home · About · Framework · Writing · Contact
- **Framework sidebar** — on any `/framework/*` page, a left-rail sidebar listing all sections + current-page indicator
- **Breadcrumbs** — on framework pages: `Home › Framework › MCP › What is MCP`
- **Prev/Next** — bottom of every framework article, linking to the next logical read
- **Footer** — same on every page, LinkedIn, © line, maybe RSS
- **Related articles** — bottom of each article, 2–4 links to related pages
- **Callout boxes** — styled blockquotes for "key insight," "warning," "example code"
- **Code blocks** — monospace, syntax-aware styling (no JS needed, just CSS on `<code>`)
- **Reading time** — "6 min read" at top of each article
- **Last updated** — "Updated 2026-04-18" date on every article

---

## 5. Content style rules

### Hard no-mentions (privacy-critical)
- **NO mention of Agent Lead Engine** — ever, anywhere on the site.
- **NO mention of Yardi** (current employer) — not even in "currently at…" framing.
- **NO mention that Samuel is actively running a business** — someone at Yardi may visit the site. Avoid present-tense phrasing like "I run…" "I'm building…" "my team." Always past-tense or interest-framed.

### Safe positioning language
- "AI researcher"
- "Writer on autonomous AI"
- "Serial entrepreneur" (generic, no companies named, no present-tense)
- "Past founder"
- "Independent AI researcher"
- "I've built / advised / shipped…" (past tense OK)
- "I write about…" / "I study…" / "I research…" (present tense OK — these are intellectual activities, not businesses)

### Unsafe phrasing (avoid)
- "I run…" / "currently running" / "I'm building"
- "My business" / "my team" / "we're hiring"
- "Founder @ [anything]" / "CEO of…"
- Any language that says or implies he has a side business while employed

### Voice + style
- **Vendor-neutral where possible** — "Claude is one option, GPT and Gemini work similarly" — but written with Claude-first depth since that's what I know.
- **Concrete over abstract** — always include code snippets, screenshots (placeholders), or concrete examples.
- **First-person essay voice** on personal pages. **Third-person clear exposition** on framework pages (more authoritative).
- **No hype** — if a technique is overrated, say so. Credibility comes from honest assessments.
- **Every framework page answers 1 question in the URL slug** — if you can't reduce the page to one question, it's two pages.
- **Length target per framework page**: 800–1500 words. Enough to be authoritative, short enough to scan.

---

## 6. Navigation model

### Top-level nav (on every page)
- Home
- Framework (dropdown: Foundations / Claude / MCP / Plugins / Claude Code / Patterns / Autonomous / Build / Tools)
- Writing
- About
- Contact

### Framework sidebar structure
```
Foundations
  What is autonomous AI
  The autonomy spectrum
  Glossary

Claude
  Overview
  Prompting for agents
  Extended thinking
  Tool use

MCP
  What is MCP
  Anatomy
  Transports
  Servers
  Clients
  Security
  Directory

Plugins
  Overview
  Plugins vs MCP
  Marketplace

Claude Code
  Overview
  Settings
  Permissions
  Hooks
  Skills
  Memory

Patterns
  ReAct loop
  Plan-execute
  Multi-agent
  Evaluation
  Prompt caching

Autonomous
  What is fully autonomous
  Headless
  Scheduling
  Self-monitoring
  Safety

Build Guides
  First agent in 60 min
  Voice agent
  Research agent

Tools
  Browser automation
  Desktop control
```

---

## 7. SEO + discoverability

- **Unique `<title>` and `<meta description>` per page** — targeted keywords without stuffing
- **Open Graph + Twitter cards** on every page (uses existing color scheme for the image)
- **Schema.org `Article` markup** on every framework page
- **Schema.org `Person` on about.html** (already done on index)
- **Canonical URLs** to prevent dupe content
- **Sitemap.xml** — auto-generated list of all 50 URLs for search engines
- **robots.txt** — standard, crawl-friendly
- **RSS feed** for /writing/ if we add ongoing essays later

---

## 8. Design system (decisions to make)

Most of these I'll defer to the design-change pass you mentioned, but seeding defaults:
- Colors: purple (`#6200FF` + `#8B5CF6`) matches ALE, plus greys for body
- Fonts: Inter for UI/body, Instrument Serif italic for tasteful emphasis, JetBrains Mono for code
- Layout: 860px max width on personal pages, 720px + sidebar on framework pages
- Spacing: generous (Medium-ish feel)
- Reading-first: big line-height, comfortable font size (17–18px)
- Dark mode: maybe v2

---

## 9. Build strategy (how we'll actually make 50 pages)

1. **Shared stylesheet** — create `/styles.css` once, import on every page.
2. **Template** — one HTML skeleton used across all framework pages (header, sidebar, content slot, prev/next, footer).
3. **Personal pages first** — 8 pages, starting from the existing index.html as base.
4. **Framework hub + foundations next** — the entry points and definitions people land on.
5. **MCP section next** — heaviest content because it's the core of the framework.
6. **Claude Code next** — our own harness, most opinionated section.
7. **Patterns, Autonomous, Build, Tools** — round out.
8. **Polish pass** — cross-link, fix typos, verify nav consistency.
9. **Sitemap + RSS last** — once all URLs are stable.

Estimated wall-clock: 2–3 focused sessions.

---

## 10. What I'd flag before building

- **Some content crosses into Anthropic's official docs territory.** We should be additive (opinions, patterns, honest assessments) not duplicative. "Here's what the docs don't tell you" framing.
- **"Plugins" terminology is ambiguous** — need to settle on what "plugin" means in the AI-agent context vs Chrome extension or WordPress plugin. Clarified in plugins/index.html.
- **MCP and Claude Code are moving targets** — docs will need updates as features evolve. Keep "Last updated" dates honest.
- **We should not publish author names of specific third-party MCPs** in the directory without checking licensing / attribution norms.
- **Code snippets** should be pseudocode or minimal — we're positioning as a framework/concept site, not a code cookbook. If folks want working code, link to the official docs.

---

## 11. Next steps (waiting on you)

1. Approve this page map (or suggest adds/cuts)
2. Lock color/typography/design direction
3. Then we build

Once approved, I'll:
- Extract shared styles into `styles.css`
- Create the HTML template
- Build pages in the order above
- Cross-link as we go
- Ship a working 50-page site in this folder
