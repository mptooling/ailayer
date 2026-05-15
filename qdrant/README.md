# Qdrant

> **Category:** Runtime & Retrieval Infrastructure | **Pricing:** Free OSS + managed cloud | **Type:** Vector database

Qdrant is a vector database for similarity search, hybrid retrieval, filtering, and production RAG workloads.

## When To Use

- Use Qdrant when RAG or semantic search needs a dedicated vector database.
- Reach for it when filtering, payload metadata, hybrid search, and operational reliability matter.
- Consider it for production apps that outgrow embedded or in-process vector stores.

## Practical Tips

- Store metadata needed for permission checks, filtering, citations, and debugging.
- Evaluate embeddings and chunking before blaming the database.
- Use hybrid retrieval when keyword precision matters alongside semantic recall.
- Monitor index size, latency, and recall after data changes.

## Watch Outs

- Vector search can leak unauthorized documents if filters are incomplete.
- Re-embedding data is a migration; plan versioning.
- Do not skip evals just because retrieval is fast.

## Links

- [Qdrant docs](https://qdrant.tech/documentation/)
- [Qdrant GitHub](https://github.com/qdrant/qdrant)
