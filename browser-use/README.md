# Browser Use

> **Category:** AI Agents & Automation (browser automation) | **Pricing:** Free (open source) / paid cloud | **Type:** Open Source (MIT)

---

## Repository

- [GitHub — browser-use/browser-use](https://github.com/browser-use/browser-use) ⭐ 96,000+
- Homepage: [browser-use.com](https://browser-use.com)
- Language: Python

---

## Documentation

- [Quick start](https://docs.browser-use.com/quickstart)
- [Customizing the agent & actions](https://docs.browser-use.com/customize/agent-settings)
- [Cloud API](https://docs.browser-use.com/cloud/quickstart)
- [Web UI project](https://github.com/browser-use/web-ui)

---

## Summary

Browser Use lets an LLM drive a real browser to complete tasks on the open web — navigating pages, clicking, filling forms, extracting data, and chaining steps toward a goal stated in natural language. It extracts the page's interactive elements into a structured representation the model can reason over, so the agent acts on actual DOM elements rather than brittle pixel coordinates. Built on Playwright and model-agnostic, it works with Claude, GPT, Gemini, and local models. A hosted cloud API and a separate web UI exist for teams that don't want to manage browser infrastructure. It's the most popular open-source browser-automation agent and the open counterpart to closed tools like Bardeen.

**Best for:** Developers automating web tasks that have no API — research, form-filling, data extraction, QA flows, and repetitive online workflows — using an agent that operates a real browser.

---

## Related Materials

- [Bardeen](../bardeen/README.md) — closed-source no-code browser automation; Browser Use is the open, code-first alternative
- [Firecrawl](../firecrawl/README.md) — use for clean bulk scraping/crawling; Browser Use for interactive, stateful task flows
- [LangChain](../langchain/README.md) — orchestrate Browser Use as a tool within a larger agent
- [OpenHands](../openhands/README.md) — coding agent that also includes browsing among its capabilities

---

## When To Use

- A workflow lives behind a UI with no usable API and requires logging in, clicking, or multi-step navigation.
- You need an agent to gather or enter data across pages and adapt when layouts change, instead of hard-coded selectors.
- You want to embed web automation as a tool inside a larger agent or product.

## Practical Tips

- Install with `pip install browser-use` and run Playwright's browser install; start with a short, explicit task and a strong frontier model.
- Constrain the agent: restrict allowed domains and actions, and give a clear stopping condition so it doesn't wander.
- For login-gated flows, reuse an authenticated browser profile/session rather than scripting credentials into the prompt.
- Reach for the cloud API when you need parallelism or managed browsers; self-host when data must stay local.

## Watch Outs

- The agent takes real actions in a real browser — sandbox it and never point it at destructive or financial actions without human confirmation.
- Many sites' terms prohibit automation; respect robots/ToS and rate limits, and avoid CAPTCHA-evasion or abusive scraping.
- Reliability depends on the model's reasoning; weaker models misclick or loop on complex pages — budget tokens and add step limits.
- Credentials and session cookies handled by the agent are sensitive; keep them out of prompts and logs.

---

*Last updated: 2026-05*
