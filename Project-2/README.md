# Project 2 — The Legitimacy of the TGL League

> **Research question.** How do YouTube content creators frame TGL's commercialization of professional golf, and in what ways does audience discourse in the comments reflect public acceptance, resistance, or ambivalence toward a technology-driven, entertainment-first sport model?

## About this project

Tomorrow's Golf League (TGL) is an indoor, simulator-driven, broadcast-optimized format that breaks from the conventions of outdoor tournament golf. That makes it a useful natural experiment in legitimacy: when a sport product is openly engineered for spectacle and short-form engagement, do audiences treat it as a credible evolution of golf or as a departure from "real" golf? This case examines how YouTube creators frame the league and how audiences respond, drawing on commercialization-and-authenticity scholarship (Winell et al., 2023, 2025), fan-culture theory (Cottingham, 2012), and platformed-discourse research (Levental, 2023; Sturm, 2020).

## Data

| Dataset | Unit of analysis | n |
|---|---|---|
| `TGL_VIDEO.xlsx` | Video (title, description, summary, transcript-style text) | 355 |
| `TGL_COMMENT.xlsx` | Comment | 6,102 |
| Model-specific subset | Comments explicitly discussing the TGL format | 695 |

The model-specific subset isolates legitimacy discourse from incidental conversation so the acceptance / resistance / ambivalence breakdown reflects engaged commentary.

## Methods

1. **Construct definition.** Three a-priori constructs — *legitimacy*, *technology*, and *commercialization* — operationalized through curated keyword families: `LEGIT_POS` (acceptance / legitimizing cues), `LEGIT_NEG` (resistance / delegitimizing cues), and `LEGIT_AMB` (ambivalence / mixed / uncertain cues). A sample of the dictionary is in [`AI Verification/TGL_keyword_dictionary_with_code_labels_SAMPLE.csv`](AI%20Verification/TGL_keyword_dictionary_with_code_labels_SAMPLE.csv).
2. **Creator-side coding.** Each video is coded for commercialization framing, technology framing, and the overlap of the two.
3. **Audience-side coding.** Each comment in the model-specific subset is classified as `acceptance`, `resistance`, `ambivalence`, or `neutral/other`. Coding is rule-guided and tied to legitimacy language rather than tone.
4. **Visibility context.** Coded patterns are compared against engagement (likes) and video-type metadata to flag whether certain framings appear more prominent in higher-attention spaces.
5. **AI verification.** Field-level checks, iterative dictionary refinement, repeated spot-checks of coded excerpts, cross-pass count comparisons, and percentage-total consistency checks. Full audit trail in [`AI Verification/`](AI%20Verification).

## Key findings

- **Creators speak with one voice.** Of 355 videos, **88.2%** (313) use commercialization language, **78.3%** (278) use technology language, and **68.5%** (243) combine both — TGL is consistently presented as an innovation-and-business package rather than a single-axis story.
- **Audiences do not.** Among 695 model-specific comments, **resistance (24.9%, n = 173)** slightly exceeds **acceptance (22.4%, n = 156)**, with **ambivalence at 9.1% (n = 63)** and a large **neutral/other** segment of **43.6% (n = 303)**.
- **Legitimacy is contested, not consensual.** Promotional coherence on the creator side does not produce consensus on the audience side. Resistance language is anchored in tradition ("not real golf"), acceptance in pragmatism ("future of golf"), and ambivalence captures conditional or transitional judgment.
- **Mediated legitimacy work.** YouTube comment threads function as a public sphere where legitimacy claims are tested, not just opinion polls — consistent with Levental (2023) and Sturm (2020).

## Figures

The Visualizations folder contains a GitHub-renderable Mermaid figure file and a TypeScript/React canvas component used in presentation:

- [`TGL_Key_Findings_Figures.md`](Visualizations/TGL_Key_Findings_Figures.md) — creator framing counts, audience sentiment distribution, and acceptance-vs-resistance gap rendered as Mermaid charts.
- [`tgl-key-findings-figures-presentation.canvas.tsx`](Visualizations/tgl-key-findings-figures-presentation.canvas.tsx) — interactive presentation component.

Additional headline visuals are embedded in [`CursorPros_Presentation_P2.pdf`](CursorPros_Presentation_P2.pdf).

## Files in this folder

| File | Purpose |
|---|---|
| [`CursorPros_REPORT_P2.md`](CursorPros_REPORT_P2.md) | Full project report. |
| [`CursorPros_PLAN_P2.md`](CursorPros_PLAN_P2.md) | Pre-registered plan with construct definitions and AI use disclosures. |
| [`CursorPros_Presentation_P2.pdf`](CursorPros_Presentation_P2.pdf) | Slide deck. |
| [`Python Script/`](Python%20Script) | Workflow logs: keyword-search code strings, visualization code, and the report-workflow code log. |
| [`AI Verification/`](AI%20Verification) | Outline construction verification, keyword-search iteration log, and dictionary sample. |
| [`Visualizations/`](Visualizations) | Mermaid figure file plus the presentation canvas component. |

## Reproduction

`Python Script/TGL_Report_Workflow_Code_Log.md` documents the end-to-end workflow including keyword construction (`TGL_keyword_search_codestrings.md`) and figure generation (`TGL_Visualization_Code.md`). The two `TGL_*.xlsx` files (not redistributed in this repo) are the inputs.
