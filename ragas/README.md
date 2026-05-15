# Ragas

> **Category:** Evals & Observability | **Pricing:** Free OSS + hosted offerings | **Type:** RAG and agent evaluation framework

Ragas is an evaluation framework focused on RAG pipelines, retrieval quality, groundedness, answer relevance, and agent workflows.

## When To Use

- Use Ragas when retrieval quality and grounded answers are central to the product.
- Reach for it when comparing chunking, embeddings, rerankers, and prompt strategies.
- Consider it when you need repeatable RAG evals before shipping knowledge-base changes.

## Practical Tips

- Evaluate retrieval and generation separately.
- Build test sets from real queries, failed answers, and support tickets.
- Track context precision/recall alongside answer correctness.
- Re-run evals after document ingestion, embedding, or model changes.

## Watch Outs

- Synthetic test generation is useful, but real user failures should anchor the suite.
- RAG metrics can hide permission bugs and stale-source issues.
- Good eval scores do not guarantee citations are usable for humans.

## Links

- [Ragas docs](https://docs.ragas.io/)
- [Ragas GitHub](https://github.com/explodinggradients/ragas)
