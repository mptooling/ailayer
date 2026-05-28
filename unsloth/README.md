# Unsloth

> **Category:** Runtime & Retrieval Infrastructure (fine-tuning) | **Pricing:** Free (open source) | **Type:** Open Source (Apache-2.0)

---

## Repository

- [GitHub — unslothai/unsloth](https://github.com/unslothai/unsloth) ⭐ 65,000+
- Homepage: [unsloth.ai](https://unsloth.ai)
- Language: Python (PyTorch / Triton kernels)

---

## Documentation

- [Fine-tuning guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide)
- [Notebooks (Colab / Kaggle)](https://github.com/unslothai/notebooks)
- [Supported models](https://unsloth.ai/docs/get-started/all-our-models)
- [Saving & exporting (GGUF, vLLM, Ollama)](https://unsloth.ai/docs)

---

## Summary

Unsloth makes LLM fine-tuning dramatically faster and lighter on memory by rewriting the hot paths — attention, the training loop, LoRA/QLoRA math — as custom Triton kernels, with no loss in accuracy. It claims roughly 2x faster training and up to ~70–80% less VRAM than stock Hugging Face + PEFT, which means you can fine-tune modern open models (Llama, Qwen, Gemma, Mistral, DeepSeek, gpt-oss) on a single consumer or free Colab GPU. It supports LoRA/QLoRA and full fine-tuning plus reinforcement-style methods, and exports trained models to GGUF, vLLM, and Ollama for serving. Ready-to-run notebooks cover most popular models, making it the most accessible on-ramp to customizing open models on modest hardware.

**Best for:** Teams and individuals fine-tuning open-weight models on limited GPU budgets who want frontier-speed training and easy export to local-serving formats.

---

## Related Materials

- [Ollama](../ollama/README.md) — run your Unsloth-exported model locally
- [vLLM](../vllm/README.md) — high-throughput serving target for fine-tuned weights
- [LiteLLM](../litellm/README.md) — route to your fine-tuned model behind a unified API
- [DSPy](../dspy/README.md) — when prompt/program optimization may beat fine-tuning for your task

---

## When To Use

- You need to fine-tune an open model but only have a single or consumer GPU (or free Colab/Kaggle).
- Prompt engineering and RAG aren't enough — the task needs domain knowledge or a behavior baked into the weights.
- You want a fast LoRA/QLoRA workflow that exports cleanly to GGUF/Ollama/vLLM for self-hosted serving.

## Practical Tips

- Start from an official Unsloth notebook for your target model; they encode the right kernel and quantization settings.
- Prefer QLoRA on small GPUs (4-bit base + LoRA adapters) to fit larger models in limited VRAM.
- Curate a small, high-quality instruction dataset — data quality moves results far more than extra epochs.
- Export to GGUF for Ollama or merge adapters for vLLM once eval looks good, then serve locally.

## Watch Outs

- Decide if you even need fine-tuning: RAG or better prompting is often cheaper and more maintainable for knowledge tasks; fine-tune for behavior/format/style.
- Speedups depend on hardware and model; NVIDIA GPUs are best supported — verify support for your card and target model before planning a run.
- Fine-tuning can degrade general capability or introduce overfitting; always hold out an eval set and compare against the base model.
- Library moves fast alongside new model releases; pin versions and re-validate notebooks after upgrades.

---

*Last updated: 2026-05*
