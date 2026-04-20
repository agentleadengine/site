#!/usr/bin/env python3
"""Rewrite AI glossary entries with plain-English, thorough explanations.

Template for each term:
- def        - one-sentence plain-English answer to "what is this?"
- explain    - a paragraph that builds intuition from zero (no jargon,
               or jargon explicitly introduced)
- example    - concrete, everyday scenario
- why        - why it matters / what you do with this knowledge

The site's existing .gloss-def/.gloss-detail slots become:
- .gloss-def (the simple definition)
- .gloss-explain (new - the build-intuition paragraph)
- .gloss-example (new - boxed example)
- .gloss-why (new - why-it-matters)

Writes back by finding the existing .gloss-topic…related block and
swapping the inner content.
"""
import re
from pathlib import Path

ROOT = Path("/Users/ble/Desktop/sams site")
GLOSSARY = ROOT / "glossary"

# ---------------------------------------------------------------------------
# Content. Each entry: { term, topic, def, explain, example, why, related[] }
# Written at roughly a 5th-6th grade reading level: plain language, clear
# analogies, no "leveraging synergies" language. Thorough without being
# condescending.
# ---------------------------------------------------------------------------
TERMS = {
    "context-window": {
        "term": "Context Window",
        "topic": "AI",
        "def": "The AI's working memory. Everything it can 'see' and 'think about' at once.",
        "explain": (
            "Imagine the model is reading a book out loud to answer your question, "
            "but it can only hold a certain number of pages in its hands at one time. "
            "The context window is how many pages those are. It includes your question, "
            "the conversation so far, any documents you pasted in, the AI's instructions, "
            "and the answer it's generating. When the window is full, the oldest pages "
            "get put down and forgotten. The AI does not remember anything that falls "
            "off the edge of the window unless you tell it again."
        ),
        "example": (
            "You paste a 50-page PDF into Claude and ask a question. That PDF plus your "
            "question plus Claude's answer all have to fit inside the context window. "
            "If you then paste ANOTHER 50-page PDF, the first one might start getting "
            "squeezed out. Ask about page 3 of the first PDF later and Claude might not "
            "remember it - not because it was a bad model, but because the page is no "
            "longer in its hands."
        ),
        "why": (
            "Bigger window = you can feed it more without it losing track. Claude Sonnet "
            "holds 1 million tokens (roughly 750,000 words, about 10 full novels). Older "
            "models held 4,000 tokens (about 3,000 words, 10 pages). When an agent starts "
            "acting weird after a long session, the usual reason is that the important "
            "context has fallen off the window. Fix it by summarizing, chunking, or starting "
            "fresh."
        ),
        "related": ["token", "llm", "attention"],
    },
    "token": {
        "term": "Token",
        "topic": "AI",
        "def": "A small chunk of text. It's how the AI counts how much it's reading and writing.",
        "explain": (
            "The AI doesn't see whole words the way you and I do. It breaks everything into "
            "pieces called tokens. A short word like 'the' is one token. A longer word "
            "like 'autonomous' might be two or three ('aut', 'ono', 'mous'). Punctuation "
            "counts. Spaces count. Emojis count. Roughly, 1 token = 4 characters of English "
            "= 3/4 of a word. 1,000 tokens ≈ 750 words ≈ 3 paragraphs."
        ),
        "example": (
            "The sentence 'Claude is an AI assistant' is about 6 tokens. A 10-page document "
            "is about 3,000-5,000 tokens. This whole glossary entry is about 400 tokens."
        ),
        "why": (
            "You pay per token. Context windows are measured in tokens. Every API bill is a "
            "token bill. If you know your input is 10,000 tokens and your output is 2,000 "
            "tokens, you can estimate cost and speed before you hit Run."
        ),
        "related": ["context-window", "llm"],
    },
    "llm": {
        "term": "LLM (Large Language Model)",
        "topic": "AI",
        "def": "A very large pattern-matcher trained on enormous amounts of text. What people mean when they say 'AI' these days.",
        "explain": (
            "An LLM is a computer program that learned to predict the next word by reading "
            "most of the writing on the internet. That's it. That's the magic trick. If you "
            "give it a half-finished sentence, it can guess what comes next so well that the "
            "answer feels intelligent. Because it learned from so much text, it has absorbed "
            "facts, grammar, code, reasoning patterns, and writing styles. ChatGPT, Claude, "
            "and Gemini are all LLMs."
        ),
        "example": (
            "Type 'The capital of France is' into an LLM. It knows the next most likely word "
            "is 'Paris' because it read that sentence or a close variant hundreds of thousands "
            "of times during training. Now type 'Write a poem about Paris in the style of "
            "Shakespeare' and it's doing the same trick, just over a much longer answer."
        ),
        "why": (
            "Understanding that an LLM is predicting text, not looking things up, explains "
            "almost every strange thing it does: why it can hallucinate, why prompting works, "
            "why it's amazing at some tasks and terrible at others. It is a very smart writer. "
            "It is not a database."
        ),
        "related": ["foundation-model", "transformer", "hallucination", "context-window"],
    },
    "agent": {
        "term": "Agent",
        "topic": "AI",
        "def": "An AI that can take actions on its own. Not just answer, but DO.",
        "explain": (
            "A chatbot writes you an email. An agent writes the email AND sends it. That's "
            "the difference. An agent has tools (send email, search the web, open a file, "
            "run code), a goal, and the ability to decide when to use which tool. It runs "
            "in a loop: think → act → look at the result → think again. It keeps going "
            "until the goal is met or it hits a limit you set."
        ),
        "example": (
            "You tell an agent: 'Find me 5 podcasts about AI and draft personalized pitches.' "
            "A chatbot would give you a template. An agent would search Spotify for AI "
            "podcasts, open each show page, extract the host's name and style, then write "
            "5 custom drafts, and save them to a file. You come back in 10 minutes and the "
            "work is done."
        ),
        "why": (
            "Agents are the whole point of building on top of models. A model by itself is "
            "a parlor trick. A model plus tools plus a loop is a worker. Every useful AI "
            "product shipping in 2026 is some flavor of agent."
        ),
        "related": ["tool-use", "react", "mcp", "function-calling"],
    },
    "mcp": {
        "term": "MCP (Model Context Protocol)",
        "topic": "AI",
        "def": "A standard way for an AI to talk to tools and data. Think of it as a USB port for AI.",
        "explain": (
            "Before MCP, every AI tool had its own custom way of hooking into outside systems. "
            "Want Claude to read your Notion? Custom code. Want ChatGPT to use your CRM? "
            "Different custom code. MCP fixes this by defining ONE protocol. You write an MCP "
            "server once (for Notion, Gmail, your database, whatever), and any MCP-compatible "
            "AI can plug into it. Like how any USB-C device works with any USB-C port."
        ),
        "example": (
            "You install the 'Gmail MCP' and the 'Calendar MCP'. Now Claude, Claude Code, "
            "Cursor, and any other MCP-supporting app can read your email and check your "
            "calendar without anyone writing custom glue code. You add a third tool later, "
            "and every app you have picks it up."
        ),
        "why": (
            "MCP is what turns an AI from a chat window into a hub that connects to everything "
            "you actually use. Without a standard, every integration is a one-off project. "
            "With MCP, it's a plug-in. If you want to build an autonomous system that touches "
            "real tools, MCP is how you do it."
        ),
        "related": ["tool-use", "agent", "function-calling"],
    },
    "rag": {
        "term": "RAG (Retrieval-Augmented Generation)",
        "topic": "AI",
        "def": "Giving an AI a library to look things up in before it answers. Open-book mode.",
        "explain": (
            "An LLM only knows what it learned during training. It doesn't know your company's "
            "internal docs, last week's emails, or a PDF you just got. RAG solves this in three "
            "steps: (1) store your documents in a searchable index; (2) when a question comes in, "
            "find the most relevant snippets; (3) paste those snippets into the AI's prompt along "
            "with the question. Now the AI is 'open-book' - it can quote from your library."
        ),
        "example": (
            "You build a customer support bot for your SaaS. You load all 500 help-center articles "
            "into a vector database. When a customer asks 'how do I cancel?', RAG finds the 3 most "
            "relevant articles, pastes them into the prompt, and the AI writes an answer using only "
            "facts from those articles. No hallucinations."
        ),
        "why": (
            "Fine-tuning takes days, costs money, and gets stale the moment your docs change. RAG "
            "updates the moment you update your docs. Almost every 'ChatGPT for your company' "
            "product is RAG under the hood."
        ),
        "related": ["embedding", "vector-database", "semantic-search", "chunking", "reranking"],
    },
    "embedding": {
        "term": "Embedding",
        "topic": "AI",
        "def": "A way to turn text into numbers that represent its meaning, so computers can compare ideas.",
        "explain": (
            "An embedding is a long list of numbers (usually 384 to 1,536 of them) that captures "
            "the meaning of a piece of text. The trick is: similar meanings get similar number "
            "lists. 'The cat sat on the mat' and 'A feline rested on the rug' will have embeddings "
            "that are very close together, even though they share almost no words. This is how a "
            "computer can 'know' two sentences mean the same thing."
        ),
        "example": (
            "You embed your 500 help-center articles. You embed the question 'how do I cancel?'. "
            "You measure distance between that question's embedding and every article's embedding. "
            "The 3 closest articles are probably the ones that answer the question, even if they "
            "don't use the word 'cancel' (they might say 'end subscription' or 'close account')."
        ),
        "why": (
            "Embeddings are the foundation of RAG, semantic search, classification, and clustering. "
            "Once you have good embeddings for your data, you can do things that keyword search can't."
        ),
        "related": ["vector-database", "semantic-search", "rag", "chunking"],
    },
    "vector-database": {
        "term": "Vector Database",
        "topic": "AI",
        "def": "A database designed to store embeddings and find similar ones fast.",
        "explain": (
            "A vector database is a special kind of database. Instead of letting you search by "
            "exact match ('find rows where email = bob@...'), it lets you search by similarity "
            "('find the embeddings closest to this one'). It can do this across millions or "
            "billions of items in milliseconds because it uses a clever index tuned for high-"
            "dimensional number comparisons."
        ),
        "example": (
            "Pinecone, Weaviate, Qdrant, pgvector (Postgres extension), and Chroma are all vector "
            "databases. You push in a million article embeddings. Later you send an embedded "
            "question. It returns the 5 closest articles in 20 milliseconds."
        ),
        "why": (
            "Without one, RAG doesn't scale. You can fake it with a Python list for 100 documents. "
            "You can't for 100,000."
        ),
        "related": ["embedding", "rag", "semantic-search"],
    },
    "chunking": {
        "term": "Chunking",
        "topic": "AI",
        "def": "Cutting long documents into smaller pieces so the AI can work with them.",
        "explain": (
            "A 300-page manual won't fit in a prompt, and even if it did, asking the model to "
            "reason over it all at once gives bad answers. Chunking is the practice of splitting "
            "documents into smaller, self-contained pieces (usually 200-800 words each) before "
            "you store them. Each chunk gets its own embedding. When a question comes in, you "
            "retrieve the best matching CHUNKS, not whole documents."
        ),
        "example": (
            "You have a 50-page employee handbook. You chunk it into 150 pieces, one per section. "
            "When someone asks 'how many sick days do I get?', RAG retrieves the 3 chunks that "
            "mention sick leave, pastes them into the prompt, and the AI answers using just those "
            "3 paragraphs - not all 50 pages."
        ),
        "why": (
            "Bad chunking is the single biggest reason RAG systems give bad answers. Chunks too "
            "small = missing context. Too big = irrelevant noise overwhelms the real answer. "
            "Getting this right matters more than which model or database you pick."
        ),
        "related": ["rag", "embedding", "retrieval"],
    },
    "semantic-search": {
        "term": "Semantic Search",
        "topic": "AI",
        "def": "Searching by meaning, not exact words.",
        "explain": (
            "Classic keyword search (what Google used to be) matches your query against exact "
            "words on the page. Semantic search matches against MEANING. Under the hood, it "
            "embeds your query and every document, then finds the ones with the closest "
            "embeddings. You can search for 'how to fix a slow laptop' and find articles titled "
            "'speeding up your PC' or 'performance troubleshooting', even though they share zero "
            "keywords with your query."
        ),
        "example": (
            "A product search: the user types 'gift for someone who loves coffee'. Keyword "
            "search returns nothing useful. Semantic search returns espresso machines, coffee "
            "subscription boxes, and artisan mug sets - because those products are semantically "
            "close to 'coffee gift'."
        ),
        "why": (
            "Semantic search is the superpower layer underneath most useful AI features you see "
            "today: smart support bots, 'similar items' recommendations, better search boxes. "
            "When paired with classic keyword search (a 'hybrid' approach), it's the gold standard."
        ),
        "related": ["embedding", "vector-database", "rag", "bm25"],
    },
    "bm25": {
        "term": "BM25",
        "topic": "AI",
        "def": "A classic keyword-matching algorithm. The 'old way' of search that still works great.",
        "explain": (
            "BM25 (short for 'Best Match 25') is a math formula for ranking documents by how well "
            "they match your keyword query. It's been around since the 1990s. It handles word "
            "frequency, document length, and rare-word bonuses in a clever way. Elasticsearch, "
            "OpenSearch, and most classic search engines use it as their core scoring function."
        ),
        "example": (
            "You search 'refund policy' across 10,000 help articles. BM25 ranks articles that use "
            "both 'refund' AND 'policy' frequently, but not too frequently (so it doesn't reward "
            "keyword stuffing), and bumps up shorter articles over longer ones (less fluff)."
        ),
        "why": (
            "The best modern RAG systems don't use semantic search alone. They combine BM25 (for "
            "exact-term precision) with semantic search (for meaning) - this is called 'hybrid "
            "search.' BM25 catches the things semantic search misses, like proper names, codes, "
            "and exact phrases."
        ),
        "related": ["semantic-search", "rag", "embedding"],
    },
    "reranking": {
        "term": "Reranking",
        "topic": "AI",
        "def": "A second pass that reorders search results by how well they actually answer the question.",
        "explain": (
            "The first step of RAG retrieval casts a wide net - pulls back maybe 20-50 "
            "potentially-relevant chunks, fast. Reranking is a smarter-but-slower second pass: "
            "a specialized model reads the query AND each candidate chunk together, then scores "
            "how well that chunk actually answers the query. The top 3-5 get passed to the LLM. "
            "This two-step approach gets much better results than either step alone."
        ),
        "example": (
            "You ask your company bot 'how do I request time off?'. Initial retrieval returns 20 "
            "HR docs. A reranker reads all 20 against your question and promotes the PTO-request "
            "policy page to #1 - even though the retrieval step had it at #7 based on embedding "
            "similarity alone."
        ),
        "why": (
            "Reranking is the single fastest way to improve a mediocre RAG system. Cohere, Voyage "
            "AI, and others sell rerankers as standalone APIs. Adding a reranker usually gives a "
            "10-30% boost in answer quality."
        ),
        "related": ["rag", "semantic-search", "retrieval"],
    },
    "prompt-engineering": {
        "term": "Prompt Engineering",
        "topic": "AI",
        "def": "The craft of writing instructions that get an AI to do what you want.",
        "explain": (
            "LLMs are extraordinarily sensitive to how you phrase a request. The same task can "
            "produce garbage or gold depending on word choice, structure, and what you include. "
            "Prompt engineering is the practice of testing, refining, and standardizing those "
            "prompts so you get reliable results. It includes things like: giving examples "
            "(few-shot), assigning a role ('you are a careful tax accountant'), breaking tasks "
            "into steps, and specifying the output format."
        ),
        "example": (
            "Bad prompt: 'Summarize this.' Better prompt: 'Summarize the key findings of the "
            "following report in 3 bullet points, each no longer than 15 words. Focus on "
            "financial implications, not marketing. Report: [...]'. The second gets consistent, "
            "usable output every time. The first gets a different flavor each run."
        ),
        "why": (
            "Prompt engineering is the cheapest lever you have. Before you fine-tune, before you "
            "build agents, before you add RAG - try rewriting the prompt. A better prompt often "
            "closes 80% of the quality gap."
        ),
        "related": ["system-prompt", "few-shot", "zero-shot"],
    },
    "system-prompt": {
        "term": "System Prompt",
        "topic": "AI",
        "def": "Standing instructions for the AI. The 'rules of engagement' baked in before the conversation starts.",
        "explain": (
            "A system prompt is a message at the very beginning of a chat that sets the AI's role, "
            "tone, constraints, and goals. The user never sees it. It persists for the whole "
            "conversation. It's the difference between a generic assistant and a focused specialist. "
            "Think of it as the job description the AI is working from."
        ),
        "example": (
            "System prompt: 'You are a customer support agent for Acme Corp. Only answer questions "
            "about Acme products. Never discuss competitors. If unsure, say so and offer to hand off "
            "to a human. Keep responses under 80 words.' Now every user message is interpreted "
            "through that lens, with no further setup."
        ),
        "why": (
            "The system prompt is where most production behavior gets defined. Changing one line "
            "can completely transform your agent. Most people underinvest in their system prompt "
            "and then wonder why their AI is inconsistent."
        ),
        "related": ["prompt-engineering", "few-shot"],
    },
    "few-shot": {
        "term": "Few-Shot Prompting",
        "topic": "AI",
        "def": "Teaching the AI a task by showing it a handful of examples, right in the prompt.",
        "explain": (
            "Instead of describing what you want, you SHOW the AI what you want. You put 2-5 "
            "examples of the input-output pattern at the start of your prompt, then ask it to "
            "continue the pattern for a new input. The model picks up the shape, style, and rules "
            "from your examples without any training."
        ),
        "example": (
            "Prompt:\n"
            "Input: 'The product was great'\n"
            "Output: Positive\n\n"
            "Input: 'Never buying again'\n"
            "Output: Negative\n\n"
            "Input: 'It arrived late but worked fine'\n"
            "Output: ?\n\n"
            "The model answers 'Mixed' because you showed it the format."
        ),
        "why": (
            "Few-shot is a superpower for edge cases and domain-specific outputs. When a plain "
            "description isn't enough, examples fix it fast. No code, no training - just add a "
            "few sample inputs and outputs to the prompt."
        ),
        "related": ["zero-shot", "prompt-engineering", "system-prompt"],
    },
    "zero-shot": {
        "term": "Zero-Shot Prompting",
        "topic": "AI",
        "def": "Asking the AI to do a task without showing it any examples. Just describing what you want.",
        "explain": (
            "Zero-shot means zero examples in the prompt. You rely entirely on the model's training "
            "to understand the task from your description alone. Modern LLMs are strong zero-shot "
            "learners - they can usually figure out 'classify this as spam/not-spam' or 'translate "
            "to Spanish' with no examples, because those tasks were well-represented in training."
        ),
        "example": (
            "Prompt: 'Classify this email as urgent, normal, or spam: [email text]'. No examples, "
            "just the task description. The model gets it right most of the time."
        ),
        "why": (
            "Zero-shot works until it doesn't. For common tasks, it's the fastest path to a working "
            "prompt. For niche, ambiguous, or custom-format tasks, you'll need few-shot examples "
            "instead. Start zero-shot; escalate to few-shot when quality slips."
        ),
        "related": ["few-shot", "prompt-engineering"],
    },
    "fine-tuning": {
        "term": "Fine-Tuning",
        "topic": "AI",
        "def": "Teaching an existing model new tricks by training it on your specific examples.",
        "explain": (
            "You take a base model (like GPT or Claude or Llama) that already knows language and "
            "you show it hundreds or thousands of examples of YOUR task. The model's internal "
            "weights shift slightly to get better at that specific kind of input. Done right, "
            "fine-tuning produces a model that's genuinely better at your niche - faster, cheaper "
            "per call, and more consistent than prompt tricks alone."
        ),
        "example": (
            "You have 5,000 support tickets labeled with the correct department. You fine-tune a "
            "small model on those. Now that model routes new tickets with 95% accuracy, at one-"
            "tenth the cost of sending each one to GPT-4 with a big prompt."
        ),
        "why": (
            "Don't reach for fine-tuning first. Try better prompts, then RAG, then agents. "
            "Fine-tune only when (a) you have lots of high-quality labeled data, (b) the task is "
            "repeated at high volume, (c) prompts have topped out, and (d) the cost savings or "
            "consistency gains justify the engineering."
        ),
        "related": ["foundation-model", "llm", "prompt-engineering"],
    },
    "foundation-model": {
        "term": "Foundation Model",
        "topic": "AI",
        "def": "A very large, general-purpose model trained on broad data. The base layer that specific applications build on.",
        "explain": (
            "Foundation models are the big ones: GPT-5, Claude Opus, Gemini, Llama. They cost "
            "hundreds of millions to train. They're designed to be broadly capable - handling "
            "writing, code, math, reasoning, and more. Everything downstream (fine-tuned models, "
            "agents, RAG pipelines, ChatGPT itself) is built on top of a foundation model. The "
            "term 'foundation' is literal: without them, nothing else in the AI product layer exists."
        ),
        "example": (
            "Claude Sonnet is a foundation model. When you use Claude.ai, or an app built with the "
            "Claude API, you're hitting that same foundation model underneath. Cursor, Perplexity, "
            "and thousands of products are just interfaces on top of foundation models they don't own."
        ),
        "why": (
            "Picking the right foundation model is the single biggest product decision you'll make. "
            "The rest - prompts, tools, UI - can be rebuilt. The model choice determines what's even "
            "possible."
        ),
        "related": ["llm", "fine-tuning", "transformer"],
    },
    "transformer": {
        "term": "Transformer",
        "topic": "AI",
        "def": "The neural network design that made modern AI possible. What's inside every LLM.",
        "explain": (
            "The transformer is a blueprint for a type of neural network, introduced by Google in "
            "a 2017 paper titled 'Attention Is All You Need.' Its key insight was the attention "
            "mechanism - a way for the model to weigh which parts of the input matter most for each "
            "word it's generating. Before transformers, AI read text word-by-word, losing track of "
            "long-range context. Transformers can see the whole input at once. Every major LLM - "
            "GPT, Claude, Gemini - is a transformer."
        ),
        "example": (
            "When the model reads 'The bank of the river was muddy', the transformer's attention "
            "mechanism lets 'bank' attend to 'river' strongly. This is how it knows you mean the "
            "river edge, not a financial institution. That same mechanism operating across thousands "
            "of words is what makes LLMs coherent."
        ),
        "why": (
            "You don't need to understand transformer internals to build with AI, but knowing the "
            "architecture name helps you read the literature and understand why models have context "
            "limits, why attention is computationally expensive, and why different model families "
            "differ."
        ),
        "related": ["llm", "foundation-model", "attention"],
    },
    "attention": {
        "term": "Attention",
        "topic": "AI",
        "def": "The mechanism that lets an AI focus on the right parts of its input.",
        "explain": (
            "When you read 'I walked to the bank', your brain instantly figures out which 'bank' is "
            "meant based on surrounding context. Attention is the math that lets a model do the same "
            "thing. For every word it processes, it computes which OTHER words in the input are most "
            "important to pay attention to. This is how transformers handle long, complicated inputs "
            "without losing the thread."
        ),
        "example": (
            "In 'The dog that chased the cat was brown', attention links 'brown' back to 'dog' "
            "(not 'cat'), because it has learned from training data that adjectives usually refer "
            "to the grammatical subject. Without attention, the model would struggle to know which "
            "noun to describe."
        ),
        "why": (
            "Attention is what makes LLMs feel smart. It's also why they're slow and expensive - "
            "comparing every word to every other word is computationally heavy. Most performance "
            "research on LLMs is really about making attention cheaper."
        ),
        "related": ["transformer", "llm", "context-window"],
    },
    "hallucination": {
        "term": "Hallucination",
        "topic": "AI",
        "def": "When an AI makes up facts and says them confidently. The most common failure mode of LLMs.",
        "explain": (
            "LLMs are trained to produce plausible-sounding text, not true text. Usually those "
            "overlap. Sometimes they don't. When the model generates a fact, citation, name, or "
            "statistic that sounds right but isn't real, that's a hallucination. The model isn't "
            "lying on purpose - it's doing what it was trained to do (predict the next likely word), "
            "and the most likely next word happens to be wrong. The dangerous part is that "
            "hallucinations read with the same tone of confidence as correct answers."
        ),
        "example": (
            "Ask a model for a legal citation and it might produce 'Smith v. Jones, 2019, 447 F.3d "
            "221' - which is formatted correctly, spelled like real case law, and completely "
            "invented. Lawyers have been fined for filing briefs with hallucinated citations."
        ),
        "why": (
            "Hallucinations don't go away; you manage them. Use RAG so the model can cite real "
            "sources. Ask it to show its work. Build checks that verify claims against a trusted "
            "database. For anything consequential (legal, medical, financial), never trust the "
            "first output."
        ),
        "related": ["grounding", "rag", "llm"],
    },
    "grounding": {
        "term": "Grounding",
        "topic": "AI",
        "def": "Tying an AI's answers to real, verifiable sources so it can't just make things up.",
        "explain": (
            "Grounding is the opposite of hallucination. Instead of letting the model answer from "
            "its training memory (which might be stale or wrong), you force it to answer ONLY using "
            "sources you provide - documents, database rows, search results. The model is instructed "
            "to cite or refuse. A well-grounded system is much harder to catch in a lie because every "
            "claim traces back to a source."
        ),
        "example": (
            "A grounded customer support bot is told: 'Answer only using the help articles I'm pasting "
            "below. If the answer isn't in them, say \"I don't have that info\" and offer to hand off "
            "to a human.' Now if a user asks something off-topic, the bot honestly says it doesn't "
            "know - instead of making something up."
        ),
        "why": (
            "Grounding is what turns an AI from a plausibly-wrong chatbot into a reliable production "
            "system. Every serious enterprise AI app is grounded. If you're shipping AI to end users, "
            "figure out grounding before you ship."
        ),
        "related": ["rag", "hallucination", "semantic-search"],
    },
    "tool-use": {
        "term": "Tool Use",
        "topic": "AI",
        "def": "When an AI can call external functions to do things it can't do itself.",
        "explain": (
            "An LLM on its own can only output text. It can't actually send an email, query a "
            "database, or check a calendar. Tool use is the mechanism by which the model says "
            "'I want to use tool X with these arguments' - and your code runs the tool and gives "
            "the result back. The model then reads the result and decides what to do next. With "
            "tools, an LLM stops being a chat partner and becomes something much more capable."
        ),
        "example": (
            "You give Claude a 'search_database' tool. User asks 'what's our biggest account?'. "
            "Claude decides to call search_database(query=\"top accounts by revenue, limit 1\"), "
            "reads the result, and replies: 'Your biggest account is Acme, with $1.2M in ARR.' "
            "Without tools, it would just guess or say it couldn't answer."
        ),
        "why": (
            "Tools are how LLMs become agents. Every autonomous system is really an LLM plus a good "
            "set of tools plus a loop that lets it call them repeatedly. The tools you give it are "
            "what define what your agent can do."
        ),
        "related": ["function-calling", "agent", "mcp", "react"],
    },
    "function-calling": {
        "term": "Function Calling",
        "topic": "AI",
        "def": "The technical mechanism behind tool use. How a model formally requests to run a specific function.",
        "explain": (
            "Function calling is the same idea as tool use, told from a programmer's perspective. "
            "You define a function (name, parameters, description) and register it with the model. "
            "When the model decides it needs that function, it outputs a structured JSON object "
            "naming the function and its arguments. Your code parses that JSON, runs the real "
            "function, and sends the return value back to the model as a new message."
        ),
        "example": (
            "You register a function: get_weather(city: str). The model, given 'what's it like in "
            "Tokyo?', outputs: {'function': 'get_weather', 'args': {'city': 'Tokyo'}}. Your code "
            "calls get_weather('Tokyo'), gets '72°F sunny', sends that back. The model then "
            "writes: 'It's 72°F and sunny in Tokyo.'"
        ),
        "why": (
            "Function calling is the precise, structured form of tool use. If you're building on an "
            "API like Claude's or OpenAI's, this is the term you'll actually see in the docs."
        ),
        "related": ["tool-use", "agent", "mcp"],
    },
    "react": {
        "term": "ReAct (Reason + Act)",
        "topic": "AI",
        "def": "A loop where an agent alternates between thinking out loud and taking an action, over and over until the task is done.",
        "explain": (
            "ReAct stands for 'Reasoning and Acting.' It's a pattern for building agents: the model "
            "writes a THOUGHT (what it wants to do next and why), then an ACTION (the tool call it "
            "picks), then gets back an OBSERVATION (the tool result), then thinks again. This cycle "
            "continues until the goal is met. The interleaving of reasoning with acting makes the "
            "agent much more reliable than having it decide all steps upfront."
        ),
        "example": (
            "Task: 'Find 3 competitors of Acme and summarize their pricing.'\n"
            "Thought: I should search for Acme's industry first.\n"
            "Action: web_search('Acme company industry')\n"
            "Observation: 'Acme sells project management software'\n"
            "Thought: Now I'll search for competitors.\n"
            "Action: web_search('project management software competitors')\n"
            "... and so on until 3 competitors are found and analyzed."
        ),
        "why": (
            "ReAct is the most common pattern under the hood of agentic systems. Claude's agent "
            "harness, LangChain's AgentExecutor, and most open-source agents implement some flavor "
            "of ReAct. Knowing the pattern helps you debug when your agent misbehaves - usually "
            "it's because the thought→action linkage broke somewhere."
        ),
        "related": ["agent", "tool-use", "function-calling"],
    },
}


PAGE_TEMPLATE_BLOCK = """<a href="index.html" style="color:#4a00e0; text-decoration: none; font-size: 14px;">← Glossary</a>
<span class="gloss-topic" style="margin-top: 24px;">{topic}</span>
<h1 class="gloss-term">{term}</h1>
<p class="gloss-def">{def_}</p>

<h3 class="gloss-section-head">Explained simply.</h3>
<p class="gloss-explain">{explain}</p>

<h3 class="gloss-section-head">An example.</h3>
<div class="gloss-example">{example}</div>

<h3 class="gloss-section-head">Why it matters.</h3>
<p class="gloss-why">{why}</p>

<div class="gloss-related"><h4>Related terms</h4>{related_links}</div>
"""

# New CSS to add into each page's <style> block
EXTRA_CSS = """
.gloss-section-head { font-size: 13px; text-transform: uppercase; letter-spacing: 0.12em; color: #4a00e0; font-weight: 800; margin: 32px 0 8px 0; }
.gloss-explain, .gloss-why { font-size: 16px; line-height: 1.75; color: #2a2a30; margin: 0 0 8px 0; }
.gloss-example { font-size: 15px; line-height: 1.7; color: #3f3f46; background: #f7f5ff; border-left: 3px solid #4a00e0; padding: 14px 18px; border-radius: 6px; margin: 0 0 8px 0; white-space: pre-line; }
"""


def build_related_links(related):
    return "".join(f'<a href="{r}.html">{r.replace("-", " ").title()}</a>' for r in related)


for slug, data in TERMS.items():
    path = GLOSSARY / f"{slug}.html"
    if not path.exists():
        print(f"SKIP (missing): {slug}")
        continue

    text = path.read_text(encoding="utf-8")

    # Build replacement block
    new_block = PAGE_TEMPLATE_BLOCK.format(
        topic=data["topic"],
        term=data["term"],
        def_=data["def"],
        explain=data["explain"],
        example=data["example"],
        why=data["why"],
        related_links=build_related_links(data["related"]),
    )

    # Replace the content between the old ← Glossary link and the closing </div>
    # that precedes the <footer>
    pattern = re.compile(
        r'<a href="index\.html"[^>]*>← Glossary</a>.*?</div><footer',
        re.DOTALL,
    )
    replacement = new_block + '</div><footer'
    text, n = pattern.subn(replacement, text, count=1)
    if n == 0:
        print(f"WARN: could not find block in {slug}")
        continue

    # Inject extra CSS if not already present
    if ".gloss-section-head" not in text and "</style>" in text:
        text = text.replace("</style>", EXTRA_CSS + "\n</style>", 1)

    path.write_text(text, encoding="utf-8")
    print(f"OK: {slug}")

print(f"\nDone. Rewrote {len(TERMS)} AI glossary entries.")
