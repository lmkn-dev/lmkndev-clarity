# LMKN Clarity evaluation rubric

Score each response manually on a 0–2 scale per dimension. The test script only validates the skill package and scenario data; it **does not** evaluate a language model or prove behavioral quality.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Directness | Misses the answer | Answer is delayed | Direct answer first |
| Structure | Distracting / unclear | Mostly scannable | Correct format with clean hierarchy |
| Visual accuracy | Misleading relation | Useful but clumsy | Adds clarity without false implications |
| Density | Fluff / repetition | Some excess | Minimal while complete |
| Fidelity | Omits or invents key facts | Minor loss | All constraints, nuance and evidence retained |

**Pass target:** 9/10 or more, with **Fidelity = 2** and no misleading diagram.

## Manual procedure

1. Load `SKILL.md` into a skills-compatible agent.
2. Ask each prompt from `evals/cases.json` once with the skill and once without it.
3. Inspect both answers with the rubric; verify `must_include` and `must_avoid` semantically.
4. Record source support separately for any factual output.
5. Iterate the main routing rule when a repeated failure pattern appears.

## Failure patterns worth tracking

- "Always diagram": shows a flowchart for a one-line factual answer.
- "Everything is a bullet": forces a requested essay into a list.
- "Visual hallucination": claims a rendered or interactive diagram where none is supported.
- "False chain": converts related topics into chronological or causal steps.
- "Compressed away a caveat": omits an important condition, risk, status or citation.
- "Summary drift": reports a brainstormed possibility as a firm decision.
