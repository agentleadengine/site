#!/usr/bin/env python3
"""RAG content part 2: Embeddings + Vector Stores + Retrieval (18 pages)."""
from _build_rag import write_rag_page


# ============================================================
# EMBEDDINGS (5 pages)
# ============================================================

write_rag_page(
    slug="embeddings/what-are-embeddings",
    title="What embeddings are",
    description="Embeddings turn text into vectors where semantically similar text is close in space. Here's the mental model and what actually matters about them for RAG.",
    reading_time=5,
    body_html="""
<p class="lede">An embedding is a vector of numbers that represents a piece of text. Two pieces of text with similar meaning produce vectors that point in similar directions. That's the entire idea. The rest is engineering: which model produces those vectors, how many dimensions, at what cost, for what content.</p>

<h2>The geometry</h2>
<p>Embedding models map text into a high-dimensional space (typically 768, 1024, 1536, or 3072 dimensions). In this space:</p>
<ul>
  <li>"Reset my password" and "I forgot my login" are close (similar meaning)</li>
  <li>"Reset my password" and "What's the weather" are far apart</li>
  <li>Similarity is measured with cosine similarity (angle between vectors) or dot product</li>
</ul>

<p>This geometry is how retrieval works: embed the user's query, find the nearest neighbors in your index, return those chunks.</p>

<h2>How embedding models learn this</h2>
<p>Embedding models are trained on massive pairs of related text — from semi-supervised scraping, from annotated datasets, or from contrastive learning objectives. The model is rewarded when its vectors for "similar" pairs are close and "dissimilar" pairs are far apart. Over billions of examples, it learns a space where semantic similarity maps to geometric proximity.</p>

<h2>What embeddings are good at</h2>
<ul>
  <li>Synonyms and paraphrases ("car" ≈ "automobile")</li>
  <li>Cross-lingual (in multilingual models)</li>
  <li>Topic matching ("payment failed" ≈ chunks about billing issues)</li>
  <li>Abstract relationships ("Jeff Bezos" ≈ "Amazon founder")</li>
</ul>

<h2>What embeddings are bad at</h2>
<ul>
  <li>Exact string matching (product codes, UUIDs, specific part numbers)</li>
  <li>Negation ("does NOT include X" often embeds similarly to "includes X")</li>
  <li>Rare named entities not well-represented in training data</li>
  <li>Long documents with multiple topics (the average doesn't represent any one topic well)</li>
  <li>Fine distinctions in technical domains (two very similar-sounding API calls with different behavior)</li>
</ul>

<p>These failure modes are why pure vector search underperforms. Hybrid search (dense + sparse) exists specifically to cover embedding weaknesses.</p>

<h2>Dense vs sparse</h2>
<ul>
  <li><strong>Dense embeddings</strong> (what most people mean): continuous vectors from a neural model. Good at semantic similarity, weak at exact matches.</li>
  <li><strong>Sparse embeddings</strong> (BM25, SPLADE): high-dimensional vectors with mostly zero values, where each dimension corresponds to a term or learned token. Good at exact matches and keyword-heavy queries.</li>
</ul>

<p>Modern RAG often combines both — see <a href="../retrieval/hybrid.html">hybrid retrieval</a>.</p>

<h2>The two things that matter for RAG</h2>
<ol>
  <li><strong>Model quality.</strong> How well the model captures the semantics of your domain.</li>
  <li><strong>Cost.</strong> Per-million-token pricing for API models, inference cost for self-hosted.</li>
</ol>

<p>Dimensions, latency, and context length matter too, but model quality dominates the retrieval ceiling.</p>

<h2>What the numbers mean</h2>

<h3>Dimensions</h3>
<p>How many numbers per vector. More dimensions = more storage, more compute. The model designers pick this — you don't tune it (except via Matryoshka, see <a href="dimensions-cost.html">dimensions and cost</a>). Ranges from 384 (small models) to 3072+ (large).</p>

<h3>Context length</h3>
<p>Max tokens the model will embed at once. 512 is the old standard, 8192 is modern, and some models now go to 32K+. Longer context = can embed bigger chunks, but diminishing returns — an embedding is still one vector summarizing all tokens.</p>

<h3>Similarity metric</h3>
<ul>
  <li><strong>Cosine</strong> (angle-based): most common, scale-invariant</li>
  <li><strong>Dot product</strong>: used when vectors are normalized (many modern models output pre-normalized vectors, so dot product = cosine)</li>
  <li><strong>Euclidean</strong>: rare for text, more common in computer vision</li>
</ul>

<p>Check which metric your model was trained with and use that one. Mismatched metrics degrade retrieval silently.</p>

<h2>The mental model for debugging</h2>
<p>When retrieval is failing:</p>
<ol>
  <li>Look at the top-k results for a failing query</li>
  <li>Are they wrong? The embeddings don't understand your domain</li>
  <li>Are they right but buried at rank 5-10? The embeddings work, but you need reranking</li>
  <li>Are they missing entirely? The relevant chunk wasn't in your index (chunking or ingestion problem)</li>
</ol>

<p style="margin-top:40px;">Next: <a href="picking-a-model.html">Picking an embedding model</a>.</p>
""",
    prev=("Chunking code", "../chunking/chunking-code.html"),
    nxt=("Picking an embedding model", "picking-a-model.html"),
)


write_rag_page(
    slug="embeddings/picking-a-model",
    title="Picking an embedding model",
    description="There are hundreds of embedding models. The right choice depends on domain, volume, latency, cost, and language. Here's the decision framework.",
    reading_time=6,
    body_html="""
<p class="lede">Embedding model choice has a larger impact on retrieval quality than almost any other decision in the RAG stack. The right model for a general-knowledge corpus may be wrong for legal documents, code, or Japanese-language content. Here's how I pick.</p>

<h2>The MTEB leaderboard is the starting point</h2>
<p>MTEB (Massive Text Embedding Benchmark) ranks embedding models on standardized tasks. Look up current leaderboards on Hugging Face. Not gospel, but a reasonable starting short-list.</p>

<p>Caveats:</p>
<ul>
  <li>MTEB measures average performance across tasks. Your domain may not match any task.</li>
  <li>Top models on MTEB are often very large and expensive to run.</li>
  <li>Leaderboards don't capture latency, cost, or context length well.</li>
</ul>

<h2>The five decision dimensions</h2>

<h3>1. Quality</h3>
<p>Proxy: MTEB score, or better, your own eval set. Test 2-3 candidate models against a held-out set of real queries.</p>

<h3>2. Cost</h3>
<ul>
  <li>OpenAI text-embedding-3-small: $0.02 / 1M tokens</li>
  <li>OpenAI text-embedding-3-large: $0.13 / 1M tokens</li>
  <li>Cohere embed-v3: ~$0.10 / 1M tokens</li>
  <li>Voyage-3-large: ~$0.18 / 1M tokens</li>
  <li>Self-hosted open-source: GPU-hours only (often significantly cheaper at scale)</li>
</ul>
<p>Embedding cost compounds: every reindex pays the cost again. For large corpora, this matters.</p>

<h3>3. Latency</h3>
<p>Embedding time per query affects user-facing latency. API calls: 50-200ms. Self-hosted small models: 5-20ms. Self-hosted large models: 30-100ms. For real-time systems, this is load-bearing.</p>

<h3>4. Context length</h3>
<p>Match to your chunk size. If your chunks are 1000 tokens, a model with 512-token context silently truncates your chunks. Check the spec.</p>

<h3>5. Domain fit</h3>
<p>General-purpose models work for general content. For code, law, medicine, or finance, domain-specific or domain-aware models (or fine-tuned ones) beat general models significantly.</p>

<h2>My current default picks</h2>

<h3>For general prose, production</h3>
<ul>
  <li><strong>OpenAI text-embedding-3-small</strong>: cheap, fast, solid. Good baseline.</li>
  <li><strong>OpenAI text-embedding-3-large</strong>: when quality matters and cost is secondary.</li>
  <li><strong>Cohere embed-v3 (multilingual)</strong>: best-in-class multilingual retrieval.</li>
  <li><strong>Voyage-3-large</strong>: often tops benchmarks, especially for finance/legal.</li>
</ul>

<h3>For general prose, self-hosted</h3>
<ul>
  <li><strong>BGE-M3</strong>: strong multilingual, unified dense/sparse/colbert, Apache-2.0 license</li>
  <li><strong>E5-mistral-7b-instruct</strong>: top open-source quality, heavier inference</li>
  <li><strong>nomic-embed-text-v1.5</strong>: efficient, strong, 8K context, Apache-2.0</li>
  <li><strong>gte-large</strong>: efficient, decent quality, 512 context</li>
</ul>

<h3>For code</h3>
<ul>
  <li><strong>Voyage-code-2 or Voyage-code-3</strong>: code-specific</li>
  <li><strong>jina-embeddings-v2-base-code</strong>: open-source code embeddings</li>
</ul>

<h3>For legal/financial/medical</h3>
<p>Evaluate domain-specific options first:</p>
<ul>
  <li>Voyage-law-2 for legal</li>
  <li>Voyage-finance-2 for finance</li>
  <li>BioBERT / Clinical BERT for medical</li>
</ul>
<p>If none fit, fine-tune a general model on domain data (see <a href="fine-tuning.html">fine-tuning embeddings</a>).</p>

<h3>For multilingual</h3>
<ul>
  <li>Cohere embed-v3 multilingual (excellent quality)</li>
  <li>BGE-M3 (open-source, competitive)</li>
  <li>multilingual-e5-large</li>
</ul>

<h2>Closed vs open</h2>
<p>See the dedicated page: <a href="closed-vs-open.html">closed vs open embedding models</a>.</p>

<h2>The testing protocol</h2>
<ol>
  <li>Build a small eval set: 30-100 queries with known-good answer chunks</li>
  <li>Index your corpus with candidate models</li>
  <li>Measure hit-rate@k, MRR, NDCG for each</li>
  <li>Compare alongside cost and latency</li>
  <li>Pick the one on the best quality/cost frontier for your use case</li>
</ol>

<p>This is a one-afternoon exercise that saves months of subtle retrieval issues.</p>

<h2>The lock-in question</h2>
<p>Switching embedding models means reindexing your entire corpus. For large corpora, this is expensive and slow. Factors to consider:</p>
<ul>
  <li>How often will you want to change models?</li>
  <li>Can you afford a migration window?</li>
  <li>Does your infra support running two embedding models in parallel during migration?</li>
</ul>

<p>Build the infrastructure to switch embedding models without rebuilding everything else. Treat embedding_model_version as first-class metadata.</p>

<p style="margin-top:40px;">Next: <a href="closed-vs-open.html">Closed vs open embedding models</a>.</p>
""",
    prev=("What embeddings are", "what-are-embeddings.html"),
    nxt=("Closed vs open models", "closed-vs-open.html"),
)


write_rag_page(
    slug="embeddings/closed-vs-open",
    title="Closed vs open embedding models",
    description="OpenAI, Cohere, and Voyage run API models. Hugging Face has open-source alternatives. Here's how to pick between them for production.",
    reading_time=5,
    body_html="""
<p class="lede">The choice between closed-source API embeddings (OpenAI, Cohere, Voyage) and open-source self-hosted (BGE, E5, Nomic) is a real decision with different tradeoffs for different teams. Here's how I approach it.</p>

<h2>Closed / API advantages</h2>
<ul>
  <li>Zero ops overhead. Upload tokens, get vectors.</li>
  <li>Consistent latency and reliability (SLAs).</li>
  <li>Automatic upgrades as providers release new versions.</li>
  <li>Usually highest raw quality (providers invest heavily).</li>
  <li>No GPU infrastructure required.</li>
</ul>

<h2>Closed / API disadvantages</h2>
<ul>
  <li>Per-token pricing that compounds with every reindex.</li>
  <li>Your queries and documents leave your infrastructure.</li>
  <li>Rate limits can bottleneck large ingestion jobs.</li>
  <li>Vendor lock-in: switching means reindexing.</li>
  <li>Dependency on external uptime.</li>
</ul>

<h2>Open / self-hosted advantages</h2>
<ul>
  <li>No per-token cost (only compute).</li>
  <li>Data stays in your VPC (critical for regulated industries).</li>
  <li>Predictable cost at scale.</li>
  <li>Can fine-tune on your domain.</li>
  <li>Full control over latency (batch size tuning, hardware choice).</li>
</ul>

<h2>Open / self-hosted disadvantages</h2>
<ul>
  <li>GPU infrastructure needed (or careful CPU inference tuning).</li>
  <li>Ops burden: model updates, deployments, monitoring.</li>
  <li>Quality slightly below top commercial models (gap is closing).</li>
  <li>Engineering time to serve at scale.</li>
</ul>

<h2>The cost break-even</h2>
<p>Rough rule of thumb:</p>
<ul>
  <li><strong>Below ~10M chunks total:</strong> API is almost always cheaper. You're spending $100-500/month; not worth ops time.</li>
  <li><strong>10M-100M chunks, growing:</strong> depends. Model a 1-year TCO before deciding.</li>
  <li><strong>Above 100M chunks with frequent reindexing:</strong> self-hosted typically wins on cost alone.</li>
</ul>

<h2>The compliance angle</h2>
<p>For regulated industries (healthcare, finance, government), sending proprietary data to an external embedding API may be disqualifying. Some vendors offer dedicated deployments or in-VPC options (AWS Bedrock, Azure OpenAI, private Cohere deployments). Self-hosted open-source is the cleanest compliance story.</p>

<h2>The quality gap (2026)</h2>
<p>Top open-source models (BGE-M3, E5-mistral, nomic-embed-v1.5) are within 2-5 points on MTEB of the best commercial models. For most RAG applications, this difference is smaller than the variance from chunking and retrieval choices.</p>

<p>For specialized domains (legal, finance), commercial domain-tuned models (Voyage-law, Voyage-finance) currently have a wider lead. Unless you can fine-tune your own.</p>

<h2>The hybrid pattern</h2>
<p>Many serious teams end up running both:</p>
<ul>
  <li>Commercial API for the main retrieval index (quality, simplicity)</li>
  <li>Self-hosted model for query-time embedding (latency, cost on high-volume queries)</li>
  <li>Self-hosted for sensitive data segments where external APIs aren't allowed</li>
</ul>

<p>This requires maintaining two embedding pipelines but can optimize cost and compliance simultaneously.</p>

<h2>Self-hosting stack</h2>
<ul>
  <li><strong>Text Embeddings Inference (TEI)</strong>: Hugging Face's production serving for embedding models. Fast, optimized.</li>
  <li><strong>vLLM</strong>: general LLM serving, supports embedding models.</li>
  <li><strong>Triton Inference Server</strong>: NVIDIA's production serving, heavy but capable.</li>
  <li><strong>Sentence-Transformers + FastAPI</strong>: simple DIY for smaller scale.</li>
</ul>

<h2>What I actually recommend</h2>
<ul>
  <li>Starting out: OpenAI text-embedding-3-small. Cheap, fast, good enough.</li>
  <li>Scaling up (10M+ chunks) with spare engineering capacity: evaluate BGE-M3 or nomic-embed-v1.5 self-hosted.</li>
  <li>Quality-sensitive: test Voyage, text-embedding-3-large, or BGE-M3 against your eval set. Let numbers decide.</li>
  <li>Regulated: commercial with dedicated deployment, or self-hosted open-source.</li>
</ul>

<p style="margin-top:40px;">Next: <a href="dimensions-cost.html">Dimensions, cost, and MRL</a>.</p>
""",
    prev=("Picking an embedding model", "picking-a-model.html"),
    nxt=("Dimensions, cost, and MRL", "dimensions-cost.html"),
)


write_rag_page(
    slug="embeddings/dimensions-cost",
    title="Dimensions, cost, and MRL",
    description="Vector dimensions drive storage cost and search latency. Matryoshka Representation Learning lets you shrink vectors without retraining. Here's the math.",
    reading_time=5,
    body_html="""
<p class="lede">Every dimension in your embedding vector costs storage, search time, and network bandwidth. For small corpora it doesn't matter. For 100M+ vectors, the difference between 768-dim and 3072-dim vectors is the difference between an affordable vector store and a cost-prohibitive one. Matryoshka embeddings are a recent innovation that gives you both options from one model.</p>

<h2>The cost math</h2>

<p>Every vector is stored as 32-bit floats (or 16-bit, or quantized). Storage per vector:</p>
<ul>
  <li>768 dim × 4 bytes = 3 KB</li>
  <li>1536 dim × 4 bytes = 6 KB</li>
  <li>3072 dim × 4 bytes = 12 KB</li>
</ul>

<p>For 100 million vectors:</p>
<ul>
  <li>768 dim = 300 GB</li>
  <li>1536 dim = 600 GB</li>
  <li>3072 dim = 1.2 TB</li>
</ul>

<p>Vector databases charge per stored dimension. Search latency also scales roughly with dimensions. The difference between picking a 768-dim and 3072-dim model is material.</p>

<h2>The quality-vs-dim tradeoff</h2>
<p>Higher dimensions generally capture more information, which means better retrieval quality. But the relationship is sub-linear — going from 768 to 1536 often gives only a few percent quality improvement. Going from 1536 to 3072 gives even less.</p>

<p>For cost-conscious deployments, the sweet spot is often 1024-1536 dimensions. Higher is usually not worth the cost.</p>

<h2>Matryoshka Representation Learning (MRL)</h2>
<p>MRL trains models so that the first N dimensions of the vector are themselves a usable embedding. You can truncate a 3072-dim vector to 768 dim and still have a functional (if slightly lower quality) embedding.</p>

<p>This is huge for RAG:</p>
<ul>
  <li>Store full 3072-dim vectors only for the top-tier retrieval set</li>
  <li>Use truncated 768-dim for a fast first-pass filter</li>
  <li>Use even smaller truncations for extreme-scale problems</li>
  <li>All from the same model, no retraining</li>
</ul>

<h2>Models that support MRL</h2>
<ul>
  <li><strong>OpenAI text-embedding-3-small</strong> (default 1536, truncatable to 256, 512, 1024)</li>
  <li><strong>OpenAI text-embedding-3-large</strong> (default 3072, truncatable)</li>
  <li><strong>Cohere embed-v3</strong> (supports dim reduction via its dimensions parameter)</li>
  <li><strong>nomic-embed-v1.5</strong> (768 max, but MRL-trained for smaller sizes)</li>
</ul>

<h2>Quantization</h2>
<p>Beyond dimension reduction, you can reduce precision:</p>
<ul>
  <li><strong>float32 → float16</strong>: 50% storage savings, minimal quality loss</li>
  <li><strong>float32 → int8</strong>: 75% savings, 1-5% quality loss depending on model</li>
  <li><strong>Binary quantization</strong>: 32x savings, 5-15% quality loss — works well with reranking to recover quality</li>
</ul>

<p>Some vector databases support native quantization (Qdrant's scalar and binary quantization, for example). At scale, the storage and speed wins are dramatic.</p>

<h2>The combined cost strategy</h2>
<p>For a large-scale RAG system:</p>
<ol>
  <li>Start with a high-quality high-dim model (e.g., text-embedding-3-large at 3072 dim)</li>
  <li>Use MRL to store truncated 1024-dim vectors in the index</li>
  <li>Use binary quantization for coarse first-pass retrieval</li>
  <li>Rerank top-100 candidates with full-precision, full-dimension vectors (or with a cross-encoder)</li>
</ol>

<p>This gives most of the quality of the full model with 1/30th the storage and significantly faster search.</p>

<h2>When this matters</h2>
<p>Below 1M vectors, ignore this entire page. Just pick a reasonable model and move on.</p>
<p>Between 1M and 100M, dimensions start to matter for cost and latency.</p>
<p>Above 100M, dimensions and quantization strategy dominate your infrastructure bill.</p>

<h2>The operational cost</h2>
<p>Re-embedding 100M vectors is not free. If you pick a 3072-dim model and later want to change, budget days of compute time. Build your pipeline so you can swap models without full reindexes where possible — store raw chunks separately from their vectors, so you can re-embed without re-parsing.</p>

<p style="margin-top:40px;">Next: <a href="fine-tuning.html">Fine-tuning embeddings</a>.</p>
""",
    prev=("Closed vs open models", "closed-vs-open.html"),
    nxt=("Fine-tuning embeddings", "fine-tuning.html"),
)


write_rag_page(
    slug="embeddings/fine-tuning",
    title="Fine-tuning embeddings",
    description="Fine-tuning an embedding model on your domain data is one of the highest-leverage moves in specialized RAG systems. Here's when it's worth it and how to do it.",
    reading_time=5,
    body_html="""
<p class="lede">A general-purpose embedding model knows general English. It doesn't know that in your company, "Jaguar" means a specific product line, not the animal or the car. Fine-tuning embeddings teaches the model your domain's semantic space. For specialized corpora, this is one of the highest-leverage optimizations available.</p>

<h2>When fine-tuning is worth it</h2>
<ul>
  <li>Highly specialized vocabulary (legal, medical, financial, scientific, pharma)</li>
  <li>Proprietary terminology that doesn't exist in general training data</li>
  <li>Internal product names or codenames that generic models don't recognize</li>
  <li>Non-English or code-mixed content where general models underperform</li>
  <li>Domains where generic embeddings demonstrably underperform on eval</li>
</ul>

<h2>When it isn't</h2>
<ul>
  <li>Small corpora (&lt; 10K documents) — not enough data to fine-tune effectively</li>
  <li>General content where commercial models already perform well</li>
  <li>Early-stage projects before you have meaningful eval data</li>
  <li>Teams without ML ops capacity to maintain the fine-tuned model</li>
</ul>

<h2>The data you need</h2>
<p>Fine-tuning requires query-document pairs. The positive pairs: a query and a chunk that actually answers it. Optionally, hard negatives: queries with chunks that look relevant but aren't.</p>

<p>Where this data comes from:</p>
<ul>
  <li><strong>Click logs</strong>: if you have an existing search system, click-through data is gold</li>
  <li><strong>Q&amp;A pairs</strong>: FAQs, support tickets, knowledge base questions</li>
  <li><strong>Synthetic generation</strong>: use an LLM to generate queries for each chunk. Works surprisingly well.</li>
  <li><strong>Human annotation</strong>: expensive but highest quality</li>
</ul>

<p>For most domain fine-tuning, you want at least 1000-10000 query-document pairs. More is better.</p>

<h2>The synthetic data pipeline</h2>
<p>Common approach when you don't have natural query data:</p>
<ol>
  <li>Sample 5000-10000 chunks from your corpus</li>
  <li>For each chunk, prompt an LLM: "Generate 3 questions a user might ask that this chunk answers."</li>
  <li>You now have 15000-30000 query-chunk pairs</li>
  <li>Fine-tune on these</li>
</ol>

<p>The quality of your synthetic queries determines fine-tune quality. Use a strong model (GPT-4, Claude) and iterate on the prompt to get queries that match real user style.</p>

<h2>Fine-tuning approaches</h2>

<h3>Contrastive learning</h3>
<p>The classic approach. Train with (query, positive_chunk, negative_chunks) triplets. Reward the model when positive is closer than negatives in embedding space.</p>

<h3>Matryoshka fine-tuning</h3>
<p>Fine-tune in a way that preserves MRL property. Lets you still truncate the fine-tuned vectors.</p>

<h3>LoRA / PEFT</h3>
<p>Parameter-efficient fine-tuning. Train a small adapter on top of the base model. Dramatically reduces GPU requirements for fine-tuning. Works for most embedding models.</p>

<h2>Tools</h2>
<ul>
  <li><strong>Sentence-Transformers</strong>: library with built-in fine-tuning loops for most open-source embedding models</li>
  <li><strong>Hugging Face Trainer</strong>: lower-level but more flexible</li>
  <li><strong>LlamaIndex finetuning</strong>: wrappers for common patterns</li>
  <li><strong>Voyage / Cohere fine-tuning APIs</strong>: for closed models where supported</li>
</ul>

<h2>The OpenAI / commercial reality</h2>
<p>As of 2026, OpenAI embedding models aren't fine-tunable. Cohere and Voyage offer fine-tuning APIs. For maximum flexibility, open-source models are the path.</p>

<h2>Expected gains</h2>
<p>Well-done domain fine-tuning typically produces 10-30% improvement on retrieval metrics over a general-purpose baseline. For highly specialized domains (medical coding, legal citations), gains can be larger.</p>

<h2>The maintenance cost</h2>
<p>Fine-tuned models need maintenance:</p>
<ul>
  <li>Re-tune as your corpus evolves</li>
  <li>Version your fine-tuned models and track which indexes use which</li>
  <li>Re-evaluate quarterly against fresh eval data</li>
  <li>When the base model is upgraded, decide whether to re-fine-tune or skip the upgrade</li>
</ul>

<h2>The pragmatic path</h2>
<p>For most teams, I recommend:</p>
<ol>
  <li>Ship with a commercial embedding model</li>
  <li>Build an eval set that reflects real queries</li>
  <li>Measure baseline retrieval quality</li>
  <li>Only fine-tune if you can demonstrate the baseline is genuinely underperforming</li>
  <li>If you fine-tune, run it against the same eval set to prove the gain is real</li>
</ol>

<p>Don't fine-tune because it's cool. Fine-tune because measurement says you need to.</p>

<p style="margin-top:40px;">Next: <a href="../vectors/overview.html">Vector database overview</a>.</p>
""",
    prev=("Dimensions, cost, and MRL", "dimensions-cost.html"),
    nxt=("Vector database overview", "../vectors/overview.html"),
)


# ============================================================
# VECTOR STORES (6 pages)
# ============================================================

write_rag_page(
    slug="vectors/overview",
    title="Vector database overview",
    description="Vector databases are infrastructure for nearest-neighbor search at scale. Here's what they do, how they differ from traditional databases, and the major players.",
    reading_time=5,
    body_html="""
<p class="lede">A vector database stores high-dimensional vectors and finds nearest neighbors at query time, fast. Traditional databases store rows and look up by exact match or range. Vector databases store embeddings and look up by similarity. Both have their place, and serious RAG systems usually involve both.</p>

<h2>What a vector database does</h2>
<ol>
  <li><strong>Ingests vectors</strong> with associated metadata</li>
  <li><strong>Indexes</strong> them in a structure optimized for nearest-neighbor queries</li>
  <li><strong>Queries</strong>: given a query vector, returns the top-k nearest</li>
  <li><strong>Filters</strong>: combine vector similarity with metadata predicates</li>
  <li><strong>Updates</strong>: handles upserts, deletes, partial metadata updates</li>
</ol>

<h2>Why you can't just use Postgres</h2>
<p>You can, actually — pgvector is a perfectly good choice for many workloads. But dedicated vector databases offer:</p>
<ul>
  <li>Purpose-built ANN indexes (HNSW, IVF, PQ) optimized for high dimensions</li>
  <li>Specialized query planners for hybrid vector+metadata queries</li>
  <li>Horizontal scaling for billion-vector workloads</li>
  <li>Features like multi-tenancy, namespaces, and streaming updates</li>
</ul>

<p>The decision: use pgvector until you're constrained by it. Move to a dedicated vector DB when you actually hit its limits.</p>

<h2>The major players (2026)</h2>

<h3>Pinecone</h3>
<p>Fully managed, serverless pricing model. Easiest to get started. Strong multi-tenancy. More expensive at scale than self-hosted alternatives. Namespaces are powerful.</p>

<h3>Weaviate</h3>
<p>Open-source with managed option. Strong hybrid search (native BM25 + vector). Rich filtering. Good for production.</p>

<h3>Qdrant</h3>
<p>Open-source, Rust-based, extremely fast. Strong quantization support (scalar, binary). Excellent filtering performance. Easy self-hosting.</p>

<h3>Milvus</h3>
<p>Open-source, enterprise-grade. Scales to billions of vectors. Complex to operate. Best for very large deployments.</p>

<h3>Chroma</h3>
<p>Open-source, embeddable. Great for prototyping and small-to-medium workloads. Not battle-tested at massive scale (yet).</p>

<h3>pgvector</h3>
<p>Postgres extension. Free, familiar, integrates with existing databases. Good for hundreds of thousands to low millions of vectors. Less purpose-built indexes than dedicated vector DBs.</p>

<h3>Turbopuffer</h3>
<p>Newer serverless vector DB designed for cost. S3-backed storage with caching. Very cheap per stored vector.</p>

<h3>Vespa</h3>
<p>Yahoo's battle-tested search engine, now open-source. Handles vector search alongside full-text, filtering, ranking. Complex but powerful.</p>

<h3>Elasticsearch / OpenSearch</h3>
<p>Full-text search platforms with vector support. Natural fit if you already run them for BM25.</p>

<h3>LanceDB</h3>
<p>Open-source embedded vector DB built on Apache Arrow. Good for local-first and notebook workflows.</p>

<h3>FAISS (not a database)</h3>
<p>Facebook's library for vector similarity search. Not a database — no persistence, no filtering, no API. But the underlying algorithms of many vector DBs. Use directly for research, not production.</p>

<h2>Comparison dimensions</h2>

<h3>Managed vs self-hosted</h3>
<p>Pinecone and Weaviate Cloud vs Qdrant, Milvus, pgvector on your own infra. The tradeoff is standard: cost vs ops burden.</p>

<h3>Scale</h3>
<ul>
  <li>Thousands to low millions: any option works, pick by feature fit</li>
  <li>10M to 100M: Pinecone, Weaviate, Qdrant, Milvus, Turbopuffer</li>
  <li>100M+: Milvus, Pinecone (at significant cost), Turbopuffer, Vespa</li>
</ul>

<h3>Hybrid search</h3>
<p>Weaviate, Qdrant, OpenSearch, and Vespa have the best native hybrid search. Pinecone now supports sparse vectors. See <a href="hybrid-search.html">hybrid search</a>.</p>

<h3>Filtering performance</h3>
<p>Qdrant and Weaviate have excellent filtered search. Pinecone's filtering is adequate. pgvector with proper indexes can be very fast on structured filters.</p>

<h3>Multi-tenancy</h3>
<p>Pinecone's namespaces are clean. Weaviate has per-tenant shards. For multi-tenant RAG, these features matter a lot. See <a href="../cases/multi-tenant.html">multi-tenant RAG</a>.</p>

<h2>The decision framework</h2>
<ol>
  <li>Starting out, low volume: pgvector or Chroma. Cheap, simple.</li>
  <li>Growing, managed preference: Pinecone. Fast to scale, costs predictable.</li>
  <li>Growing, self-hosted preference: Qdrant or Weaviate. Full control.</li>
  <li>Very large scale: Milvus or Vespa.</li>
  <li>Need full-text + vectors in one system: Elasticsearch / OpenSearch / Vespa.</li>
  <li>Already running Postgres heavily: pgvector, unless you hit limits.</li>
</ol>

<p>Most vector DB decisions are reversible with some migration effort. Don't over-optimize this choice early.</p>

<p style="margin-top:40px;">Next: <a href="indexing-strategies.html">HNSW, IVF, PQ</a>.</p>
""",
    prev=("Fine-tuning embeddings", "../embeddings/fine-tuning.html"),
    nxt=("HNSW, IVF, PQ", "indexing-strategies.html"),
)


write_rag_page(
    slug="vectors/indexing-strategies",
    title="HNSW, IVF, PQ",
    description="Approximate nearest neighbor algorithms trade exact results for speed. Here's how HNSW, IVF, and PQ work, and when to use which.",
    reading_time=6,
    body_html="""
<p class="lede">Exact nearest-neighbor search over millions of vectors is too slow for real-time use. Vector databases use approximate algorithms (ANN) that trade a few percent of recall for 10-100x speedups. The three dominant algorithms are HNSW, IVF, and PQ. You don't need to implement them, but you need to understand the tradeoffs.</p>

<h2>HNSW (Hierarchical Navigable Small World)</h2>
<p>The dominant algorithm for most production vector databases.</p>

<h3>How it works</h3>
<p>HNSW builds a multi-layer graph where each vector is a node connected to its neighbors. The top layer has few nodes with long-range connections; lower layers have more nodes with shorter connections. Search starts at the top, greedily follows edges toward the query, and descends layer by layer.</p>

<h3>Strengths</h3>
<ul>
  <li>Very high recall at low latency</li>
  <li>Supports streaming inserts well</li>
  <li>Well-tuned across many vector DBs</li>
</ul>

<h3>Weaknesses</h3>
<ul>
  <li>Memory-heavy: the graph structure significantly exceeds raw vector storage</li>
  <li>Index construction is slow and CPU-intensive</li>
  <li>Deletion is awkward — usually lazy (mark as deleted, filter out at query)</li>
</ul>

<h3>Key tuning parameters</h3>
<ul>
  <li><code>M</code>: max connections per node. Higher = better recall, more memory. Typical 16-32.</li>
  <li><code>ef_construction</code>: how many candidates to explore during index build. Higher = slower build, better index. Typical 100-200.</li>
  <li><code>ef_search</code>: how many candidates to explore during query. Higher = better recall, slower queries. Typical 50-200.</li>
</ul>

<h2>IVF (Inverted File)</h2>
<p>Older algorithm, still useful especially at enormous scale or memory-constrained.</p>

<h3>How it works</h3>
<p>Cluster all vectors into K centroids (via k-means). For each query, find the nearest centroid(s), then exhaustively search only the vectors assigned to those clusters.</p>

<h3>Strengths</h3>
<ul>
  <li>Low memory (just store cluster assignments)</li>
  <li>Fast queries when you probe few clusters</li>
  <li>Easier to distribute across shards</li>
</ul>

<h3>Weaknesses</h3>
<ul>
  <li>Lower recall than HNSW at equivalent speed</li>
  <li>Quality degrades if cluster choice is wrong</li>
  <li>Rebuilding required when distribution shifts</li>
</ul>

<h3>Key parameters</h3>
<ul>
  <li><code>nlist</code>: number of clusters. Rule of thumb: sqrt(N) for N vectors.</li>
  <li><code>nprobe</code>: how many clusters to search per query. Higher = better recall, slower.</li>
</ul>

<h2>PQ (Product Quantization)</h2>
<p>A compression technique, usually combined with IVF or HNSW.</p>

<h3>How it works</h3>
<p>Split each vector into M sub-vectors. Train a separate codebook per sub-vector position (typically 256 codes per position). Store each sub-vector as a single byte index into its codebook. A 768-dim float vector (3072 bytes) becomes ~48 bytes. Storage reduction: ~60x.</p>

<h3>Strengths</h3>
<ul>
  <li>Dramatic storage reduction</li>
  <li>Fast distance computation via table lookups</li>
  <li>Works well combined with IVF or HNSW for hybrid indexes</li>
</ul>

<h3>Weaknesses</h3>
<ul>
  <li>Lossy — introduces quantization error</li>
  <li>Codebook training is one-time cost, doesn't adapt to new data well</li>
  <li>Recall gap from exact search</li>
</ul>

<h2>The common combinations</h2>

<h3>HNSW alone</h3>
<p>Default for most production systems up to ~10M vectors. Highest quality.</p>

<h3>IVF-PQ</h3>
<p>Cluster + compress. Scales to billions. Lower recall than HNSW but much cheaper storage. Used at Meta, Google scale.</p>

<h3>HNSW + PQ</h3>
<p>Graph structure for navigation, PQ-compressed vectors for distance calculation. Good balance. Qdrant's default at scale.</p>

<h3>Scalar / binary quantization</h3>
<p>Simpler than PQ. Each float reduced to int8 or a single bit. Combined with HNSW in many modern DBs. Qdrant and Milvus both support binary quantization natively.</p>

<h2>The recall-speed-memory triangle</h2>
<p>You get to pick two of three: recall, speed, memory. Tuning parameters move you along the frontier:</p>
<ul>
  <li>High recall + fast: HNSW with large ef, lots of memory</li>
  <li>Fast + low memory: IVF-PQ with aggressive compression, sacrifice recall</li>
  <li>High recall + low memory: not really achievable at scale; you pay with query time</li>
</ul>

<h2>The pragmatic approach</h2>
<p>For systems below ~10M vectors, accept the defaults of your vector DB and move on. Index strategy rarely bottlenecks RAG quality at this scale.</p>

<p>Above 10M vectors, budget time to tune. Run your eval set at different parameter settings. Look at recall@10 vs query latency. Find the parameter sweet spot for your workload.</p>

<p>Above 100M vectors, index strategy is a serious engineering effort. Expect to iterate on quantization and sharding over months.</p>

<h2>When to rebuild</h2>
<p>Indexes don't update forever gracefully:</p>
<ul>
  <li>HNSW: degrades slowly with high churn. Rebuild quarterly or annually at scale.</li>
  <li>IVF: degrades if distribution shifts. Rebuild when recall drops or when you re-embed.</li>
  <li>PQ: codebook stale if new data differs from training. Retrain codebook as data evolves.</li>
</ul>

<p style="margin-top:40px;">Next: <a href="hybrid-search.html">Hybrid search</a>.</p>
""",
    prev=("Vector database overview", "overview.html"),
    nxt=("Hybrid search", "hybrid-search.html"),
)


write_rag_page(
    slug="vectors/hybrid-search",
    title="Hybrid search",
    description="Dense vectors find semantic matches. Sparse methods (BM25) find keyword matches. Hybrid search combines them and usually beats either alone.",
    reading_time=5,
    body_html="""
<p class="lede">Dense embeddings are great at synonyms and paraphrases but weak at exact matches, rare entities, and specific codes. Keyword search (BM25) is the opposite. Hybrid search runs both and combines the results. For production RAG, hybrid retrieval consistently outperforms dense-only. Most teams ship dense-only first and then regret it.</p>

<h2>Why hybrid matters</h2>
<p>Consider a user query: "error E-47 in the invoice processor"</p>
<ul>
  <li>Dense embedding sees "error ... invoice processor" — retrieves semantically similar documents about invoice errors in general</li>
  <li>BM25 sees "E-47" as a specific term — retrieves documents actually mentioning E-47</li>
  <li>Hybrid gets both: documents about invoice errors, with a boost for those explicitly mentioning E-47</li>
</ul>
<p>The hybrid result is almost always more useful.</p>

<h2>The two components</h2>

<h3>Dense (vector) retrieval</h3>
<p>Embed query, find nearest neighbors. Covered throughout this section.</p>

<h3>Sparse (BM25) retrieval</h3>
<p>Classical information retrieval. Score documents by term frequency, inverse document frequency, and document length. Fast, exact, no training required. See <a href="../retrieval/bm25-sparse.html">BM25 and sparse retrieval</a>.</p>

<h2>Combining results: fusion strategies</h2>

<h3>Reciprocal Rank Fusion (RRF)</h3>
<p>The default and usually best-performing fusion method. For each document, compute its score as:</p>

<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
RRF_score(d) = Σ  1 / (k + rank_i(d))
              i
</pre>

<p>where <code>rank_i(d)</code> is the document's rank in the i-th retrieval method's result list, and <code>k</code> is a small constant (typically 60). Sum over all retrievers.</p>

<p>RRF normalizes differently-scored retrievers (BM25 scores can be 0-30, vector cosine 0-1) without any tuning. Just combines ranks.</p>

<h3>Score normalization + weighted sum</h3>
<p>Min-max or z-score normalize each retriever's scores, then weighted sum:</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
final_score = α * dense_score + (1 - α) * sparse_score
</pre>
<p>Requires tuning α. Typical sweet spot: α = 0.5 to 0.7 (slightly favor dense).</p>

<h3>Learned fusion</h3>
<p>Train a small model to combine scores from multiple retrievers. Best quality, most complexity.</p>

<h3>Late interaction (ColBERT)</h3>
<p>A different approach: embed every token in queries and documents, match at the token level. Stronger for precise retrieval but more expensive to store and serve.</p>

<h2>Implementation patterns</h2>

<h3>Single database that supports both</h3>
<p>Weaviate, Qdrant, OpenSearch, Elasticsearch, Vespa, and Pinecone (with sparse vectors) all support hybrid natively. Cleanest architecture.</p>

<h3>Two databases, fused at query time</h3>
<p>Run BM25 in Elasticsearch/OpenSearch, dense in a vector DB. At query time, call both, fuse results with RRF. More infrastructure but maximum flexibility.</p>

<h3>Single database, fused manually</h3>
<p>Store dense vectors in a vector DB, use its full-text capabilities for BM25 (pgvector + Postgres full-text, for example). Works, less optimized than dedicated hybrid solutions.</p>

<h2>Common pitfalls</h2>

<h3>Mismatched top-k</h3>
<p>If BM25 returns top-20 and dense returns top-100, the union is skewed toward dense results. Match top-k across retrievers, or normalize the retrieval depth.</p>

<h3>Text preprocessing differences</h3>
<p>BM25 tokenization (stopwords, stemming, lowercase) must match what you expect. A query "reset my password" with stopword removal becomes "reset password" and matches differently than with stopwords preserved.</p>

<h3>No dedup between retrievers</h3>
<p>A chunk appearing in both retriever results should be combined, not duplicated. RRF handles this. Weighted sum doesn't without explicit dedup logic.</p>

<h3>Hybrid without reranking</h3>
<p>Even hybrid retrieval benefits from a cross-encoder rerank on top. See <a href="../retrieval/reranking.html">reranking</a>.</p>

<h2>The quality gain</h2>
<p>On standard benchmarks, hybrid RRF typically outperforms dense-only by 5-20% on retrieval metrics. On domain-specific corpora with lots of proper nouns, technical terms, or rare identifiers, the gain can be 30%+.</p>

<p>Cost: roughly 2x retrieval latency (you run two searches), negligible extra storage (sparse indexes are small).</p>

<h2>My default recommendation</h2>
<p>Any production RAG system should use hybrid retrieval. Dense-only is a prototype-stage choice. The engineering cost is modest, the quality gain is real, and the failure modes are asymmetric — hybrid handles the edge cases (rare terms, IDs, codes) that pure dense can't.</p>

<p style="margin-top:40px;">Next: <a href="metadata-filtering.html">Metadata filtering</a>.</p>
""",
    prev=("HNSW, IVF, PQ", "indexing-strategies.html"),
    nxt=("Metadata filtering", "metadata-filtering.html"),
)


write_rag_page(
    slug="vectors/metadata-filtering",
    title="Metadata filtering",
    description="Metadata filtering is what lets you do multi-tenant RAG, access control, freshness, and narrow-scope queries. The performance model matters.",
    reading_time=4,
    body_html="""
<p class="lede">Metadata filtering combines vector similarity with structured predicates: "find chunks similar to this query, but only from documents owned by tenant X, published after date Y, with visibility = public." Every production RAG system needs this. The performance characteristics differ dramatically between vector databases.</p>

<h2>The query shape</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
query: vector(embedding of user question)
filter: {
  tenant_id: "acme",
  visibility: {$in: ["public", "internal"]},
  updated_at: {$gte: "2024-01-01"},
  document_type: "policy"
}
top_k: 10
</pre>

<p>The database's job: find the 10 nearest neighbors that also satisfy all filter conditions. Sounds simple, isn't.</p>

<h2>Three strategies</h2>

<h3>Pre-filter</h3>
<p>Narrow the candidate set to matching metadata first, then search only those. Exact: returns only filter-matching documents.</p>
<ul>
  <li>Fast when filter is selective (narrows to small subset)</li>
  <li>Slow when filter matches most documents (still scans everything)</li>
  <li>Requires metadata indexes</li>
</ul>

<h3>Post-filter</h3>
<p>Do vector search first over all documents, then filter. Fast search, but may return fewer-than-k if filter is selective.</p>
<ul>
  <li>Fast when filter is non-selective</li>
  <li>Broken when filter is very selective — your top-10 vector results might all be filtered out, leaving empty results</li>
</ul>

<h3>Dynamic / hybrid</h3>
<p>The database decides based on estimated filter selectivity. Modern vector DBs (Pinecone, Qdrant, Weaviate) do this automatically.</p>

<h2>The performance failure mode</h2>
<p>A query with a highly selective filter on a post-filter-only database:</p>
<ul>
  <li>Vector search returns top-100 candidates</li>
  <li>Filter matches 2 of them</li>
  <li>You wanted top-10, got 2</li>
</ul>

<p>You can increase the search k to compensate (over-fetch), but this is wasteful and still unreliable when filters are very selective.</p>

<p>The right answer: a vector DB that supports pre-filtering or dynamic filtering. Or query the metadata first to get document IDs, then run a restricted vector search.</p>

<h2>Vector DB comparison on filtering</h2>
<ul>
  <li><strong>Qdrant</strong>: excellent. Payload indexes, pre-filter and dynamic filtering, fast on complex queries.</li>
  <li><strong>Weaviate</strong>: very good. Native filtering during HNSW traversal.</li>
  <li><strong>Pinecone</strong>: adequate. Filters applied during search, performance varies by selectivity.</li>
  <li><strong>Milvus</strong>: good. Supports partition-based filtering and field-level filters.</li>
  <li><strong>pgvector</strong>: strong for filters Postgres can index well. Combine vector and SQL.</li>
  <li><strong>Chroma</strong>: basic. Works but not optimized for high-selectivity filters at scale.</li>
</ul>

<h2>Index the metadata fields you'll filter on</h2>
<p>Every vector DB lets you index specific metadata fields for fast filtering. Index every field that appears in common queries. Un-indexed fields force a full scan per query.</p>

<p>Typical fields to index:</p>
<ul>
  <li><code>tenant_id</code></li>
  <li><code>source_system</code></li>
  <li><code>document_type</code></li>
  <li><code>visibility</code> or <code>permissions</code></li>
  <li>Date fields used for freshness filters</li>
  <li>Numeric fields used for range queries</li>
</ul>

<h2>The multi-tenant special case</h2>
<p>In multi-tenant RAG, tenant_id filter runs on every query. Options:</p>

<h3>Single index, filter on tenant_id</h3>
<p>One physical index, logical separation via filter. Simple. Performance depends on tenant distribution.</p>

<h3>Namespace per tenant (Pinecone pattern)</h3>
<p>Each tenant has its own namespace. Physical separation. No risk of cross-tenant leaks. Better performance for tenant-scoped queries.</p>

<h3>Collection per tenant</h3>
<p>One collection per tenant. Extreme isolation. Expensive in overhead if you have many small tenants.</p>

<p>See <a href="../cases/multi-tenant.html">multi-tenant RAG</a> for more detail.</p>

<h2>Common filter patterns</h2>

<h3>Access control</h3>
<pre style="background:#f5f5f7; padding:12px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
permissions: {$in: [user.roles]}
</pre>

<h3>Freshness boost</h3>
<p>Filters to published_after: (today - 2 years). Older documents are still searchable if you remove the filter for broad queries.</p>

<h3>Document type scoping</h3>
<p>User asks "what's our refund policy" — filter to document_type = "policy".</p>

<h3>Tenant + source</h3>
<pre style="background:#f5f5f7; padding:12px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
tenant_id: "acme" AND source_system: {$in: ["confluence", "drive"]}
</pre>

<h2>Filter-aware reranking</h2>
<p>After retrieval, you can apply soft filters (boosts rather than hard filters) via the reranker:</p>
<ul>
  <li>Boost recent documents</li>
  <li>Boost canonical sources over derived</li>
  <li>Boost documents user has previously engaged with</li>
</ul>

<p>See <a href="../retrieval/reranking.html">reranking</a>.</p>

<p style="margin-top:40px;">Next: <a href="cost-optimization.html">Cost optimization</a>.</p>
""",
    prev=("Hybrid search", "hybrid-search.html"),
    nxt=("Cost optimization", "cost-optimization.html"),
)


write_rag_page(
    slug="vectors/cost-optimization",
    title="Cost optimization",
    description="Vector storage and retrieval can get expensive at scale. Here are the levers I pull to reduce cost without killing quality.",
    reading_time=5,
    body_html="""
<p class="lede">A naive production RAG system scales cost linearly with corpus size and query volume. At 100M vectors and millions of monthly queries, that cost becomes real. Here are the cost levers, ranked by impact.</p>

<h2>Storage costs</h2>

<h3>1. Reduce dimensions</h3>
<p>Use Matryoshka truncation to store 1024-dim vectors from a 3072-dim model. 3x storage savings, typically &lt;5% quality loss. See <a href="../embeddings/dimensions-cost.html">dimensions and cost</a>.</p>

<h3>2. Quantize</h3>
<p>int8 quantization: 4x savings, minimal quality loss. Binary quantization: 32x savings, larger quality loss but recoverable with reranking.</p>

<h3>3. Prune redundant chunks</h3>
<p>Many corpora have duplicate or near-duplicate content. Deduplicate at ingestion time. For news, blog archives, or documentation with multiple versions, this often removes 20-40% of the index.</p>

<h3>4. Archive cold data</h3>
<p>Separate recent/hot data from cold historical data. Put cold data on cheaper tiered storage or take it out of the active index. Serverless vector DBs (Turbopuffer, Pinecone serverless) price partly on access frequency.</p>

<h2>Query costs</h2>

<h3>5. Cache query embeddings</h3>
<p>Common queries repeat. Cache the embedding of each query for 24 hours or until you re-embed the corpus. See <a href="../prod/caching.html">caching</a>.</p>

<h3>6. Cache full retrieval results</h3>
<p>For deterministic queries against an unchanged index, cache top-k results. Especially valuable for popular questions in customer-facing RAG.</p>

<h3>7. Skip retrieval when possible</h3>
<p>Use a lightweight classifier or the LLM itself to decide whether the query needs RAG. Trivial queries ("hi", "thanks", "can you help") don't require retrieval — serve them directly.</p>

<h3>8. Reduce top-k when possible</h3>
<p>Passing top-5 instead of top-20 cuts reranker and generation costs. Only increase top-k when reranking proves top-5 isn't enough.</p>

<h2>Embedding costs</h2>

<h3>9. Avoid needless reindexing</h3>
<p>Don't re-embed unchanged chunks. Hash each chunk's content; only re-embed when hash changes.</p>

<h3>10. Use cheaper embeddings for lower-value segments</h3>
<p>Old archives, long-tail content, or low-volume segments can use cheaper embedding models. Hot content can use the premium model.</p>

<h3>11. Self-host for bulk ingestion</h3>
<p>At high volume, self-hosted embedding models beat API pricing. Even if you use an API for queries, batch ingestion can run on self-hosted infrastructure.</p>

<h2>Reranker costs</h2>

<h3>12. Rerank fewer candidates</h3>
<p>Reranking top-50 is cheaper than top-200. If quality is adequate at smaller candidate sets, use them.</p>

<h3>13. Use lighter rerankers</h3>
<p>cross-encoder/ms-marco-MiniLM vs cross-encoder/ms-marco-electra-base: meaningful cost difference, smaller quality difference.</p>

<h3>14. Skip reranking for high-confidence results</h3>
<p>If dense retrieval returns a very high-scoring result (cosine &gt; 0.85, say), you may not need reranking. Test the threshold against your eval set.</p>

<h2>Generation costs</h2>

<h3>15. Route to smaller models</h3>
<p>Use GPT-4o-mini, Claude Haiku, Gemini Flash for simple queries. Reserve large models for complex reasoning.</p>

<h3>16. Trim context</h3>
<p>If retrieved chunks contain boilerplate, trim it before sending to the generator. Every 100 tokens saved is real money at scale.</p>

<h3>17. Summarize long contexts</h3>
<p>When retrieved context is very long, a cheap summarization pass can produce a more focused input for the final answer generation.</p>

<h2>Infrastructure costs</h2>

<h3>18. Right-size the vector DB</h3>
<p>Many teams over-provision. Measure actual query QPS and scale down. Serverless options scale to zero.</p>

<h3>19. Consolidate indexes</h3>
<p>Multiple small indexes have overhead. One index with metadata filters can be cheaper than ten tiny indexes.</p>

<h3>20. Use managed when small, self-hosted when big</h3>
<p>The crossover point for Pinecone vs Qdrant self-hosted is usually around $500-1500/month in usage. Do the math.</p>

<h2>The budget hierarchy</h2>
<p>For a typical production RAG system at moderate scale, the cost breakdown looks like:</p>
<ul>
  <li>40-60%: LLM generation (largest single cost for most systems)</li>
  <li>15-25%: embedding generation (especially at ingestion and on reindexes)</li>
  <li>10-20%: vector DB storage and queries</li>
  <li>5-15%: reranker inference</li>
  <li>5-10%: infrastructure (ingestion workers, monitoring, etc.)</li>
</ul>

<p>Optimize from biggest to smallest. No point shaving 10% off vector DB costs if generation is 10x bigger.</p>

<h2>The quality-cost frontier</h2>
<p>Every cost optimization has a quality cost. Maintain an eval set. Measure quality before and after each optimization. Ship only changes where the quality loss is acceptable.</p>

<p>Without an eval set, cost optimization is gambling — you're reducing bills but also reducing quality invisibly.</p>

<p style="margin-top:40px;">Next: <a href="choosing-a-db.html">Choosing a vector DB</a>.</p>
""",
    prev=("Metadata filtering", "metadata-filtering.html"),
    nxt=("Choosing a vector DB", "choosing-a-db.html"),
)


write_rag_page(
    slug="vectors/choosing-a-db",
    title="Choosing a vector DB",
    description="Every vector DB choice involves managed vs self-hosted, scale, features, and lock-in. Here's my decision framework and what I actually pick for different projects.",
    reading_time=5,
    body_html="""
<p class="lede">The vector DB decision gets over-engineered. Most of the time the right answer is "the one your team can operate" plus "it supports hybrid search and metadata filtering." Everything else is second-order. Here's how I actually pick.</p>

<h2>The decision matrix</h2>

<h3>Prototype / &lt; 1M vectors / low traffic</h3>
<ul>
  <li><strong>Chroma</strong>: embeddable, zero-config. Great for notebooks and demos.</li>
  <li><strong>pgvector</strong>: if you already have Postgres. Simple, fast enough.</li>
  <li><strong>LanceDB</strong>: for local-first or desktop apps.</li>
</ul>
<p>Don't pay for a managed vector DB at this scale. It's wasted money.</p>

<h3>Production, small to medium (1M-10M vectors)</h3>
<ul>
  <li><strong>pgvector</strong>: still viable. Combined with proper HNSW indexes, handles this range well.</li>
  <li><strong>Qdrant</strong>: self-hosted, excellent performance, open-source. My usual pick for production at this size.</li>
  <li><strong>Pinecone</strong>: if you want fully managed with low ops burden.</li>
  <li><strong>Weaviate</strong>: if hybrid search and rich filtering are load-bearing features.</li>
</ul>

<h3>Production, medium to large (10M-100M vectors)</h3>
<ul>
  <li><strong>Qdrant</strong>: scales well, excellent filtering performance.</li>
  <li><strong>Pinecone</strong>: costs get real but operational simplicity is worth it for some teams.</li>
  <li><strong>Weaviate</strong>: good choice, especially for hybrid search.</li>
  <li><strong>Turbopuffer</strong>: cheapest at this scale if you can accept its cold-start characteristics.</li>
</ul>

<h3>Very large (100M+ vectors)</h3>
<ul>
  <li><strong>Milvus</strong>: designed for this scale. Complex to operate.</li>
  <li><strong>Vespa</strong>: battle-tested at Yahoo scale.</li>
  <li><strong>Qdrant (cluster mode)</strong>: now viable for this scale.</li>
  <li><strong>Pinecone</strong>: works, expensive. Reserve for when your team's engineering cost outweighs DB cost.</li>
</ul>

<h3>Already running Elasticsearch / OpenSearch</h3>
<p>Use their vector support. The integration with your existing BM25 + filtering infrastructure is worth more than a slightly better dedicated vector DB.</p>

<h2>The features that actually matter</h2>

<h3>Must-have</h3>
<ul>
  <li>Hybrid search (dense + sparse), either native or via an integration</li>
  <li>Metadata filtering with indexed fields</li>
  <li>Upsert semantics (not just insert)</li>
  <li>Bulk insert performance (matters at ingestion time)</li>
  <li>Quantization support (becomes important at scale)</li>
</ul>

<h3>Nice-to-have</h3>
<ul>
  <li>Multiple tenants / namespaces</li>
  <li>Reranking integration (some DBs can call rerankers natively)</li>
  <li>Multi-vector support (ColBERT-style late interaction)</li>
  <li>Streaming updates for real-time indexes</li>
  <li>Geographic replication</li>
</ul>

<h3>Often oversold</h3>
<ul>
  <li>"Billions of vectors" — most teams never hit this scale</li>
  <li>"Sub-millisecond latency" — end-to-end RAG latency is dominated by generation, not retrieval</li>
  <li>"Serverless" — can be cost-effective, but some workloads don't benefit</li>
</ul>

<h2>Cost comparison (2026 approximate)</h2>
<p>For 10M vectors, 1024 dim, 100K queries/month:</p>
<ul>
  <li><strong>Pinecone serverless</strong>: ~$300-600/month</li>
  <li><strong>Qdrant self-hosted on a modest server</strong>: ~$100-200/month in cloud costs</li>
  <li><strong>pgvector on existing Postgres</strong>: marginal cost</li>
  <li><strong>Weaviate Cloud</strong>: ~$400-800/month</li>
  <li><strong>Turbopuffer</strong>: ~$50-200/month</li>
</ul>

<p>Self-hosted wins on cost at scale. Managed wins on operational simplicity.</p>

<h2>Lock-in considerations</h2>
<p>Migrating vector DBs is moderately painful but not catastrophic:</p>
<ul>
  <li>Re-index is the big cost. If you can keep embeddings, migration is data movement.</li>
  <li>Metadata schema differences require mapping.</li>
  <li>Query API differences require code changes.</li>
</ul>

<p>Build an abstraction layer over your vector DB calls. Don't scatter provider-specific code across your app. A simple repository/interface pattern saves weeks when you eventually migrate.</p>

<h2>The trap to avoid</h2>
<p>Don't pick a vector DB based on a benchmark blog post. Every vendor publishes benchmarks that show them winning. The meaningful questions are:</p>
<ul>
  <li>Can your team operate it?</li>
  <li>Does it support your required features?</li>
  <li>Is the cost sustainable at your projected scale?</li>
  <li>Does it integrate with your stack?</li>
</ul>

<p>The performance differences between top-tier vector DBs at reasonable scale are usually less than the differences between chunking strategies. Pick a reasonable DB and move on.</p>

<h2>My current defaults</h2>
<ul>
  <li>Prototype: Chroma or pgvector</li>
  <li>Production, self-hosted leaning: Qdrant</li>
  <li>Production, managed leaning: Pinecone</li>
  <li>Production with heavy hybrid search needs: Weaviate</li>
  <li>Already in AWS, already use Postgres: pgvector on RDS</li>
  <li>Already running ES/OS: their vector support</li>
</ul>

<p style="margin-top:40px;">Next: <a href="../retrieval/vector-search.html">Vector similarity search</a>.</p>
""",
    prev=("Cost optimization", "cost-optimization.html"),
    nxt=("Vector similarity search", "../retrieval/vector-search.html"),
)


# ============================================================
# RETRIEVAL STRATEGIES (7 pages)
# ============================================================

write_rag_page(
    slug="retrieval/vector-search",
    title="Vector similarity search",
    description="The core retrieval primitive in RAG. Simple in concept, with a few sharp edges worth knowing.",
    reading_time=4,
    body_html="""
<p class="lede">Vector similarity search is the baseline retrieval operation in RAG: embed the query, find the nearest neighbors in your index, return the top-k. It's deceptively simple. The nuances are in top-k choice, similarity metrics, and what you do with the results.</p>

<h2>The basic flow</h2>
<ol>
  <li>User submits query</li>
  <li>Embed query with the same model used for the corpus</li>
  <li>Search vector index for top-k nearest neighbors</li>
  <li>Return chunks, with scores, for downstream use (rerank, generation)</li>
</ol>

<h2>Top-k choice</h2>
<p>How many chunks to retrieve? Tradeoffs:</p>
<ul>
  <li><strong>Too few</strong>: if the right chunk is at rank 8 and you retrieve top-5, you miss it.</li>
  <li><strong>Too many</strong>: more noise, more cost, diluted attention in the generator.</li>
</ul>

<p>Typical production values:</p>
<ul>
  <li>Without reranker: top-5 to top-10</li>
  <li>With reranker: top-50 to top-100 retrieved, rerank to top-5 to top-10</li>
</ul>

<p>The reranker lets you cast a wider net at retrieval, then filter precisely. Without one, you're stuck relying on the embedding model's own ranking, which is noisier.</p>

<h2>Similarity metrics</h2>

<h3>Cosine similarity</h3>
<p>Measures angle between vectors, ignores magnitude. Most common. Ranges from -1 (opposite) to 1 (identical).</p>

<h3>Dot product</h3>
<p>When vectors are normalized (length = 1), dot product equals cosine. Many modern embedding models output pre-normalized vectors, so dot product is equivalent and slightly faster.</p>

<h3>Euclidean distance</h3>
<p>Straight-line distance. Rarely used for text because it's sensitive to magnitude, which doesn't carry semantic meaning in text embeddings.</p>

<p>Match your similarity metric to what the embedding model was trained with. Mismatches degrade retrieval silently.</p>

<h2>Score thresholds</h2>
<p>Beyond top-k, you can set a minimum score threshold. Chunks below the threshold aren't returned even if they're in top-k.</p>

<p>Useful for:</p>
<ul>
  <li>Distinguishing "we found nothing relevant" from "we found something weak"</li>
  <li>Avoiding hallucination-inducing irrelevant context</li>
  <li>Reducing noise in low-signal queries</li>
</ul>

<p>Setting the threshold: run your eval set, look at score distributions for known-good vs known-bad pairs. Threshold is usually somewhere around 0.6-0.75 cosine for decent matches.</p>

<h2>The "lost in the middle" problem</h2>
<p>LLMs given long contexts pay more attention to the beginning and end than the middle. If you pass 20 retrieved chunks, the chunks in positions 8-13 often get under-weighted during generation.</p>

<p>Mitigations:</p>
<ul>
  <li>Retrieve fewer chunks and use reranking</li>
  <li>Order chunks strategically: most relevant first and last</li>
  <li>Summarize long contexts before generation</li>
</ul>

<h2>Diversity and MMR</h2>
<p>Top-k pure similarity can return 5 chunks that are near-duplicates of each other. The user wanted 5 different perspectives; they got 1 perspective repeated.</p>

<p>Maximum Marginal Relevance (MMR): trade some similarity for diversity. After each chunk is selected, penalize chunks similar to ones already selected.</p>

<p>Most vector DBs support MMR or similar diversification strategies. Worth using when you retrieve from corpora with near-duplicate content.</p>

<h2>Multi-vector queries</h2>
<p>Some systems retrieve with multiple query variations (the original query plus paraphrases, query decompositions, HyDE outputs) and union the results. See <a href="multi-query.html">multi-query + fusion</a>.</p>

<h2>The common first mistake</h2>
<p>Teams ship RAG v1 with top-5 vector search, no reranking, and wonder why quality is mediocre. The fix — top-50 retrieval with a reranker — is usually a 10-20% quality improvement for minimal additional latency.</p>

<p>Vector search is the foundation. Everything after it is where the quality wins come from.</p>

<p style="margin-top:40px;">Next: <a href="bm25-sparse.html">BM25 and sparse retrieval</a>.</p>
""",
    prev=("Choosing a vector DB", "../vectors/choosing-a-db.html"),
    nxt=("BM25 and sparse retrieval", "bm25-sparse.html"),
)


write_rag_page(
    slug="retrieval/bm25-sparse",
    title="BM25 and sparse retrieval",
    description="BM25 is 50 years old and still essential in 2026. Here's why every serious RAG system uses it alongside dense vectors.",
    reading_time=4,
    body_html="""
<p class="lede">BM25 is a classical keyword-based retrieval algorithm, older than most of your AI infrastructure. It's also essential in modern RAG. The reason: dense embeddings have blind spots that BM25 fills in cleanly. Any production RAG that isn't using BM25 somewhere is leaving 10-20% of retrieval quality on the floor.</p>

<h2>How BM25 works</h2>
<p>BM25 scores how well a query matches a document based on:</p>
<ul>
  <li><strong>Term frequency</strong>: how often query terms appear in the document</li>
  <li><strong>Inverse document frequency</strong>: how rare those terms are across the corpus</li>
  <li><strong>Document length normalization</strong>: longer documents naturally have more term occurrences; BM25 accounts for this</li>
</ul>

<p>The score rewards documents that have the query's rare terms at reasonable frequency, normalized by length.</p>

<h2>When BM25 wins over dense</h2>
<ul>
  <li>Exact identifier matches (SKU-12345, error code E-47, UUID)</li>
  <li>Proper nouns not well-represented in embedding training data (company-specific terms, acronyms)</li>
  <li>Negation ("excluding X") where embeddings confuse similar intents</li>
  <li>Very short queries (1-2 words) where embeddings struggle with context</li>
  <li>Queries where users type technical jargon verbatim</li>
</ul>

<h2>When dense wins over BM25</h2>
<ul>
  <li>Paraphrased queries ("how do I reset my password" vs docs talking about "password recovery")</li>
  <li>Cross-lingual retrieval</li>
  <li>Conceptual matches where query and doc share no exact words</li>
  <li>Queries that imply intent rather than stating keywords</li>
</ul>

<h2>BM25 in production</h2>

<h3>Elasticsearch / OpenSearch</h3>
<p>Gold standard for BM25. Full-text search with tokenization, stemming, analyzers, boosting. If you're serious about search, this is a natural fit.</p>

<h3>Postgres full-text</h3>
<p>Reasonable BM25 support via tsvector and ts_rank_cd. Good when you already have Postgres and don't need Elasticsearch-level search features.</p>

<h3>Native in vector DBs</h3>
<p>Weaviate, Qdrant (via sparse vectors), Vespa, Pinecone (sparse vectors), Milvus all support BM25 or similar sparse search natively. Removes the need for a separate search system.</p>

<h3>Library: rank-bm25 (Python)</h3>
<p>In-memory BM25 for small corpora or prototyping. Not production-scale.</p>

<h2>Tokenization matters</h2>
<p>BM25 quality depends heavily on tokenization:</p>
<ul>
  <li>Lowercase normalization</li>
  <li>Stopword removal (configurable; sometimes hurts precision)</li>
  <li>Stemming ("running" → "run"; helps recall, can hurt precision)</li>
  <li>Lemmatization (like stemming but linguistically aware)</li>
  <li>N-grams for phrase matching</li>
  <li>Language-specific tokenizers for non-English</li>
</ul>

<p>Your BM25 quality is capped by tokenization choices. Default English tokenizers work for most cases. Specialized domains (law, medicine, chemistry) often need custom tokenizers.</p>

<h2>BM25F and field-weighted search</h2>
<p>BM25F extends BM25 to weight different fields differently. A match in the title might be worth 3x a match in the body. For documents with structure (title, abstract, body), this is valuable.</p>

<p>Elasticsearch supports this via multi_match queries. Many vector DBs don't — another reason to consider ES/OS for structured text search.</p>

<h2>Learned sparse: SPLADE</h2>
<p>A newer approach: use a transformer to learn sparse vector representations. Each token contributes to a high-dimensional sparse vector, with the model learning which tokens matter and expanding queries with learned synonyms.</p>

<p>Benefits:</p>
<ul>
  <li>Bridges the gap between BM25 and dense embeddings</li>
  <li>Automatic term expansion (query "laptop" matches documents about "notebook computers")</li>
  <li>Uses existing sparse-vector infrastructure</li>
</ul>

<p>Drawbacks:</p>
<ul>
  <li>More compute at index time and query time</li>
  <li>Less mature than BM25 in production tooling</li>
</ul>

<p>Models: SPLADE v3, naver/splade. Supported by recent Qdrant, Vespa, OpenSearch.</p>

<h2>Hybrid is the answer</h2>
<p>In almost every production RAG system, BM25 + dense hybrid outperforms either alone. The sparse and dense vectors capture complementary signal. The fusion (RRF or similar) combines them cleanly. See <a href="hybrid.html">hybrid retrieval</a>.</p>

<h2>The old-school lesson</h2>
<p>BM25 is fast, predictable, debuggable, and free of GPU dependencies. When your vector search is broken, your metrics are confusing, or your embeddings go stale, BM25 still works. Keep it in the stack as a fallback if nothing else.</p>

<p style="margin-top:40px;">Next: <a href="hybrid.html">Hybrid retrieval</a>.</p>
""",
    prev=("Vector similarity search", "vector-search.html"),
    nxt=("Hybrid retrieval", "hybrid.html"),
)


write_rag_page(
    slug="retrieval/hybrid",
    title="Hybrid retrieval",
    description="Hybrid retrieval combines dense and sparse methods, fused into one ranked list. It's the production default for a reason.",
    reading_time=5,
    body_html="""
<p class="lede">Hybrid retrieval runs dense (vector) and sparse (BM25) searches and combines their results. It's the production default for any serious RAG system. This page covers the specific mechanics of how fusion works and where the tuning knobs are.</p>

<h2>The architecture</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
              query
              /    \\
             /      \\
        embed       tokenize
          |            |
     vector search  BM25 search
          |            |
       top-50       top-50
          \\           /
           \\         /
          fusion (RRF)
               |
          top-50 merged
               |
           reranker
               |
           top-10
               |
         generation
</pre>

<h2>The two retrievers</h2>
<ul>
  <li><strong>Dense retriever</strong>: vector similarity search over embeddings. See <a href="vector-search.html">vector search</a>.</li>
  <li><strong>Sparse retriever</strong>: BM25 or similar keyword-based scoring. See <a href="bm25-sparse.html">BM25 and sparse retrieval</a>.</li>
</ul>

<p>They run in parallel, each returning their own ranked list.</p>

<h2>Fusion with Reciprocal Rank Fusion (RRF)</h2>
<p>The standard combination method. Each document's final score is the sum of reciprocal ranks across retrievers:</p>

<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
final_rrf(d) = sum(1 / (k + rank_i(d))) for each retriever i
</pre>

<p>Where k is a small constant (default 60). Documents in both lists get scored from both; documents in only one get scored from that one only.</p>

<p>Why RRF works well:</p>
<ul>
  <li>Score-scale-independent: dense scores (0-1) and BM25 scores (0-30+) don't need normalization</li>
  <li>Simple, deterministic, no tuning</li>
  <li>Robust across different retriever combinations</li>
</ul>

<h2>Alternative fusion methods</h2>

<h3>Normalized weighted sum</h3>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
final = α × norm(dense_score) + (1-α) × norm(sparse_score)
</pre>
<p>Requires choosing α. Can tune on eval set. Typical α: 0.5 to 0.7 (slight dense bias).</p>

<h3>CombSUM, CombMAX, CombMNZ</h3>
<p>Variants on score combination. Rarely materially better than RRF in practice.</p>

<h3>Learned fusion (LTR)</h3>
<p>Train a learning-to-rank model on labeled query-document pairs. Most complex, potentially highest quality. Worth it at serious scale with labeled data.</p>

<h2>Native hybrid in vector DBs</h2>

<h3>Weaviate</h3>
<p>Native hybrid search with an alpha parameter (0 = pure sparse, 1 = pure dense). Simplest ergonomics.</p>

<h3>Qdrant</h3>
<p>Sparse vector support plus dense in one query. RRF or custom fusion.</p>

<h3>Pinecone</h3>
<p>Sparse-dense hybrid with rerank-on-top pattern.</p>

<h3>Elasticsearch / OpenSearch</h3>
<p>Excellent BM25 plus vector support. Rank fusion via RRF available.</p>

<h3>Vespa</h3>
<p>Strong hybrid with custom ranking expressions.</p>

<h2>The right top-k per retriever</h2>
<p>For RRF, retrieve deeper than your final desired count:</p>
<ul>
  <li>Want 10 final results? Retrieve top-50 from each retriever, fuse, take top-50 merged, rerank.</li>
  <li>Want 50 final results? Retrieve top-100+ from each retriever.</li>
</ul>

<p>The deeper retrieval gives RRF more signal. Diminishing returns beyond top-100 per retriever for most applications.</p>

<h2>Where hybrid falls short</h2>

<h3>Queries with no good sparse signal</h3>
<p>Purely semantic queries ("what's the meaning of X") don't get much help from BM25 if the query terms are different from any document terms.</p>

<h3>Corpora with non-text content</h3>
<p>BM25 doesn't help when documents are primarily tables, numbers, or images.</p>

<h3>Extremely noisy text</h3>
<p>OCR'd text with errors can match BM25 on typos; dense embeddings are more robust to this.</p>

<p>Hybrid is a reliable default, not a universal solution.</p>

<h2>The diagnostic workflow</h2>
<p>When a query is failing:</p>
<ol>
  <li>Run dense-only: did it return the right answer?</li>
  <li>Run sparse-only: did it return the right answer?</li>
  <li>Run hybrid: did fusion hurt or help?</li>
</ol>

<p>If dense has it and hybrid doesn't, fusion is buffering the right answer with weaker sparse results. Tune fusion weight.</p>
<p>If sparse has it and hybrid doesn't, the same in reverse.</p>
<p>If neither has it, it's a chunking or embedding problem upstream.</p>

<h2>Metrics</h2>
<p>Measure each retriever separately and the hybrid result. Hit rate@10 and MRR for each. Over time you'll build intuition for which query types need which retriever.</p>

<p>Some queries do best on dense only. Some do best on sparse only. Hybrid averages them, which is usually — but not always — a win. Diagnostic data helps you decide when to override hybrid with a routing strategy.</p>

<p style="margin-top:40px;">Next: <a href="reranking.html">Reranking</a>.</p>
""",
    prev=("BM25 and sparse retrieval", "bm25-sparse.html"),
    nxt=("Reranking", "reranking.html"),
)


write_rag_page(
    slug="retrieval/reranking",
    title="Reranking",
    description="Reranking is the single highest-leverage retrieval improvement. A cross-encoder on top of initial retrieval typically adds 10-30% to quality.",
    reading_time=5,
    body_html="""
<p class="lede">Reranking takes a retrieved candidate set and reorders it with a more accurate (but slower) model. It's the single most impactful addition you can make to a naive RAG system. Skipping it is the most common reason production RAG systems underperform their potential.</p>

<h2>Why reranking exists</h2>
<p>Initial retrieval (dense or hybrid) uses independent embeddings — one for the query, one for each document. The similarity score is a good approximation but not a deep match. A cross-encoder reranker considers query and document together, producing a much more accurate relevance score — at much higher cost per pair.</p>

<p>The pattern: retrieve cheaply, rerank precisely.</p>

<h2>The flow</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
1. Initial retrieval returns top-50 or top-100 candidates
2. Reranker scores each (query, candidate) pair
3. Re-sort by reranker score
4. Take top-5 or top-10 to send to generator
</pre>

<p>You retrieve wide (to catch the right answer somewhere in the set), then narrow precisely (so the generator sees clean context).</p>

<h2>Bi-encoders vs cross-encoders</h2>

<h3>Bi-encoder (initial retrieval)</h3>
<p>Embed query and documents separately. Compare via cosine similarity. Fast at retrieval time because document embeddings are precomputed.</p>

<h3>Cross-encoder (reranker)</h3>
<p>Concatenate query + document, pass through a transformer, output a score. Much more accurate because the model can attend jointly to both. Cannot be precomputed — score must be computed at query time for each candidate.</p>

<h2>Reranker options</h2>

<h3>Open-source cross-encoders</h3>
<ul>
  <li><strong>cross-encoder/ms-marco-MiniLM-L-6-v2</strong>: fast, decent quality. Good baseline.</li>
  <li><strong>cross-encoder/ms-marco-electra-base</strong>: higher quality, more compute.</li>
  <li><strong>BGE reranker</strong> (bge-reranker-large, bge-reranker-v2-m3): strong open-source rerankers.</li>
  <li><strong>Jina reranker</strong>: competitive, available as API or open weights.</li>
</ul>

<h3>Commercial rerankers</h3>
<ul>
  <li><strong>Cohere Rerank 3</strong>: widely used, strong quality. API-only.</li>
  <li><strong>Voyage Rerank 2</strong>: comparable to Cohere.</li>
  <li><strong>Mixedbread mxbai-rerank</strong>: commercial or self-hosted.</li>
</ul>

<h3>LLM-as-reranker</h3>
<p>Pass the top-20 candidates to a small LLM with a prompt to re-rank. Highest quality in some cases, but slower and more expensive per query. Worth trying when nothing else works.</p>

<h2>Latency</h2>
<p>Cross-encoder reranking adds latency:</p>
<ul>
  <li>ms-marco-MiniLM on top-50: 30-100ms on GPU</li>
  <li>bge-reranker-large on top-50: 100-300ms on GPU</li>
  <li>Cohere Rerank 3 API on top-50: 100-400ms (network + inference)</li>
  <li>LLM-based rerank on top-20: 500-2000ms</li>
</ul>

<p>For real-time RAG, choose the reranker that fits your latency budget. For batch or high-stakes queries, prefer higher quality.</p>

<h2>The quality gain</h2>
<p>On standard benchmarks, adding a reranker typically improves top-10 relevance by 15-30%. In domain-specific applications, gains can be higher.</p>

<p>On a real RAG system, the user-visible effect is usually: fewer irrelevant chunks in the context, so the generator has cleaner input and produces fewer hallucinations or off-topic answers.</p>

<h2>How many candidates to rerank</h2>
<p>Tradeoffs:</p>
<ul>
  <li>Top-20 rerank: fast, catches most of the gain</li>
  <li>Top-50 rerank: typical sweet spot</li>
  <li>Top-100 rerank: higher recall, more cost</li>
  <li>Top-200+: diminishing returns; your initial retrieval is broken if the right answer is at rank 150</li>
</ul>

<h2>Multi-stage reranking</h2>
<p>For very large initial candidate sets, chain rerankers of increasing precision:</p>
<ol>
  <li>Retrieve top-500 with fast sparse+dense hybrid</li>
  <li>Rerank with fast cross-encoder (MiniLM) → top-50</li>
  <li>Rerank with high-quality cross-encoder (bge-reranker-large or Cohere) → top-10</li>
  <li>Pass to generator</li>
</ol>

<p>Each stage is cheap in aggregate because the candidate set shrinks rapidly. Used at Google-scale search for decades.</p>

<h2>Reranking with additional signal</h2>
<p>Rerankers can take more than just text similarity into account:</p>
<ul>
  <li><strong>Recency</strong>: boost documents published recently</li>
  <li><strong>Authority</strong>: boost canonical sources over derived</li>
  <li><strong>User history</strong>: boost documents the user has previously found useful</li>
  <li><strong>Metadata match</strong>: boost documents matching inferred query intent</li>
</ul>

<p>Typical approach: combine the reranker score with metadata-derived boosts in a weighted sum. This is where reranking starts looking like a classical learning-to-rank system.</p>

<h2>When reranking doesn't help</h2>
<p>Rare but real cases:</p>
<ul>
  <li>Initial retrieval is so bad that the right answer isn't in top-100 (reranker can't save you)</li>
  <li>Corpus is small enough that top-5 retrieval is already near-optimal</li>
  <li>Query-document relevance is purely metadata-based (then prefer classical LTR over embedding-based rerank)</li>
</ul>

<h2>My default setup</h2>
<p>For production RAG:</p>
<ol>
  <li>Hybrid retrieval (dense + BM25) → top-50</li>
  <li>RRF fusion of the two result sets</li>
  <li>Cross-encoder rerank (bge-reranker or Cohere) → top-10</li>
  <li>Pass top-10 to generator</li>
</ol>

<p>This stack handles the 80% case well. It's also what I'd A/B test against any naive "just vector search" baseline.</p>

<p style="margin-top:40px;">Next: <a href="query-rewriting.html">Query rewriting</a>.</p>
""",
    prev=("Hybrid retrieval", "hybrid.html"),
    nxt=("Query rewriting", "query-rewriting.html"),
)


write_rag_page(
    slug="retrieval/query-rewriting",
    title="Query rewriting",
    description="Users ask poorly-phrased questions. An LLM can rewrite them into forms that retrieve better. Here's how and when to do this.",
    reading_time=4,
    body_html="""
<p class="lede">Users don't phrase queries the way documents do. They use pronouns, they're brief, they ask follow-ups that depend on context. Query rewriting uses an LLM to rewrite the user's query into a form better suited for retrieval. It's one of the lowest-effort quality wins in modern RAG.</p>

<h2>The problem query rewriting solves</h2>

<h3>Ambiguous pronouns</h3>
<p>User: "how does it handle rate limiting?"</p>
<p>The embedding of "how does it handle rate limiting" doesn't know what "it" is. Retrieved chunks may be about rate limiting in general, missing the specific product the user meant.</p>

<h3>Conversational follow-ups</h3>
<p>Turn 1: "Tell me about Pinecone's pricing."</p>
<p>Turn 2: "What about performance?"</p>
<p>Turn 2 alone embeds as a generic performance question. With rewriting: "How does Pinecone perform?"</p>

<h3>Short queries</h3>
<p>"refund policy" vs "what is our customer refund policy including eligibility, timeframe, and process"</p>
<p>The expanded version retrieves better because it provides more signal to match against.</p>

<h3>Mismatched vocabulary</h3>
<p>User says "login not working"; docs say "authentication failures." Rewriting to include synonyms bridges the gap.</p>

<h2>The rewriting patterns</h2>

<h3>1. Contextualization</h3>
<p>Rewrite the query to resolve pronouns and implicit context from conversation history.</p>

<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
Given the conversation history:
- User: Tell me about Pinecone pricing
- Assistant: [response about Pinecone]
- User: What about performance?

Rewrite the last user query as a standalone search query.

→ "How does Pinecone perform?"
</pre>

<h3>2. Query expansion</h3>
<p>Add synonyms, related terms, or rephrasings to improve lexical matching.</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
"login issues" → "login authentication sign-in access issues problems failures"
</pre>

<h3>3. Query decomposition</h3>
<p>Break a compound query into sub-queries. Retrieve for each separately.</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
"What's our refund policy and how do I escalate a billing dispute?"
→ ["What is the refund policy?", "How to escalate a billing dispute?"]
</pre>

<h3>4. Step-back questions</h3>
<p>Generate a more general version of the query to retrieve broader context.</p>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
"Why did my OAuth token expire after 2 hours?"
→ step-back: "How does OAuth token expiration work?"
</pre>

<h3>5. Hypothetical Document Embeddings (HyDE)</h3>
<p>Generate a fake answer, embed that, retrieve based on its embedding. See <a href="hyde.html">HyDE</a>.</p>

<h2>Prompt patterns for rewriting</h2>

<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
SYSTEM: You are a search query optimizer. Given a user query, rewrite
it as a clear, self-contained search query that would retrieve the
most relevant documents. Expand abbreviations, resolve pronouns, and
include relevant synonyms. Return only the rewritten query.

USER: [raw query]
</pre>

<h2>Using a small model</h2>
<p>Query rewriting doesn't need your best reasoning model. A fast, cheap model (GPT-4o-mini, Claude Haiku, Gemini Flash) does this well. Latency 50-200ms per rewrite. Cost is a fraction of the generation step.</p>

<h2>The multi-query pattern</h2>
<p>Generate multiple rewrites and run retrieval for each. Union and dedupe. More coverage, more cost. See <a href="multi-query.html">multi-query + fusion</a>.</p>

<h2>When to skip query rewriting</h2>
<ul>
  <li>Very short queries with clear intent ("reset password")</li>
  <li>Latency-critical applications where the extra LLM call is too expensive</li>
  <li>When the corpus vocabulary closely matches user vocabulary</li>
</ul>

<h2>Diagnostic: is rewriting helping?</h2>
<p>Compare retrieval quality with and without rewriting on the same eval set. Rewriting should improve hit rate, especially on:</p>
<ul>
  <li>Conversational queries with history</li>
  <li>Short, ambiguous queries</li>
  <li>Queries with vocabulary mismatches</li>
</ul>

<p>If rewriting doesn't help, your initial retrieval already handles query variety well (or your rewriting prompt is wrong). Test both hypotheses.</p>

<h2>Preserving user intent</h2>
<p>The failure mode of query rewriting: the rewrite subtly changes what the user asked. Guard against this by:</p>
<ul>
  <li>Logging both original and rewritten queries</li>
  <li>Including the original query in the final context to the LLM, not just the rewritten version</li>
  <li>A/B testing rewriter prompts against held-out evaluation queries</li>
</ul>

<p style="margin-top:40px;">Next: <a href="hyde.html">HyDE</a>.</p>
""",
    prev=("Reranking", "reranking.html"),
    nxt=("HyDE", "hyde.html"),
)


write_rag_page(
    slug="retrieval/hyde",
    title="HyDE (Hypothetical Document Embeddings)",
    description="HyDE has the LLM hallucinate an answer first, then retrieves documents similar to that hallucination. Counterintuitive and often effective.",
    reading_time=4,
    body_html="""
<p class="lede">HyDE (Hypothetical Document Embeddings) is a retrieval technique with a counterintuitive core idea: generate a fake answer to the user's query with an LLM, embed that fake answer, and retrieve real documents similar to it. The LLM's hallucination serves as a better query representation than the original question. It works surprisingly well.</p>

<h2>Why it works</h2>
<p>Dense retrieval matches query embeddings to document embeddings. A short query is a weak representation — it matches <em>questions</em> better than <em>answers</em>. But your documents are answers. A hallucinated "answer-shaped" text is a stronger representation of what you're looking for, so it matches better.</p>

<p>The LLM's factual accuracy doesn't matter for retrieval — only its structural and vocabulary similarity to real documents.</p>

<h2>The flow</h2>
<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
1. User query: "How do I set up OAuth with Google?"
2. LLM prompt: "Write a short passage that would answer this question"
3. LLM output: "To set up OAuth with Google, first create a project in
   the Google Cloud Console. Then enable the Google+ API, configure
   OAuth consent, and generate client credentials. Use these credentials
   in your application's OAuth flow..."
4. Embed the LLM output (not the query)
5. Retrieve documents similar to the hypothetical passage
6. Pass real retrieved docs to final generation
</pre>

<h2>When HyDE wins</h2>
<ul>
  <li>Queries are short and retrieval quality is noisy</li>
  <li>The corpus is answer-shaped (documentation, encyclopedias, manuals)</li>
  <li>Vocabulary mismatch between queries and documents</li>
  <li>No labeled query-doc pairs are available to fine-tune an embedding model</li>
</ul>

<h2>When HyDE doesn't help</h2>
<ul>
  <li>Queries are already detailed and verbose</li>
  <li>Corpus has strong BM25-friendly keyword overlap with queries</li>
  <li>Latency budget is tight (HyDE adds an LLM call)</li>
  <li>The corpus domain is unfamiliar to the LLM (it can't hallucinate plausibly)</li>
</ul>

<h2>Cost and latency</h2>
<p>HyDE adds one LLM call before retrieval. With a small fast model, this is 100-500ms. For real-time RAG, weigh the latency cost against quality gain.</p>

<p>Mitigation: use the cheapest fast model (Haiku, GPT-4o-mini, Flash) for the hypothetical generation. Accuracy of the hallucination isn't critical — structural similarity is.</p>

<h2>Variants</h2>

<h3>Query + HyDE combined</h3>
<p>Retrieve using both the original query embedding and the HyDE embedding. Fuse results with RRF. Often better than either alone.</p>

<h3>Multiple hypothetical documents</h3>
<p>Generate 3-5 hypothetical passages, embed each, retrieve with each, union. More coverage but more cost.</p>

<h3>HyDE with reasoning</h3>
<p>Prompt the LLM to first reason about what kinds of documents would answer the question, then write one. Produces higher-quality hypothetical passages for complex queries.</p>

<h2>The hallucination risk</h2>
<p>HyDE generates fake content. The concern: what if the fake passage anchors the user's understanding or biases downstream generation?</p>

<p>The safeguard: the fake passage is only used for retrieval, never shown to the user and never passed to the final generation step. Final generation uses the real retrieved documents. HyDE is invisible to everything after retrieval.</p>

<h2>Implementation</h2>

<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:12px;">
SYSTEM: Given a user question, write a 3-5 sentence passage that would
be a plausible excerpt from a document that answers the question. Use
the vocabulary, structure, and level of detail typical of technical
documentation. Don't worry about factual accuracy; focus on writing
text that matches the style of real documentation.

USER: [user question]

ASSISTANT: [hypothetical passage]
</pre>

<p>Then: <code>retrieval_query = embed(hypothetical_passage)</code></p>

<h2>Measured gains</h2>
<p>On benchmarks, HyDE typically improves retrieval metrics by 5-15% over standard dense retrieval for short queries. The gain shrinks as query length grows (long queries are already answer-shaped).</p>

<h2>The mental model</h2>
<p>Dense retrieval matches "the shape of what you're asking for" to "the shape of documents in the corpus." A short query is a poor shape-match. An answer passage is a great shape-match. HyDE manufactures the latter from the former. That's it.</p>

<p style="margin-top:40px;">Next: <a href="multi-query.html">Multi-query + fusion</a>.</p>
""",
    prev=("Query rewriting", "query-rewriting.html"),
    nxt=("Multi-query + fusion", "multi-query.html"),
)


write_rag_page(
    slug="retrieval/multi-query",
    title="Multi-query + fusion",
    description="One query produces one retrieval. Multiple query variations produce many retrievals that can be fused for better coverage.",
    reading_time=4,
    body_html="""
<p class="lede">A single query embedding represents one angle on what the user wants. Multi-query retrieval generates several variations, retrieves for each, and fuses the results. It's a robust way to improve recall on tricky queries at the cost of more compute.</p>

<h2>The pattern</h2>
<ol>
  <li>Take the user's original query</li>
  <li>Use an LLM to generate N variations (paraphrases, sub-questions, step-back questions, HyDE passages)</li>
  <li>Run retrieval for each variation independently</li>
  <li>Fuse the result lists (RRF or similar)</li>
  <li>Take the top-K merged results</li>
  <li>Optionally rerank</li>
</ol>

<h2>Kinds of variations</h2>

<h3>Paraphrases</h3>
<p>Same meaning, different words.</p>
<ul>
  <li>"How do I reset my password?"</li>
  <li>"What's the process for changing login credentials?"</li>
  <li>"Steps to recover account access when locked out"</li>
</ul>

<h3>Sub-questions</h3>
<p>Decompose into parts.</p>
<ul>
  <li>"Why is our API slow?" → "What's the current API latency?" + "What are common causes of API latency?" + "How do we measure API performance?"</li>
</ul>

<h3>Step-back</h3>
<p>More general framing.</p>
<ul>
  <li>"Why did OAuth token expire?" → "How does OAuth token expiration work?"</li>
</ul>

<h3>Step-forward</h3>
<p>More specific framing.</p>
<ul>
  <li>"How do I integrate your API?" → "How do I integrate your API in Node.js?" + "How do I integrate your API in Python?"</li>
</ul>

<h3>HyDE-style answers</h3>
<p>Hypothetical answer passages. See <a href="hyde.html">HyDE</a>.</p>

<h2>Fusion</h2>
<p>Same as hybrid retrieval fusion — RRF is the default.</p>

<pre style="background:#f5f5f7; padding:14px; border-radius:6px; font-family:'JetBrains Mono', monospace; font-size:13px;">
For each document d:
  rrf_score(d) = sum over all queries q: 1 / (k + rank_q(d))

Sort documents by rrf_score. Take top-K.
</pre>

<p>Documents that appear in multiple query variations' results get boosted. Documents that only appear in one get retained at lower ranks.</p>

<h2>The RAG-Fusion technique</h2>
<p>A specific multi-query pattern popularized around 2023:</p>
<ol>
  <li>Generate 4-5 paraphrases of the original query</li>
  <li>Retrieve top-k for each paraphrase</li>
  <li>RRF fusion</li>
</ol>

<p>Robust improvement over single-query retrieval on queries with vocabulary mismatch.</p>

<h2>Parallel vs sequential retrieval</h2>
<p>All query variations can run in parallel. With async retrieval, total latency is (LLM variation generation) + (longest single retrieval) — not the sum.</p>

<p>With 4 variations and ~100ms each retrieval, parallel retrieval adds roughly 100ms total latency, not 400ms.</p>

<h2>Cost tradeoffs</h2>
<ul>
  <li>N variations = N retrieval calls. At high QPS this adds up.</li>
  <li>LLM call to generate variations: 100-400ms, modest cost with cheap models.</li>
  <li>Reranking cost increases too (more candidates to rerank).</li>
</ul>

<p>In return: typically 5-15% recall improvement, higher for short or ambiguous queries.</p>

<h2>When multi-query is overkill</h2>
<ul>
  <li>Queries that are already specific and verbose</li>
  <li>When hybrid retrieval already covers the recall gap</li>
  <li>Cost-sensitive applications where extra LLM calls aren't justified</li>
  <li>Latency-sensitive applications where the extra 100ms matters</li>
</ul>

<h2>The pragmatic recipe</h2>
<p>For a production RAG system that wants best-in-class retrieval:</p>
<ol>
  <li>Generate 3 paraphrases of the original query (using a fast model)</li>
  <li>For each of the 4 queries (original + 3 paraphrases), run hybrid retrieval for top-50</li>
  <li>RRF-fuse across all 4 result lists</li>
  <li>Rerank top-50 merged → top-10</li>
  <li>Pass to generator</li>
</ol>

<p>This adds about 150-300ms of latency and roughly 4x retrieval cost. For queries that benefited from it, quality is noticeably better. For queries that didn't, you've paid the cost without improvement.</p>

<h2>Routing: when to use multi-query</h2>
<p>Not every query benefits. A lightweight classifier or prompt can decide:</p>
<ul>
  <li>Short queries (&lt; 5 words): use multi-query</li>
  <li>Long detailed queries: single-query is sufficient</li>
  <li>Vague queries with ambiguous intent: use multi-query</li>
  <li>Queries with specific terminology and clear intent: single-query</li>
</ul>

<p>Skip multi-query when it doesn't help. Use it when it does. Measurement tells you which is which.</p>

<p style="margin-top:40px;">Next: <a href="../advanced/agentic-rag.html">Agentic RAG</a>.</p>
""",
    prev=("HyDE", "hyde.html"),
    nxt=("Agentic RAG", "../advanced/agentic-rag.html"),
)

print("\n✓ RAG Part 2: Embeddings + Vectors + Retrieval (18 pages)")
