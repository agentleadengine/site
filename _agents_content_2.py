#!/usr/bin/env python3
"""AI Agents expertise content part 2: Memory + Multi-agent + Eval (14 pages)."""
from _build_agents import write_page


# ============================================================
# MEMORY (5 pages)
# ============================================================
write_page("memory/short-term", "Short-term memory",
    "Short-term memory is the agent's active context. Here's how to manage it as sessions get long.",
    reading_time=3,
    body_html="""
<p class="lede">Short-term memory is whatever's in the agent's context window right now. It's what the model sees in the current LLM call. Managing short-term memory well means keeping the relevant, trimming the stale, and surviving long sessions without quality collapse.</p>

<h2>What lives in short-term</h2>
<ul>
<li>System prompt</li>
<li>User's current message</li>
<li>Recent turns in conversation</li>
<li>Tool call history for this session</li>
<li>Any context the agent actively needs</li>
</ul>

<h2>The long-session problem</h2>
<p>After 20-30 tool calls, a session's context can balloon to 50K+ tokens. Problems:</p>
<ul>
<li><strong>"Lost in the middle"</strong> - the model under-attends to middle sections of long context</li>
<li><strong>Cost</strong> - every LLM call pays for the full context</li>
<li><strong>Latency</strong> - longer context = slower inference</li>
<li><strong>Quality decay</strong> - models' reasoning degrades with very long contexts</li>
</ul>

<h2>Strategies</h2>

<h3>Trimming</h3>
<p>Drop old tool call results once they're no longer relevant. Keep a summary, drop the raw data.</p>

<h3>Summarization</h3>
<p>When context exceeds a threshold, compress old parts into a summary. "Earlier in this session: [key facts, decisions, results]."</p>

<h3>Chunking</h3>
<p>Break very long tasks into sub-sessions. Each sub-session has bounded context; final summary bridges them.</p>

<h3>Selective recall</h3>
<p>Store everything externally (vector DB); retrieve only what's relevant for the current step. This blends short-term and long-term.</p>

<h2>What to keep in full</h2>
<ul>
<li>Original user request</li>
<li>System prompt</li>
<li>Last 2-3 turns of conversation</li>
<li>Most recent tool results (if still relevant)</li>
<li>Any ground-truth artifacts (the document being edited, the plan)</li>
</ul>

<h2>What to trim or summarize</h2>
<ul>
<li>Old tool calls whose results were consumed</li>
<li>Intermediate reasoning traces from earlier phases</li>
<li>Search results that were skimmed, not used</li>
</ul>
""",
    prev=("Tool budgets", "../tools/tool-budgets.html"),
    nxt=("Long-term memory", "long-term.html"))


write_page("memory/long-term", "Long-term memory",
    "Long-term memory persists across sessions. Facts about the user, prior decisions, accumulated knowledge.",
    reading_time=3,
    body_html="""
<p class="lede">Long-term memory is everything the agent remembers across sessions. Without it, every conversation starts from zero. With it, the agent builds relationship, knows preferences, and remembers what worked.</p>

<h2>What belongs in long-term</h2>
<ul>
<li>User profile and preferences</li>
<li>Past decisions that should inform future ones</li>
<li>Accumulated knowledge about the domain</li>
<li>Documented patterns the agent has learned</li>
<li>Facts the user has shared once that should persist</li>
</ul>

<h2>Storage models</h2>

<h3>Key-value store</h3>
<p>Structured facts: user_name, preferences, settings. Fast, bounded, simple.</p>

<h3>Vector store</h3>
<p>Embeddings of past conversations or artifacts. Retrieve by semantic similarity at query time.</p>

<h3>Document store</h3>
<p>Plain-text notes the agent writes to itself. Reviewed or summarized at intervals.</p>

<h3>Graph</h3>
<p>Entities and relationships (people, projects, decisions, dates). Query by traversal.</p>

<h2>What and when to write</h2>
<p>Not every utterance needs persisted. Good patterns:</p>
<ul>
<li>Explicit "remember this" requests from the user</li>
<li>Significant decisions or preferences ("I'm allergic to peanuts")</li>
<li>Recurring patterns ("You always ask for X context")</li>
<li>End-of-session summaries of what happened</li>
</ul>

<h2>What not to write</h2>
<ul>
<li>Every message verbatim (storage bloat + retrieval noise)</li>
<li>Sensitive information without user consent</li>
<li>Transient context that doesn't matter tomorrow</li>
</ul>

<h2>The retrieval problem</h2>
<p>Long-term memory is only useful if the agent retrieves the right piece at the right moment. Patterns:</p>
<ul>
<li>Retrieve on session start (load the user profile)</li>
<li>Retrieve on demand (agent tool: <code>recall_about(topic)</code>)</li>
<li>Retrieve automatically on similarity match (vector search at each turn)</li>
</ul>

<h2>The staleness problem</h2>
<p>User's preferences change. Facts become outdated. Have explicit update and expiry semantics, not just append-only.</p>
""",
    prev=("Short-term memory", "short-term.html"),
    nxt=("Episodic memory", "episodic.html"))


write_page("memory/episodic", "Episodic memory",
    "Episodic memory stores specific past events or interactions the agent can recall. Like a memory of 'what happened last Tuesday.'",
    reading_time=2,
    body_html="""
<p class="lede">Episodic memory is the agent's record of specific past events. Unlike structured facts ("user likes Python") or general knowledge, episodic memory captures whole interactions or trajectories the agent can reference.</p>

<h2>What it enables</h2>
<ul>
<li>"Last week when I helped you debug this issue..."</li>
<li>"In our last session, we decided X"</li>
<li>"That approach we tried in project Y didn't work"</li>
</ul>
<p>Reference to specific prior episodes makes the agent feel less amnesic and more like a long-term collaborator.</p>

<h2>Implementation</h2>
<p>Store full session transcripts (or distilled summaries) keyed by timestamp and topic. At the start of a new session, retrieve episodes relevant to the current task.</p>

<p>Typical structure:</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
{
  "episode_id": "session_2026_04_19_abc",
  "timestamp": "2026-04-19T14:30:00Z",
  "user": "user_123",
  "topic_tags": ["debugging", "python", "database"],
  "summary": "User had a database timeout issue. We traced it to missing index, added one.",
  "artifacts": [...],  // code changes, docs created
  "outcome": "resolved"
}
</pre>

<h2>Retrieval</h2>
<p>At session start, query episodic memory:</p>
<ul>
<li>By user</li>
<li>By recent time window</li>
<li>By topic similarity to current request</li>
</ul>

<h2>The summarization step</h2>
<p>Raw session transcripts are too long. Distill each session into a brief episode record at session end. Agent can expand into the full transcript only if needed.</p>

<h2>Privacy considerations</h2>
<p>Episodes contain sensitive information. Respect retention limits, access controls, and user deletion rights.</p>
""",
    prev=("Long-term memory", "long-term.html"),
    nxt=("Procedural memory", "procedural.html"))


write_page("memory/procedural", "Procedural memory",
    "Procedural memory is how-to knowledge: skills and routines the agent has learned and can reuse.",
    reading_time=2,
    body_html="""
<p class="lede">Procedural memory is the agent's how-to knowledge. Not facts, not episodes - skills. "How I usually handle this kind of task." "The recipe that worked last time." Agents that build up procedural memory get better at recurring tasks over time.</p>

<h2>What qualifies</h2>
<ul>
<li>Step-by-step recipes for recurring tasks</li>
<li>Default parameters that worked in prior cases</li>
<li>Decision rules: "if X, usually do Y"</li>
<li>Templates for common outputs</li>
</ul>

<h2>How it's built</h2>
<p>After a successful task, agent (or human) distills the solution into a reusable recipe:</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
{
  "procedure_id": "deploy_staging",
  "description": "How to deploy a branch to staging",
  "steps": [
    "Confirm branch is up to date with main",
    "Run tests locally",
    "Push to remote",
    "Trigger staging deploy workflow",
    "Verify at staging.example.com"
  ],
  "constraints": "Don't deploy on Fridays after 3pm"
}
</pre>

<h2>How it's used</h2>
<p>When agent starts a task matching an existing procedure, retrieve it and follow (or adapt). Much faster than reasoning from scratch.</p>

<h2>The learning loop</h2>
<ol>
<li>Agent attempts new task, succeeds after some exploration</li>
<li>Post-task: distill successful trajectory into a procedure</li>
<li>Next similar task: retrieve the procedure, apply directly</li>
<li>Refine procedure over time as edge cases emerge</li>
</ol>

<h2>Relationship to other memory types</h2>
<ul>
<li><strong>Short-term</strong> = current working memory</li>
<li><strong>Long-term</strong> = facts that persist</li>
<li><strong>Episodic</strong> = specific past events</li>
<li><strong>Procedural</strong> = reusable how-to</li>
</ul>
<p>A mature agent system has all four, layered.</p>
""",
    prev=("Episodic memory", "episodic.html"),
    nxt=("Memory system design", "memory-systems.html"))


write_page("memory/memory-systems", "Memory system design",
    "How to architect memory for a production agent. What goes where, what retrieval looks like, what to delete.",
    reading_time=3,
    body_html="""
<p class="lede">A real agent memory system combines short-term, long-term, episodic, and procedural memory into one architecture. Here's how to design it so the agent has the right context at the right time without drowning in data.</p>

<h2>The layered architecture</h2>

<h3>Layer 1: Session context (short-term)</h3>
<p>In-memory, per-session. Current conversation and recent tool results. Cleaned up at session end.</p>

<h3>Layer 2: User profile (long-term, structured)</h3>
<p>Key-value store. Preferences, settings, stable facts. Loaded at session start.</p>

<h3>Layer 3: Semantic memory (long-term, unstructured)</h3>
<p>Vector store of past conversations, notes, artifacts. Retrieved on demand by similarity.</p>

<h3>Layer 4: Episodic log (history)</h3>
<p>Chronological record of past sessions with summaries. Queryable by time or topic.</p>

<h3>Layer 5: Procedure library</h3>
<p>Named how-to recipes the agent can invoke.</p>

<h2>The retrieval stack</h2>
<p>At each agent step, the orchestrator decides what memory to pull:</p>
<ol>
<li>Always: user profile (short, cheap, always relevant)</li>
<li>On session start: relevant recent episodes</li>
<li>On demand: agent calls <code>recall(topic)</code> tool to fetch specific memories</li>
<li>Automatic: vector search for semantically related memories when the task matches</li>
</ol>

<h2>Writes are as important as reads</h2>
<p>Writing to long-term memory should be deliberate, not automatic:</p>
<ul>
<li><strong>Always write</strong>: explicit user-requested facts ("I'm allergic to peanuts")</li>
<li><strong>Sometimes write</strong>: preferences inferred from repeated behavior</li>
<li><strong>Rarely write</strong>: transient conversation details</li>
<li><strong>Never write</strong>: PII the user hasn't consented to persist</li>
</ul>

<h2>Expiry and updates</h2>
<p>Memory that never decays or updates becomes wrong. Build explicit:</p>
<ul>
<li>TTL on volatile facts</li>
<li>Update semantics (overwrite, append, supersede)</li>
<li>User-facing memory management (view, edit, delete)</li>
</ul>

<h2>Tools for memory</h2>
<p>Expose memory operations as tools the LLM can call:</p>
<ul>
<li><code>remember(fact)</code> - write to long-term</li>
<li><code>recall(topic)</code> - semantic retrieval</li>
<li><code>forget(fact_id)</code> - delete</li>
<li><code>list_procedures()</code> - browse procedure library</li>
</ul>

<p>The LLM uses these as first-class citizens alongside its other tools.</p>
""",
    prev=("Procedural memory", "procedural.html"),
    nxt=("Orchestrator-worker", "../multi/orchestrator-worker.html"))


# ============================================================
# MULTI-AGENT (5 pages)
# ============================================================
write_page("multi/orchestrator-worker", "Orchestrator-worker",
    "The most common multi-agent pattern: one agent plans and delegates, others execute.",
    reading_time=3,
    body_html="""
<p class="lede">Orchestrator-worker is the workhorse multi-agent pattern. One agent (orchestrator) receives the task, breaks it down, and delegates subtasks to specialized workers. Workers return results; orchestrator synthesizes the final answer.</p>

<h2>The shape</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
User -> Orchestrator
         |
         +-> Worker A (research)
         +-> Worker B (code)
         +-> Worker C (writing)
         |
         Synthesis -> User
</pre>

<h2>Why split work</h2>
<ul>
<li><strong>Specialization</strong>: each worker has focused system prompt + tools for its domain</li>
<li><strong>Parallelism</strong>: independent subtasks run concurrently</li>
<li><strong>Cost control</strong>: cheap workers for bulk tasks, expensive model for orchestration</li>
<li><strong>Modularity</strong>: easier to test and improve one worker at a time</li>
</ul>

<h2>When it's overkill</h2>
<p>Single-agent ReAct handles most tasks fine. Split when:</p>
<ul>
<li>The task genuinely has distinct, parallelizable subtasks</li>
<li>Workers can use different models or different tool sets</li>
<li>The synthesis work (combining results) is non-trivial</li>
</ul>

<h2>Worker design</h2>
<p>Each worker is itself a small agent:</p>
<ul>
<li>Has its own system prompt tuned to its specialty</li>
<li>Has access to a subset of tools relevant to its domain</li>
<li>Has its own loop with its own budget</li>
<li>Returns a structured result to the orchestrator</li>
</ul>

<h2>Handoff as a tool call</h2>
<p>In practice: the orchestrator treats workers as tools. "Call research_worker with topic X." Clean interface.</p>

<h2>Common failure modes</h2>
<ul>
<li><strong>Orchestrator over-delegates</strong>: spawns too many workers for small tasks</li>
<li><strong>Worker outputs don't combine</strong>: inconsistent schemas require orchestrator to do messy reconciliation</li>
<li><strong>No budget at worker level</strong>: each worker runs away independently</li>
<li><strong>Synthesis loss</strong>: important details from workers get dropped in final answer</li>
</ul>

<h2>Design checklist</h2>
<ul>
<li>Clear schema for worker inputs and outputs</li>
<li>Budget per worker</li>
<li>Orchestrator's job is coordination, not re-doing worker work</li>
<li>Synthesis step is carefully prompted to preserve key details</li>
</ul>
""",
    prev=("Memory system design", "../memory/memory-systems.html"),
    nxt=("Peer agents", "peer-agents.html"))


write_page("multi/peer-agents", "Peer agents",
    "Peer agents work together without a central orchestrator. Harder to design, powerful when it works.",
    reading_time=2,
    body_html="""
<p class="lede">Peer agent systems have multiple agents that interact directly without a central orchestrator. They coordinate by passing messages, sharing state, or using shared tools. Harder to reason about, but fits some problems better than orchestrator-worker.</p>

<h2>When peer structure helps</h2>
<ul>
<li>Simulating multi-party interactions (debate, negotiation)</li>
<li>Emergent behavior from agent-to-agent communication</li>
<li>Distributed problem-solving where no single agent has full context</li>
</ul>

<h2>The shape</h2>
<p>Agents communicate via shared channels, message passing, or by reading/writing to shared state. No one is "in charge."</p>

<h2>Coordination mechanisms</h2>
<ul>
<li><strong>Turn-taking</strong>: agents speak in sequence</li>
<li><strong>Event-driven</strong>: agents respond when something they care about happens</li>
<li><strong>Shared blackboard</strong>: agents write facts or claims to a shared space, others react</li>
<li><strong>Voting or consensus</strong>: agents reach agreement through explicit protocols</li>
</ul>

<h2>The complexity tax</h2>
<p>Peer systems are hard to debug:</p>
<ul>
<li>Non-determinism from interaction order</li>
<li>Deadlocks (agents waiting on each other)</li>
<li>Cost explosion if agents trigger each other recursively</li>
<li>Hard to set clear success criteria</li>
</ul>

<h2>Pragmatic use</h2>
<p>For most production systems, start with orchestrator-worker. Move to peer agents only when the problem genuinely needs distributed coordination and you can accept the debugging cost.</p>
""",
    prev=("Orchestrator-worker", "orchestrator-worker.html"),
    nxt=("Debate + consensus", "debate.html"))


write_page("multi/debate", "Debate + consensus",
    "Have multiple agents argue opposing sides of a question. The emergent answer is often better than any single agent's.",
    reading_time=3,
    body_html="""
<p class="lede">Debate is a multi-agent pattern where two or more agents argue opposing sides of a question. A judge (another agent or a human) evaluates. On many reasoning tasks, debate produces more accurate answers than a single agent.</p>

<h2>The basic setup</h2>
<ol>
<li>Question is posed</li>
<li>Agent A is assigned one position</li>
<li>Agent B is assigned the opposite position (or "find the flaws" role)</li>
<li>They exchange arguments for N rounds</li>
<li>Judge reviews the transcript and decides or synthesizes</li>
</ol>

<h2>When debate helps</h2>
<ul>
<li>Decision problems with multiple plausible answers</li>
<li>Fact-checking (one agent claims, another verifies)</li>
<li>Strategy problems (competing approaches)</li>
<li>Risk analysis (optimist vs pessimist)</li>
</ul>

<h2>The quality hypothesis</h2>
<p>A single agent can be wrong in the same direction its entire reasoning. Forcing it to construct opposing arguments surfaces flaws in its initial position. The judge, seeing both sides, often reaches a better answer than either debater alone.</p>

<h2>Research findings</h2>
<p>Academic work has shown debate-based agents outperforming single agents on math, logic, and fact-checking benchmarks. The effect is strongest on problems where single-agent output is inconsistent.</p>

<h2>Failure modes</h2>
<ul>
<li><strong>Both agents converge</strong> instead of debating (model is too compliant)</li>
<li><strong>Shallow arguments</strong> if model doesn't have depth on the topic</li>
<li><strong>Judge weakness</strong>: poorly-designed judge undoes the value of the debate</li>
<li><strong>Cost</strong>: 3-5x single-agent token use</li>
</ul>

<h2>Practical adoption</h2>
<p>Use debate sparingly - for high-stakes decisions or fact-checking. Every LLM call with debate costs 3-5x single-turn. But for tasks where accuracy matters more than cost, it's worth the premium.</p>
""",
    prev=("Peer agents", "peer-agents.html"),
    nxt=("Agent handoffs", "handoffs.html"))


write_page("multi/handoffs", "Agent handoffs",
    "How one agent hands off control to another without losing context or user experience.",
    reading_time=2,
    body_html="""
<p class="lede">When multiple agents participate in a task, handoff is the moment one passes control to another. Done cleanly, it's invisible to the user. Done poorly, context is lost and the user has to repeat themselves.</p>

<h2>The handoff payload</h2>
<p>What passes from agent A to agent B:</p>
<ul>
<li>Original user goal</li>
<li>Context gathered so far (facts, decisions, partial work)</li>
<li>Specific task for agent B</li>
<li>Constraints (budget, time, quality bar)</li>
<li>Success criteria for the handoff</li>
</ul>

<h2>When to hand off</h2>
<ul>
<li>Current agent has reached its specialty boundary</li>
<li>Another agent has better tools for the remaining work</li>
<li>Escalation to a more capable model (cheap → expensive when needed)</li>
<li>Human-in-the-loop (agent → human)</li>
</ul>

<h2>The clean handoff pattern</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
{
  "original_goal": "User wanted X",
  "progress_summary": "I've done A, B, C. Remaining: D, E.",
  "next_task": "Do D using tools X, Y",
  "context_to_preserve": [...key facts...],
  "constraints": {"budget": "$0.50", "timeout": "60s"}
}
</pre>

<h2>The user experience</h2>
<p>User shouldn't know they were handed off. The receiving agent introduces itself naturally: "I'll take it from here on the technical review." No "transferring you to a different department" moments.</p>

<h2>Failure modes</h2>
<ul>
<li>Handoff loses critical context → user has to repeat</li>
<li>Both agents partially do the same work → wasted cost</li>
<li>Handoff happens too late → receiving agent can't catch up</li>
<li>Handoff happens too early → sending agent hadn't finished its part</li>
</ul>

<h2>Designing the trigger</h2>
<p>Make handoff conditions explicit in each agent's system prompt. "When X happens, hand off to agent Y via tool Z." Clear boundaries reduce thrashing.</p>
""",
    prev=("Debate + consensus", "debate.html"),
    nxt=("Agent routing", "routing.html"))


write_page("multi/routing", "Agent routing",
    "Routing decides which agent handles an incoming request. The classifier between user and agent pool.",
    reading_time=2,
    body_html="""
<p class="lede">In multi-agent systems, incoming requests need to reach the right agent. Routing is the classifier that picks which agent to invoke based on the request. Get routing wrong and users talk to the wrong specialist.</p>

<h2>Routing approaches</h2>

<h3>Rule-based</h3>
<p>Hard-coded logic. If message contains "password" → auth agent. If contains "billing" → billing agent. Simple, fast, brittle.</p>

<h3>LLM classifier</h3>
<p>A lightweight LLM reads the request and emits a category. Flexible, handles novel phrasings. Costs one LLM call per route.</p>

<h3>Embedding-based</h3>
<p>Embed the request, find nearest agent by similarity to their capability description. Fast, doesn't require LLM call per route.</p>

<h3>Hybrid</h3>
<p>Rules for obvious cases, LLM fallback for ambiguous. Best balance of speed and accuracy.</p>

<h2>Routing to multiple agents</h2>
<p>Sometimes a request needs multiple specialists. Router can:</p>
<ul>
<li>Pick one agent; that agent can call others as tools</li>
<li>Fan out to multiple agents, aggregate results</li>
<li>Pick the primary agent; loop in others on demand</li>
</ul>

<h2>The "general" agent</h2>
<p>Always have a fallback generalist agent for requests that don't match any specialist. Without one, unusual queries fall through the cracks.</p>

<h2>Measuring routing quality</h2>
<ul>
<li>Correct-route rate (did the request reach the right agent?)</li>
<li>Handoff rate (% of requests that require cross-agent handoff)</li>
<li>Ambiguous-route rate (routes that the classifier wasn't confident on)</li>
</ul>
""",
    prev=("Agent handoffs", "handoffs.html"),
    nxt=("Why eval agents", "../eval/why-eval-agents.html"))


# ============================================================
# EVAL (4 pages)
# ============================================================
write_page("eval/why-eval-agents", "Why eval agents",
    "Agents fail in subtle ways. Without evaluation, you ship a system that works in demos and silently fails in production.",
    reading_time=3,
    body_html="""
<p class="lede">Agents are much harder to eval than single LLM calls. A single call has one output to score. An agent has a trajectory: a sequence of reasoning steps and tool calls, any of which can go wrong without changing the final answer. Without agent-specific eval, quality erodes invisibly.</p>

<h2>Why single-call eval isn't enough</h2>
<ul>
<li>Agent might produce a correct final answer via the wrong tools</li>
<li>Agent might produce a correct answer 60% of the time (non-determinism)</li>
<li>Agent might hit budget limits or loop forever on certain inputs</li>
<li>Agent might have unsafe behaviors that rarely surface</li>
</ul>

<h2>What to measure</h2>

<h3>Task completion</h3>
<p>Did the agent accomplish what was asked? Binary or graded.</p>

<h3>Trajectory quality</h3>
<p>Was the path efficient? Right tools? Right order?</p>

<h3>Cost</h3>
<p>Tokens and tool-call count per task.</p>

<h3>Latency</h3>
<p>Total time from request to completion.</p>

<h3>Safety</h3>
<p>Did the agent do anything unsafe (harmful tool calls, leaked data)?</p>

<h2>The eval set</h2>
<p>A diverse set of representative tasks:</p>
<ul>
<li>Happy path (common cases)</li>
<li>Edge cases (unusual inputs)</li>
<li>Adversarial (prompt injection attempts, contradictory requests)</li>
<li>Error paths (tools deliberately fail)</li>
<li>Long-tail (uncommon but important tasks)</li>
</ul>

<h2>Automated vs human eval</h2>
<p>Automated evals scale. LLM-as-judge works for many dimensions. Human review catches what automation misses. Real agent programs run both.</p>

<h2>The regression problem</h2>
<p>Change your system prompt, switch models, update a tool description - all can regress agent quality. Without an eval suite, you don't know until users complain.</p>

<p>Run the eval on every meaningful change. Ship only if quality holds.</p>
""",
    prev=("Agent routing", "../multi/routing.html"),
    nxt=("Task completion", "task-completion.html"))


write_page("eval/task-completion", "Task completion",
    "The most important agent metric. Did it do what was asked? Here's how to measure it.",
    reading_time=2,
    body_html="""
<p class="lede">Task completion is the primary agent metric. Forget trajectory, forget cost - did the agent achieve the user's goal? If not, nothing else matters. Measuring task completion reliably is harder than it sounds.</p>

<h2>Grading approaches</h2>

<h3>Binary</h3>
<p>Did it work? Yes/no. Works when the task has a clear success criterion (test passed, file created with expected contents, correct answer to a question).</p>

<h3>Graded</h3>
<p>Scale 1-5. Useful for tasks where "correct" has degrees (writing quality, helpfulness, thoroughness).</p>

<h3>Ground-truth comparison</h3>
<p>Compare agent's output to a known-correct answer. Direct match, semantic similarity, or structured equivalence.</p>

<h3>LLM-as-judge</h3>
<p>Use a strong LLM to grade agent output. Scales, but introduces judge bias.</p>

<h2>What to watch out for</h2>
<ul>
<li><strong>False success</strong>: agent claims completion but didn't actually finish</li>
<li><strong>Partial completion</strong>: did half the task, stopped</li>
<li><strong>Silent failure</strong>: error occurred but was swallowed; final response is plausible but wrong</li>
<li><strong>Over-completion</strong>: did what was asked and also did things not asked (scope creep)</li>
</ul>

<h2>Verifier design</h2>
<p>For each eval case, the verifier should check the actual outcome, not just the agent's claim. Agent says "I deleted the file" - verifier checks the file is actually gone.</p>

<h2>Run multiple times</h2>
<p>Agents are non-deterministic. Run each eval case 3-5 times. If it passes 5/5 you have high confidence. 3/5 is a reliability problem.</p>
""",
    prev=("Why eval agents", "why-eval-agents.html"),
    nxt=("Trajectory evaluation", "trajectory-eval.html"))


write_page("eval/trajectory-eval", "Trajectory evaluation",
    "Beyond whether the agent got the right answer - did it get there the right way?",
    reading_time=3,
    body_html="""
<p class="lede">Trajectory evaluation looks at how the agent got to its answer, not just whether it got there. Two agents with the same final answer can differ by 10x in cost, or produce the answer via completely different reasoning paths.</p>

<h2>What to measure in trajectories</h2>

<h3>Efficiency</h3>
<ul>
<li>Number of tool calls</li>
<li>Number of reasoning steps</li>
<li>Total tokens used</li>
<li>Time elapsed</li>
</ul>

<h3>Tool selection</h3>
<ul>
<li>Did it use the right tools?</li>
<li>Did it use tools it shouldn't have (safety)?</li>
<li>Did it use tools redundantly?</li>
</ul>

<h3>Reasoning quality</h3>
<ul>
<li>Did the reasoning follow logically from observations?</li>
<li>Were any steps circular or contradictory?</li>
<li>Did the agent reason about its own uncertainty?</li>
</ul>

<h3>Error recovery</h3>
<ul>
<li>When tools failed, did the agent respond sensibly?</li>
<li>Did it try alternatives?</li>
<li>Did it loop forever?</li>
</ul>

<h2>Automated checks</h2>
<p>Some trajectory properties can be checked automatically:</p>
<ul>
<li>Step count (should be below threshold)</li>
<li>No forbidden tools called</li>
<li>No tool called more than N times with same args (loop detection)</li>
<li>Final answer in expected shape</li>
</ul>

<h2>LLM-as-judge on trajectories</h2>
<p>Give a judge LLM the full trajectory + expected answer. Ask:</p>
<ul>
<li>Did the agent take a reasonable path?</li>
<li>Were there obvious inefficiencies?</li>
<li>Any warning signs in reasoning?</li>
</ul>

<h2>Comparative trajectory eval</h2>
<p>Compare trajectories across model versions or prompt changes. Even if task-completion rate is the same, shorter/cheaper trajectories indicate improvement.</p>
""",
    prev=("Task completion", "task-completion.html"),
    nxt=("Regression testing", "regression.html"))


write_page("eval/regression", "Regression testing",
    "Every agent change can quietly break something. Regression tests catch regressions before production.",
    reading_time=2,
    body_html="""
<p class="lede">Every tweak to a system prompt, every model upgrade, every tool change can break something that used to work. Regression testing catches these breaks before they hit production.</p>

<h2>The eval set as regression suite</h2>
<p>Your eval set doubles as your regression tests. Run it before shipping any agent change. If pass rate drops, investigate.</p>

<h2>What to include</h2>
<ul>
<li>All known-good behaviors (the "this used to work" cases)</li>
<li>Past bugs (so they don't come back)</li>
<li>Adversarial inputs (prompt injection, edge cases)</li>
<li>Safety-critical cases (never-do-this boundaries)</li>
</ul>

<h2>Running regression</h2>
<p>Set up as CI-like pipeline:</p>
<ol>
<li>Developer proposes change (prompt edit, new tool, model upgrade)</li>
<li>Run full regression suite against the new config</li>
<li>Compare pass rate to baseline</li>
<li>Ship only if no meaningful regression</li>
</ol>

<h2>The flaky-test problem</h2>
<p>Agents are non-deterministic. A test might pass 4/5 runs and fail 1/5. Classify:</p>
<ul>
<li>Consistent pass → fine</li>
<li>Consistent fail → definite regression</li>
<li>Flaky → run more times, calculate real pass rate, may need to accept statistical noise</li>
</ul>

<h2>Cost of regression runs</h2>
<p>Running a 100-case eval suite on every change can add up. Strategies:</p>
<ul>
<li>Tiered: fast subset on every change, full suite before release</li>
<li>Smart selection: run tests most likely to be affected by the change</li>
<li>Monthly full runs with smaller per-change runs</li>
</ul>

<h2>Eval set maintenance</h2>
<ul>
<li>Add cases for every production bug</li>
<li>Remove cases that no longer reflect reality</li>
<li>Quarterly audit to make sure it still represents real use</li>
</ul>
""",
    prev=("Trajectory evaluation", "trajectory-eval.html"),
    nxt=("Observability + tracing", "../prod/observability.html"))

print("\n✓ Agents content part 2: 14 pages")
