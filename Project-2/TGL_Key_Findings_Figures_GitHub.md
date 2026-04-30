# TGL Key Findings Figures (GitHub Display Version)

This file is designed to render directly on GitHub web using Mermaid charts.

## Figure 1: Creator Framing (Out of 355 Videos)

```mermaid
xychart-beta
  title "Creator Framing Counts"
  x-axis ["Commercialization","Technology","Combined"]
  y-axis "Video Count" 0 --> 355
  bar [313,278,243]
```

- Commercialization: **313 / 355 (88.2%)**
- Technology: **278 / 355 (78.3%)**
- Combined framing: **243 / 355 (68.5%)**

## Figure 2: Audience Model-Specific Sentiment (n = 695)

```mermaid
pie showData
  title Audience Sentiment Distribution
  "Resistance (24.9%, 173)" : 173
  "Acceptance (22.4%, 156)" : 156
  "Ambivalence (9.1%, 63)" : 63
  "Neutral/Other (43.6%, 303)" : 303
```

## Figure 3: Acceptance vs Resistance Gap

```mermaid
xychart-beta
  title "Acceptance vs Resistance"
  x-axis ["Resistance","Acceptance","Gap (pp)"]
  y-axis "Value" 0 --> 30
  bar [24.9,22.4,2.5]
```

### Data Source Notes

- Values reproduced from `TGL_Presentation_Slides.md`, `CursorPros_Presentation_P2.pdf`, and `TGL_Analysis_Report.md`.
- Percentages are reported values from your analysis pipeline.
- Creator framing categories intentionally overlap by design.
