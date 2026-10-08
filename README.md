# LMKN Clarity

**Adaptive response design for AI assistants.**

LMKN Clarity helps an AI answer with clear hierarchy, concise bullets, useful tables, quick arrow-chain summaries and, where appropriate, mindmaps or decision flowcharts. It intentionally avoids generic "AI formatting" and unnecessary filler.

**Core idea:** Answer first → choose the right structure → show only visuals that clarify real relationships.

## What it does

| Input | Output |
| --- | --- |
| Quick factual question | Direct 1–2 sentence answer |
| Multi-point explanation | Compact bullet hierarchy |
| Sequence / workflow | `A → B → C` chain or numbered steps |
| Complex connected concepts | Mermaid mindmap or legible text-tree fallback |
| Decision with yes/no conditions | Branching flowchart |
| Multiple options and criteria | Small Markdown comparison table |
| Long project/chat recap | Current status + decision chain + open actions |
| Strict essay, email, JSON or code | Keeps the requested format intact |

Visuals are **conditional**, not automatic decoration. The skill does not provide a renderer itself: rich inline diagrams appear only if the chat client supports them. Otherwise the answer falls back to Markdown or readable text.

## Files

~~~text
lmkn-clarity/
├── SKILL.md                  # Agent instructions + selection logic
├── README.md                 # Overview and installation
├── references/
│   ├── routing.md            # Format decision matrix / anti-patterns
│   ├── visuals.md            # Mindmaps, chains, flowcharts, fallbacks
│   └── examples.md           # Before/after examples
├── evals/
│   ├── cases.json            # Test prompts and behavioral expectations
│   └── RUBRIC.md             # Manual model evaluation checklist
└── tests/
    └── test_skill.py         # Standard-library package validation
~~~

## Install with Codex

Clone the repository into the skill directory, using the **folder name `lmkn-clarity`** to match the skill's manifest.

macOS / Linux:

~~~bash
mkdir -p ~/.agents/skills
git clone https://github.com/lmkn-dev/lmkndev-clarity.git ~/.agents/skills/lmkn-clarity
~~~

Windows PowerShell:

~~~powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
git clone https://github.com/lmkn-dev/lmkndev-clarity.git "$env:USERPROFILE\.agents\skills\lmkn-clarity"
~~~

For a repository-local skill, clone into `.agents/skills/lmkn-clarity` under that project. Restart/reload the client if it only scans skills on startup. The linked GitHub repo is private, so Git credentials/access are required.

Explicit invocation where skill invocation is supported:

~~~text
$lmkn-clarity Fasse die Entscheidungen dieser Diskussion als Pfeilkette zusammen.
~~~

An installed skill is not necessarily invoked for every message; automatic activation depends on the host's skill discovery and routing. To make it apply to **every** answer, configure your host's persistent/custom instructions accordingly.

## Use in ChatGPT

A GitHub repository is **not automatically installed into every ChatGPT chat** by linking GitHub. Use the skill through a supported skill-enabled environment/plugin, or adapt the principles into custom instructions if your client lacks skill installation. Some ChatGPT interfaces have native rich visuals; others accept only Markdown. Do not promise inline rendering without checking the actual client.

## Quick manual demo

**Prompt:** "Fasse zusammen: Zuerst wollten wir eine App, dann entschieden wir uns für eine Website. Das Budget ist noch offen."

**Desired:**

~~~text
Stand: Website entschieden, Budget offen.
App-Idee → Website gewählt → Budget klären
~~~

The arrow chain records actual decisions; it does not pretend budget approval has happened.

## Validate locally

~~~bash
python -m unittest discover -s tests -v
~~~

This checks the skill package, key metadata, references, and evaluation-case shape. It **does not** prove the model will follow the style in every conversation. For behavior, use the prompts and manual scoring rubric in `evals/`.

## Relationship to Human-Writing

Use **Human-Writing** for natural voice, genre, and human-sounding prose. Use **LMKN Clarity** for the *architecture of explanations*. When drafting an essay or email, preserve the requested prose rather than forcing bullets or a diagram.

## Maintenance

- Keep the instructions in `SKILL.md` short enough for quick loading.
- Add new response patterns to `references/`.
- Add a matching case to `evals/cases.json` when fixing a recurring failure.
- Prefer fewer clearer rules over global "always do X" formatting mandates.

Repository: https://github.com/lmkn-dev/lmkndev-clarity
