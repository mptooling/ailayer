# Ollama

> **Category:** Runtime & Retrieval Infrastructure | **Pricing:** Free OSS | **Type:** Local model runtime

Ollama is a local runtime for downloading, serving, and experimenting with open models on developer machines and private infrastructure.

## When To Use

- Use Ollama for local prototyping, privacy-sensitive experiments, and offline model workflows.
- Reach for it when developers need quick access to open models without cloud setup.
- Consider it for lightweight internal tools where latency and model quality are acceptable.

## Practical Tips

- Pick model size based on hardware, not benchmark charts alone.
- Use local models for summarization, classification, and code assistance where quality is sufficient.
- Keep prompts and outputs comparable when testing against hosted models.
- Document required model names in project setup instructions.

## Watch Outs

- Local models vary widely in quality and context limits.
- Developer laptops are not production inference infrastructure.
- Avoid assuming private local inference means the surrounding app has no data leakage risk.

## Links

- [Ollama](https://ollama.com/)
- [Ollama GitHub](https://github.com/ollama/ollama)
