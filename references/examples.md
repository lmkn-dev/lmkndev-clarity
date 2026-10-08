# Examples: input → desired output

These are illustrations, not rigid templates. Keep format choice tied to meaning.

## A. Tiny factual answer: no over-formatting

**User:** Was ist ein MVP?

**Good:**
Ein **MVP** ist die kleinste nutzbare Produktversion, mit der du eine zentrale Annahme bei echten Nutzern testest.

**Bad:** `## Definition`, `## Vorteile`, `## Fazit` for this one-sentence question.

## B. Process: arrow chain

**User:** Wie validiere ich eine Software-Idee kurz?

**Good:**
**Problemgespräche → Zahlungsbereitschaft prüfen → Kleinen Prototyp testen → Ergebnisse auswerten**

Erst danach entscheiden, ob sich der Ausbau lohnt.

**Bad:** A big mindmap containing an inherently sequential workflow.

## C. Comparison: table

**User:** Vergleiche Abo-SaaS und Einmalverkauf für ein kleines Tool.

**Good:**

| | Abo-SaaS | Einmalverkauf |
| --- | --- | --- |
| Umsatz | Wiederkehrend | Pro Kauf |
| Aufwand | Laufender Support | Weniger Abo-Verwaltung |
| Risiko | Kündigungen | Schwankende Verkäufe |

Entscheidend sind laufender Kundennutzen und Supportkosten.

## D. Network of concepts: mindmap

**User:** Zeig mir die Bausteine einer Geschäftsidee als Mindmap.

**Good when Mermaid is supported:**

~~~mermaid
mindmap
  root((Geschäftsidee))
    Kundenproblem
    Lösung
    Einnahmen
    Vertrieb
~~~

**Good when Mermaid is unsupported:**

~~~text
Geschäftsidee
├─ Kundenproblem
├─ Lösung
├─ Einnahmen
└─ Vertrieb
~~~

## E. Real decision branches: flowchart

**User:** Wie entscheide ich, ob ein MVP launchbereit ist?

**Good when Mermaid is supported:**

~~~mermaid
flowchart TD
    A{Kernfunktion verlässlich?} -->|Nein| B[Fehler beheben]
    A -->|Ja| C{Nutzertest bestanden?}
    C -->|Ja| D[Begrenzten Launch planen]
    C -->|Nein| E[Überarbeiten]
~~~

## F. Conversation recap: chain + status

**User:** Fasse diese Projektdiskussion zusammen: Wir wollten erst eine App. Dann haben wir uns für eine responsive Website entschieden. Die Funktionen sind definiert; die Preise müssen wir noch testen.

**Good:**
**Stand:** Website-Konzept festgelegt, Preisvalidierung offen.

App-Idee → Responsive Website gewählt → Funktionen definiert → **Preise noch testen**

## G. Nuance beats excessive compression

**User:** Kann ich mit einem Testzertifikat behaupten, jemand sei staatlich anerkannt?

**Good:**
**Nein, nicht allein durch dein eigenes Testzertifikat.** Ein privat ausgestelltes Zertifikat bestätigt nur deinen Test; staatliche Anerkennung erfordert eine entsprechende rechtliche Grundlage.

**Bad:** `Test → Zertifikat → staatlich anerkannt` (unsupported and misleading).

## H. Preserve a requested essay or email

**User:** Schreib eine zusammenhängende englische Analyse von 180 Wörtern ohne Stichpunkte.

**Good:** Write the continuous 180-word English analysis. Do not inject a mindmap, bullets or a "3 takeaways" list into the artifact.

## I. Coding and structured output

**User:** Antworte ausschließlich als JSON mit `status` und `reasons`.

**Good:** Output only syntactically valid JSON with those keys. Do not add a Markdown summary or diagram.
