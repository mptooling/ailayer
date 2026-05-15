# vLLM

> **Category:** Runtime & Retrieval Infrastructure | **Pricing:** Free OSS | **Type:** High-throughput LLM inference engine

vLLM is an open-source inference engine for serving large language models with high throughput, efficient memory use, and OpenAI-compatible APIs.

## When To Use

- Use vLLM when serving open models at scale matters.
- Reach for it when throughput, batching, latency, and GPU utilization are key constraints.
- Consider it for internal model platforms and production inference services.

## Practical Tips

- Benchmark with your actual prompt lengths, concurrency, and output sizes.
- Expose an OpenAI-compatible endpoint to simplify client integration.
- Track GPU memory, queueing latency, and tokens per second.
- Separate experimentation from production serving configs.

## Watch Outs

- Serving models is operations-heavy: capacity, upgrades, drivers, and safety filters all matter.
- Higher throughput does not fix model quality or alignment.
- Watch license terms for the models you serve.

## Links

- [vLLM docs](https://docs.vllm.ai/)
- [vLLM GitHub](https://github.com/vllm-project/vllm)
