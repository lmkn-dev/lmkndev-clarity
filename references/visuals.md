# Visual recipes and fallbacks

Choose the lightest representation that accurately communicates the relationship.

## 1. Inline arrow chain — short, linear process

~~~text
Idee → Prototyp → Test → Verbesserung → Veröffentlichung
~~~

Use only when each step actually leads to the next. Five short labels are easier to scan than five explanatory sentences. Do not conflate an open action with a completed one.

## 2. Chat recap chain — traceable decisions

~~~text
Problem erkannt → Zwei Optionen geprüft → Option A gewählt → MVP geplant
~~~

Follow with only unresolved items, e.g. `Offen: Budget und Launchdatum`. If the discussion did not establish Option A was chosen, replace that segment with `Entscheidung offen`.

## 3. Concept map — use Mermaid where supported

~~~mermaid
mindmap
  root((Produktidee))
    Zielgruppe
      Bedarf
      Zahlungsbereitschaft
    Produkt
      Kernnutzen
      MVP
    Vertrieb
      Kanal
      Kosten
~~~

Fallback when mindmap rendering is unavailable:

~~~text
Produktidee
├─ Zielgruppe
│  ├─ Bedarf
│  └─ Zahlungsbereitschaft
├─ Produkt
│  ├─ Kernnutzen
│  └─ MVP
└─ Vertrieb
   ├─ Kanal
   └─ Kosten
~~~

For clients that render Mermaid `flowchart` but not `mindmap`, use a hub-and-spoke diagram:

~~~mermaid
flowchart TD
    A[Produktidee] --> B[Zielgruppe]
    A --> C[Produkt]
    A --> D[Vertrieb]
    B --> E[Bedarf]
    C --> F[MVP]
    D --> G[Kanal]
~~~

Do not repeat the same map as an exhaustive adjacent list.

## 4. Decision / branch / feedback loop

~~~mermaid
flowchart TD
    A[Idee] --> B{Kundennachfrage bestätigt?}
    B -->|Ja| C[MVP testen]
    B -->|Nein| D[Problem neu prüfen]
    C --> E{Wiederholbare Nutzung?}
    E -->|Ja| F[Launch vorbereiten]
    E -->|Nein| D
~~~

Fallback:

~~~text
Nachfrage bestätigt?
├─ Ja → MVP testen → Nutzung prüfen
└─ Nein → Problem neu prüfen
~~~

A flowchart must reflect actual conditions. Do not draw a linear arrow if there are mutually exclusive paths.

## 5. Comparison table

| Option | Stärke | Grenze |
| --- | --- | --- |
| A | Geringe Startkosten | Weniger Kontrolle |
| B | Mehr Kontrolle | Höhere Fixkosten |

Use comparable dimensions and the same level of specificity across options. Never fabricate numeric ratings.

## 6. Final-state recap

~~~text
Status: MVP definiert.
Verlauf: Idee → Funktionen priorisiert → MVP-Scope beschlossen
Offen: Kostenprüfung; Verantwortlichkeiten
Nächster Schritt: MVP-Backlog erstellen
~~~

Avoid implying all listed actions happened if only proposals were discussed.

## Display capability checklist

- Native host visual/table components exist → use them only if available and actually appropriate.
- Mermaid renderer exists → output a single concise, valid diagram.
- Markdown tables only → use table or compact text outline.
- Plain text / terminal → ASCII tree or arrow chain.
- Strict JSON/code/essay requested → preserve the requested format, no decorating.

The skill itself is instructional: it does not install a renderer, create interactive widgets, or guarantee inline diagrams in every client.
