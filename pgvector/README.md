# pgvector

> **Category:** Runtime & Retrieval Infrastructure | **Pricing:** Free OSS | **Type:** PostgreSQL vector extension

pgvector adds vector storage and similarity search to PostgreSQL, making it a pragmatic option for RAG and semantic search inside existing Postgres systems.

## When To Use

- Use pgvector when your app already runs on Postgres and vector search is part of the same product data.
- Reach for it when transactional data, metadata filters, and embeddings should live together.
- Consider it before adding a separate vector database for modest RAG workloads.

## Practical Tips

- Model embeddings as product data with migrations, indexes, and versioning.
- Use metadata and tenant filters in the same query as vector search.
- Benchmark exact vs approximate indexes with realistic data sizes.
- Keep embedding generation idempotent and observable.

## Watch Outs

- Postgres is convenient, but very large vector workloads may need dedicated infrastructure.
- Missing tenant filters can expose private data.
- Re-embedding can be expensive and operationally disruptive.

## Links

- [pgvector GitHub](https://github.com/pgvector/pgvector)
- [PostgreSQL docs](https://www.postgresql.org/docs/)
