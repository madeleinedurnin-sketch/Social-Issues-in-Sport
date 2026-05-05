# Project 1 — Audience Influence on the Angel Reese vs Caitlin Clark Rivalry

> **Research question.** How does social media coverage of Angel Reese's and Caitlin Clark's public comments, particularly the frequency and framing of their references to one another, contribute to the perception of rivalry between the two athletes?

## About this project

The rapid growth of women's basketball has put Caitlin Clark and Angel Reese at the center of an evolving media narrative in which audiences are no longer passive consumers of rivalry, but active co-creators of it. This case asks whether the rivalry frame so often imposed by sports media is reproduced — or amplified — in the comment sections fans inhabit. We compare cross-athlete reference rates and framing on Instagram and YouTube before and after the rivalry became a dominant media story.

## Data

We work with the ARCC (Angel Reese & Caitlin Clark) dataset spanning 2017–2024, drawn from Instagram and YouTube:

- `ARCC_INS_COMMENT.xlsx` — Instagram comments
- `ARCC_INS_POST.xlsx` — Instagram post metadata
- `ARCC_YT_COMMENT.xlsx` — YouTube comments
- `ARCC_YT_VIDEO.xlsx` — YouTube video metadata (titles, views, comment counts)

The corpus is partitioned into a **pre-2023** phase (before the rivalry became a high-visibility media story) and a **2023–2024** phase (peak collegiate competition through the WNBA transition), enabling a longitudinal contrast. Preprocessing standardized text across platforms, removed spam and bot-like comments, and dropped empty entries.

## Methods

1. Build keyword dictionaries for four constructs — **personality** (e.g., *cocky, classy, humble, arrogant*), **post and mention frequency**, **skill comparison** (e.g., *goat, trash, stats, points*), and **beauty standards**.
2. Score each comment for keyword hits and tag cross-athlete mentions.
3. Group comments into framing categories — competitive, collaborative, media-manufactured, and neutral.
4. Compare pre-2023 vs 2023–2024 distributions with **chi-square tests of independence**.
5. Run **VADER sentiment** on cross-reference comments and compare across platforms.

## Key findings

- **Cross-reference rates differ sharply by platform.** YouTube comments mentioned Clark 21.6% of the time and Reese 13.49%, compared with 3.26% (Clark) and 4.71% (Reese) on Instagram — YouTube discourse is far more rivalry-centered.
- **Sentiment in cross-mentions is mildly positive everywhere.** Mean VADER scores on Instagram were 0.287 (Clark) and 0.322 (Reese); on YouTube, 0.142 (Clark) and 0.134 (Reese). Rivalry framing and audience appreciation coexist rather than cancel each other out.
- **Personality-based vocabulary outpaces basketball vocabulary.** Discussion frequently judged the athletes through personality and image (*cocky*, *classy*, *arrogant*) rather than on-court performance, indicating that female-athlete coverage still routes through cultural symbolism.
- **YouTube clickbait amplifies controversy.** Videos with conflict-framed titles produced higher engagement and a denser mix of cross-athlete mentions, evidence that platform incentives rather than the athletes themselves drive much of the rivalry narrative.

## Files in this folder

| File | Purpose |
|---|---|
| [`CursorPros_REPORT_P1.md`](CursorPros_REPORT_P1.md) | Full project report (introduction, related literature, data, methods, results, discussion, ethics, references). |
| [`CursorPros_PLAN_P1.md`](CursorPros_PLAN_P1.md) | Pre-registered plan: research question, data, constructs, AI use disclosures. |
| [`CursorPros_Presentation_P1.pdf`](CursorPros_Presentation_P1.pdf) | Slide deck used in the in-class presentation; headline visualizations live here. |
| [`Python Script/`](Python%20Script) | Analysis script (`project1_script.py`). |
| [`AI Verfication/`](AI%20Verfication) | AI-assisted analysis log (`project1_analysis.md`). |
| [`Visualizations/`](Visualizations) | Reserved for figure exports; primary visuals for P1 are in the slide deck. |

## Reproduction

The Python script in `Python Script/` is the entry point. Run with the four `ARCC_*.xlsx` files placed in the working directory and a Python environment that includes `pandas`, `numpy`, `matplotlib`, and `vaderSentiment`. See the script header for any local-path arguments.
