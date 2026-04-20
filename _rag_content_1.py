#!/usr/bin/env python3
"""RAG content part 1: Hub + Foundations + Documents + Chunking (22 pages)."""
from _build_rag import write_rag_page


# ============================================================
# HUB
# ============================================================

hub_body = """
<p class="lede">RAG (Retrieval-Augmented Generation) is the discipline of grounding a language model's answers in your own data. Almost every production AI system I've worked on eventually converges to some version of RAG. It's the difference between a model that bluffs and a model that cites. Between a demo that looks good and a system that holds up under real traffic.</p>

<p>This section is 56 pages on how to take a RAG system from "throwing docs into a vector database and hoping" all the way to production-grade retrieval. Rags to riches - from the naive v1 most teams ship and regret, to the layered, evaluated, observable systems that actually work at scale.</p>

<h2>The ten sections</h2>

<div class="cards" style="margin-top:32px;">
  <a href="foundations/what-is-rag.html" class="card"><h3>Foundations</h3><p>What RAG is, why it beats fine-tuning for most use cases, the architecture map, and when to skip it entirely.</p></a>
  <a href="docs/ingestion-pipeline.html" class="card"><h3>Documents + Ingestion</h3><p>PDFs, HTML, tables, figures, OCR, metadata - the unglamorous 80% of every real RAG system.</p></a>
  <a href="chunking/why-chunking.html" class="card"><h3>Chunking</h3><p>Fixed-size, semantic, recursive, structure-aware. The single most under-thought part of most RAG stacks.</p></a>
  <a href="embeddings/what-are-embeddings.html" class="card"><h3>Embeddings</h3><p>Picking models, closed vs open, dimensions, MRL, fine-tuning. Where your retrieval ceiling is actually set.</p></a>
  <a href="vectors/overview.html" class="card"><h3>Vector Stores</h3><p>HNSW, IVF, PQ, hybrid indexes, metadata filtering, cost. The infrastructure layer.</p></a>
  <a href="retrieval/vector-search.html" class="card"><h3>Retrieval Strategies</h3><p>Dense, sparse, hybrid, reranking, HyDE, query rewriting, multi-query fusion. The real craft.</p></a>
  <a href="advanced/agentic-rag.html" class="card"><h3>Advanced Patterns</h3><p>Agentic RAG, GraphRAG, CRAG, Self-RAG, multi-hop. Where modern RAG is actually going.</p></a>
  <a href="eval/why-eval.html" class="card"><h3>Evaluation</h3><p>Retrieval metrics, generation metrics, RAGAS, building eval sets. If you skip this section your system will silently rot.</p></a>
  <a href="prod/latency.html" class="card"><h3>Production</h3><p>Latency, caching, observability, cost, security. Turning a notebook into a service.</p></a>
  <a href="cases/customer-support.html" class="card"><h3>Use Cases</h3><p>Customer support, internal KB, code search, legal, multi-tenant. The patterns I keep reaching for.</p></a>
</div>

<h2 style="margin-top:56px;">How to read this</h2>
<p>If you're new to RAG, start at <a href="foundations/what-is-rag.html">Foundations</a> and go section by section. If you've already shipped a v1 and it underwhelms in production, skip to <a href="retrieval/reranking.html">Reranking</a> and <a href="eval/why-eval.html">Evaluation</a>. Those are the two places where most naive RAG systems leave the most value on the floor.</p>

<p>The thread running through all of it: RAG isn't one thing. It's a pipeline with a dozen independent decisions, and the quality of your system is the product of all of them - not the max.</p>
"""

write_rag_page(
    slug="index",
    title="RAGS to Riches",
    description="A 56-page reference on Retrieval-Augmented Generation: ingestion, chunking, embeddings, vector stores, retrieval, evaluation, and production RAG systems.",
    reading_time=3,
    body_html=hub_body,
    prev=None,
    nxt=("What is RAG?", "foundations/what-is-rag.html"),
)


# ============================================================
# FOUNDATIONS (4 pages + hub)
# ============================================================

write_rag_page(
    slug="foundations/what-is-rag",
    title="What is RAG?",
    description="Retrieval-Augmented Generation (RAG) is the architectural pattern that lets an LLM answer questions using your data. Here's what it actually is and what it isn't.",
    reading_time=5,
    body_html="""
<p class="lede">RAG is short for Retrieval-Augmented Generation. At its simplest: before you ask the language model a question, you retrieve relevant context from your own data and paste it into the prompt. The model then answers using that context. It's three moves - embed, retrieve, generate - dressed up with pipelines, metadata, and increasingly sophisticated orchestration on top.</p>

<h2>The three-step loop</h2>
<ol>
  <li><strong>Embed.</strong> Convert your documents into numeric vectors using an embedding model. Store the vectors in a searchable index.</li>
  <li><strong>Retrieve.</strong> At query time, embed the user's question and find the closest document vectors by similarity.</li>
  <li><strong>Generate.</strong> Concatenate the retrieved chunks with the user's question and send the combined prompt to an LLM.</li>
</ol>

<p>That's vanilla RAG. Everything in this section is what you do once you realize vanilla RAG produces a good demo and a mediocre product.</p>

<h2>What RAG gives you</h2>
<ul>
  <li><strong>Grounded answers.</strong> The model responds with your data, not its pretraining.</li>
  <li><strong>Citations.</strong> Because the retrieval step returns specific chunks, you can link answers to source documents.</li>
  <li><strong>Freshness.</strong> Update the index, update the answers. No retraining required.</li>
  <li><strong>Access control.</strong> Filter retrieved documents by user, tenant, or permission before generation.</li>
  <li><strong>Cost control.</strong> You only pay for the tokens you actually pass into the context window.</li>
  <li><strong>Auditable behavior.</strong> Logs of what was retrieved let you debug why a model said what it said.</li>
</ul>

<h2>What RAG doesn't give you</h2>
<ul>
  <li><strong>Reasoning you don't already have.</strong> RAG can't teach a model to solve a problem it didn't learn in pretraining. It only makes facts available.</li>
  <li><strong>Style or tone changes.</strong> Those come from fine-tuning or prompting, not retrieval.</li>
  <li><strong>Magical "search your docs" quality.</strong> Retrieval quality is capped by chunking, embedding, and reranking choices - and vanilla setups leave most of that ceiling unclaimed.</li>
  <li><strong>Guaranteed factuality.</strong> The model can still hallucinate over retrieved context if the context is noisy, contradictory, or incomplete.</li>
</ul>

<h2>The surface is small. The depth is enormous.</h2>
<p>A naive RAG system fits on one whiteboard. But each of those three steps has its own sub-discipline:</p>
<ul>
  <li>Before embedding, you have to parse documents - which for PDFs alone is a category of software.</li>
  <li>Chunking strategies affect retrieval quality as much as model choice.</li>
  <li>Vector indexes have failure modes that don't show up until 10M+ documents.</li>
  <li>Retrieval itself is a stack of techniques (dense, sparse, hybrid, rerank, query rewriting) where each layer compounds on the last.</li>
  <li>Evaluation is its own rabbit hole - "is my RAG better?" is genuinely hard to answer.</li>
  <li>Production concerns (latency, cost, observability, security) transform the system once it leaves the notebook.</li>
</ul>
<p>The reason I wrote 56 pages on this topic is that every one of those layers matters, and most teams under-invest in all of them.</p>

<h2>The mental model</h2>
<p>Think of RAG as a pipeline where information flows from documents to answers. The quality of the final answer is bounded by the <em>worst</em> stage of that pipeline. You can have world-class embeddings and a terrible chunking strategy, and you'll get poor answers. You can have perfect retrieval and a weak generator, and you'll get poor answers. The job of a RAG engineer is to keep all stages strong enough that the overall product is good.</p>

<p>Call it the minimum-weak-link law. It's the single most useful frame for debugging a bad RAG system.</p>

<p style="margin-top:40px;">Next: <a href="why-rag.html">Why RAG over fine-tuning</a>.</p>
""",
    prev=("Overview", "../index.html"),
    nxt=("Why RAG over fine-tuning", "why-rag.html"),
)


write_rag_page(
    slug="foundations/why-rag",
    title="Why RAG over fine-tuning",
    description="Fine-tuning teaches a model new behaviors. RAG gives a model new facts. Most of what teams think they want from fine-tuning is actually a RAG problem.",
    reading_time=5,
    body_html="""
<p class="lede">Every time a team says "we want to fine-tune a model on our company docs," I ask one question: do you want to change how the model behaves, or do you want to make facts available to it? If it's the second one - and it almost always is - you want RAG, not fine-tuning. This is the most common architectural mistake I see in AI projects.</p>

<h2>The clean split</h2>

<h3>Use RAG when you need</h3>
<ul>
  <li>Factual grounding in your own data</li>
  <li>Citations and auditability</li>
  <li>Frequently changing information</li>
  <li>Access control per user/tenant</li>
  <li>Large knowledge bases (more than fits in a context window)</li>
  <li>Quick iteration without retraining</li>
</ul>

<h3>Use fine-tuning when you need</h3>
<ul>
  <li>Specific output structure (JSON schemas, code style)</li>
  <li>Stable voice or tone across all outputs</li>
  <li>Latency reduction on a well-defined task</li>
  <li>Cost reduction for a high-volume narrow task</li>
  <li>Behavior that prompting alone can't reliably produce</li>
</ul>

<h3>Use both when you need</h3>
<ul>
  <li>Grounded answers in a specific voice</li>
  <li>A small specialized model that still reasons over your data</li>
  <li>Domain-specific embeddings plus retrieval on top</li>
</ul>

<h2>The economics are not close</h2>
<p>Fine-tuning a serious model costs anywhere from a few hundred to tens of thousands of dollars per run. Updating a RAG index costs pennies. When your knowledge base changes - which it does constantly - the RAG system is updated in seconds. The fine-tuned model is a stale artifact until the next training run.</p>

<p>For any system where facts update more than once a quarter, RAG wins on cost alone.</p>

<h2>The failure mode nobody warns you about</h2>
<p>Fine-tuning on factual data teaches the model to produce <em>tokens that look like your data</em>. Not to reason about it. The model will confidently invent answers that sound like your docs but contradict them. This is especially bad with small datasets, where the model memorizes surface patterns without generalizing.</p>

<p>I've seen teams fine-tune on internal wikis and get a model that hallucinates internal wiki content - which is worse than useless. RAG, done well, doesn't have this failure mode because the actual source text is in the prompt at generation time.</p>

<h2>The hybrid pattern - when it pays</h2>
<p>The right hybrid: fine-tune a smaller/cheaper model on the <em>shape</em> of responses you want (format, style, common patterns), then use RAG to inject the specific facts at inference time. You get the efficiency of a smaller model, the consistency of fine-tuning, and the factuality of RAG.</p>

<p>This is the architecture most serious production systems converge on. Not "RAG or fine-tuning" but "fine-tuning for behavior, RAG for facts."</p>

<h2>A quick test</h2>
<p>Ask yourself: if a new fact is added to our knowledge base tomorrow, do we need the system to answer about it?</p>
<ul>
  <li>Yes → RAG (or hybrid)</li>
  <li>No, and the behavior is stable → fine-tuning might be enough</li>
  <li>The answer changes daily → pure RAG, and probably with real-time indexing</li>
</ul>

<h2>Long context isn't a replacement</h2>
<p>Some teams now argue that with 1M+ token context windows, you can just stuff everything in. In practice: you can't afford to, your latency triples, and retrieval quality (what the model pays attention to) degrades in the middle of massive contexts. The "lost in the middle" phenomenon is real. Long context is a tool in the RAG toolbox, not a replacement for retrieval.</p>

<p>The right mental model: use a long context window to pass more <em>retrieved</em> chunks, not to skip retrieval.</p>

<p style="margin-top:40px;">Next: <a href="the-architecture.html">The RAG architecture map</a>.</p>
""",
    prev=("What is RAG?", "what-is-rag.html"),
    nxt=("The RAG architecture map", "the-architecture.html"),
)


write_rag_page(
    slug="foundations/the-architecture",
    title="The RAG architecture map",
    description="Every production RAG system has the same core layers. Here's the full architecture map and what decisions each layer forces.",
    reading_time=6,
    body_html="""
<p class="lede">A RAG system isn't one thing. It's a pipeline with 8-10 distinct stages, each of which has its own design space. Understanding the full map is how you move from "we're using RAG" to "we're making specific defensible choices at each layer." Here's the map I use.</p>

<h2>The ten stages</h2>

<h3>1. Source integration</h3>
<p>Where documents come from. Confluence, Google Drive, Notion, S3, SharePoint, databases, APIs, websites, Slack. Every source has its own auth model, rate limits, and permission system. Ingestion connectors are often the biggest single engineering cost.</p>

<h3>2. Parsing + extraction</h3>
<p>Turning raw files into text. PDFs, HTML, Word docs, spreadsheets, scanned images, video transcripts. The quality of downstream retrieval is capped by how well parsing preserves structure (headings, tables, lists).</p>

<h3>3. Cleaning + normalization</h3>
<p>Stripping boilerplate, fixing encoding, deduplicating, normalizing whitespace, handling multiple languages. Small choices here affect retrieval accuracy more than most teams realize.</p>

<h3>4. Chunking</h3>
<p>Splitting documents into retrievable units. The chunk size, overlap, and boundary rules determine what retrieval can possibly return. See the <a href="../chunking/why-chunking.html">chunking section</a>.</p>

<h3>5. Metadata enrichment</h3>
<p>Attaching structured data to each chunk: source URL, document type, author, timestamp, tags, permissions. This is what lets you filter, sort, and scope retrieval later.</p>

<h3>6. Embedding</h3>
<p>Converting each chunk into a vector using an embedding model. The model choice sets a ceiling on retrieval quality - and costs compound across every reindex.</p>

<h3>7. Index storage</h3>
<p>Storing vectors in a searchable index. Pinecone, Weaviate, Qdrant, Chroma, pgvector, Milvus, FAISS. Each has different performance characteristics at scale.</p>

<h3>8. Retrieval</h3>
<p>At query time: embed the question, search the index, possibly combine with keyword search, possibly rerank. This is the layer where most production RAG systems win or lose.</p>

<h3>9. Generation</h3>
<p>Passing retrieved context plus the user's question to an LLM. Prompt design, model choice, structured output schemas, citation formatting.</p>

<h3>10. Observability + feedback</h3>
<p>Logging queries, retrieved chunks, and final answers. Collecting user feedback. Building evaluation datasets. Without this layer the system silently degrades.</p>

<h2>The data plane vs the query plane</h2>
<p>These ten stages split into two workflows:</p>
<ul>
  <li><strong>Data plane (offline):</strong> stages 1-7. Runs on a schedule or in response to document updates. Builds and maintains the index.</li>
  <li><strong>Query plane (online):</strong> stages 8-10. Runs on every user query. Latency-sensitive.</li>
</ul>
<p>The split matters because they have different scaling profiles, different failure modes, and usually different engineering ownership. Teams that conflate them end up with systems where a re-ingestion job blocks live queries, or where a query optimization breaks the indexer.</p>

<h2>The decisions I force teams to make explicit</h2>
<p>For every new RAG project, I write down a one-pager covering:</p>

<blockquote style="border-left:3px solid var(--purple); padding-left:16px; margin:20px 0; color:var(--text-muted);">
<strong>Sources:</strong> which systems feed the index? Auth model for each?<br>
<strong>Parsing:</strong> which file types, which library, what's the fallback?<br>
<strong>Chunking:</strong> size, overlap, boundary rules, structure-aware or not?<br>
<strong>Metadata:</strong> what fields per chunk, used for filtering how?<br>
<strong>Embedding:</strong> model, dimensions, cost per million chunks, reindex cadence?<br>
<strong>Index:</strong> which DB, algorithm (HNSW/IVF/PQ), sharding, replication?<br>
<strong>Retrieval:</strong> dense-only, hybrid, rerank? Top-k? Score cutoff?<br>
<strong>Generation:</strong> which model, prompt structure, citation format?<br>
<strong>Eval:</strong> what metrics, what golden set, continuous or episodic?<br>
<strong>Observability:</strong> logging, alerting, feedback loops, human review?
</blockquote>

<p>Ten questions. Most teams have answers for 3-4. The rest becomes "we'll figure that out later" - and "later" is when the system breaks in production.</p>

<h2>The common anti-architecture</h2>
<p>A surprising number of production RAG systems look like this:</p>
<ul>
  <li>LangChain default PDF loader</li>
  <li>1000-character chunks with 200-character overlap</li>
  <li>OpenAI text-embedding-3-small</li>
  <li>Chroma running in-memory</li>
  <li>Top-10 retrieval passed to GPT-4</li>
  <li>No eval, no observability, no reranker</li>
</ul>
<p>It's the default path, and it's not terrible - but it's also the system that will plateau at "okay" and never get to "good." Everything in this section is the work of getting past that plateau.</p>

<p style="margin-top:40px;">Next: <a href="when-not-to-use.html">When not to use RAG</a>.</p>
""",
    prev=("Why RAG over fine-tuning", "why-rag.html"),
    nxt=("When not to use RAG", "when-not-to-use.html"),
)


write_rag_page(
    slug="foundations/when-not-to-use",
    title="When not to use RAG",
    description="RAG isn't always the right answer. Here are the scenarios where it adds complexity without improving outcomes and what to use instead.",
    reading_time=5,
    body_html="""
<p class="lede">RAG solves a specific problem: grounding an LLM's answers in data the model didn't see during training. If your problem isn't that, you don't need RAG. Here's when I push teams toward simpler or different architectures.</p>

<h2>When the entire knowledge fits in a prompt</h2>
<p>If your "knowledge base" is 30 pages of internal docs, put it in a system prompt and move on. Retrieval pipelines add latency, cost, and surface area. For small, bounded knowledge that rarely changes, a long system prompt beats RAG every time.</p>

<p>Rule of thumb: if all your content fits in 40-60K tokens comfortably, skip RAG. You can always add it later if the knowledge base grows.</p>

<h2>When the answer doesn't depend on specific documents</h2>
<p>"Generate a marketing email in our brand voice" doesn't need RAG. It needs a well-crafted system prompt with examples. "Summarize this document" doesn't need RAG. You already have the document.</p>

<p>RAG is for questions that require finding the right document. If there's no retrieval problem, there's no RAG.</p>

<h2>When you need deep reasoning over a single document</h2>
<p>If the user uploads one PDF and asks complex questions about it, you're better off sending the whole document (or large sections of it) to a long-context model than chunking-retrieving-generating. RAG chunking can break chains of reasoning that span multiple sections of a single document.</p>

<p>For "analyze this contract" or "review this codebase file," long-context inference outperforms chunked retrieval.</p>

<h2>When precision matters more than recall</h2>
<p>RAG is optimistic retrieval: fetch the most likely documents and let the model figure it out. For legal discovery, compliance auditing, or anything where a missed document is a lawsuit, you want exhaustive search with human review - not approximate vector similarity. Traditional keyword search with Boolean operators and proper workflows beats RAG in these cases.</p>

<h2>When the task is structured data, not unstructured text</h2>
<p>If your "documents" are rows in a database, you don't want vector retrieval - you want SQL. An LLM with structured tool access and a well-defined query interface beats RAG for any task where the underlying data is tabular and queryable.</p>

<p>Text-to-SQL or tool-calling agents are the right pattern here. RAG over a database export is usually worse than querying the database directly.</p>

<h2>When latency matters more than quality</h2>
<p>Full RAG adds 200-1500ms of latency (embedding + search + rerank + generation). If you're building something real-time (voice, streaming autocomplete), RAG may be too slow. Consider:</p>
<ul>
  <li>Preloading common context into the prompt</li>
  <li>Caching retrieved chunks per session</li>
  <li>Using a smaller embedding model</li>
  <li>Running retrieval asynchronously with a fallback to no-retrieval answers</li>
</ul>

<h2>When you can't afford to maintain an index</h2>
<p>RAG is a live system. It needs document ingestion pipelines, index maintenance, embedding recomputation when you change models, and monitoring. If your team won't own this, RAG will rot. The index will drift out of sync with the actual data, and answers will silently get worse.</p>

<p>For one-off projects or prototypes that won't have ongoing ownership, a long-context approach is often better. You pay more per query but you avoid an operational burden nobody will carry.</p>

<h2>When fine-tuning is actually the right answer</h2>
<p>Revisit: if you need stable output structure, consistent tone, or latency-critical task-specific behavior, fine-tuning may beat RAG. See <a href="why-rag.html">why RAG over fine-tuning</a> for the split.</p>

<h2>When the LLM already knows it</h2>
<p>If the information is in the model's training data (common knowledge, standard programming patterns, general reasoning), RAG adds no value. Trying to RAG-retrieve "how do I reverse a string in Python" is worse than just asking the model.</p>

<p>A quick test: does the base model, without any context, get this question mostly right? If yes, RAG is solving the wrong problem.</p>

<h2>The red-flag phrase</h2>
<p>Whenever a team says "we want to use RAG for...", I ask them to complete the sentence without the word RAG. "We want to ground answers in our product docs." "We want users to ask questions about their uploaded files." "We want to search across internal wikis with a natural-language interface." Those are real use cases. "We want to use RAG" is architecture looking for a problem.</p>

<p style="margin-top:40px;">Next: <a href="../docs/ingestion-pipeline.html">The ingestion pipeline</a>.</p>
""",
    prev=("The RAG architecture map", "the-architecture.html"),
    nxt=("The ingestion pipeline", "../docs/ingestion-pipeline.html"),
)


# ============================================================
# DOCUMENTS + INGESTION (6 pages)
# ============================================================

write_rag_page(
    slug="docs/ingestion-pipeline",
    title="The ingestion pipeline",
    description="Ingestion is 80% of a real RAG system. Here's the pipeline pattern I use and the stages that matter most.",
    reading_time=6,
    body_html="""
<p class="lede">Ingestion is the unsexy 80% of any production RAG system. Demos skip it. Real systems live and die by it. If your ingestion is broken, no amount of retrieval sophistication saves you - you're doing advanced reasoning on garbage.</p>

<h2>The canonical pipeline</h2>
<ol>
  <li><strong>Connect to source</strong> (API, filesystem, storage bucket, database)</li>
  <li><strong>Detect changes</strong> (full, delta, or event-driven)</li>
  <li><strong>Fetch raw document</strong> with auth and rate limiting</li>
  <li><strong>Parse</strong> into structured text plus metadata</li>
  <li><strong>Clean + normalize</strong> (boilerplate, encoding, whitespace)</li>
  <li><strong>Enrich</strong> (extract entities, tags, summaries)</li>
  <li><strong>Chunk</strong></li>
  <li><strong>Embed</strong></li>
  <li><strong>Upsert</strong> to index with metadata</li>
  <li><strong>Log + monitor</strong></li>
</ol>

<h2>Full vs delta vs event-driven</h2>

<h3>Full reindex</h3>
<p>Simplest. Rebuild the entire index from scratch on a schedule. Safe, easy to reason about. Expensive and slow for large corpora. Okay up to ~100K documents or whenever the corpus fits in a nightly rebuild window.</p>

<h3>Delta sync</h3>
<p>Only re-ingest documents that changed since the last sync. Requires reliable change detection - last-modified timestamps, content hashes, or a change log from the source system. Most common pattern at medium scale.</p>

<h3>Event-driven</h3>
<p>Source system emits events (webhook, message queue, CDC stream) that trigger per-document updates. Near-real-time. Most complex to operate. Required when freshness matters in minutes rather than hours.</p>

<p>Pick the least complex pattern that meets your freshness requirement. Most teams over-engineer this.</p>

<h2>Idempotency</h2>
<p>Every ingestion step must be safely retryable. Networks fail, parsers crash, embedding APIs rate-limit. The pipeline needs to handle partial failures without producing duplicate chunks or corrupted indexes.</p>

<p>Implementation patterns:</p>
<ul>
  <li>Deterministic chunk IDs (hash of document ID + chunk position)</li>
  <li>Upsert by ID, not insert</li>
  <li>Store document-level metadata separately from chunk embeddings so you can reprocess chunks without re-fetching sources</li>
  <li>Use a durable job queue (not in-memory tasks) for anything that runs longer than seconds</li>
</ul>

<h2>The change detection problem</h2>
<p>Most RAG failures in production come from silent data drift: the source system changed, the pipeline didn't notice, and the index is stale.</p>

<p>What to monitor:</p>
<ul>
  <li>Document count per source (sudden drops = upstream broken)</li>
  <li>Time since last successful sync per source</li>
  <li>Hash collisions or version mismatches</li>
  <li>Failed parse rate per document type</li>
  <li>Embedding failures</li>
</ul>

<h2>The permissions propagation problem</h2>
<p>Documents in source systems have access controls. If you don't propagate those controls into your index, you'll leak data across tenants. Every chunk needs to carry its permission metadata from source to retrieval.</p>

<p>Two main patterns:</p>
<ul>
  <li><strong>Static permissions at ingest:</strong> record who can see each chunk at ingestion time. Filter at query time. Fast but requires reindexing when permissions change.</li>
  <li><strong>Dynamic permissions at query:</strong> store a reference to the source document, check permissions against the source system at query time. Slower but always accurate.</li>
</ul>
<p>Static with incremental permission sync is the common production compromise.</p>

<h2>The "where did this come from" problem</h2>
<p>Every chunk in your index must be traceable back to its source document. At minimum:</p>
<ul>
  <li>Source system identifier</li>
  <li>Document ID in that system</li>
  <li>Document URL (for citations and for the user)</li>
  <li>Ingestion timestamp</li>
  <li>Chunk position within the document</li>
  <li>Embedding model version (so you know when to reindex)</li>
</ul>

<p>Without this metadata, your RAG system can't produce real citations, and it can't recover from bad chunks - you can't find and fix what you can't trace.</p>

<h2>Tools I actually use</h2>
<ul>
  <li><strong>Unstructured.io</strong> - polymorphic document parser, handles most file types reasonably</li>
  <li><strong>LlamaIndex</strong> for high-level pipeline orchestration</li>
  <li><strong>Temporal</strong> or <strong>Airflow</strong> for production workflow scheduling</li>
  <li><strong>Celery</strong> or <strong>SQS</strong> for job queues at smaller scale</li>
  <li><strong>Custom Python</strong> for everything that actually ships, because every real corpus has weird edge cases</li>
</ul>

<h2>The build-vs-buy trap</h2>
<p>Commercial "RAG-as-a-service" ingestion tools (Vectara, Superlinked, etc.) save time on the happy path and cost you when your data has edge cases - which it will. For a serious system, expect to own the ingestion pipeline end-to-end. The question isn't whether to build, it's whether to build now or after you've outgrown a vendor.</p>

<p style="margin-top:40px;">Next: <a href="parsing-pdfs.html">Parsing PDFs</a>.</p>
""",
    prev=("When not to use RAG", "../foundations/when-not-to-use.html"),
    nxt=("Parsing PDFs", "parsing-pdfs.html"),
)


write_rag_page(
    slug="docs/parsing-pdfs",
    title="Parsing PDFs",
    description="PDFs are where RAG projects go to die. Here's what works, what doesn't, and the specific libraries I reach for in each situation.",
    reading_time=6,
    body_html="""
<p class="lede">PDFs are where the "we'll just parse the docs" plan meets reality. PDF is not a document format - it's a visual layout format that happens to contain text. Every serious RAG project eventually has a PDF problem. Here's how I think about it.</p>

<h2>The three kinds of PDFs</h2>

<h3>1. Born-digital with clean text layer</h3>
<p>Generated from Word, LaTeX, or pandoc. Text is extractable with basic tools. Usually has a coherent reading order. Still may have headers/footers/page numbers that pollute text.</p>

<h3>2. Born-digital with messy text layer</h3>
<p>Text is there but reading order is scrambled. Multi-column layouts, text boxes, sidebars, footnotes. Basic extraction yields jumbled output. This is the most common production case.</p>

<h3>3. Scanned images</h3>
<p>No text layer. Just pixels. Requires OCR. See <a href="ocr.html">OCR</a>.</p>

<h2>The library landscape</h2>

<h3>PyPDF / pdfplumber</h3>
<p>Good for clean, simple PDFs. Fast and free. Fails on multi-column layouts, tables, and scanned content. My baseline for quick prototyping.</p>

<h3>PyMuPDF (fitz)</h3>
<p>More robust. Handles complex layouts better. Better table detection. Slightly tricky licensing for commercial use (AGPL, requires license for closed-source).</p>

<h3>Unstructured.io</h3>
<p>Opinionated parser that preserves structure: headings, lists, tables. Returns elements with types, which is valuable for structure-aware chunking. Slower than raw text extraction but usually worth the tradeoff.</p>

<h3>Docling (IBM)</h3>
<p>Open-source, strong on complex document layouts. Produces structured output with headings, tables, and lists preserved. Under active development and my current default for complex PDFs.</p>

<h3>LLM-based parsers (GPT-4 Vision, Claude, Gemini)</h3>
<p>Highest quality on difficult documents. Handles layouts, tables, figures, and scanned content. Expensive (dollars per document for complex PDFs). Right tool when accuracy matters more than cost.</p>

<h3>Commercial (Mathpix, Azure Document Intelligence, AWS Textract, Llamaparse)</h3>
<p>Mathpix for math-heavy PDFs. Llamaparse for general high-quality parsing. Azure and AWS are decent general-purpose. All charge per page.</p>

<h2>The parsing decision tree</h2>
<ol>
  <li>Is the PDF text-selectable in Preview/Acrobat? If no → OCR pipeline.</li>
  <li>Is it a single-column, simple layout? pdfplumber or PyMuPDF.</li>
  <li>Does it have tables or complex structure? Docling, Unstructured, or Llamaparse.</li>
  <li>Does it have math, diagrams, or highly specialized content? Mathpix or LLM-based parser.</li>
  <li>Is accuracy more important than per-document cost? LLM-based parser.</li>
</ol>

<h2>The gotchas that cost days</h2>

<h3>Reading order</h3>
<p>PDFs don't store reading order - they store visual positions. A two-column PDF parsed naively produces "column 1 line 1, column 2 line 1, column 1 line 2, column 2 line 2..." which is nonsense. Always check that your parser reorders text correctly on multi-column layouts.</p>

<h3>Headers and footers</h3>
<p>Page numbers, running headers, and footer boilerplate get concatenated into your content unless you strip them. Most retrieval failures traced to "why does it think the answer is on page 47" come from headers polluting chunks.</p>

<h3>Tables</h3>
<p>A table parsed as raw text is a string of numbers with no structure. Either use a parser that preserves tables as structured data (then serialize them into readable form), or detect tables and send them to a dedicated extractor. See <a href="tables-figures.html">tables and figures</a>.</p>

<h3>Figures and charts</h3>
<p>Text extraction drops them entirely. For technical documents, figures often contain 30% of the information. Strategies:</p>
<ul>
  <li>Extract figure captions and embed those</li>
  <li>Send figures through a vision model to generate descriptions, embed the descriptions</li>
  <li>In the index, store figure references alongside text chunks so retrieved chunks can pull in their surrounding visuals</li>
</ul>

<h3>Hyphenation and line breaks</h3>
<p>PDF text often has hyphens at line breaks that become mid-word hyphens after extraction ("im-\\nportant" becomes "im-portant"). Always post-process to rejoin these.</p>

<h3>Ligatures and special characters</h3>
<p>"ﬁ" and "ﬂ" ligatures, Greek letters in math, non-breaking spaces - all of these break tokenization and retrieval if not normalized.</p>

<h2>The ground-truth test</h2>
<p>For any significant PDF corpus, take 10 random documents and spot-check the parsed output against the original. Look specifically for:</p>
<ul>
  <li>Is reading order correct?</li>
  <li>Are tables intelligible?</li>
  <li>Are headings preserved as headings (not mixed into body)?</li>
  <li>Is boilerplate removed?</li>
  <li>Are figures at least referenced?</li>
</ul>
<p>If fewer than 8 of 10 pass, your parser is wrong for this corpus. Don't embed bad text - garbage-in compounds through the rest of the pipeline.</p>

<h2>The commercial reality</h2>
<p>For any serious business-critical RAG system, I recommend budgeting for LLM-based parsing or a commercial service on difficult documents. Over a full corpus, paying $0.05-0.20/page for quality parsing is often cheaper than debugging retrieval failures caused by bad text extraction.</p>

<p style="margin-top:40px;">Next: <a href="parsing-html.html">Parsing HTML + web pages</a>.</p>
""",
    prev=("The ingestion pipeline", "ingestion-pipeline.html"),
    nxt=("Parsing HTML + web pages", "parsing-html.html"),
)


write_rag_page(
    slug="docs/parsing-html",
    title="Parsing HTML + web pages",
    description="Parsing HTML is deceptively hard. Boilerplate, nav menus, ads, and dynamic content all pollute the useful text. Here's how to get clean content reliably.",
    reading_time=5,
    body_html="""
<p class="lede">Every web page has ~10% content and ~90% navigation, ads, menus, footers, cookie banners, and boilerplate. Naive HTML-to-text extraction feeds all of that into your index, which pollutes retrieval and embedding space. Clean web extraction is a discipline.</p>

<h2>The extraction stack</h2>

<h3>1. Fetch</h3>
<p>HTTP GET (or a headless browser for JS-heavy sites). Handle redirects, cookies, user agents, rate limits. Respect robots.txt when applicable.</p>

<h3>2. Dynamic content rendering</h3>
<p>If the site is an SPA (React, Vue, Angular), raw HTML is empty. You need a headless browser (Playwright, Puppeteer) to render the DOM before extraction. Significantly slower and more expensive than static fetching.</p>

<h3>3. Boilerplate removal</h3>
<p>Strip navigation, sidebars, footers, comments, ads. This is the make-or-break step.</p>

<h3>4. Content extraction</h3>
<p>Preserve structure: headings, paragraphs, lists, code blocks, tables.</p>

<h3>5. Link rewriting</h3>
<p>Absolute-ize relative URLs. Keep link targets as metadata if they matter for your use case.</p>

<h2>The library landscape</h2>

<h3>Readability / trafilatura</h3>
<p>Python libraries that heuristically extract "main content" from HTML. Trafilatura is my default - best signal-to-noise ratio on general-purpose web content. Handles blog posts, news articles, documentation pages well.</p>

<h3>Readability.js / Mozilla Readability</h3>
<p>The algorithm that powers browser reader modes. Good baseline. Works well for article-style content.</p>

<h3>BeautifulSoup / lxml</h3>
<p>Low-level HTML parsers. Use when you know the structure and can write specific selectors (e.g., "every .docs-content div"). Precise but brittle - breaks when sites redesign.</p>

<h3>Jina Reader / Diffbot / Firecrawl</h3>
<p>Managed services that return clean markdown from URLs. Jina Reader is free for light use, Firecrawl is the commercial leader for RAG-oriented scraping. Worth it when you have many sources and don't want to maintain extraction logic.</p>

<h3>html-to-text / html-to-markdown</h3>
<p>Naive converters. Avoid for RAG - they preserve all the junk.</p>

<h2>HTML → Markdown is usually the right format</h2>
<p>For RAG, convert HTML to Markdown rather than plaintext. Markdown preserves structure (headings, lists, code, links) in a format that chunking and embeddings both handle well. Plain text loses everything.</p>

<p>My stack: trafilatura or Firecrawl → Markdown → chunker. Skipping to plaintext drops too much signal.</p>

<h2>Patterns for documentation sites</h2>
<p>Developer docs, knowledge bases, and product help centers usually have predictable structure. For these:</p>
<ul>
  <li>Use the site's sitemap.xml as your crawl list</li>
  <li>Target the main content area with a specific CSS selector</li>
  <li>Extract headings as metadata (for structure-aware chunking)</li>
  <li>Preserve code blocks as distinct chunks</li>
  <li>Capture the full breadcrumb path as metadata</li>
</ul>

<h2>Patterns for messy sources (blogs, news, general web)</h2>
<ul>
  <li>Trafilatura with its default config handles most cases</li>
  <li>Filter out pages with very short extracted content (likely boilerplate-only)</li>
  <li>Filter out pages that look identical to each other (deduplicate by content hash)</li>
  <li>Keep the canonical URL if present (many pages have multiple URLs)</li>
</ul>

<h2>The hidden problems</h2>

<h3>Duplicate content</h3>
<p>Many sites have print versions, AMP versions, paginated archives, and tag pages that duplicate core content. Deduplicate aggressively during ingestion.</p>

<h3>Stale + evergreen mixed</h3>
<p>A site might have a 2015 blog post right next to a 2024 product doc. Without publish dates as metadata, retrieval can surface outdated info. Always capture dates when available and use them as filters or boosts.</p>

<h3>Paywalls and auth walls</h3>
<p>Public URL ≠ public content. Check what your scraper is actually seeing. Many sites serve a paywall page with the article name but no content.</p>

<h3>Single-page apps that break fetching</h3>
<p>If curl returns "Loading..." and nothing else, you need a headless browser. This adds 3-10x latency per page and requires significantly more infrastructure.</p>

<h3>Rate limiting</h3>
<p>Aggressive scraping gets blocked. Use polite delays, rotate user agents, respect Retry-After headers. For large-scale scraping of a single domain, talk to them about a partnership or an official feed before you get blocked.</p>

<h2>The quality check</h2>
<p>Same as for PDFs: sample 10 pages randomly from your extracted corpus. Look at the raw extracted text. Is it the article? Is it the article plus ten lines of nav menu? Is it empty because the extraction failed silently? Fix the extraction before embedding.</p>

<p style="margin-top:40px;">Next: <a href="tables-figures.html">Tables and figures</a>.</p>
""",
    prev=("Parsing PDFs", "parsing-pdfs.html"),
    nxt=("Tables and figures", "tables-figures.html"),
)


write_rag_page(
    slug="docs/tables-figures",
    title="Tables and figures",
    description="Tables and figures carry a disproportionate share of information in technical documents. Naive RAG drops most of it. Here's how to handle them.",
    reading_time=5,
    body_html="""
<p class="lede">Tables and figures are where most RAG systems silently lose information. Naive text extraction strips them entirely or converts them to unreadable streams. For technical, financial, scientific, or compliance documents, this means 30-50% of the actual information never reaches the index.</p>

<h2>Why tables are hard</h2>
<p>A table is a two-dimensional data structure. Prose is one-dimensional. When a parser flattens a table into prose, it loses:</p>
<ul>
  <li>The column-row relationship (which value goes with which row and column)</li>
  <li>Header hierarchy (multi-level headers)</li>
  <li>Merged cells</li>
  <li>Units and formatting</li>
  <li>Footnotes and caveats attached to specific cells</li>
</ul>

<h2>Four strategies for tables</h2>

<h3>1. Serialize as readable prose</h3>
<p>Convert each row into a sentence: "In 2023, Revenue was $4.2M, COGS was $1.8M, Gross Margin was 57%." Preserves semantics in a format embeddings handle well. Loses compactness but gains retrievability.</p>

<p>Works for: small to medium tables where the row-level facts are the important thing.</p>

<h3>2. Serialize as Markdown</h3>
<p>Keep the table as Markdown syntax. Preserves structure. Embeddings still handle it reasonably well for retrieval, and the LLM can reason over the original structure during generation.</p>

<p>Works for: tables with clear headers and moderate size (&lt;50 rows).</p>

<h3>3. Chunk per row</h3>
<p>Each row becomes its own chunk, with the table's column headers prepended or added as metadata. Fine-grained retrieval but you lose the row-to-row comparisons.</p>

<p>Works for: large reference tables (product catalogs, drug databases, parts lists).</p>

<h3>4. Keep the table as structured data, retrieve by key</h3>
<p>Store the table in a database. Have the LLM emit a structured query when it needs table data. Not strictly RAG, but a common hybrid for systems that need to reason over tabular data.</p>

<p>Works for: large financial statements, time series, anything with a lot of numeric comparison.</p>

<h2>Picking a strategy</h2>
<p>Look at what questions users actually ask:</p>
<ul>
  <li>"What was revenue in 2022?" → row-level retrieval works</li>
  <li>"How did margin change from 2020 to 2023?" → need multi-row context, so serialize whole small tables or use structured queries</li>
  <li>"Find products with power rating between X and Y" → structured query is the only sane option</li>
</ul>

<h2>Table extraction tools</h2>
<ul>
  <li><strong>Camelot / Tabula</strong> - classic Python table extractors. Good on bordered tables in simple PDFs.</li>
  <li><strong>pdfplumber</strong> - built-in table detection, solid for clean tables.</li>
  <li><strong>Docling</strong> - strong table detection including nested and multi-header tables.</li>
  <li><strong>Azure Document Intelligence, AWS Textract</strong> - commercial OCR with excellent table support.</li>
  <li><strong>LLM vision models</strong> (GPT-4V, Claude, Gemini) - highest quality on complex or messy tables. Expensive.</li>
</ul>

<h2>Figures and images</h2>

<h3>The captions-only baseline</h3>
<p>Extract and embed just the figure caption. Fast, cheap, catches most user questions that reference figures by number or topic.</p>

<h3>The description-generated approach</h3>
<p>Pass the figure image through a vision model to generate a text description. Embed the description. Expensive at scale but captures visual content. Use for technical diagrams, charts, and anything where the image carries real information.</p>

<h3>The retrieve-adjacent-text approach</h3>
<p>When a figure is retrieved, also pull the paragraphs immediately before and after it. Figures rarely stand alone - the surrounding text usually explains what the figure shows.</p>

<h3>The multimodal retrieval approach</h3>
<p>Use a multimodal embedding model (CLIP, Jina Multimodal, Voyage-Multimodal) to embed both images and text into a shared vector space. Retrieval can return images when queries match visual content. Emerging pattern. Works well for product catalogs, image-heavy documentation, medical imaging.</p>

<h2>Putting it together</h2>
<p>For a document with mixed content, my typical pipeline:</p>
<ol>
  <li>Parse into typed elements (text, heading, list, table, figure)</li>
  <li>Chunk text elements with structure-aware chunking</li>
  <li>For each table: generate both a Markdown serialization and a prose description. Embed both.</li>
  <li>For each figure: extract caption. If the figure matters for the use case, generate a vision-model description. Embed caption and description.</li>
  <li>Keep a document-level link between elements so retrieved chunks can pull their table/figure context.</li>
</ol>

<p>This is significantly more work than "dump text into a vector DB" but it's the difference between a RAG system that handles technical docs and one that handles "some docs."</p>

<p style="margin-top:40px;">Next: <a href="ocr.html">OCR for scanned documents</a>.</p>
""",
    prev=("Parsing HTML + web pages", "parsing-html.html"),
    nxt=("OCR for scanned documents", "ocr.html"),
)


write_rag_page(
    slug="docs/ocr",
    title="OCR for scanned documents",
    description="OCR is necessary, imperfect, and cost-sensitive. Here's how to handle scanned PDFs, images, and handwritten content in a RAG pipeline.",
    reading_time=5,
    body_html="""
<p class="lede">Scanned documents are a fact of life in enterprise RAG - legal contracts, old manuals, medical records, government filings. Optical Character Recognition (OCR) is the bridge from pixels to text. It's imperfect, it's slow, and the quality differences between tools are enormous. Here's how I handle it.</p>

<h2>Detecting what needs OCR</h2>
<p>First move: detect whether a document has a usable text layer before running OCR. Running OCR on a clean digital PDF is expensive, slow, and often produces worse text than the embedded text layer.</p>

<p>Heuristics:</p>
<ul>
  <li>Try text extraction first. If you get less than 100 characters per page, suspect scanned.</li>
  <li>Check if PDF has a text layer (PyMuPDF's get_text with "text" mode returns empty for pure images)</li>
  <li>If the PDF was generated from Word/LaTeX, text layer is present. If it's a scan, it isn't.</li>
</ul>

<h2>OCR tools</h2>

<h3>Tesseract</h3>
<p>The open-source baseline. Decades of development. Good on clean printed text, weak on complex layouts, handwriting, and poor scans. Free. Run in Docker to avoid install pain.</p>

<h3>AWS Textract</h3>
<p>Solid general-purpose OCR with structured output (tables, forms, key-value pairs). Charges per page. Production-ready. My default for English-language enterprise documents.</p>

<h3>Azure Document Intelligence</h3>
<p>Comparable to Textract. Slightly better on forms and pre-built document types (invoices, receipts, IDs). Charges per page.</p>

<h3>Google Cloud Vision / Document AI</h3>
<p>Strong on handwritten text and non-English languages. Per-page pricing.</p>

<h3>GPT-4V / Claude / Gemini (LLM vision)</h3>
<p>Highest quality on difficult documents: poor scans, unusual layouts, handwritten annotations, mixed-language content. Slowest and most expensive. Handles layout-aware extraction better than any dedicated OCR tool. My go-to for high-value, low-volume use cases.</p>

<h3>EasyOCR, PaddleOCR</h3>
<p>Open-source alternatives to Tesseract with better multilingual support. Useful when cost matters and Tesseract isn't cutting it.</p>

<h3>Mistral OCR / Marker / Nougat</h3>
<p>Newer specialized models for academic papers, scientific documents, and math. Marker and Nougat are particularly strong on technical content.</p>

<h2>The quality tiers</h2>
<ol>
  <li><strong>Tier 1 (freebie):</strong> Tesseract on clean English print. 95%+ accuracy. Good for most scanned business documents.</li>
  <li><strong>Tier 2 (commercial):</strong> Textract / Azure DI. 98%+ on clean, handles layouts well.</li>
  <li><strong>Tier 3 (LLM vision):</strong> Claude / GPT-4V / Gemini. 99%+ on most content. Handles tables, diagrams, multi-column layouts with context-aware correction.</li>
</ol>

<h2>The specific gotchas</h2>

<h3>Low-quality scans</h3>
<p>Pre-process: deskew, denoise, binarize, increase DPI (300+ for OCR). OpenCV or PIL can do all of this in ten lines. Worth it before any OCR pass.</p>

<h3>Mixed languages</h3>
<p>Some OCR tools auto-detect language, others need it specified. Test your pipeline against multilingual samples early.</p>

<h3>Tables in scans</h3>
<p>Most general OCR returns tables as space-separated text streams that destroy structure. Use a table-aware OCR (Textract, Azure DI) or pass the table region to a vision model for structured extraction.</p>

<h3>Handwriting</h3>
<p>Tesseract: poor. Textract: okay. Azure DI: good. Vision LLMs: best. If your corpus has significant handwriting, pay for the good tool.</p>

<h3>Rotated pages</h3>
<p>Scans often include pages rotated 90° or 180°. Most OCR tools handle this, but not all. Test.</p>

<h3>Multi-column layouts after OCR</h3>
<p>OCR output may have correct characters but wrong reading order. Same problem as born-digital PDFs. Most commercial tools handle this; Tesseract often doesn't.</p>

<h2>Cost engineering</h2>
<p>OCR is the most expensive step in most ingestion pipelines. Strategies:</p>
<ul>
  <li>Tier routing: detect document quality, send clean docs to Tesseract, difficult ones to commercial OCR, only the hardest to vision LLMs.</li>
  <li>Cache results by document hash. Never re-OCR the same document.</li>
  <li>Only OCR pages with actual content (skip blank or nearly-blank pages).</li>
  <li>Deduplicate the corpus before OCR: if you have 50 copies of the same contract, OCR it once.</li>
</ul>

<h2>OCR is not the end</h2>
<p>After OCR, run a cleanup pass:</p>
<ul>
  <li>Remove page numbers, headers, footers</li>
  <li>Rejoin words split across lines by hyphens</li>
  <li>Normalize whitespace and fix common OCR errors ("rn" → "m", "0" → "O" depending on context)</li>
  <li>For LLM-based post-processing: run chunks through a fast model with a prompt to correct OCR artifacts while preserving factual content</li>
</ul>

<p>Garbage-in still compounds. OCR'd text quality bounds retrieval quality.</p>

<p style="margin-top:40px;">Next: <a href="metadata.html">Metadata extraction</a>.</p>
""",
    prev=("Tables and figures", "tables-figures.html"),
    nxt=("Metadata extraction", "metadata.html"),
)


write_rag_page(
    slug="docs/metadata",
    title="Metadata extraction",
    description="Metadata is the quiet multiplier in RAG. Good metadata enables filtering, boosting, access control, and citations. Most teams ship without it and regret it.",
    reading_time=5,
    body_html="""
<p class="lede">Metadata is what turns a flat blob of vectors into a queryable knowledge graph. Good metadata makes retrieval 3-10x better and unlocks features that pure vector search can't do. Most RAG systems ship without it, then spend months bolting it on retroactively.</p>

<h2>What metadata is for</h2>
<ol>
  <li><strong>Filtering.</strong> Only retrieve chunks where product = "Enterprise" and user has access.</li>
  <li><strong>Boosting.</strong> Prefer recent docs, canonical sources, high-authority authors.</li>
  <li><strong>Grouping.</strong> Return top-k diverse sources instead of five chunks from the same doc.</li>
  <li><strong>Citation.</strong> Tell the user "I learned this from [document], section 3.2, published 2024-01-15."</li>
  <li><strong>Access control.</strong> Enforce permissions at retrieval time.</li>
  <li><strong>Debugging.</strong> Trace bad answers back to specific chunks and source documents.</li>
</ol>

<h2>The metadata I always include</h2>

<h3>Provenance</h3>
<ul>
  <li><code>source_system</code> (e.g., "confluence", "google_drive", "s3")</li>
  <li><code>source_id</code> (ID in that system)</li>
  <li><code>source_url</code> (canonical URL)</li>
  <li><code>title</code></li>
  <li><code>author</code></li>
  <li><code>created_at</code>, <code>updated_at</code></li>
  <li><code>ingested_at</code>, <code>embedding_model_version</code></li>
</ul>

<h3>Content structure</h3>
<ul>
  <li><code>document_type</code> (e.g., "blog", "manual", "policy")</li>
  <li><code>section_path</code> (e.g., "Setup &gt; Authentication &gt; OAuth")</li>
  <li><code>chunk_position</code> (index within document)</li>
  <li><code>chunk_total</code> (so you can reconstruct)</li>
  <li><code>element_type</code> (e.g., "paragraph", "table", "heading", "list_item")</li>
</ul>

<h3>Access + governance</h3>
<ul>
  <li><code>tenant_id</code></li>
  <li><code>visibility</code> (public, internal, restricted)</li>
  <li><code>permissions</code> (list of roles or groups with access)</li>
  <li><code>data_classification</code> (public, confidential, PII, etc.)</li>
</ul>

<h3>Domain-specific</h3>
<ul>
  <li><code>product</code>, <code>version</code>, <code>language</code></li>
  <li><code>topics</code>, <code>tags</code> (extracted or human-assigned)</li>
  <li><code>entities</code> (named entities extracted from the text)</li>
</ul>

<h2>Where metadata comes from</h2>

<h3>From the source system</h3>
<p>Confluence gives you author, labels, space, creation date. Drive gives you owner, sharing settings, MIME type. APIs usually return more metadata than you think - capture it all, decide what to use later.</p>

<h3>From the document itself</h3>
<p>Title from the first heading. Author from a byline. Date from a publication header. Section hierarchy from structure-aware parsing. Take metadata from inside the document wherever possible - it's often more accurate than the source system's metadata.</p>

<h3>Inferred via LLM or NER</h3>
<p>Run an LLM or a named-entity recognizer over each chunk to extract:</p>
<ul>
  <li>Named entities (people, organizations, locations, products)</li>
  <li>Topics / categories</li>
  <li>Sentiment</li>
  <li>Document type (if not provided)</li>
  <li>Language</li>
  <li>Summary (useful for reranking and LLM-based routing)</li>
</ul>

<p>LLM enrichment costs money per chunk but often pays back in retrieval quality. A small model (Haiku, GPT-4o-mini) works fine for structured extraction.</p>

<h2>Metadata filtering in retrieval</h2>
<p>Most production vector DBs support filtered search: "find nearest neighbors where tenant_id = 'acme' AND visibility != 'restricted' AND updated_at &gt; '2024-01-01'."</p>

<p>The pattern:</p>
<ol>
  <li>User sends query + their user context (tenant, role, etc.)</li>
  <li>Build filter from user context + query-derived constraints</li>
  <li>Run vector search with filter applied</li>
  <li>Rerank or boost based on remaining metadata (recency, authority)</li>
</ol>

<h2>Pre-filter vs post-filter</h2>
<p>Vector DBs handle metadata filtering in one of two ways:</p>

<h3>Pre-filter</h3>
<p>Narrow the candidate set to matching metadata first, then search. Exact - returns only documents matching the filter. Slow when filters are selective.</p>

<h3>Post-filter</h3>
<p>Do vector search first, then filter results. Fast but may return fewer-than-k results if matches are rare.</p>

<h3>Hybrid (dynamic)</h3>
<p>The DB decides based on filter selectivity. Pinecone, Qdrant, and Weaviate do this well.</p>

<p>For narrow filters (e.g., "tenant_id = X"), pre-filter is usually right. For broad filters (e.g., "language = en"), post-filter is fine.</p>

<h2>The access control pattern</h2>
<p>Every chunk carries a list of roles or groups allowed to see it. At query time, compute the user's allowed roles. Filter retrieval to chunks where <code>permissions</code> intersects with the user's roles. This is how you run multi-tenant RAG without leaks.</p>

<p>See also <a href="../cases/multi-tenant.html">multi-tenant RAG</a> and <a href="../prod/security.html">security</a>.</p>

<h2>The common mistakes</h2>
<ul>
  <li><strong>Missing timestamps.</strong> Users get outdated answers and there's no way to boost recency.</li>
  <li><strong>No source_url.</strong> Citations are broken or fake.</li>
  <li><strong>Permissions as a string instead of a list.</strong> Makes multi-role access impossible to query.</li>
  <li><strong>Mutable metadata stored immutably.</strong> When a document's permissions change, the index is out of sync until you reindex.</li>
  <li><strong>No embedding_model_version.</strong> When you upgrade embedding models, you can't tell which chunks need reprocessing.</li>
</ul>

<p style="margin-top:40px;">Next: <a href="../chunking/why-chunking.html">Why chunking matters</a>.</p>
""",
    prev=("OCR for scanned documents", "ocr.html"),
    nxt=("Why chunking matters", "../chunking/why-chunking.html"),
)


# ============================================================
# CHUNKING (6 pages)
# ============================================================

write_rag_page(
    slug="chunking/why-chunking",
    title="Why chunking matters",
    description="Chunking is the most under-thought part of most RAG systems. Here's why it matters, why the defaults are usually wrong, and what to optimize for.",
    reading_time=5,
    body_html="""
<p class="lede">Chunking is where the most avoidable quality loss in RAG happens. Most teams use LangChain's default 1000-character splitter and never revisit the decision. That default is wrong for almost every real corpus. Chunking affects retrieval quality more than most teams realize, and getting it right is one of the highest-leverage changes you can make.</p>

<h2>Why chunking exists at all</h2>
<p>Three reasons you can't just embed whole documents:</p>
<ol>
  <li><strong>Embedding context windows.</strong> Most embedding models cap at 512-8192 tokens. Documents often exceed this.</li>
  <li><strong>Retrieval granularity.</strong> If the answer to a question lives in one paragraph, retrieving the whole 50-page document buries it.</li>
  <li><strong>Prompt context limits.</strong> Even with long-context LLMs, passing 10 whole documents of retrieved context is expensive and dilutes attention.</li>
</ol>

<h2>What you're optimizing for</h2>
<p>A good chunk has three properties:</p>
<ul>
  <li><strong>Self-contained meaning.</strong> A reader can understand it without surrounding context.</li>
  <li><strong>Single topic.</strong> The chunk is about one thing, not a mix.</li>
  <li><strong>Retrievable.</strong> It matches the kind of query a user would make.</li>
</ul>
<p>Fixed-size chunking often fails on all three. A 1000-character window can split mid-sentence, blend two topics, and lose enough context that the chunk is meaningless standalone.</p>

<h2>The chunking trade-off curve</h2>

<h3>Too small</h3>
<ul>
  <li>Fragments without context</li>
  <li>High recall, low precision (too many false-positive matches)</li>
  <li>LLM can't reason about the isolated snippet</li>
  <li>More chunks = more embeddings = more cost</li>
</ul>

<h3>Too large</h3>
<ul>
  <li>Single chunk covers multiple topics, embedding becomes a muddled average</li>
  <li>Lower recall (the specific answer is buried in surrounding text)</li>
  <li>LLM context budget wasted on irrelevant content</li>
  <li>Harder to cite precisely</li>
</ul>

<h3>Goldilocks</h3>
<p>Usually 200-800 tokens for prose, with some overlap, and respecting natural boundaries (paragraphs, sections). Exact sweet spot depends heavily on content type.</p>

<h2>The overlap question</h2>
<p>Overlap (including some tokens from the end of the previous chunk in the start of the next) prevents information loss at boundaries. Common settings: 10-20% overlap.</p>

<p>Overlap helps when:</p>
<ul>
  <li>Important information spans arbitrary boundaries</li>
  <li>Context before/after a fact matters for answering</li>
  <li>You're using fixed-size chunking without structure awareness</li>
</ul>

<p>Overlap hurts when:</p>
<ul>
  <li>You have good natural boundaries (paragraphs, headings) and should use those instead</li>
  <li>You care about precision (overlapping chunks can match the same query and both show up in top-k, reducing diversity)</li>
</ul>

<h2>The chunking-for-query principle</h2>
<p>Chunks should look like the retrievable unit of a question, not the unit of a document. If users ask "what's our refund policy?" the right chunk is the refund policy paragraph - not arbitrarily chunked 1000-character slices of a policy document.</p>

<p>This means chunking strategy depends on the <em>queries</em> you expect, not just the documents you have. For many corpora, semantic or structure-aware chunking beats fixed-size because it produces chunks that look more like complete thoughts.</p>

<h2>Why the defaults are wrong</h2>
<p>LangChain's default RecursiveCharacterTextSplitter with 1000 chars and 200 overlap is:</p>
<ul>
  <li>Too large for short-query retrieval</li>
  <li>Too small for reasoning-intensive content</li>
  <li>Blind to structure (doesn't care about headings, sections, or paragraphs)</li>
  <li>Character-based (ignores that tokens vary in size across languages)</li>
</ul>

<p>It's a reasonable zero-config starting point. It's a terrible final answer.</p>

<h2>Chunking strategies by content type</h2>
<ul>
  <li><strong>Documentation / knowledge bases:</strong> structure-aware, by heading sections</li>
  <li><strong>Long prose / books:</strong> semantic or recursive, 400-800 tokens</li>
  <li><strong>FAQs / Q&amp;A:</strong> one question+answer per chunk</li>
  <li><strong>Code:</strong> function/class/file boundaries (see <a href="chunking-code.html">chunking code</a>)</li>
  <li><strong>Chat logs / conversational:</strong> by conversation turn or topic shift</li>
  <li><strong>Legal / contracts:</strong> by clause with surrounding context</li>
  <li><strong>Scientific papers:</strong> by section, with special handling for abstracts and references</li>
</ul>

<h2>The experiment mindset</h2>
<p>Chunking is one of the easiest things to A/B test in RAG. Index the same corpus with different chunking strategies, run the same eval set against both, compare retrieval metrics. Most teams never do this. The teams that do typically find their chunking baseline was leaving 20-40% of retrieval quality on the table.</p>

<p style="margin-top:40px;">Next: <a href="fixed-size.html">Fixed-size chunking</a>.</p>
""",
    prev=("Metadata extraction", "../docs/metadata.html"),
    nxt=("Fixed-size chunking", "fixed-size.html"),
)


write_rag_page(
    slug="chunking/fixed-size",
    title="Fixed-size chunking",
    description="Fixed-size chunking is the simplest strategy. It's the default for a reason and a trap for a reason. Here's when it works and how to tune it.",
    reading_time=4,
    body_html="""
<p class="lede">Fixed-size chunking splits text into equal-sized pieces by character count or token count. It's the simplest strategy, the default in almost every RAG framework, and a perfectly reasonable baseline for many corpora. It's also the first thing to reconsider when your retrieval underperforms.</p>

<h2>How it works</h2>
<ol>
  <li>Pick a chunk size (e.g., 512 tokens)</li>
  <li>Pick an overlap (e.g., 64 tokens)</li>
  <li>Iterate through the document, emitting chunks of the target size with overlap between consecutive chunks</li>
</ol>

<h2>Character-based vs token-based</h2>
<p>Character-based is simpler and faster. Token-based is more accurate because embedding models have token context limits, not character limits.</p>
<ul>
  <li>English prose: ~4 characters per token, so 2000 characters ≈ 500 tokens</li>
  <li>Code: ~3 characters per token</li>
  <li>Non-English or heavy punctuation: varies widely</li>
</ul>
<p>Use token-based chunking in production. Character-based is fine for prototyping.</p>

<h2>The sweet spots</h2>
<ul>
  <li><strong>Short, factual content (FAQs, definitions):</strong> 100-200 tokens</li>
  <li><strong>Typical prose:</strong> 400-600 tokens</li>
  <li><strong>Reasoning-heavy technical content:</strong> 600-1000 tokens</li>
  <li><strong>Narrative or contextual content:</strong> 800-1200 tokens</li>
</ul>
<p>Overlap typically 10-15% of chunk size.</p>

<h2>When fixed-size works well</h2>
<ul>
  <li>Uniform content type (e.g., all blog posts, all similar-length docs)</li>
  <li>Prose-dominant content without strong structure</li>
  <li>Early prototyping before you know query patterns</li>
  <li>Corpora where structural metadata is unreliable</li>
</ul>

<h2>When fixed-size breaks</h2>
<ul>
  <li>Mixed content (prose + tables + code): size that works for one doesn't work for others</li>
  <li>Strong document structure (headings, sections) where boundaries carry meaning</li>
  <li>Content where semantic boundaries matter (legal clauses, code functions)</li>
  <li>Very short content (individual FAQs that shouldn't be combined)</li>
</ul>

<h2>The implementation details that matter</h2>

<h3>Don't split mid-word</h3>
<p>Naive character splitting can break "chunk" into "chu" and "nk". Always snap to word boundaries.</p>

<h3>Prefer sentence boundaries</h3>
<p>Even with fixed-size targets, snap to the nearest sentence end (or paragraph end) within a tolerance window. Keeps each chunk a complete thought.</p>

<h3>Handle short documents</h3>
<p>If a document is shorter than your chunk size, don't pad it or drop it. Emit one chunk with the full content.</p>

<h3>Deterministic IDs</h3>
<p>Chunk IDs should be stable across re-ingestions. Use hash(document_id + chunk_position) so the same content always gets the same chunk ID and you can do proper upserts.</p>

<h2>The experiment to run</h2>
<p>For any non-trivial corpus, test three chunk sizes (e.g., 256, 512, 1024 tokens) against the same eval set. Often the best size is 30-50% off from your gut estimate. The only way to know is to measure.</p>

<p style="margin-top:40px;">Next: <a href="semantic.html">Semantic chunking</a>.</p>
""",
    prev=("Why chunking matters", "why-chunking.html"),
    nxt=("Semantic chunking", "semantic.html"),
)


write_rag_page(
    slug="chunking/semantic",
    title="Semantic chunking",
    description="Semantic chunking splits on meaning, not size. It uses embeddings to find natural topic boundaries. Here's how and when it's worth the extra cost.",
    reading_time=5,
    body_html="""
<p class="lede">Semantic chunking splits text where the meaning changes, not where a character counter runs out. Instead of "1000 characters from here, then overlap, then 1000 more," it asks: "where does one idea end and the next begin?" The result is chunks that look more like coherent thoughts, which usually retrieve better than arbitrary slices.</p>

<h2>The core idea</h2>
<ol>
  <li>Split the document into candidate boundaries (sentences or paragraphs)</li>
  <li>Embed each candidate</li>
  <li>Measure the similarity between adjacent candidates</li>
  <li>When similarity drops below a threshold, you've hit a topic boundary - start a new chunk</li>
</ol>

<p>The output: variable-length chunks that each cover a single topic or subtopic.</p>

<h2>The algorithm in detail</h2>

<h3>Sentence-level approach</h3>
<pre style="background:#f5f5f7; padding:16px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
1. Split document into sentences
2. Embed each sentence
3. Compute cosine similarity between sentence i and sentence i+1
4. If similarity &lt; threshold, mark as boundary
5. Form chunks by grouping consecutive sentences between boundaries
6. If a chunk is too small, merge with neighbor
7. If a chunk is too large, split at the weakest similarity within it
</pre>

<h3>Window-based approach</h3>
<p>Instead of comparing sentence-to-sentence (noisy), compare windows of N sentences to the next N. Smoother signal, better boundaries.</p>

<h3>Percentile-based thresholding</h3>
<p>Instead of a fixed similarity threshold (which varies by embedding model), use the Nth percentile of all adjacent similarities in the document. E.g., split at the bottom 5% of similarities. Adapts to each document's intrinsic similarity distribution.</p>

<h2>When semantic chunking wins</h2>
<ul>
  <li>Long-form content with shifting topics (books, long articles, research papers)</li>
  <li>Mixed content where one part is explanation, another is examples, another is references</li>
  <li>Content where manual structure (headings) isn't available or isn't reliable</li>
  <li>Cases where fixed-size chunking is demonstrably splitting mid-thought</li>
</ul>

<h2>When it's overkill</h2>
<ul>
  <li>Short documents where one or two chunks cover the whole thing anyway</li>
  <li>Highly structured content (docs with clear headings) - use structure-aware chunking instead</li>
  <li>Very homogeneous content (FAQs, product catalog entries) where topic boundaries are already obvious from structure</li>
  <li>When embedding costs matter and the corpus is large</li>
</ul>

<h2>The cost</h2>
<p>Semantic chunking requires embedding every sentence or window during ingestion - often 5-20x more embedding calls than you'd need for retrieval alone. For a 100M-token corpus, this is a material cost.</p>

<p>Mitigation: use a cheap embedding model for chunking (text-embedding-3-small, open-source models) and a better one for the retrieval index. The chunking-time embeddings don't have to match your retrieval embeddings.</p>

<h2>The tuning knobs</h2>
<ul>
  <li><strong>Similarity threshold</strong> (or percentile): controls how often you split. Lower = more chunks, smaller size.</li>
  <li><strong>Window size</strong>: sentence-level is noisy, window of 3-5 sentences is smoother.</li>
  <li><strong>Min/max chunk size</strong>: prevent degenerate cases. Clamp between, say, 100 and 1500 tokens.</li>
  <li><strong>Merge strategy for small chunks</strong>: merge with previous, next, or highest-similarity neighbor.</li>
</ul>

<h2>Implementations</h2>
<ul>
  <li><strong>LlamaIndex SemanticSplitterNodeParser</strong>: the reference implementation. Works. Configurable.</li>
  <li><strong>LangChain SemanticChunker</strong>: similar, different defaults.</li>
  <li><strong>Custom</strong>: the algorithm is ~30 lines of Python. Most teams who care end up writing their own.</li>
</ul>

<h2>The diminishing returns question</h2>
<p>Semantic chunking usually beats fixed-size by 5-15% on retrieval metrics for long-form prose. For highly structured content, structure-aware chunking beats both. Before switching to semantic, ask: do my documents have structure I could use instead? If yes, use that. Semantic is the fallback for unstructured content.</p>

<p style="margin-top:40px;">Next: <a href="recursive.html">Recursive chunking</a>.</p>
""",
    prev=("Fixed-size chunking", "fixed-size.html"),
    nxt=("Recursive chunking", "recursive.html"),
)


write_rag_page(
    slug="chunking/recursive",
    title="Recursive chunking",
    description="Recursive chunking tries natural separators in order of preference. It's a pragmatic middle ground between fixed-size and semantic, and it's often the best default.",
    reading_time=4,
    body_html="""
<p class="lede">Recursive chunking is the pragmatic middle ground: try to split on natural boundaries (paragraphs, then sentences, then spaces), but enforce a size limit. It's simple, fast, and usually the best default. It's what LangChain's RecursiveCharacterTextSplitter does, and it's a big improvement over pure fixed-size chunking.</p>

<h2>The algorithm</h2>
<ol>
  <li>Define a list of separators in order of preference: typically ["\\n\\n", "\\n", ". ", " ", ""]</li>
  <li>Try to split the text on the first separator</li>
  <li>If any resulting piece is still larger than the target size, recursively split that piece using the next separator</li>
  <li>Continue until all pieces fit within the target size</li>
  <li>Combine adjacent pieces to approach the target size without exceeding it</li>
</ol>

<p>The result: chunks that prefer paragraph boundaries, fall back to sentence boundaries, and only split mid-sentence as a last resort.</p>

<h2>Why it works well as a default</h2>
<ul>
  <li>Respects natural text structure without requiring structure-aware parsing</li>
  <li>Avoids splitting mid-sentence in most cases</li>
  <li>Works on any plaintext without configuration</li>
  <li>Fast: no embeddings required during chunking</li>
  <li>Deterministic: same input produces same chunks</li>
</ul>

<h2>The separator list matters</h2>
<p>Default separator lists are reasonable for generic prose. For specific content types, customize:</p>

<ul>
  <li><strong>Markdown:</strong> add heading separators first: ["\\n# ", "\\n## ", "\\n### ", "\\n\\n", "\\n", ". ", " "]</li>
  <li><strong>Code:</strong> use language-aware separators (see <a href="chunking-code.html">chunking code</a>)</li>
  <li><strong>HTML:</strong> convert to Markdown first, then use Markdown separators</li>
  <li><strong>Legal/technical:</strong> add numbered section separators: ["\\n\\n§", "\\n\\n(", "\\n\\n"]</li>
</ul>

<h2>Size tuning</h2>
<p>Same sweet spots as fixed-size:</p>
<ul>
  <li>Chunk size: 400-800 tokens for general prose</li>
  <li>Chunk overlap: 10-15% of chunk size</li>
  <li>Use tokens, not characters</li>
</ul>

<h2>When recursive falls short</h2>
<ul>
  <li>Very heterogeneous content (mixed prose, tables, code) where one separator strategy doesn't fit</li>
  <li>Long narrative with few paragraph breaks (the recursive splitter falls back to sentence or word splits)</li>
  <li>Content where structure should drive chunking (headings, sections) rather than just natural separators</li>
</ul>

<h2>The hybrid pattern</h2>
<p>The strongest practical chunking strategy for most corpora:</p>
<ol>
  <li>Parse the document into structural elements (headings, paragraphs, lists, tables)</li>
  <li>Apply recursive chunking within each structural element</li>
  <li>Respect element boundaries - never merge a heading into a paragraph, never split a table across chunks</li>
</ol>
<p>This combines recursive chunking's simplicity with structure-aware chunking's semantic respect. See <a href="structure-aware.html">structure-aware chunking</a>.</p>

<h2>Common mistakes</h2>
<ul>
  <li>Forgetting to configure separators for non-English content (punctuation differs)</li>
  <li>Using character-based when the embedding model is token-based (causes overflow on dense text)</li>
  <li>Setting overlap too high (20-30%), which wastes embeddings and dilutes retrieval diversity</li>
  <li>Using defaults on Markdown, which treats headings as regular text and fragments sections</li>
</ul>

<p style="margin-top:40px;">Next: <a href="structure-aware.html">Structure-aware chunking</a>.</p>
""",
    prev=("Semantic chunking", "semantic.html"),
    nxt=("Structure-aware chunking", "structure-aware.html"),
)


write_rag_page(
    slug="chunking/structure-aware",
    title="Structure-aware chunking",
    description="Structure-aware chunking uses document hierarchy (headings, sections, lists) as the primary boundary signal. For any corpus with real structure, this beats everything.",
    reading_time=5,
    body_html="""
<p class="lede">Structure-aware chunking uses the document's own organization as the chunk boundary: headings, sections, lists, tables. For any corpus that has real structure (technical docs, wikis, legal documents, Markdown, HTML), this is the highest-performing chunking strategy. It's also the most underused.</p>

<h2>The core idea</h2>
<p>Authors already decided where ideas begin and end - that's what headings and paragraphs are. Respect their decisions.</p>

<p>Chunk boundaries come from:</p>
<ul>
  <li>Heading changes (H1, H2, H3 shifts)</li>
  <li>Section breaks</li>
  <li>List boundaries</li>
  <li>Table boundaries</li>
  <li>Code block boundaries</li>
</ul>

<h2>The algorithm</h2>
<ol>
  <li>Parse document into typed elements with hierarchy (heading levels, sections, lists, etc.)</li>
  <li>Walk the element tree, grouping adjacent elements under the same heading into candidate chunks</li>
  <li>If a candidate chunk exceeds target size, split it by sub-element (or by recursive chunking within)</li>
  <li>If a candidate chunk is too small, merge it with the next one (but only within the same section)</li>
  <li>Never break across top-level sections or merge across major heading transitions</li>
</ol>

<h2>The heading context trick</h2>
<p>Every chunk carries its heading path as metadata or prepended text. For a chunk under "Setup &gt; Authentication &gt; OAuth &gt; Configuration", the chunk text might be prepended with:</p>

<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
# Setup &gt; Authentication &gt; OAuth &gt; Configuration

[actual chunk content...]
</pre>

<p>The LLM and embedding model both benefit from knowing where a chunk sits in the document hierarchy. Without this, a chunk about "rate limits" could be about API rate limits, OAuth token rate limits, or webhook rate limits - all of which might exist in the same document.</p>

<h2>Element-type-specific rules</h2>

<h3>Headings</h3>
<p>Never a chunk by itself. Attach to the following content.</p>

<h3>Tables</h3>
<p>Never split. Serialize as a single chunk with surrounding context. See <a href="../docs/tables-figures.html">tables and figures</a>.</p>

<h3>Code blocks</h3>
<p>Never split within. Often a chunk by themselves plus a surrounding context chunk.</p>

<h3>Lists</h3>
<p>Keep lists together when possible. If a list is huge (e.g., a reference list), chunk by list sections or by logical groups.</p>

<h3>Images/figures</h3>
<p>Attach to nearest text chunk. Store figure metadata in chunk metadata. See <a href="../docs/tables-figures.html">tables and figures</a>.</p>

<h2>The Markdown case</h2>
<p>Markdown is the easiest case. Headings are unambiguous, paragraphs are clear, code blocks are explicit. A good Markdown chunker:</p>
<ol>
  <li>Parses into an AST</li>
  <li>Walks headings, creating sections</li>
  <li>Produces one chunk per section, with heading hierarchy as metadata</li>
  <li>Splits large sections on subheadings or natural paragraph boundaries</li>
  <li>Preserves code blocks, tables, and lists as atomic units</li>
</ol>

<h2>The HTML case</h2>
<p>HTML is Markdown's messy cousin. Parse into DOM, identify content containers, extract hierarchical sections from heading tags. Convert to Markdown for downstream processing, then chunk as Markdown.</p>

<h2>The PDF case</h2>
<p>PDFs don't have guaranteed structure, but good parsers (Docling, Unstructured, Llamaparse) return typed elements with heading levels inferred from font size, style, and position. Quality of structure-aware chunking depends heavily on parser quality - see <a href="../docs/parsing-pdfs.html">parsing PDFs</a>.</p>

<h2>Why it outperforms fixed-size</h2>
<ul>
  <li>Chunks align with semantic units (one section = one chunk)</li>
  <li>Heading context disambiguates ambiguous terms</li>
  <li>Retrieved chunks are self-contained and LLM-friendly</li>
  <li>Citations are natural ("from Section 3.2")</li>
  <li>User experience improves because returned chunks look like explanations, not fragments</li>
</ul>

<h2>Implementation</h2>
<ul>
  <li><strong>Unstructured.io</strong> returns typed elements suitable for structure-aware chunking out of the box</li>
  <li><strong>LlamaIndex MarkdownNodeParser / HTMLNodeParser</strong> handle structure</li>
  <li><strong>Custom parsers</strong> for domain-specific document types (legal contracts, medical records) often pay back quickly</li>
</ul>

<h2>When it's overkill</h2>
<ul>
  <li>Plain text without structure (chat logs, emails without formatting)</li>
  <li>Very short documents where one chunk covers everything</li>
  <li>Homogeneous corpora (all blog posts of similar length and shape)</li>
</ul>

<p>For everything else - documentation, knowledge bases, reports, books, technical manuals - structure-aware chunking is worth the extra engineering.</p>

<p style="margin-top:40px;">Next: <a href="chunking-code.html">Chunking code</a>.</p>
""",
    prev=("Recursive chunking", "recursive.html"),
    nxt=("Chunking code", "chunking-code.html"),
)


write_rag_page(
    slug="chunking/chunking-code",
    title="Chunking code",
    description="Code is not prose. Function, class, and file boundaries matter more than line counts. Here's how to chunk code for retrieval without destroying its structure.",
    reading_time=5,
    body_html="""
<p class="lede">Code has syntax and structure that prose doesn't. Fixed-size chunking of a Python file can split a function in the middle, which makes both halves useless for retrieval. Chunking code needs its own rules, and the rules are straightforward once you accept that code is not prose.</p>

<h2>The principle</h2>
<p>Code chunks should align with semantic units of the language:</p>
<ul>
  <li>Functions</li>
  <li>Classes</li>
  <li>Methods</li>
  <li>Modules (for small files)</li>
  <li>Logical blocks (for scripts without functions)</li>
</ul>

<p>Never split a function across two chunks. Never put half a class definition in one chunk and half in another.</p>

<h2>Language-aware parsers</h2>

<h3>Tree-sitter</h3>
<p>Industry-standard incremental parser with grammars for 100+ languages. Produces concrete syntax trees from source code. The backbone of most serious code-chunking implementations.</p>

<h3>LangChain CodeSplitter</h3>
<p>Uses tree-sitter under the hood for common languages. Works for prototyping.</p>

<h3>Language-specific AST tools</h3>
<ul>
  <li>Python: <code>ast</code> module</li>
  <li>JavaScript/TypeScript: <code>@babel/parser</code>, tsc's compiler API</li>
  <li>Go: <code>go/ast</code></li>
  <li>Rust: <code>syn</code></li>
  <li>Java: JavaParser</li>
</ul>

<h2>The chunking strategy by code type</h2>

<h3>Small file (&lt; 500 tokens)</h3>
<p>One chunk for the whole file.</p>

<h3>Medium file (500-2000 tokens)</h3>
<p>One chunk per top-level definition (function, class, module). Keep imports and file-level context attached to the first chunk.</p>

<h3>Large file (&gt; 2000 tokens)</h3>
<p>Split by class or function. For large classes, one chunk per method with class signature prepended as context.</p>

<h3>Monolithic function (rare but real)</h3>
<p>If a single function exceeds chunk size, split by logical blocks (while respecting brace matching). This is a code smell anyway - surface it in documentation.</p>

<h2>Context enrichment</h2>
<p>Each code chunk benefits from surrounding context:</p>
<ul>
  <li>File path and project structure</li>
  <li>Class signature (for method chunks)</li>
  <li>Import statements from the same file</li>
  <li>Module docstring</li>
  <li>Immediate preceding/following functions (for cross-reference understanding)</li>
</ul>

<p>Pattern: prepend a context header to each chunk:</p>

<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
# File: services/payments/processor.py
# Module docstring: Handles payment processing and refunds.
# Class: PaymentProcessor
# Imports: stripe, pydantic, ..repositories.orders

def process_refund(self, order_id: str, amount: Decimal) -&gt; RefundResult:
    ...
</pre>

<h2>Embedding models for code</h2>
<p>General-purpose text embeddings work for code but not optimally. Code-specific embedding models include:</p>
<ul>
  <li><strong>Voyage Code</strong> - optimized for code retrieval</li>
  <li><strong>OpenAI text-embedding-3-large</strong> with code-specific prompting</li>
  <li><strong>CodeBERT, GraphCodeBERT</strong> - research models</li>
  <li><strong>jina-embeddings-v2-base-code</strong> - open-source code embeddings</li>
</ul>

<p>For systems that primarily retrieve code, a code-specific embedding model typically gives 15-30% better retrieval quality.</p>

<h2>Code + docs hybrid</h2>
<p>Most documentation RAG systems need to retrieve across code AND prose:</p>
<ul>
  <li>API reference docs (prose)</li>
  <li>Code examples (code)</li>
  <li>Error messages and their causes (mixed)</li>
  <li>Changelog and migration guides (prose with embedded code)</li>
</ul>

<p>Strategy: chunk prose and code with their respective strategies, embed everything into the same index with element_type metadata. At retrieval, you can optionally filter or boost by type depending on query intent.</p>

<h2>Code search use case specifics</h2>
<p>If the use case is "find the function that does X" (semantic code search):</p>
<ul>
  <li>Embed function name + signature + docstring + body as the chunk</li>
  <li>For very large bodies, emit a second chunk with just name + signature + docstring (higher weight for name-based queries)</li>
  <li>Include function invocations in the chunk context (helps with "how is this used" queries)</li>
</ul>

<h2>The common mistakes</h2>
<ul>
  <li>Using prose chunking defaults on code (splits functions)</li>
  <li>Treating code and comments as separate chunks (they reinforce each other)</li>
  <li>Dropping imports (they encode dependencies)</li>
  <li>Ignoring file structure (a function's meaning depends on what file it's in)</li>
</ul>

<p style="margin-top:40px;">Next: <a href="../embeddings/what-are-embeddings.html">What embeddings are</a>.</p>
""",
    prev=("Structure-aware chunking", "structure-aware.html"),
    nxt=("What embeddings are", "../embeddings/what-are-embeddings.html"),
)

print("\n✓ RAG Part 1: Hub + Foundations + Documents + Chunking (16 pages)")
