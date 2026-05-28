# AI Tools & Skills Library

> A curated, living library of impactful AI tools, agent skills, and workflow tips, grouped by use case and audience.
>
> **Last updated:** May 2026

---

## How To Use This Library

Each top-level directory contains one `README.md` profile. Use the category tables below to find a tool, then open the profile for practical guidance: when to use it, how to apply it, and what to watch out for.

---

## AI Coding Assistants

*For IT/engineering teams. Tools that write, complete, review, and refactor code.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [GitHub Copilot](./github-copilot/README.md) | — (closed source) | $10-39/mo | Enterprise dev teams, GitHub-native workflows |
| [Cursor](./cursor/README.md) | — (closed source) | Free / $20/mo | Deep codebase understanding, model choice |
| [Continue](./continue/README.md) | 24,000+ | Free (OSS) | Data privacy, on-prem, model flexibility |
| [Aider](./aider/README.md) | 25,000+ | Free (OSS) | Terminal-native, git-integrated, batch refactors |
| [Windsurf](./windsurf/README.md) | — (closed source) | Free / $15/mo | Autonomous multi-step coding agents, enterprise self-hosting |
| [Caveman](./caveman/README.md) | 53,000+ | Free (OSS) | Cutting agent output by roughly 75%; terse multi-agent collaboration |
| [Claude-Mem](./claude-mem/README.md) | 71,000+ | Free (OSS, AGPL-3.0) | Persistent cross-session memory for coding agents |
| [Everything Claude Code](./everything-claude-code/README.md) | 185,000+ | Free (OSS, MIT) / Pro app $19/seat/mo | Cross-harness skills, hooks, rules, security checks, and workflow conventions |
| [Claude Code](./claude-code/README.md) | — (closed source) | Paid via Anthropic plans/API usage | Terminal-native autonomous coding with repo context |
| [Codex](./codex/README.md) | — (closed source) | Paid via OpenAI plans/API usage | OpenAI-native coding agent workflows |
| [Cline](./cline/README.md) | OSS | Free client / API costs vary | Open-source VS Code agent with MCP and tool approvals |
| [Roo Code](./roo-code/README.md) | OSS | Free client / API costs vary | Configurable open-source VS Code coding agent modes |
| [OpenCode](./opencode/README.md) | OSS | Free client / API costs vary | Open terminal coding agent with model flexibility |
| [Kiro](./kiro/README.md) | — (closed source) | Paid SaaS / preview availability varies | Spec-driven agentic development environment |
| [RTK](./rtk/README.md) | 54,000+ | Free (OSS, Apache-2.0) | CLI proxy that cuts 60–90% of tool-output tokens (git, tests, lint, AWS, k8s) for coding agents |
| [OpenHands](./openhands/README.md) | 75,000+ | Free (OSS, MIT) / paid cloud | Self-hosted autonomous SWE agent that executes whole tasks in a sandbox |

---

## Methodology Skills

*Workflow skills that change how an agent or human operator works, not what tool they integrate with.*

These workflow skills are compatible with the Superpowers style of agent collaboration: clarify intent, plan multi-step work, execute in small verified batches, and report only after verification.

| Skill | Stars | Pricing | Best for |
|---|---|---|---|
| [Brainstorming](./brainstorming/README.md) | — (this library) | Free (OSS, MIT) | Socratic intent clarification before creative work |
| [Verification-before-completion](./verification-before-completion/README.md) | — (this library) | Free (OSS, MIT) | Evidence-backed completion claims |
| [TDD](./tdd/README.md) | — (this library) | Free (OSS, MIT) | Strict red-green-refactor for features and bug fixes |
| [Systematic Debugging](./systematic-debugging/README.md) | — (this library) | Free (OSS, MIT) | Reproduce, isolate, root-cause, fix, and defend |
| [Writing Plans](./writing-plans/README.md) | — (this library) | Free (OSS, MIT) | Turning a confirmed brief into a phased implementation plan |
| [Executing Plans](./executing-plans/README.md) | — (this library) | Free (OSS, MIT) | Working through a written plan with checkpoints |
| [Dispatching Parallel Agents](./dispatching-parallel-agents/README.md) | — (this library) | Free (OSS, MIT) | Splitting independent work across parallel agents |
| [Using Git Worktrees](./using-git-worktrees/README.md) | — (this library) | Free (OSS, MIT) | Isolating feature work in separate worktrees |
| [Matt Pocock — Skills for Real Engineers](./mattpocock-skills/README.md) | 109,000+ | Free (OSS, MIT) | Install-ready external skill pack: grilling, TDD, diagnose, PRD/issues, handoff |

---

## AI Agents & Automation

*Cross-functional. Tools for building autonomous agents and workflow automation.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [LangChain](./langchain/README.md) | 126,000+ | Free (OSS) | Production AI apps, RAG pipelines, agent chains |
| [AutoGPT](./autogpt/README.md) | 167,000+ | Free (OSS) / Cloud | Autonomous goal-directed agents, no-code platform |
| [n8n](./n8n/README.md) | 150,000+ | Free / $24/mo | No-code AI workflow automation, 600+ integrations |
| [CrewAI](./crewai/README.md) | 44,300+ | Free (OSS) | Role-based multi-agent teams, marketing/sales workflows |
| [LangGraph](./langgraph/README.md) | 24,800+ | Free (OSS) | Production multi-agent systems, stateful orchestration |
| [LlamaIndex](./llamaindex/README.md) | OSS | Free OSS + managed services | Data-grounded RAG and document-agent applications |
| [Pydantic AI](./pydantic-ai/README.md) | OSS | Free OSS | Typed Python agents and structured outputs |
| [OpenAI Agents SDK](./openai-agents-sdk/README.md) | OSS | Free SDK / API usage billed separately | OpenAI-native agents, tools, handoffs, tracing, and guardrails |
| [Anthropic Agent SDK](./anthropic-agent-sdk/README.md) | — | Free SDK / API usage billed separately | Claude-centered agent SDK patterns |
| [AutoGen](./autogen/README.md) | OSS | Free OSS | Microsoft multi-agent orchestration and research workflows |
| [Semantic Kernel](./semantic-kernel/README.md) | OSS | Free OSS | Microsoft AI orchestration for .NET, Python, and Java |
| [Mastra](./mastra/README.md) | OSS | Free OSS + cloud services | TypeScript agents, workflows, RAG, and evals |
| [Vercel AI SDK](./vercel-ai-sdk/README.md) | OSS | Free OSS / provider usage billed separately | Streaming AI features and tool calling for TypeScript web apps |
| [DSPy](./dspy/README.md) | OSS | Free OSS | Evaluation-driven LLM program optimization |
| [Dify](./dify/README.md) | 143,000+ | Free (OSS, modified Apache-2.0) / paid cloud | Low-code platform for building, shipping, and operating LLM apps and agentic workflows |
| [Browser Use](./browser-use/README.md) | 96,000+ | Free (OSS, MIT) / paid cloud | LLM-driven browser automation for web tasks with no API |

---

## Evals & Observability

*For engineering teams shipping AI systems. Tools for tracing, regression testing, model comparison, and production quality control.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [Braintrust](./braintrust/README.md) | — | Free tier + paid SaaS | CI/CD evals, production traces, and model/prompt comparisons |
| [Arize Phoenix](./phoenix/README.md) | OSS | Free OSS + Arize platform | Open-source AI observability, tracing, and evals |
| [Langfuse](./langfuse/README.md) | OSS | Free OSS + paid cloud | Self-hostable LLM tracing, prompt management, and scores |
| [W&B Weave](./weave/README.md) | OSS | Free tier + paid W&B plans | W&B-native LLM tracing and experiment lineage |
| [DeepEval](./deepeval/README.md) | OSS | Free OSS + Confident AI platform | pytest-style LLM, RAG, and agent evaluation |
| [Ragas](./ragas/README.md) | OSS | Free OSS + hosted offerings | RAG quality metrics and retrieval evaluation |
| [promptfoo](./promptfoo/README.md) | OSS | Free OSS + paid cloud | Prompt, model, and red-team regression tests |

---

## MCP & Tooling

*For agent platform builders. Tools for connecting agents to APIs, data, files, browsers, and developer systems.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [Model Context Protocol](./mcp/README.md) | Open standard | Free | Standardizing agent access to tools, resources, and prompts |
| [FastMCP](./fastmcp/README.md) | OSS | Free OSS | Building production-friendly Python MCP servers |
| [MCP Servers](./modelcontextprotocol-servers/README.md) | OSS | Free OSS | Reusing common MCP server integrations |
| [Firecrawl](./firecrawl/README.md) | 125,000+ | Free (OSS, AGPL-3.0) / paid cloud | Scrape, crawl, and search the web into clean LLM-ready data for agents and RAG |

---

## Runtime & Retrieval Infrastructure

*For AI platform teams. Libraries and infrastructure for model routing, local inference, serving, fine-tuning, embeddings, and vector search.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [LiteLLM](./litellm/README.md) | OSS | Free OSS + enterprise offerings | Model routing, budgets, fallbacks, and provider abstraction |
| [Ollama](./ollama/README.md) | OSS | Free OSS | Local open-model development and private prototypes |
| [vLLM](./vllm/README.md) | OSS | Free OSS | High-throughput open-model inference serving |
| [Qdrant](./qdrant/README.md) | OSS | Free OSS + managed cloud | Production vector search and RAG retrieval |
| [Chroma](./chroma/README.md) | OSS | Free OSS + hosted cloud | Local-first vector storage and RAG prototypes |
| [pgvector](./pgvector/README.md) | OSS | Free OSS | PostgreSQL-native vector search |
| [Unsloth](./unsloth/README.md) | 65,000+ | Free (OSS, Apache-2.0) | Fast, low-VRAM fine-tuning of open models (LoRA/QLoRA) on a single GPU |

---

## AI Writing & Marketing

*For Marketing, Sales, and content teams. Tools for creating and scaling content.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [Jasper](./jasper/README.md) | — (closed source) | $39/mo+ | On-brand enterprise marketing content at scale |
| [Copy.ai](./copy-ai/README.md) | — (closed source) | Free / $36/mo | GTM automation, sales copy, personalised outreach |
| [Perplexity](./perplexity/README.md) | — (closed source) | Free / $20/mo | Research, competitive intel, cited content |
| [Notion AI](./notion-ai/README.md) | — (closed source) | $10/mo add-on | Teams already on Notion, meeting summaries, docs |
| [Writesonic](./writesonic/README.md) | — (closed source) | Free / $16/mo | SEO content, custom chatbots, high-volume writing |

---

## AI Data & Analytics

*For C-Level, analysts, Sales, and Marketing. Tools for insights without SQL or data science.*

| Tool | Stars | Pricing | Best for |
|---|---|---|---|
| [Julius AI](./julius-ai/README.md) | — (closed source) | Free / $20/mo | Conversational data analysis, scheduled reports |
| [Akkio](./akkio/README.md) | — (closed source) | $49/mo+ | Predictive analytics, lead scoring, churn prediction |
| [Obviously AI](./obviously-ai/README.md) | — (closed source) | $75/mo+ | Explainable ML predictions, no-code forecasting |
| [Bardeen](./bardeen/README.md) | — (closed source) | Free / $10/mo | Browser automation, web scraping, lead enrichment |
| [Polymer](./polymer/README.md) | — (closed source) | Free / $10/mo | Self-serve dashboards, shareable data visualisation |

---

## Audience Quick-Reference

| Role | Recommended tools |
|---|---|
| **IT / Engineering** | Claude Code, Codex, Cursor, GitHub Copilot, Cline, Aider, LangGraph, OpenAI Agents SDK |
| **AI Platform** | LiteLLM, vLLM, Ollama, Qdrant, pgvector, MCP, FastMCP, Phoenix |
| **AI Product Engineering** | Vercel AI SDK, Mastra, Pydantic AI, LlamaIndex, Braintrust, promptfoo, Ragas |
| **Marketing** | Jasper, Copy.ai, Writesonic, Notion AI, Perplexity, n8n, CrewAI |
| **Sales** | Copy.ai, Bardeen, Akkio, Julius AI, Perplexity, n8n |
| **C-Level** | Julius AI, Polymer, Perplexity, Akkio, AutoGPT, Notion AI |
| **All roles** | n8n, Perplexity, Notion AI |

---

## Maintenance Notes

- Keep each profile concise and practical.
- Prefer official docs and source repositories over second-hand summaries.
- Update pricing, star counts, and product positioning when they change.
- Add new entries only when they provide a distinct tool, skill, or workflow tip.

---

*Built with Purpose Green · AI Tools Library · May 2026*
