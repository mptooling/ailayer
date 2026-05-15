# LlamaIndex

> **Category:** AI Agents & Automation | **Pricing:** Free OSS + managed services | **Type:** Open-source data and agent framework

LlamaIndex is a framework for building knowledge-grounded LLM applications, especially RAG systems, document agents, and data connectors.

## When To Use

- Use LlamaIndex when your app needs retrieval over documents, databases, APIs, or enterprise knowledge sources.
- Reach for it when ingestion, chunking, indexing, retrieval, reranking, and query orchestration matter more than generic chat.
- Consider it for agent workflows where tools need strong data context.

## Practical Tips

- Start with the simplest retriever that gives measurable answer quality before adding routers or agents.
- Evaluate chunking, metadata filters, rerankers, and citation behavior with real user questions.
- Keep ingestion pipelines reproducible; RAG bugs often live in parsing and metadata, not the model call.
- Use observability/evals early so retrieval quality can be improved deliberately.

## Watch Outs

- RAG frameworks do not fix poor source data, stale documents, or missing permissions.
- Avoid hiding retrieval failures behind confident model answers.
- Watch token cost when stuffing too many retrieved chunks into context.

## Links

- [LlamaIndex docs](https://docs.llamaindex.ai/)
- [LlamaIndex GitHub](https://github.com/run-llama/llama_index)
