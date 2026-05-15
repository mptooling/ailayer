# Chroma

> **Category:** Runtime & Retrieval Infrastructure | **Pricing:** Free OSS + hosted cloud | **Type:** Vector database and embedding store

Chroma is an open-source vector database commonly used for local-first RAG prototypes, embedding storage, and AI application development.

## When To Use

- Use Chroma for fast local RAG prototypes and smaller knowledge-base applications.
- Reach for it when developer ergonomics matter more than distributed database operations.
- Consider it for experiments before choosing heavier vector infrastructure.

## Practical Tips

- Keep document IDs stable so re-ingestion is predictable.
- Store source metadata for citations and debugging.
- Use representative eval questions before scaling ingestion.
- Revisit the storage choice when concurrency, permissions, or dataset size grow.

## Watch Outs

- Prototype-friendly defaults may not match production security or scale needs.
- Poor chunking creates poor retrieval regardless of vector DB.
- Track embedding model versions for every collection.

## Links

- [Chroma docs](https://docs.trychroma.com/)
- [Chroma GitHub](https://github.com/chroma-core/chroma)
