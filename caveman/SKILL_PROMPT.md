# Caveman skill

Code like a caveman. Solve the problem in front of you with the dumbest construct that works. No clever indirection, no speculative abstractions, no patterns you don't actively need.

## When to apply

- Default mode for any code change in this project unless the user explicitly asks for a refactor or a design pattern.
- Especially when adding a feature, fixing a bug, or writing one-off scripts.

## Rules

- Three is the number. Duplicate code two times before considering an abstraction; only extract on the third occurrence. Two near-duplicates are cheaper than one wrong abstraction.
- Inline first, extract later. Write the logic where it runs. Helper functions earn their place by being called from at least two real sites — not "just in case."
- No new layers. Do not add a class, a module, a wrapper, or an interface unless the problem already has two concrete shapes that need it.
- No flags, no hooks, no plugins for hypothetical futures. Add the option when the second user shows up, not before.
- Prefer concrete over generic. Hard-code the value, the path, the type. Generic code is a tax paid every time someone reads it.
- Short call stacks beat short functions. A 40-line function you can read top-to-bottom beats six 8-line functions scattered across a file.
- Comments only for *why* (a constraint, an invariant, a gotcha). Never for *what* — the code says what.

## Debugging caveman-style

- `print()` first, profiler/debugger second. Sprinkle prints, run, read, remove. Do not invest in tracing infrastructure for a one-off bug.
- Bisect by deletion. When a system misbehaves, delete code until it works, then add back. Faster than reasoning.
- Reproduce before fixing. If you cannot reproduce, you cannot fix — do not patch in the dark.

## When NOT to apply

- Public APIs, library interfaces, or anything with multiple consumers — these need stable shapes; caveman code is fine in implementations *behind* them.
- Security-critical paths (auth, crypto, query construction) — boring, well-trodden patterns beat hand-rolled logic.
- Code that touches money, PII, or irreversible side effects — be deliberate, not minimal.

## Avoid

- "Refactoring while you're in there." If the change you were asked for is done and tested, stop. Drive-by refactors create noise in diffs and bugs in unrelated code.
- Adding a strategy/factory/visitor pattern because "we might need to swap implementations later." You won't, and if you do, the *real* shape will tell you what to do.
- Wrapping standard library or framework functions in single-line helpers — it just adds a hop for the next reader.
- Moving working code into "utils" or "helpers" without a second caller. Premature dumping ground.
- Caveman code in modules other people import. Keep the discipline scoped to leaves of the call graph.
