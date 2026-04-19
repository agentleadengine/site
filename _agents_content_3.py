#!/usr/bin/env python3
"""AI Agents expertise content part 3: Production + Patterns + Frameworks (16 pages)."""
from _build_agents import write_page


# ============================================================
# PRODUCTION (5 pages)
# ============================================================
write_page("prod/observability", "Observability + tracing",
    "Without tracing, agent bugs are invisible. Every production agent needs logs, spans, and replayable traces.",
    reading_time=3,
    body_html="""
<p class="lede">Agents fail in ways that traditional apps don't: non-deterministic reasoning, cascading tool errors, quality drift. Without comprehensive tracing, these failures are invisible until a customer complains. Observability isn't optional.</p>

<h2>What to log per session</h2>
<ul>
<li>User input (with identifiers)</li>
<li>System prompt version</li>
<li>Model version</li>
<li>Every LLM call: full input, full output, token counts, latency</li>
<li>Every tool call: name, args, result, latency, error (if any)</li>
<li>Memory reads/writes</li>
<li>Session cost accumulator</li>
<li>Final output</li>
<li>Termination reason (completed, budget hit, error, timeout)</li>
</ul>

<h2>Traces as debugging artifacts</h2>
<p>A trace is the replayable record of an agent session. Given a trace you should be able to:</p>
<ul>
<li>See the exact input/output of every LLM and tool call</li>
<li>Step through reasoning turn-by-turn</li>
<li>Spot where things went wrong</li>
<li>Reproduce the failure locally</li>
</ul>

<h2>Tools</h2>
<ul>
<li><strong>Langfuse</strong> — open-source LLM observability with tracing</li>
<li><strong>LangSmith</strong> — LangChain's hosted tracing</li>
<li><strong>Phoenix (Arize)</strong> — open-source, strong eval integration</li>
<li><strong>Weights &amp; Biases Weave</strong> — W&amp;B's tracing</li>
<li><strong>Helicone</strong> — LLM observability, focused on cost and latency</li>
<li><strong>OpenTelemetry</strong> — general distributed tracing, integrates with above</li>
</ul>

<h2>Sampling</h2>
<p>Full tracing at high QPS gets expensive. Sample:</p>
<ul>
<li>Trace 1-5% of normal requests</li>
<li>Trace 100% of errors</li>
<li>Trace 100% of requests that hit cost budget</li>
<li>Trace 100% of user-reported issues</li>
</ul>

<h2>Alerts</h2>
<p>Alert on:</p>
<ul>
<li>Error rate exceeding threshold</li>
<li>Average cost per session climbing</li>
<li>p99 latency regressing</li>
<li>Task completion rate dropping</li>
<li>Specific tools failing repeatedly</li>
</ul>

<h2>The feedback loop</h2>
<p>Observability feeds eval:</p>
<ol>
<li>Production trace reveals a failure</li>
<li>Turn the failing case into an eval case</li>
<li>Fix the issue</li>
<li>Verify fix in eval; add to regression suite</li>
</ol>
<p>Without this loop, the same bugs recur.</p>
""",
    prev=("Regression testing", "../eval/regression.html"),
    nxt=("Cost control", "cost-control.html"))


write_page("prod/cost-control", "Cost control",
    "Agents can burn through LLM credit fast. Here's how to keep costs bounded without killing quality.",
    reading_time=3,
    body_html="""
<p class="lede">Agents can rack up bills fast. A single runaway session can cost $10. A thousand users hitting the same problem can cost $10,000 in a day. Cost control is a first-class production concern, not an afterthought.</p>

<h2>Where the cost goes</h2>
<ul>
<li>LLM tokens in (context + user input)</li>
<li>LLM tokens out (reasoning + final output)</li>
<li>Tool call side-costs (paid APIs, compute)</li>
<li>Memory/vector DB storage and queries</li>
</ul>

<h2>Cost reduction strategies</h2>

<h3>Model routing</h3>
<p>Cheap model for simple tasks, expensive model for complex ones. Classify upfront or escalate mid-session.</p>

<h3>Prompt caching</h3>
<p>Claude and Gemini support caching the system prompt so it's not reprocessed each turn. Massive savings in multi-turn sessions.</p>

<h3>Context trimming</h3>
<p>Don't send 50K of history when the model needs 5K. Summarize aggressively.</p>

<h3>Tool output limits</h3>
<p>Cap each tool's response size. Huge tool outputs balloon the next LLM call.</p>

<h3>Budget per session</h3>
<p>Hard cap: "This session can't exceed $0.50." When reached, gracefully terminate.</p>

<h3>Caching expensive tool results</h3>
<p>Same search query = cached result. Same model inference on same prompt = cached.</p>

<h2>The budget stack</h2>
<ul>
<li>Per-request cost cap</li>
<li>Per-user daily cap</li>
<li>Per-tenant monthly cap</li>
<li>Global hourly rate limit</li>
</ul>
<p>Layered, so no single failure breaks the bank.</p>

<h2>Measuring cost per outcome</h2>
<p>Cost per resolved task, not cost per request. A task that takes 3 sessions to complete costs more than it looks.</p>

<h2>Cost alerts</h2>
<p>Alert when cost per task rises 20%+. Usually signals a regression (bad prompt, model downgrade, agent stuck in loops).</p>
""",
    prev=("Observability + tracing", "observability.html"),
    nxt=("Latency optimization", "latency.html"))


write_page("prod/latency", "Latency optimization",
    "Agent sessions can take 30+ seconds. Here's how to cut the lag without sacrificing quality.",
    reading_time=3,
    body_html="""
<p class="lede">A multi-step agent session can take 30-120 seconds. For async workflows this is fine. For user-facing agents, most users won't wait. Latency optimization is how you make agents feel responsive.</p>

<h2>Where latency goes</h2>
<ul>
<li>LLM inference (time to first token + full generation)</li>
<li>Tool execution (especially web-hitting tools)</li>
<li>Sequential LLM calls (each turn adds latency)</li>
<li>Context size (bigger context = slower inference)</li>
</ul>

<h2>Techniques</h2>

<h3>Streaming</h3>
<p>Stream the final output to the user so they see progress. 500ms to first token feels much faster than 10s to a complete response.</p>

<h3>Status updates</h3>
<p>Show the agent's current step to the user. "Searching..." "Thinking..." reassures they haven't hung.</p>

<h3>Parallel tool calls</h3>
<p>Covered on <a href="../tools/parallel-tools.html">parallel tool calls</a>. Cuts latency for independent operations.</p>

<h3>Smaller, faster model</h3>
<p>Route to Haiku or 4o-mini when the task doesn't need Sonnet or Opus.</p>

<h3>Prompt caching</h3>
<p>Reduces both cost and latency since cached tokens don't need reprocessing.</p>

<h3>Shorter context</h3>
<p>Bigger context = slower inference. Aggressive trimming helps.</p>

<h3>Async processing</h3>
<p>For non-interactive workflows, run agents in background. User gets notified when done.</p>

<h2>The latency budget</h2>
<ul>
<li>Real-time chat: under 5s total feels fast, 10s is tolerable</li>
<li>Form submit with agent processing: 5-15s okay with spinner</li>
<li>Async/batch: minutes to hours, no latency concern</li>
</ul>
<p>Choose the mode that fits your UX, not the other way around.</p>

<h2>The p99 problem</h2>
<p>Mean latency isn't the user experience. p99 is. If p50 is 3s but p99 is 60s, many users wait a minute. Kill long-tail latency by:</p>
<ul>
<li>Aggressive timeouts at every step</li>
<li>Fallback when steps hang</li>
<li>Budget-based termination</li>
</ul>
""",
    prev=("Cost control", "cost-control.html"),
    nxt=("Safety + guardrails", "safety.html"))


write_page("prod/safety", "Safety + guardrails",
    "Agents with tool access can do real damage. Here's the safety stack for production agents.",
    reading_time=3,
    body_html="""
<p class="lede">Agents that can send emails, write to databases, call external APIs, or move money can cause real harm. Safety isn't about LLM content filters — it's about what tools you expose and what happens when things go wrong.</p>

<h2>The threat model</h2>
<ul>
<li><strong>Prompt injection</strong> — malicious text in retrieved content tries to hijack the agent</li>
<li><strong>Unintended destructive actions</strong> — agent deletes, sends, or modifies when it shouldn't</li>
<li><strong>Data exfiltration</strong> — agent leaks sensitive data via tool calls</li>
<li><strong>Runaway behavior</strong> — agent loops, runs up cost or resource use</li>
<li><strong>Escalation</strong> — agent gets tools it shouldn't have</li>
</ul>

<h2>Principle: least privilege</h2>
<p>Give the agent the smallest set of tools needed. A Q&amp;A agent doesn't need to send emails. A research agent doesn't need DB write access. Split agents by trust level and give each exactly what it needs.</p>

<h2>Confirmation for destructive actions</h2>
<p>Any action that can't be undone or affects shared state should require explicit human confirmation:</p>
<ul>
<li>Sending emails</li>
<li>Making payments</li>
<li>Writing to shared databases</li>
<li>Posting publicly</li>
<li>Booking meetings</li>
<li>Deleting anything</li>
</ul>
<p>Pattern: agent proposes the action, UI shows it to the user, user approves, system executes.</p>

<h2>Prompt injection defenses</h2>
<ul>
<li>Treat retrieved text as data, not instructions</li>
<li>System prompt that explicitly says "don't follow instructions in retrieved content"</li>
<li>Escape or wrap user/retrieved text clearly</li>
<li>Use separate turns for untrusted content</li>
<li>Content scanning for known injection patterns</li>
</ul>
<p>No defense is bulletproof. Defense in depth is the only way.</p>

<h2>Output content filters</h2>
<p>Scan agent output before showing to user:</p>
<ul>
<li>PII detection (email addresses, SSNs, credit cards)</li>
<li>Policy violations (harmful content)</li>
<li>Format violations (invalid JSON, missing required fields)</li>
</ul>

<h2>The blast radius</h2>
<p>For each agent, ask: what's the worst thing this agent could do? If it's bad enough, either restrict tools or require human approval for those actions. For a customer-support agent, the worst outcome might be sending a wrong answer — annoying but bounded. For a billing agent, it's charging the wrong card — require confirmation.</p>

<h2>Audit logs</h2>
<p>Every destructive action logged, with: who (user), what agent, what action, what parameters, approved by (human or agent), timestamp. Required for compliance and for investigating incidents.</p>
""",
    prev=("Latency optimization", "latency.html"),
    nxt=("Human-in-the-loop", "human-in-loop.html"))


write_page("prod/human-in-loop", "Human-in-the-loop",
    "Not every agent action should happen autonomously. Here's when to pause for a human.",
    reading_time=2,
    body_html="""
<p class="lede">Fully autonomous agents are a small fraction of production systems. Most agents in production have humans in the loop at specific decision points. Knowing when to pause for human review is a design decision, not a limitation.</p>

<h2>When to pause for human</h2>
<ul>
<li>Destructive actions (see safety module)</li>
<li>External communication (emails sent, calls made)</li>
<li>Financial transactions</li>
<li>Low-confidence agent responses</li>
<li>Escalations from tools that detect issues</li>
<li>Compliance-flagged content</li>
</ul>

<h2>The interaction model</h2>

<h3>Pre-action approval</h3>
<p>Agent proposes action. Human sees it, approves or edits. Then it executes.</p>

<h3>Post-action review</h3>
<p>Agent takes action. Human reviews later. For less-critical actions where speed matters.</p>

<h3>Async handoff</h3>
<p>Agent pauses task, surfaces to human queue. Human resumes with annotations. Agent continues.</p>

<h2>Queue management</h2>
<p>If agent actions exceed human review capacity, queue builds up and UX degrades. Either:</p>
<ul>
<li>Automate more (tolerate more autonomy)</li>
<li>Hire more reviewers</li>
<li>Reduce agent throughput</li>
<li>Tier the queue (urgent vs routine)</li>
</ul>

<h2>The confidence threshold</h2>
<p>Agent can estimate its own confidence. Route high-confidence actions through automatically; queue low-confidence for review. Over time, track which actions were approved vs changed — calibrate the threshold.</p>

<h2>Agent proposing vs executing</h2>
<p>Strong pattern: agent always proposes, human clicks to execute. Keeps human as the actor of record. Lowers liability and improves trust.</p>
""",
    prev=("Safety + guardrails", "safety.html"),
    nxt=("Research agent", "../patterns/research-agent.html"))


# ============================================================
# PATTERNS (6 pages)
# ============================================================
write_page("patterns/research-agent", "Research agent",
    "A research agent does web research, synthesizes findings, and produces structured reports. Here's the pattern.",
    reading_time=3,
    body_html="""
<p class="lede">A research agent takes a question, searches the web (and internal sources), reads results, synthesizes a structured answer with citations. Useful for competitive intelligence, market research, due diligence, fact-finding.</p>

<h2>The loop</h2>
<ol>
<li>Decompose the question into sub-queries</li>
<li>Search for each sub-query</li>
<li>Read top results</li>
<li>Extract relevant claims with source links</li>
<li>Identify gaps; iterate with more searches if needed</li>
<li>Synthesize final answer with citations</li>
</ol>

<h2>Core tools</h2>
<ul>
<li><code>web_search(query)</code> — public web search</li>
<li><code>read_url(url)</code> — fetch and parse a page</li>
<li><code>search_internal(query)</code> — internal knowledge base</li>
<li><code>summarize(text, focus)</code> — distill relevant info</li>
</ul>

<h2>Design choices</h2>

<h3>Breadth vs depth</h3>
<p>Breadth: more queries, shallower read per result. Depth: fewer queries, full-article read per source. Research tasks usually need both in sequence.</p>

<h3>Source diversity</h3>
<p>Don't summarize from one source. Require multiple corroborating sources for key claims.</p>

<h3>Citation quality</h3>
<p>Every factual claim should link to the specific source. Without citations, hallucinations creep in.</p>

<h2>Failure modes</h2>
<ul>
<li>Research keeps going, never produces final output (budget hits first)</li>
<li>Summarizes from a single source without cross-checking</li>
<li>Cites sources that don't actually support the claim</li>
<li>Misses a key perspective (no counter-search)</li>
</ul>

<h2>Production tools</h2>
<p>Frameworks: Manus, OpenDevin (code research), Claude with web search, custom pipelines built on LangGraph. Commercial: Perplexity, Consensus, Elicit.</p>
""",
    prev=("Human-in-the-loop", "../prod/human-in-loop.html"),
    nxt=("Coding agent", "coding-agent.html"))


write_page("patterns/coding-agent", "Coding agent",
    "Coding agents write, modify, and test code. Claude Code, Cursor, Devin — the shape of modern software development.",
    reading_time=3,
    body_html="""
<p class="lede">Coding agents write code, run it, read errors, fix, iterate. The test suite is the verifier; the error trace is the feedback. Claude Code, Cursor, and tools like Devin are built on this pattern.</p>

<h2>The loop</h2>
<ol>
<li>Read the task</li>
<li>Explore the codebase (read files, search)</li>
<li>Plan changes</li>
<li>Write code</li>
<li>Run tests</li>
<li>Read errors if any</li>
<li>Fix and iterate until passing</li>
<li>Submit changes</li>
</ol>

<h2>Core tools</h2>
<ul>
<li><code>read_file(path)</code></li>
<li><code>write_file(path, contents)</code></li>
<li><code>run_command(cmd)</code> — for tests, build, linters</li>
<li><code>search_code(query)</code></li>
<li><code>list_files(dir)</code></li>
</ul>

<h2>Why this works</h2>
<p>Code has a natural verifier: compilers, test suites, linters. When the agent writes bad code, the feedback is unambiguous. The LLM uses the error message to plan the fix. Few domains have this tight feedback loop — it's why coding agents are ahead of other verticals.</p>

<h2>Context management</h2>
<p>Codebases are too big to fit in context. Agent must:</p>
<ul>
<li>Navigate via search and directory listings</li>
<li>Pull only relevant files into context</li>
<li>Keep track of file paths and recent edits</li>
</ul>

<h2>Testing matters</h2>
<p>Agent quality tracks test suite quality. Without tests, agent has no feedback. Encourage users to have good tests before deploying a coding agent.</p>

<h2>Safety</h2>
<p>Coding agents can do damage. Guardrails:</p>
<ul>
<li>Run in sandboxed environment</li>
<li>Restrict filesystem access</li>
<li>Require human approval for git push, deploy</li>
<li>Don't give access to production secrets</li>
</ul>

<h2>Tools in the ecosystem</h2>
<ul>
<li>Claude Code — CLI-based coding agent</li>
<li>Cursor / Windsurf — IDE-integrated</li>
<li>Cognition Devin — more autonomous, session-based</li>
<li>GitHub Copilot Workspace — task-level agent</li>
<li>Aider, Continue, Cline — open-source variants</li>
</ul>
""",
    prev=("Research agent", "research-agent.html"),
    nxt=("Customer support agent", "customer-support.html"))


write_page("patterns/customer-support", "Customer support agent",
    "Customer support agents handle user questions, reference knowledge bases, escalate when needed. Here's the pattern.",
    reading_time=3,
    body_html="""
<p class="lede">Customer support agents field user questions, retrieve relevant articles, answer with citations, escalate when the question is outside scope. Simple concept; many failure modes in production.</p>

<h2>The flow</h2>
<ol>
<li>User asks question</li>
<li>Agent retrieves relevant KB articles</li>
<li>Agent answers with citations</li>
<li>If question is out of scope: escalate to human</li>
<li>If question contains PII or policy content: apply guardrails</li>
<li>Log for review</li>
</ol>

<h2>Core tools</h2>
<ul>
<li><code>search_kb(query)</code> — the main retrieval tool</li>
<li><code>get_user_context(user_id)</code> — user history, plan, tickets</li>
<li><code>create_ticket(summary, priority)</code> — escalation</li>
<li><code>send_reply(user_id, text)</code> — actually respond</li>
</ul>

<h2>Key design choices</h2>

<h3>Retrieval quality is everything</h3>
<p>See the RAG section of the site. Bad retrieval = agent has no good context = bad answers. Invest in hybrid retrieval, reranking, and eval.</p>

<h3>Escalation must be fast and clean</h3>
<p>When agent can't answer, don't fake competence. Escalate with all context preserved so the human doesn't start from zero.</p>

<h3>Personalization with caution</h3>
<p>Pulling user context helps answers but leaks can embarrass. Never cross user boundaries. Audit carefully.</p>

<h3>Guardrails</h3>
<ul>
<li>Don't promise refunds, discounts, or policy exceptions</li>
<li>Don't acknowledge or deny account specifics you can't verify</li>
<li>Escalate legal, threat, or abuse situations</li>
</ul>

<h2>Measurement</h2>
<ul>
<li>Deflection rate (tickets handled without escalation)</li>
<li>Customer satisfaction on agent responses</li>
<li>Accuracy (did the answer match the right KB article?)</li>
<li>Escalation rate</li>
<li>False positive escalations (should have handled)</li>
</ul>

<h2>The trap: too eager to answer</h2>
<p>Agent should say "I don't know — let me get a human" more readily than "here's my best guess." In support, confident wrong answers are worse than acknowledged gaps.</p>
""",
    prev=("Coding agent", "coding-agent.html"),
    nxt=("Data analyst agent", "data-analyst.html"))


write_page("patterns/data-analyst", "Data analyst agent",
    "Data analyst agents query databases, analyze data, produce reports. Text-to-SQL plus reasoning.",
    reading_time=3,
    body_html="""
<p class="lede">A data analyst agent answers questions by querying databases, running analyses, and producing reports. The core skill: translating natural language questions into SQL (or similar), then interpreting results.</p>

<h2>The loop</h2>
<ol>
<li>User asks a question</li>
<li>Agent understands the data schema (via tool)</li>
<li>Agent writes SQL</li>
<li>Executes, gets results</li>
<li>Interprets results</li>
<li>May write more queries for follow-ups</li>
<li>Synthesizes final answer with visualizations or tables</li>
</ol>

<h2>Core tools</h2>
<ul>
<li><code>list_tables()</code></li>
<li><code>describe_table(table)</code></li>
<li><code>run_query(sql)</code></li>
<li><code>create_chart(data, type)</code></li>
<li><code>explain_plan(sql)</code> — for expensive queries</li>
</ul>

<h2>Why schema context matters</h2>
<p>LLM can't write correct SQL without knowing table structure. Schema must be in context or discoverable via tools. For large schemas, this is a RAG problem over your DB metadata.</p>

<h2>Safety</h2>
<ul>
<li>Read-only database access (usually)</li>
<li>Query timeouts (agent doesn't crash the DB)</li>
<li>Row-level security on the DB side (the agent sees only what the user should)</li>
<li>Cost caps on long-running queries</li>
</ul>

<h2>Interpretation quality</h2>
<p>Numbers without interpretation aren't useful. Agent should:</p>
<ul>
<li>State findings in natural language</li>
<li>Point out surprising numbers</li>
<li>Flag data quality issues (missing, inconsistent)</li>
<li>Offer follow-up analyses</li>
</ul>

<h2>When to visualize</h2>
<p>Charts for trends, distributions, comparisons. Tables for exact numbers, specific records. Agent picks based on the question.</p>

<h2>Common failure modes</h2>
<ul>
<li>Writes SQL that runs but answers wrong question</li>
<li>Misinterprets query results (confuses counts with sums)</li>
<li>Doesn't notice join mistakes</li>
<li>Confidently answers from bad data</li>
</ul>

<p>Mitigation: test queries on small samples, sanity-check totals, flag anomalies.</p>
""",
    prev=("Customer support agent", "customer-support.html"),
    nxt=("Browser agent", "browser-agent.html"))


write_page("patterns/browser-agent", "Browser agent",
    "Browser agents navigate web pages, click, type, extract data. Powerful, slow, hard to make reliable.",
    reading_time=3,
    body_html="""
<p class="lede">A browser agent drives a real browser: navigates URLs, clicks, types, scrolls, reads rendered content. Useful for tasks sites don't expose via APIs. Powerful. Slow. Fragile.</p>

<h2>Use cases</h2>
<ul>
<li>Scraping data from sites without APIs</li>
<li>Filling out forms</li>
<li>Booking appointments, reservations</li>
<li>Research requiring dynamic content</li>
<li>Testing web applications</li>
</ul>

<h2>Tooling</h2>
<ul>
<li><strong>Playwright / Puppeteer</strong> — headless browser automation</li>
<li><strong>Claude Computer Use</strong> — Anthropic's vision-based browser control</li>
<li><strong>OpenAI Operator</strong> — operator model with browser</li>
<li><strong>browser-use, Skyvern, Browserbase</strong> — higher-level frameworks</li>
</ul>

<h2>Vision vs DOM</h2>
<p>Two control paradigms:</p>
<ul>
<li><strong>Vision</strong>: screenshot the page, let vision LLM decide where to click by pixel. Flexible, slow.</li>
<li><strong>DOM</strong>: extract accessibility tree or DOM, agent works with structured elements. Faster, more fragile if page is dynamic.</li>
</ul>
<p>Hybrid systems use both.</p>

<h2>Challenges</h2>

<h3>Page reliability</h3>
<p>Modern sites are SPAs with async loading, anti-bot protections, captchas. Agents break often.</p>

<h3>Latency</h3>
<p>Each click takes seconds. Agent sessions measured in minutes, not seconds.</p>

<h3>Cost</h3>
<p>Vision LLM calls on screenshots are expensive. Heavy context.</p>

<h3>Authentication</h3>
<p>Logged-in scenarios need credential handling. Big security surface.</p>

<h2>When to use</h2>
<ul>
<li>No API exists for the site</li>
<li>Task is high-value enough to justify latency and cost</li>
<li>You have a sandboxed environment to run the browser</li>
</ul>

<h2>When to skip</h2>
<ul>
<li>API exists (always prefer API)</li>
<li>Task is frequent and needs low latency</li>
<li>Target site has strong anti-automation</li>
</ul>
""",
    prev=("Data analyst agent", "data-analyst.html"),
    nxt=("Email agent", "email-agent.html"))


write_page("patterns/email-agent", "Email agent",
    "Email agents triage, draft, send, and schedule email. High-value, high-risk: email actions are mostly irreversible.",
    reading_time=3,
    body_html="""
<p class="lede">Email agents read incoming messages, classify them, draft replies, schedule follow-ups. They save hours per week for people with heavy email load. They also have high blast radius: sent emails can't be unsent.</p>

<h2>Common patterns</h2>

<h3>Triage agent</h3>
<p>Classifies every incoming email: urgent, can wait, archive, auto-reply. Doesn't send; just sorts.</p>

<h3>Draft agent</h3>
<p>Proposes replies to emails. Human reviews and sends.</p>

<h3>Auto-reply agent</h3>
<p>For well-defined inbound (FAQ questions, standard vendor requests), actually sends without human review.</p>

<h3>Scheduling agent</h3>
<p>Negotiates meeting times on your behalf across email threads.</p>

<h2>Core tools</h2>
<ul>
<li><code>list_inbox()</code></li>
<li><code>read_email(id)</code></li>
<li><code>search_past_emails(query)</code></li>
<li><code>draft_reply(id, text)</code></li>
<li><code>send_email(draft_id)</code> — usually requires human confirmation</li>
<li><code>schedule_send(draft_id, time)</code></li>
<li><code>create_calendar_event(...)</code></li>
</ul>

<h2>Safety is paramount</h2>
<p>Sent emails are irreversible and can go to the wrong person, contain wrong info, or violate privacy. Safety guardrails:</p>
<ul>
<li>Human approval for every send (draft-first workflow)</li>
<li>Per-contact allowlists for auto-send</li>
<li>Redaction of PII before sending drafts to LLM</li>
<li>Review queue for anything unusual</li>
<li>Daily summary of agent-sent emails for user review</li>
</ul>

<h2>Prompt injection risk</h2>
<p>Email bodies can contain injection attempts. A hostile email could try to manipulate the agent into sending, deleting, or forwarding. Defense:</p>
<ul>
<li>Treat all email content as untrusted data</li>
<li>System prompt explicitly rejects instructions from email bodies</li>
<li>Extra guardrails on tools that can send or delete</li>
</ul>

<h2>Tone matching</h2>
<p>Replies should sound like the user. Train on past sent emails (with permission) for voice. Review samples to ensure the agent isn't drifting into generic voice.</p>
""",
    prev=("Browser agent", "browser-agent.html"),
    nxt=("Claude Agent SDK", "../frameworks/claude-agent-sdk.html"))


# ============================================================
# FRAMEWORKS (5 pages)
# ============================================================
write_page("frameworks/claude-agent-sdk", "Claude Agent SDK",
    "Anthropic's SDK for building agents on Claude. Here's what it does, when to use it.",
    reading_time=3,
    body_html="""
<p class="lede">The Claude Agent SDK is Anthropic's opinionated framework for building agents that use Claude. Built on the same primitives as Claude Code, it handles tool use, multi-turn orchestration, and sub-agents.</p>

<h2>What it provides</h2>
<ul>
<li>Tool-use loop orchestration</li>
<li>Structured tool definitions via TypeScript/Python</li>
<li>Sub-agent spawning and delegation</li>
<li>Built-in support for MCP tool servers</li>
<li>File system, shell, and web tools out of the box</li>
<li>Streaming output</li>
</ul>

<h2>When to use</h2>
<ul>
<li>Building on Claude</li>
<li>Want opinions on how to structure agents (not a DIY framework)</li>
<li>Need MCP integration</li>
<li>Want close behavior parity with how Claude Code works</li>
</ul>

<h2>When it's not the right fit</h2>
<ul>
<li>Multi-model (GPT, Gemini in the same system) — use LangGraph or CrewAI</li>
<li>Highly custom orchestration logic — build your own on raw API</li>
<li>Research settings where you want control over every step</li>
</ul>

<h2>Relationship to Claude Code</h2>
<p>Claude Code is the end-user CLI. The Agent SDK is the library you'd use to build your own agents with similar capabilities. Think of Claude Code as an agent built with the SDK.</p>

<h2>MCP integration</h2>
<p>Model Context Protocol is Anthropic's standard for tool servers. The Agent SDK natively supports MCP servers, so you can plug in community-built tool providers without writing glue code.</p>

<h2>Getting started</h2>
<p>See docs at anthropic.com. Typical starter: npm/pip install the SDK, define tools, define system prompt, launch agent loop. Most production agents fit in a few hundred lines of code.</p>
""",
    prev=("Email agent", "../patterns/email-agent.html"),
    nxt=("LangGraph", "langgraph.html"))


write_page("frameworks/langgraph", "LangGraph",
    "LangChain's graph-based agent framework. Explicit control flow, multi-agent support.",
    reading_time=3,
    body_html="""
<p class="lede">LangGraph is LangChain's successor framework for building stateful, multi-actor LLM applications. You define agent logic as a directed graph: nodes are steps (LLM calls, tool calls, logic), edges route based on state. More explicit than chain-style frameworks.</p>

<h2>Why graph-based</h2>
<p>LangChain's older chain-based approach couldn't easily express branching, loops, and multi-agent coordination. LangGraph solves this: explicit nodes and edges with conditional transitions.</p>

<h2>What it provides</h2>
<ul>
<li>State machines for agent workflows</li>
<li>Built-in multi-agent patterns</li>
<li>Checkpointing (save/resume agent state)</li>
<li>Human-in-the-loop support</li>
<li>Streaming</li>
<li>Strong observability via LangSmith</li>
</ul>

<h2>When to use</h2>
<ul>
<li>Complex agent workflows with branching logic</li>
<li>Multi-agent systems</li>
<li>Long-running agents that need to pause/resume</li>
<li>Teams already using LangChain</li>
</ul>

<h2>When it's overkill</h2>
<ul>
<li>Simple ReAct loops (raw API + small wrapper is cleaner)</li>
<li>Small projects that don't need the abstraction</li>
<li>Teams uncomfortable with the LangChain ecosystem's complexity</li>
</ul>

<h2>Criticism</h2>
<p>LangChain has a reputation for abstraction overhead. LangGraph addresses some of this but retains some of the complexity. Evaluate against raw API approaches before adopting.</p>
""",
    prev=("Claude Agent SDK", "claude-agent-sdk.html"),
    nxt=("CrewAI", "crewai.html"))


write_page("frameworks/crewai", "CrewAI",
    "CrewAI is a multi-agent orchestration framework. Define agents by role, give them tasks, they collaborate.",
    reading_time=2,
    body_html="""
<p class="lede">CrewAI is a popular framework for multi-agent systems. You define a "crew" of agents, each with a role, tools, and backstory. You give them a task. They collaborate to solve it.</p>

<h2>Core concepts</h2>
<ul>
<li><strong>Agent</strong> — a role with goals, backstory, and tools</li>
<li><strong>Task</strong> — a unit of work assigned to agents</li>
<li><strong>Crew</strong> — a group of agents working together</li>
<li><strong>Process</strong> — how tasks are executed (sequential, hierarchical)</li>
</ul>

<h2>When CrewAI shines</h2>
<ul>
<li>Prototyping multi-agent systems fast</li>
<li>Role-based agent teams (researcher + writer + reviewer)</li>
<li>Tasks that benefit from specialization</li>
</ul>

<h2>When it doesn't</h2>
<ul>
<li>Single-agent tasks (overhead without benefit)</li>
<li>Production systems needing tight control over cost and latency</li>
<li>When the role-playing metaphor doesn't fit your problem</li>
</ul>

<h2>The role metaphor</h2>
<p>CrewAI's central idea is treating agents as characters with backstories. This can help the LLM produce more in-character outputs, but can also add cost (longer prompts) without clear benefit. Measure impact on your use case.</p>

<h2>Production considerations</h2>
<ul>
<li>Observability is less mature than LangGraph</li>
<li>Cost can be high with many agents spawned per task</li>
<li>Good for prototypes; evaluate carefully for production at scale</li>
</ul>
""",
    prev=("LangGraph", "langgraph.html"),
    nxt=("AutoGen", "autogen.html"))


write_page("frameworks/autogen", "AutoGen",
    "Microsoft's multi-agent framework. Conversational agents that talk to each other.",
    reading_time=2,
    body_html="""
<p class="lede">AutoGen is Microsoft's multi-agent framework, centered on agents that communicate via chat. Define agents, they send messages to each other, problems get solved through conversation. Research-flavored but increasingly production-ready.</p>

<h2>Core concepts</h2>
<ul>
<li><strong>ConversableAgent</strong> — agents that can send and receive messages</li>
<li><strong>UserProxyAgent</strong> — agent that can execute code and call tools on behalf of the conversation</li>
<li><strong>GroupChat</strong> — multiple agents in a shared chat with a designated manager</li>
</ul>

<h2>Strengths</h2>
<ul>
<li>Elegant for problems that fit the "agents talking" metaphor</li>
<li>Strong code execution support</li>
<li>Built-in patterns for various multi-agent shapes</li>
<li>Good for research and experimentation</li>
</ul>

<h2>Weaknesses</h2>
<ul>
<li>Steeper learning curve than CrewAI</li>
<li>Chat-message paradigm can be inefficient for simple workflows</li>
<li>Less opinionated than some alternatives</li>
</ul>

<h2>When to pick AutoGen</h2>
<ul>
<li>Research settings exploring multi-agent interaction</li>
<li>Problems genuinely structured as agent-to-agent conversation</li>
<li>Teams with Python + Microsoft tooling fit</li>
</ul>

<h2>AutoGen Studio</h2>
<p>Microsoft offers AutoGen Studio, a UI for building and debugging agent configurations. Useful for non-programmers building agent workflows.</p>
""",
    prev=("CrewAI", "crewai.html"),
    nxt=("Picking a framework", "picking.html"))


write_page("frameworks/picking", "Picking a framework",
    "Too many agent frameworks. Here's how to decide.",
    reading_time=3,
    body_html="""
<p class="lede">There are a dozen agent frameworks and the list grows monthly. Instead of comparing feature matrices, use this decision tree.</p>

<h2>Decision tree</h2>

<h3>Do you need a framework at all?</h3>
<p>For a simple ReAct agent with 3-5 tools, raw LLM API + a short Python loop might be simplest. A framework adds abstraction that may be more complexity than value for simple agents.</p>

<p>Start without a framework. Adopt one when you hit real pain that the framework solves.</p>

<h3>Are you all-in on Claude?</h3>
<p>Yes → Claude Agent SDK. Strong MCP integration, behavior parity with Claude Code, Anthropic-native.</p>

<h3>Do you need multi-model flexibility?</h3>
<p>Yes → LangGraph. Most provider-agnostic and has mature tooling.</p>

<h3>Is your problem explicitly multi-agent?</h3>
<p>Yes, role-based agents → CrewAI (simpler) or AutoGen (more flexible)<br>
Yes, graph-based flow → LangGraph</p>

<h3>Are you prototyping vs shipping?</h3>
<p>Prototyping → CrewAI or a simple direct-API approach<br>
Shipping to production → LangGraph, Claude Agent SDK, or your own framework on raw API</p>

<h3>What's your team's existing stack?</h3>
<p>Already deep in LangChain → LangGraph (natural evolution)<br>
Python data science team → AutoGen fits well<br>
Greenfield → Claude Agent SDK or DIY</p>

<h2>The recommendation I actually make</h2>
<p>For 80% of production use cases: start with Claude Agent SDK if you're on Claude, or raw OpenAI/Anthropic API with your own small orchestrator. Add a framework only when you hit limits.</p>

<p>LangGraph is the most "production-ready" of the established frameworks for multi-model use.</p>

<p>CrewAI is the fastest way to prototype multi-agent ideas.</p>

<h2>The "don't lock in" rule</h2>
<p>Build your agent logic behind your own interface so you can swap frameworks later. Frameworks change, models change, patterns change. The business logic you own. Abstract the framework.</p>
""",
    prev=("AutoGen", "autogen.html"),
    nxt=None)

print("\n✓ Agents content part 3: 16 pages. AI Agents COMPLETE (45 pages)")
