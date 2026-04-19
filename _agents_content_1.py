#!/usr/bin/env python3
"""AI Agents expertise content part 1: Foundations + Loops + Tools (15 pages)."""
from _build_agents import write_page

# ============================================================
# HUB
# ============================================================
write_page("index", "AI Agents",
    "A 45-page reference on building production AI agents: loops, tools, memory, multi-agent systems, evaluation, and patterns.",
    reading_time=3,
    body_html="""
<p class="lede">An AI agent is an LLM in a loop with tools. That's the simple definition. The complex part is everything that makes it work in production: reasoning patterns, tool design, memory systems, evaluation, safety, and the dozen subtle decisions that separate a demo from a system that holds up under real traffic.</p>

<p>This section is 45 pages on building agents that work. From ReAct loops to multi-agent orchestration, from tool design to production observability. The goal: give you the mental models and specific patterns you need to build something real.</p>

<h2>The nine sections</h2>

<div class="cards" style="margin-top:32px;">
<a href="foundations/what-is-an-agent.html" class="card"><h3>Foundations</h3><p>What agents are, when to use them, the architecture map.</p></a>
<a href="loops/react.html" class="card"><h3>Loops + Reasoning</h3><p>ReAct, planning, reflection, self-correction.</p></a>
<a href="tools/tool-design.html" class="card"><h3>Tools + Actions</h3><p>Tool design, descriptions, error handling, budgets.</p></a>
<a href="memory/short-term.html" class="card"><h3>Memory</h3><p>Short-term, long-term, episodic, procedural.</p></a>
<a href="multi/orchestrator-worker.html" class="card"><h3>Multi-agent</h3><p>Orchestration patterns, handoffs, debate.</p></a>
<a href="eval/why-eval-agents.html" class="card"><h3>Evaluation</h3><p>Task completion, trajectory eval, regression testing.</p></a>
<a href="prod/observability.html" class="card"><h3>Production</h3><p>Observability, cost, latency, safety, human-in-loop.</p></a>
<a href="patterns/research-agent.html" class="card"><h3>Patterns</h3><p>Research, coding, support, data, browser, email agents.</p></a>
<a href="frameworks/claude-agent-sdk.html" class="card"><h3>Frameworks</h3><p>Claude Agent SDK, LangGraph, CrewAI, AutoGen.</p></a>
</div>

<h2 style="margin-top:40px;">How to read this</h2>
<p>Start at <a href="foundations/what-is-an-agent.html">Foundations</a>. If you already know what agents are, jump to <a href="loops/react.html">Loops</a> then <a href="tools/tool-design.html">Tools</a>. <a href="eval/why-eval-agents.html">Evaluation</a> and <a href="prod/observability.html">Production</a> are where naive agents fall apart at scale.</p>
""",
    prev=None, nxt=("What is an AI agent?", "foundations/what-is-an-agent.html"))


# ============================================================
# FOUNDATIONS (4 pages)
# ============================================================
write_page("foundations/what-is-an-agent", "What is an AI agent?",
    "An AI agent is an LLM in a loop with tools. Here's what that actually means and why it's different from an LLM call.",
    reading_time=4,
    body_html="""
<p class="lede">The simplest definition: an AI agent is an LLM in a loop with tools. It gets a goal. It thinks. It picks a tool. It uses the tool. It thinks again based on what the tool returned. It repeats until the goal is done. That's it.</p>

<h2>The three components</h2>
<ol>
<li><strong>The LLM</strong> — the reasoning engine. Takes context, decides what to do next.</li>
<li><strong>Tools</strong> — functions the LLM can call. Search the web, query a database, send an email, run code.</li>
<li><strong>The loop</strong> — orchestration that runs until the task is complete or a stop condition fires.</li>
</ol>

<h2>Why this is different from a normal LLM call</h2>
<p>A normal LLM call: prompt in, answer out. One shot. The LLM does what it can with the context it has.</p>
<p>An agent: prompt in, but the LLM can reach out for information, take actions, and incorporate results before responding. It can decide "I don't know this — let me search," execute the search, read the results, and respond. The agent can take many reasoning and action steps, not just one.</p>

<h2>The spectrum of autonomy</h2>
<ul>
<li><strong>Prompt + single tool</strong> — minimal agent behavior, one tool call per request</li>
<li><strong>ReAct-style loops</strong> — multi-step reasoning and tool use until answer is reached</li>
<li><strong>Planning agents</strong> — form a plan first, then execute steps</li>
<li><strong>Multi-agent systems</strong> — multiple specialized agents coordinating</li>
<li><strong>Fully autonomous</strong> — agents with long-running tasks, self-correction, persistent memory</li>
</ul>

<p>Most production agents sit in the middle: structured loops with bounded autonomy.</p>

<h2>What agents enable</h2>
<ul>
<li>Tasks that require information the model doesn't have (RAG, search, tool use)</li>
<li>Multi-step workflows where each step depends on prior results</li>
<li>Tasks requiring real-world actions (sending emails, writing files, booking meetings)</li>
<li>Longer-running work that needs planning and checkpoints</li>
</ul>

<h2>What agents don't magically fix</h2>
<ul>
<li>Bad prompts — agents amplify prompt quality, they don't replace it</li>
<li>Bad tools — agents can only do what tools allow</li>
<li>Bad reasoning — if the base model reasons poorly, loops don't help</li>
<li>Bad data — garbage inputs produce garbage agent traces</li>
</ul>
""",
    prev=("Overview", "../index.html"), nxt=("Agent vs workflow", "agent-vs-workflow.html"))


write_page("foundations/agent-vs-workflow", "Agent vs workflow",
    "Not every AI system needs agentic behavior. Here's how to choose between a deterministic workflow and an agent.",
    reading_time=4,
    body_html="""
<p class="lede">Many projects that use "agents" don't need them. A deterministic workflow — a fixed sequence of LLM calls and function calls — is simpler, more reliable, and usually cheaper. The question isn't "should I use AI" but "should this be agentic."</p>

<h2>When a workflow is enough</h2>
<p>A workflow is a known sequence of steps. "Extract entities, then summarize, then categorize, then send notification." The steps don't change based on results. An LLM runs each step, but flow is hardcoded.</p>

<p>Workflows win when:</p>
<ul>
<li>The task steps are predictable</li>
<li>You can hand-author the flow once</li>
<li>Latency and cost matter</li>
<li>Reliability matters more than flexibility</li>
</ul>

<h2>When an agent is needed</h2>
<p>Agents win when the flow depends on what the agent discovers. Research, exploratory debugging, customer support that can branch into many directions, tasks where the "right next step" depends on what you just learned.</p>

<p>Agents win when:</p>
<ul>
<li>Steps are unknown in advance</li>
<li>The right sequence depends on intermediate results</li>
<li>The task requires exploration or decision-making</li>
<li>Tool selection matters</li>
</ul>

<h2>The pragmatic middle</h2>
<p>Most production systems are workflows with agent steps embedded. A workflow orchestrates the pipeline; at specific junctures, an agent handles bounded exploration.</p>
<p>Example: a deterministic email ingestion pipeline calls an agent to classify and act on "complex" emails that don't match known categories. Workflow + agent hybrid.</p>

<h2>Anti-pattern: everything as agent</h2>
<p>Wrapping deterministic logic in an agent adds cost, latency, and failure modes without benefit. If your agent's "reasoning" is always "call tool X, then call tool Y, then respond" — you have a workflow, just an expensive one.</p>

<h2>Test: can you draw the flowchart?</h2>
<p>If the steps and their order are fixed and you can draw the flowchart in advance: workflow. If the flowchart has decision points the LLM must make at runtime based on information it doesn't have yet: agent.</p>
""",
    prev=("What is an AI agent?", "what-is-an-agent.html"),
    nxt=("When not to use agents", "when-not-to-use.html"))


write_page("foundations/when-not-to-use", "When not to use agents",
    "Agents add cost, latency, and failure modes. Here are the cases where a workflow, a single LLM call, or no AI at all wins.",
    reading_time=3,
    body_html="""
<p class="lede">Agents get overused because they're exciting to build. But for many tasks they're worse on every metric: cost, latency, reliability, debuggability. Here are the cases where you should skip the agent.</p>

<h2>When the task is deterministic</h2>
<p>"Parse this document, extract these five fields, insert into database." Not an agent problem. A single LLM call, or even a traditional parser, is faster and more reliable.</p>

<h2>When latency matters</h2>
<p>Agent loops can take 10-60 seconds. For real-time applications, agents are too slow. Pre-compute, cache, or use a single-turn LLM with sufficient context.</p>

<h2>When cost matters</h2>
<p>Every tool call is additional LLM tokens. Agent sessions often run 5-10x the tokens of single-turn. At scale, this dominates your bill.</p>

<h2>When you need determinism</h2>
<p>Regulated workflows, auditable decisions, legal outputs. An agent's non-determinism (different reasoning each run) is a feature for exploration but a liability for compliance.</p>

<h2>When the task is narrow and well-defined</h2>
<p>A function call works. "Given this weather data, tell me if I should bring a jacket." The LLM gets the data in the prompt; no agent needed.</p>

<h2>When the tools are unreliable</h2>
<p>Agents amplify tool failures. If your database is flaky, your agent will encounter failures mid-task, and recovery patterns are hard. Fix infrastructure before adding agents.</p>

<h2>When the team can't debug agents</h2>
<p>Agent traces are complex. Without observability tooling and the discipline to review them, agents fail silently in production. If your team can't commit to observability, don't ship an agent.</p>

<h2>When the problem is ill-defined</h2>
<p>"Help me with marketing." Agents don't help with ambiguous tasks better than humans asking clarifying questions. Fix the spec before building the tool.</p>
""",
    prev=("Agent vs workflow", "agent-vs-workflow.html"),
    nxt=("Architecture map", "architecture.html"))


write_page("foundations/architecture", "The agent architecture map",
    "Every production agent has the same core components. Here's the map, from prompt to final response.",
    reading_time=5,
    body_html="""
<p class="lede">An agent looks simple in a slide: LLM, tools, loop. In production, it's a stack of components you need to design and operate. Here's the map.</p>

<h2>The layers</h2>
<ol>
<li><strong>User interface</strong> — where the agent's invoked (chat, API, CLI, batch)</li>
<li><strong>Input processing</strong> — validation, authentication, session state</li>
<li><strong>Prompt assembly</strong> — system prompt, user prompt, context, memory</li>
<li><strong>LLM inference</strong> — the reasoning model call</li>
<li><strong>Tool registry</strong> — the functions the LLM can call, with descriptions</li>
<li><strong>Tool execution</strong> — calling the tool, handling errors, timeouts</li>
<li><strong>Memory</strong> — short-term (session), long-term (persistent facts)</li>
<li><strong>Orchestration</strong> — the loop that drives reasoning until a stop condition</li>
<li><strong>Safety + guardrails</strong> — prompt injection defenses, content filters, rate limits</li>
<li><strong>Observability</strong> — tracing every step for debugging and eval</li>
<li><strong>Cost + latency control</strong> — budgets, timeouts, caching</li>
<li><strong>Output formatting</strong> — structured output, streaming, finalizing response</li>
</ol>

<h2>The flow</h2>
<ol>
<li>User input arrives</li>
<li>System builds context: system prompt + user prompt + relevant memory</li>
<li>Agent calls LLM with context and available tools</li>
<li>LLM responds: either a final answer or a tool call request</li>
<li>If tool call: orchestrator executes, captures result, adds to context</li>
<li>Loop continues until final answer or max steps</li>
<li>Final response formatted and returned</li>
<li>Session state persisted</li>
<li>Trace logged for observability</li>
</ol>

<h2>Where things break</h2>
<ul>
<li><strong>Prompt assembly</strong> — context too long, too short, stale memory</li>
<li><strong>Tool descriptions</strong> — LLM calls wrong tools with wrong args</li>
<li><strong>Tool execution</strong> — slow APIs, rate limits, error responses</li>
<li><strong>Infinite loops</strong> — agent keeps trying, never reaches stop</li>
<li><strong>Hallucination in tool args</strong> — LLM invents parameter values</li>
<li><strong>Runaway cost</strong> — long sessions, no budget enforcement</li>
</ul>

<h2>The minimum viable production agent</h2>
<ul>
<li>System prompt with clear goal + tool instructions</li>
<li>3-8 well-described tools</li>
<li>ReAct-style loop with max 10-20 steps</li>
<li>Structured output schema</li>
<li>Tracing (every LLM call + tool call logged)</li>
<li>Cost budget per session</li>
<li>Timeout per session</li>
<li>Error handling on every tool</li>
<li>Eval set of at least 30 test cases</li>
</ul>

<p>Missing any of these and your agent will fail in production. Not immediately — silently, over time, in ways that are hard to diagnose without the missing piece.</p>
""",
    prev=("When not to use agents", "when-not-to-use.html"),
    nxt=("ReAct", "../loops/react.html"))


# ============================================================
# LOOPS + REASONING (5 pages)
# ============================================================
write_page("loops/react", "ReAct",
    "ReAct (Reasoning + Acting) is the foundational agent pattern. Here's how it works and why most modern agents are a variation.",
    reading_time=4,
    body_html="""
<p class="lede">ReAct (Reasoning + Acting) is the foundational agent loop introduced in 2022. At each step, the agent reasons out loud about what to do next, takes an action (calls a tool), observes the result, then reasons again. Nearly every modern agent uses some variant.</p>

<h2>The loop</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
Thought: I need to find X. I'll search for it.
Action: web_search(query="X")
Observation: [search results]
Thought: Based on the results, I need to...
Action: [next tool call]
Observation: [result]
...
Thought: I have enough. Final answer: ...
</pre>

<h2>Why reasoning out loud helps</h2>
<p>Having the LLM write its reasoning explicitly before each action improves quality for complex tasks. The model commits to a rationale, which makes its actions more coherent. And the reasoning is in the context for subsequent steps.</p>

<p>Modern tool-use APIs (Claude, GPT-4, Gemini) have native support for ReAct-like reasoning via structured output, where reasoning and tool calls are emitted in a structured format the orchestrator parses.</p>

<h2>Stop conditions</h2>
<p>ReAct loops need clear stop conditions:</p>
<ul>
<li>Agent emits a final answer (not a tool call)</li>
<li>Max step count reached (typically 10-30)</li>
<li>Max cost budget reached</li>
<li>Timeout reached</li>
<li>Infinite-loop detection (same tool, same args, N times)</li>
</ul>

<h2>Common failure modes</h2>
<ul>
<li><strong>Tool hallucination</strong> — LLM calls a tool that doesn't exist or with wrong args</li>
<li><strong>Premature answer</strong> — agent stops exploring when it should keep going</li>
<li><strong>Infinite loop</strong> — agent repeats the same reasoning + action forever</li>
<li><strong>Lost-in-context</strong> — after many steps, the context is long and the model starts forgetting earlier reasoning</li>
</ul>

<h2>Variants</h2>
<ul>
<li><strong>Plan-then-execute</strong> — agent plans full sequence first, then executes. Works for tasks with known structure.</li>
<li><strong>Reflection</strong> — agent reviews its own trace and critiques itself before continuing. Higher quality, higher cost.</li>
<li><strong>Multi-agent ReAct</strong> — agents call other agents as tools.</li>
</ul>

<h2>When ReAct is the wrong shape</h2>
<p>For tasks with a known execution plan, skip ReAct and use a deterministic workflow. ReAct's value is in exploration; if the path is known, the reasoning overhead is waste.</p>
""",
    prev=("Architecture map", "../foundations/architecture.html"),
    nxt=("Tool use", "tool-use.html"))


write_page("loops/tool-use", "Tool use",
    "Tool use is the agent's ability to take actions in the world. Here's how modern tool-calling APIs work and what to watch out for.",
    reading_time=4,
    body_html="""
<p class="lede">Tool use is how agents affect anything outside their own reasoning. A tool is a function — with a name, description, parameter schema — that the LLM can request to call. The orchestrator executes it and returns the result.</p>

<h2>Modern tool-use APIs</h2>
<p>Every major LLM provider offers native tool-use support:</p>
<ul>
<li><strong>Anthropic Claude</strong> — tools defined in API call, model emits structured tool_use blocks</li>
<li><strong>OpenAI</strong> — function calling, now "tools" with JSON schema</li>
<li><strong>Google Gemini</strong> — function calling with FunctionDeclaration objects</li>
</ul>

<p>All three follow the same basic shape: you provide tool definitions, the model returns structured tool calls, your code executes them and feeds results back.</p>

<h2>Anatomy of a tool definition</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
{
  "name": "search_web",
  "description": "Search the web for recent information. Returns top 5 results with snippets.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {"type": "string", "description": "search query"},
      "recency": {"type": "string", "enum": ["day", "week", "month"]}
    },
    "required": ["query"]
  }
}
</pre>

<h2>The loop</h2>
<ol>
<li>Agent receives user prompt + tool definitions</li>
<li>Agent responds with either final answer or tool_use block</li>
<li>If tool_use: orchestrator calls actual function with given args</li>
<li>Orchestrator sends result back to agent as tool_result</li>
<li>Repeat until agent gives final answer</li>
</ol>

<h2>What the LLM sees</h2>
<p>The model sees your tool name, description, and parameter schema. That's it. It doesn't see your code. Everything the LLM needs to know about when to call the tool, how to call it, and what it returns must be in the description.</p>

<h2>Parallel tool calls</h2>
<p>Modern APIs support calling multiple tools in a single step. "Search these three things at once." Saves latency when tools are independent.</p>

<h2>The error-return pattern</h2>
<p>When a tool fails (network error, invalid args, no results), return a structured error the LLM can reason about:</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
{
  "error": "rate_limit",
  "message": "Rate limited. Try again in 60 seconds.",
  "retry_after": 60
}
</pre>
<p>The agent can see the error type and decide whether to retry, pivot, or ask the user.</p>
""",
    prev=("ReAct", "react.html"),
    nxt=("Planning loops", "planning.html"))


write_page("loops/planning", "Planning loops",
    "Instead of react-style one-step-at-a-time, planning agents form a plan first then execute. Here's when that wins.",
    reading_time=3,
    body_html="""
<p class="lede">A ReAct agent makes decisions one step at a time. A planning agent thinks about the whole problem first, produces a plan, then executes. The plan gives the system structure; the execution stays flexible.</p>

<h2>The plan-then-execute pattern</h2>
<ol>
<li><strong>Plan step:</strong> agent is prompted to produce a step-by-step plan for the task. Output is a structured list of actions.</li>
<li><strong>Execute step:</strong> orchestrator walks the plan, calling tools at each step. Agent can call for replanning if something changes.</li>
<li><strong>Final step:</strong> agent synthesizes results into a final answer.</li>
</ol>

<h2>When planning helps</h2>
<ul>
<li>Tasks with many steps where the full shape is knowable up front</li>
<li>When you want to review the plan before execution (safety, cost control)</li>
<li>When steps are independent and parallelizable</li>
<li>When failures mid-task benefit from a "restart from step N" recovery</li>
</ul>

<h2>When planning doesn't help</h2>
<ul>
<li>Exploratory tasks where each step's result changes the next step radically</li>
<li>Tasks where you genuinely don't know what the plan looks like until you start</li>
<li>Low-latency use cases (planning step adds one LLM call)</li>
</ul>

<h2>Hybrid: plan + react</h2>
<p>Most modern systems use a hybrid: produce a high-level plan, then run ReAct within each plan step. Plan gives structure, ReAct handles tactics.</p>

<h2>Replanning</h2>
<p>Real tasks don't go according to plan. Build replanning triggers:</p>
<ul>
<li>Tool returned unexpected result</li>
<li>Cost exceeded budget for a plan step</li>
<li>User intervened with new info</li>
<li>Multiple steps failed</li>
</ul>

<p>On trigger, agent generates a new plan from the current state.</p>

<h2>Plan quality is prompt quality</h2>
<p>A good plan-step prompt tells the model:</p>
<ul>
<li>The high-level goal</li>
<li>Available tools</li>
<li>Constraints (budget, time, safety)</li>
<li>Format for the plan output</li>
<li>Instructions to prefer fewer steps over more</li>
</ul>
""",
    prev=("Tool use", "tool-use.html"),
    nxt=("Reflection", "reflection.html"))


write_page("loops/reflection", "Reflection",
    "Reflection is having the agent critique its own work before finalizing. Improves quality at the cost of more tokens.",
    reading_time=3,
    body_html="""
<p class="lede">Reflection: after the agent produces an answer or a plan, it's prompted to critique itself. "Is this correct? Is anything missing? What would I change?" The revised answer is often meaningfully better than the first.</p>

<h2>The pattern</h2>
<ol>
<li>Agent produces initial output (answer, plan, code, whatever)</li>
<li>Reflection step: another LLM call asks "review this output, find issues, suggest improvements"</li>
<li>Revision step: agent produces a new version incorporating the reflection</li>
<li>Optional: loop reflection-revision until satisfied or max iterations</li>
</ol>

<h2>When reflection wins</h2>
<ul>
<li>Code generation (catches bugs before shipping)</li>
<li>Complex reasoning (catches logic errors)</li>
<li>Writing tasks (catches tone, factual, structural issues)</li>
<li>Plans (identifies missed steps or bad assumptions)</li>
</ul>

<h2>When it doesn't</h2>
<ul>
<li>Simple tasks where the first answer is fine</li>
<li>Cost-sensitive high-volume workflows</li>
<li>Latency-critical apps</li>
<li>When the model keeps producing the same "reflection" (it's not learning from itself)</li>
</ul>

<h2>Self vs separate critic</h2>
<p>Two approaches:</p>
<ul>
<li><strong>Self-reflection:</strong> same model critiques its own output. Cheaper, faster. Limited by the model's self-awareness.</li>
<li><strong>Separate critic:</strong> a different model (or different prompt persona) critiques. More expensive. Often produces meaningfully different feedback.</li>
</ul>

<p>For high-stakes outputs (production code, published content), separate critic is worth the cost.</p>

<h2>The empirical gain</h2>
<p>On standard benchmarks, reflection improves output quality by 5-20% over no reflection. Bigger gains on complex reasoning tasks, smaller on factual retrieval.</p>

<h2>Infinite reflection loops</h2>
<p>Without a stop condition, reflection can run forever. Cap at 2-3 iterations and accept diminishing returns.</p>
""",
    prev=("Planning loops", "planning.html"),
    nxt=("Self-correction", "self-correction.html"))


write_page("loops/self-correction", "Self-correction",
    "Self-correction lets agents recover from errors by detecting and fixing their own mistakes. Here's how it actually works in practice.",
    reading_time=3,
    body_html="""
<p class="lede">Self-correction is the agent detecting its own errors and fixing them without human intervention. Run a test, see it fail, fix the code, test again. Write a response, notice factual errors, rewrite. It's an underused pattern that dramatically improves reliability.</p>

<h2>What triggers self-correction</h2>
<ul>
<li>Tool returns an error</li>
<li>Test suite fails</li>
<li>Verification check fails (claim not supported by context, code doesn't compile)</li>
<li>External judge/critic flags the output</li>
<li>User feedback indicates issue</li>
</ul>

<h2>The correction loop</h2>
<ol>
<li>Agent produces output</li>
<li>Verification step: is this output actually correct?</li>
<li>If no: capture specific failure (error message, failed test, specific wrong claim)</li>
<li>Agent reasons about the failure: "the test failed because X, so I need to change Y"</li>
<li>Agent produces corrected output</li>
<li>Verify again; iterate until pass or give up</li>
</ol>

<h2>Self-correction in coding</h2>
<p>A coding agent writes code, runs tests, sees failures, reads error messages, fixes. This is why coding agents work: the test suite is the verifier, and the error trace is rich enough to act on.</p>

<h2>Self-correction in prose</h2>
<p>Harder. No automatic verifier for "is this essay good." Requires either reflection (see previous page), an LLM-as-judge, or user feedback.</p>

<h2>Self-correction in research</h2>
<p>Agent says "X is true." Verifier checks: is this supported by retrieved context? If no, agent must re-search or hedge the claim.</p>

<h2>The stop condition</h2>
<p>Self-correction can loop forever if the agent can't actually fix the problem. Hard limits:</p>
<ul>
<li>Max 3-5 correction attempts per issue</li>
<li>Cost budget</li>
<li>Escalate to human if still failing</li>
</ul>

<h2>The quality ceiling</h2>
<p>Self-correction only works if the model is <em>capable</em> of producing a correct answer. Fundamentally hard problems (genuinely novel reasoning, specialized domain knowledge the model lacks) don't yield to self-correction. The model will iterate on the same wrong answer.</p>
""",
    prev=("Reflection", "reflection.html"),
    nxt=("Tool design", "../tools/tool-design.html"))


# ============================================================
# TOOLS + ACTIONS (5 pages)
# ============================================================
write_page("tools/tool-design", "Tool design",
    "Well-designed tools are the difference between an agent that works and one that flails. Here's what actually matters.",
    reading_time=4,
    body_html="""
<p class="lede">Tools are where agents interact with the real world. A well-designed tool is easy for the LLM to use correctly, hard to misuse, and returns results the LLM can reason about. Bad tool design is the most common reason agents underperform.</p>

<h2>The principles</h2>

<h3>One tool, one job</h3>
<p>Don't build a do-everything tool with 15 optional parameters. Split it into focused tools. An LLM chooses better from specific options than generic ones.</p>

<h3>Name tools like a beginner would</h3>
<p>Tool names should be obviously-related to their function. <code>search_internal_docs</code> is better than <code>query_kb_v2</code>.</p>

<h3>Descriptions are prompts</h3>
<p>The tool description is what the LLM reads to decide whether to call it. Write descriptions like you're briefing a new hire on when to use each tool. See <a href="tool-descriptions.html">tool descriptions matter</a>.</p>

<h3>Keep parameter count low</h3>
<p>2-4 parameters per tool is the sweet spot. 6+ parameters means the LLM will sometimes miss required ones or hallucinate values. Split or default.</p>

<h3>Sensible defaults</h3>
<p>Every optional parameter should have a sensible default. Makes it easier for the LLM to call the tool correctly on first try.</p>

<h3>Types matter</h3>
<p>Constrained types (enums for fixed choices, integers for counts) reduce hallucination. Free-form strings invite mistakes.</p>

<h2>Tool granularity</h2>
<p>Too coarse: <code>do_everything_with_database(action, params)</code></p>
<p>Too fine: separate tools for <code>start_transaction</code>, <code>insert_row</code>, <code>commit</code></p>
<p>Right: high-level intents like <code>save_customer</code>, <code>find_orders_for_customer</code></p>

<h2>Response shape</h2>
<p>Tool responses should be:</p>
<ul>
<li>Text or simple structured data (JSON)</li>
<li>Meaningful to the LLM (context, not just raw data)</li>
<li>Bounded in size (truncate long results)</li>
<li>Error-rich (specific errors so the LLM can recover)</li>
</ul>

<h2>Common mistakes</h2>
<ul>
<li>Tool name that tells you nothing ("run_function")</li>
<li>Description that doesn't specify when to use the tool</li>
<li>Optional params without defaults</li>
<li>Tools that return huge unstructured blobs</li>
<li>Tools that succeed silently when they actually failed</li>
<li>Too many overlapping tools ("which one do I use?")</li>
</ul>
""",
    prev=("Self-correction", "../loops/self-correction.html"),
    nxt=("Tool descriptions matter", "tool-descriptions.html"))


write_page("tools/tool-descriptions", "Tool descriptions matter",
    "The description field of your tool IS the prompt to your agent. Here's how to write descriptions that produce reliable tool use.",
    reading_time=3,
    body_html="""
<p class="lede">Your tool description is read by the LLM at every step of the loop. It's the most important prompt in your agent that most developers treat as an afterthought. A weak description produces inconsistent tool use. A precise description produces reliable behavior.</p>

<h2>What a good description includes</h2>
<ol>
<li><strong>What the tool does</strong> — one sentence, active voice</li>
<li><strong>When to use it</strong> — the scenarios this is the right choice</li>
<li><strong>When NOT to use it</strong> — common misapplications</li>
<li><strong>What it returns</strong> — shape + meaning of the result</li>
<li><strong>Constraints or limits</strong> — rate limits, size limits, latency</li>
</ol>

<h2>Example: weak description</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
"Search the web."
</pre>

<h2>Example: strong description</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
"Search the public web for recent news and information. Use this
when the user asks about current events, recent developments, or
facts that may have changed since your training cutoff. Returns
top 5 results with title, URL, and snippet. Do NOT use for
searching internal documents (use search_internal_docs instead)
or for math (use calculator). Rate limited to 30 calls per minute."
</pre>

<h2>Parameter descriptions matter too</h2>
<p>Each parameter gets its own description. Tell the LLM what format, what valid values, any constraints.</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
{
  "query": {
    "type": "string",
    "description": "Natural language search query. 3-10 words works best. Include specific entities and timeframes."
  },
  "recency": {
    "type": "string",
    "enum": ["day", "week", "month", "year"],
    "description": "How recent results should be. Default is 'month'."
  }
}
</pre>

<h2>The "when not to use" is critical</h2>
<p>When you have multiple similar tools, each description must explicitly route the LLM to the right one. Without negative examples, the LLM picks more or less randomly when tools overlap.</p>

<h2>Test your descriptions</h2>
<p>Run your agent with intentionally ambiguous tasks and watch which tools it calls. If it's calling the wrong tool consistently, the descriptions need work, not the model.</p>
""",
    prev=("Tool design", "tool-design.html"),
    nxt=("Tool error handling", "error-handling.html"))


write_page("tools/error-handling", "Tool error handling",
    "Tool calls fail. How your agent reacts to failures determines whether it's reliable or brittle.",
    reading_time=3,
    body_html="""
<p class="lede">Tool calls fail in production. APIs go down, rate limits hit, timeouts expire, inputs get rejected. The agent's ability to handle errors gracefully is what separates a prototype from a production system.</p>

<h2>The principle: return errors as data</h2>
<p>Don't throw exceptions that crash the agent loop. Return structured error responses the LLM can reason about:</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
{
  "error": "rate_limit",
  "message": "Rate limit exceeded. Try again in 60 seconds.",
  "retry_after": 60
}
</pre>
<p>Or:</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
{
  "error": "not_found",
  "message": "No results found for query 'xyz'. Try a different search term."
}
</pre>

<h2>Error categories</h2>
<ul>
<li><strong>Transient</strong> (network, rate limit): LLM should retry, possibly with delay</li>
<li><strong>Permanent</strong> (bad arg, auth failure): LLM should not retry; pivot to different approach</li>
<li><strong>Empty result</strong>: LLM should try different query or conclude "no data"</li>
<li><strong>Ambiguous</strong> (multiple matches): LLM should ask for clarification or pick best</li>
</ul>

<h2>Retries</h2>
<p>Transient errors should be retried automatically by the orchestrator (not by the LLM). Expose permanent errors to the LLM after retries fail.</p>
<p>Rule of thumb: 3 retries with exponential backoff for transient errors before returning to the LLM.</p>

<h2>Timeouts</h2>
<p>Every tool call should have a timeout. If a tool hangs, the whole agent session hangs. Set aggressive timeouts (5-30 seconds) and return a timeout error the LLM can handle.</p>

<h2>Error message quality</h2>
<p>Cryptic errors waste LLM context. "Error 4040" is useless. "File not found at path /foo/bar.txt — check the path or list the directory first" is actionable.</p>

<h2>The silent-failure disaster</h2>
<p>Worst case: tool fails, returns empty or null result, LLM assumes success, produces wrong final answer. Always fail loudly. "I couldn't find X" beats "here's what I didn't find and made up."</p>

<h2>Testing error paths</h2>
<p>In your eval suite, include test cases where tools fail intentionally. Verify the agent handles it correctly (retries, pivots, or escalates to human).</p>
""",
    prev=("Tool descriptions matter", "tool-descriptions.html"),
    nxt=("Parallel tool calls", "parallel-tools.html"))


write_page("tools/parallel-tools", "Parallel tool calls",
    "Modern LLMs can request multiple tool calls in one step. Here's when to use parallel calls and how they change agent latency.",
    reading_time=3,
    body_html="""
<p class="lede">Modern tool-use APIs (Claude, GPT-4, Gemini) let the LLM request multiple tool calls in a single response. The orchestrator runs them in parallel and feeds back all results. This dramatically cuts latency for independent tasks.</p>

<h2>When parallel makes sense</h2>
<p>When tool calls are independent: don't depend on each other's results.</p>
<ul>
<li>"Search for X, search for Y, search for Z" — three independent searches</li>
<li>"Look up user info AND their order history AND their support tickets" — independent queries</li>
<li>"Check availability at 3 different providers" — independent checks</li>
</ul>

<h2>When NOT parallel</h2>
<p>When each call depends on the prior result:</p>
<ul>
<li>"Search for X, then based on what you find, search for Y"</li>
<li>"Look up user, then based on their plan, query different databases"</li>
</ul>
<p>These must be sequential.</p>

<h2>The latency math</h2>
<p>Three tool calls, each 500ms:</p>
<ul>
<li>Sequential: 1500ms total</li>
<li>Parallel: 500ms total (slowest of the three)</li>
</ul>
<p>At agent scale (many tool calls), the savings compound.</p>

<h2>Implementation</h2>
<p>The LLM returns multiple tool_use blocks in one response. Your orchestrator must detect this and dispatch them concurrently:</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
async def execute_tool_calls(calls):
    return await asyncio.gather(*[execute(c) for c in calls])
</pre>

<h2>Cost doesn't change</h2>
<p>Parallel calls don't cost more than sequential — same number of tool invocations. Sometimes cost is slightly lower because the orchestrator only sends one LLM prompt back with batched results.</p>

<h2>Error handling in parallel</h2>
<p>If one of three parallel calls fails, do you wait for the others? Fail fast? Return partial results?</p>
<p>Typically: wait for all to complete, return results (including any errors) to the LLM. LLM decides how to proceed. This keeps the programming model simple.</p>

<h2>When the LLM doesn't parallelize naturally</h2>
<p>Some models default to sequential tool use even when parallel would be faster. Prompt engineering can nudge them: "When you need multiple pieces of independent information, request them all in one response."</p>
""",
    prev=("Tool error handling", "error-handling.html"),
    nxt=("Tool budgets + limits", "tool-budgets.html"))


write_page("tools/tool-budgets", "Tool budgets + limits",
    "Without budgets, an agent can run away: thousands of tool calls, exhausted APIs, massive bills. Here's how to stop that.",
    reading_time=3,
    body_html="""
<p class="lede">A runaway agent can make hundreds of tool calls in minutes. Without budgets, this means exhausted API quotas, massive bills, and sometimes infinite loops. Budget enforcement is a non-negotiable production practice.</p>

<h2>The layers of budget</h2>

<h3>Per-session</h3>
<p>Max tool calls, max LLM tokens, max total time, max dollar cost per agent session. If any limit hits, the agent is stopped.</p>

<h3>Per-tool</h3>
<p>Rate limits per tool. "This tool can be called 10 times per session max." Prevents overuse of specific expensive operations.</p>

<h3>Per-user</h3>
<p>Cost limit per user per day. Prevents one user's runaway session from consuming the whole budget.</p>

<h3>Global</h3>
<p>Hard cap on total concurrent agent sessions or total spend per hour. Last line of defense.</p>

<h2>Hard stops</h2>
<ul>
<li>Max iterations reached (e.g., 30 steps)</li>
<li>Max cost reached (e.g., $2 per session)</li>
<li>Max time elapsed (e.g., 5 minutes)</li>
<li>Infinite loop detected (same tool + args called N times)</li>
</ul>

<h2>Loop detection</h2>
<p>Track a hash of (tool_name, args) per session. If the same hash appears 3 times in a row, the agent is probably stuck. Break and return what you have.</p>

<h2>Graceful termination</h2>
<p>When budget is reached, don't just stop. Give the LLM one final turn: "Your budget is reached. Summarize what you've found and give the best answer you can with current info."</p>

<h2>Surface budget status to the LLM</h2>
<p>Include remaining budget in the agent's context. "You have 5 tool calls and $0.20 remaining." The agent can self-ration.</p>

<h2>Per-tool rate limiting</h2>
<p>Some tools are expensive (GPU inference, third-party API with per-call fees). Rate-limit them specifically:</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
tool_limits = {
    "expensive_ml_model": 3,  # max 3 calls per session
    "search_web": 10,
    "read_file": 50,
}
</pre>

<h2>Observability of budget usage</h2>
<p>Log every session's final budget consumption. Alert on sessions that hit budget ceilings frequently — signal of bad prompts, buggy tools, or adversarial users.</p>
""",
    prev=("Parallel tool calls", "parallel-tools.html"),
    nxt=("Short-term memory", "../memory/short-term.html"))

print("\n✓ Agents content part 1: 15 pages")
