# Format decision matrix

Use this reference only when the best presentation is uncertain.

| Input shape | Primary format | Add only when useful | Avoid |
| --- | --- | --- | --- |
| One question, one fact | One sentence | One qualifier | Headings and bullets |
| List of independent reasons | Bullets | One lead sentence | Unnecessary diagram |
| Instructions in strict order | Numbered steps | Short chain overview | Mindmap |
| A simple linear progression | Arrow chain | Brief explanatory line | 12-node chart |
| Several alternatives with same dimensions | Table | Recommendation | Long prose per cell |
| Non-linear connected concepts | Mindmap / hub-and-spoke | One conclusion | False chronology |
| Decision with multiple outcomes | Flowchart | Branch-specific explanation | Linear chain |
| Deep explanation or analysis | Answer-first sections | Small visual with clear purpose | Decorative visual noise |
| Long discussion recap | Current status + grounded arrow chain | Decisions / open items / next step | Invented chronology |
| Essay, dialogue, email, social post | Native prose format | Minimal framing | Injecting bullets into artifact |
| JSON, source code, SQL, CSV | Exact requested machine format | Explanation only if permitted | Markdown outside schema |

## Visualization gate

Ask all three:
1. Is there a relationship that prose hides (branch, comparison, network, process)?
2. Will a visual communicate it more accurately and faster than 2–4 lines of text?
3. Can the target client actually render it or provide a readable fallback?

If not, do not add a visual.

## Density budget

- **Micro** (a fact or quick answer): 1–3 sentences, no heading.
- **Short** (a few findings): lead answer + up to 5 bullets, no forced close.
- **Medium** (multi-part task): up to 3 short sections, at most 1 primary visual.
- **Long** (complex analysis): hierarchy by topic, only the tables/diagrams doing real work.

These are defaults, not hard word limits: user requests and factual complexity win.

## Selection tie-breaks

- If information has a true order and no branches → arrows/numbering, not a mindmap.
- If branches are mutually exclusive outcomes → flowchart, not a mindmap.
- If branches are just related subtopics → mindmap, not a flowchart.
- If there are comparable metrics across options → table, not separate paragraphs.
- If the user asks for "kurz", "schnell", "short", or "only the answer" → minimize visual overhead.
- If a requested chart makes a misleading claim → explain the limitation and choose accurate prose.

## Anti-patterns

- Five headings with one sentence each.
- A "Key takeaways" box repeating the first paragraph.
- Converting every comma-separated idea into a bullet.
- Producing a Mermaid diagram for a trivial answer.
- Mixing 3 different visual languages for the same information.
- Arrows implying causation when only correlation is known.
- Omitting tradeoffs, uncertainty, sources, or requirements in the name of brevity.
- Making up ChatGPT widgets, interactivity, previews, or file links.

## Language

Keep the answer in the user's requested language. Labels inside diagrams and tables should follow that language too. Keep product names and exact quoted material unchanged.
