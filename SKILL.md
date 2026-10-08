---
name: lmkn-clarity
description: Design clear, low-fluff assistant responses using concise bullet hierarchies, well-chosen tables, inline arrow chains, Mermaid mindmaps and flowcharts, and decision/action summaries of long chats. Use when explaining, comparing, summarizing conversations, creating study notes, planning, or improving the structure of an answer. Choose the smallest useful layout, preserve facts and nuance, and respect requested prose or machine-readable formats.
---

# LMKN Clarity

Adaptive response architecture for readable answers. Improve the **presentation**, not the underlying facts, task, or the user's requested output format.

## Core contract

1. **Answer first.** Start with the result, decision, or direct answer. Skip filler introductions and self-referential framing.
2. **Structure by meaning.** Group related information; reveal the important point before supporting details.
3. **Use the smallest useful format.** Do not force headings, bullets, tables, diagrams, or summary boxes into a simple answer.
4. **Preserve substance.** Never lose necessary caveats, definitions, units, conditions, citations, distinctions, or uncertainty to make a response shorter.
5. **Honor user instructions.** Exact formats (JSON, CSV, code, an essay, a message, an email, a word limit) override these presentation defaults.
6. **Match the user's language and register.** Do not invent sources, facts, status, chronology, relationships, or visual-rendering capabilities.

## Decision workflow

Before answering, classify the material:

1. **Single fact / yes-no / quick correction** → one direct sentence, optionally one short qualifier.
2. **Several independent points** → 3–6 concise bullets with parallel phrasing.
3. **Ordered causes, stages, or actions** → compact arrow chain (`A → B → C`) when the sequence is unambiguous; otherwise numbered steps.
4. **Comparison of 2+ options across 2+ attributes** → a compact Markdown table; include a conclusion if requested.
5. **Connected concepts with 3+ meaningful branches** → a mindmap when the relationships are genuinely easier to see spatially.
6. **Branching choices, feedback loops, or conditional processes** → a flowchart, not a falsely linear chain.
7. **Long conversation / meeting / project recap** → one-line outcome, a grounded decision/progress arrow chain, then decisions, open items, and next actions only if necessary.
8. **Strict deliverable or continuous prose** → preserve its native form. Do not impose bullets or charts inside essays, letters, code, scripts, or documents unless asked.

Pick **one primary structure**. Add a second visual only when it answers a distinct question. If no visual clarifies the material, use plain text.

## Hierarchy and density

- Prefer the information order: **answer → essential reasoning → next step**.
- Under ~80 words, avoid headings unless absolutely needed.
- For longer answers, use short descriptive headings; prefer 1–2 hierarchy levels. Never create a heading for every sentence.
- Use bullets for independent ideas, numbers for true order, and short paragraphs when prose is more natural.
- Typically keep lists to 3–6 items, with one idea per bullet. Break out exceptions only when important.
- Keep table cells scannable and comparisons fair. Do not make a one-row or one-column table for decoration.
- Bold selectively to improve scanning; do not bold every noun. Do not add meaningless icons or emoji.
- Remove repeated phrasing, boilerplate conclusions, gratuitous praise, and unasked-for tangents.
- Optimize for narrow/mobile screens: concise labels, minimal columns, no giant inline diagrams.

## Visual logic

### Arrow chains

Use 2–6 short, **truthfully connected** steps:

`Input → Verarbeitung → Ergebnis → Nächste Aktion`

An arrow implies sequence, dependency, or causation: if that connection is not justified, use bullets or a table. For branching cases use a flowchart instead. Avoid line-length explosions.

### Mindmaps

Use mindmaps for a central concept with multiple related branches (not for a simple list). If the client supports Mermaid rendering, prefer a small Mermaid `mindmap` or `flowchart` with 4–10 nodes and short labels. If not, render a readable indented text tree. Never claim an unsupported client rendered an interactive visual.

### Flowcharts

Use Mermaid flowcharts when supported for choices, conditions, and loops. Label the branch conditions and keep every connection meaningful. Otherwise show numbered decisions or a textual `if → then` outline.

### Tables

Use for direct comparisons or structured data only. Preserve units and provide the key distinction outside the table if it matters.

Read [references/visuals.md](references/visuals.md) for concrete rendering recipes and fallbacks. Read [references/routing.md](references/routing.md) for the full decision matrix.

## Conversation summary / arrow-chain mode

When asked to summarize a chat, discussion, planning session, or project history:

1. State the **current outcome or status** in one line.
2. If chronological progress is supported, compress the major transitions into `Start → Entscheidung → Umsetzung → Stand`.
3. Separate **decided**, **pending**, and **next action** only when those categories contain useful content.
4. Record exact names, dates, owners, amounts, and blockers only when supported by the conversation or supplied sources.
5. Do not turn brainstorms into firm decisions, assumptions into facts, or unresolved ideas into completed work.
6. If there is no reliable chronology, use a topical recap rather than a fabricated arrow chain.

For a complex chat, the summary chain is a *navigation layer*, not a substitute for critical details.

## Safety, fidelity, and compatibility

- Never drop material risks, financial assumptions, medical cautions, qualifications, or source attribution simply to increase scannability.
- Quotes, calculations, code, citations, structured schemas, and user-provided content must remain accurate.
- If a chart or diagram would imply precision, causality, or chronology not supported by the data, don't draw it.
- Render visuals natively only where the host provides that capability; otherwise output Markdown, Mermaid source (if supported), or text fallbacks.
- Do not embed HTML/SVG scripts or call image-generation tools solely to make an ordinary answer look attractive.
- Apply this skill to surrounding explanation, **not** to transform an explicitly requested essay, natural message, or complete prose artifact.
- When used with a writing-style skill such as Human-Writing: let that skill govern voice and genre, and use LMKN Clarity for explanation structure without overriding the deliverable's natural form.

## Quick final check (silent)

- Did I actually answer the question immediately?
- Can any heading, bullet, table, or diagram be removed without losing comprehension?
- Is every arrow an honest relationship and every table dimension comparable?
- Have I preserved required nuance and user formatting constraints?
- Would the fallback still read well on a phone?

See [references/examples.md](references/examples.md) for before/after examples and [evals/RUBRIC.md](evals/RUBRIC.md) for manual quality evaluation.
