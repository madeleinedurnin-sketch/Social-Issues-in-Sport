# Comment Selection and Analysis Decisions

Date: 2026-04-09  
Project: B50 cross-platform audience analysis  
Primary reference: `P3 Reference.md`

## 1) Data Sources and Inclusion

Comments were analyzed from:
- `B50_INS_COMMENT.xlsx` (Instagram)
- `B50_X_COMMENT.xlsx` (X)
- `B50_YT_COMMENT.xlsx` (YouTube)

### Inclusion Rule
- Included all rows in each dataset.
- Harmonized text into one field:
  - Instagram `text` -> `comment_text`
  - X `contents` -> `comment_text`
  - YouTube `text` -> `comment_text`

### Exclusion Rule
- No platform-level rows were dropped during final analysis.
- Empty/blank strings were retained where present, but still coded by rule defaults.

## 2) Harmonization Decisions

Created shared analytic variables:
- `platform`: `Instagram`, `X`, `YouTube`
- `comment_text`
- `stance`: `pro-Trump`, `anti-Trump`, `neutral/non-political`
- `frame`: `sports/performance`, `politics/ideology`, `blended`
- `is_blended`: 1 if `frame=blended`, else 0
- `engagement_raw`
- `engagement_log = log1p(engagement_raw)`
- `engagement_norm`: within-platform z-score of `engagement_log`

### Engagement Construction
`engagement_raw` was computed as:
- Instagram/YouTube: `likes + comment_re`
- X: `likes + reply counts + retweets count + reference count + Comment views`

Rationale:
- Preserve available platform-native engagement signals.
- Normalize within platform before cross-platform comparison.

## 3) Comment Coding Decisions

Coding used dictionary + social-context rules, then user-guided calibration.

### Base Stance Logic
- `pro-Trump`: supportive Trump-aligned cues (e.g., MAGA, vote Trump, POTUS praise).
- `anti-Trump`: critical cues (e.g., felon/rapist/racist/dictator when directed to Trump).
- `neutral/non-political`: no clear directional cue.

### Base Frame Logic
- `sports/performance`: golf/performance vocabulary.
- `politics/ideology`: political office/party/election/ideology vocabulary.
- `blended`: both sports and political cues in same comment.

## 4) Ambiguity Resolution Decisions (User-Calibrated)

During analysis, ambiguous language categories were identified and resolved with explicit user decisions.

### Round 1 Decisions
- `47` / `45&47` defaults to `pro-Trump` political stance.
- Positive references to `president` or `American` without explicit Trump remain neutral by default.
- Mixed positive/negative political cues: negative cue wins.
- Comments like `MAGA ... domestic terrorists`: classify as `anti-Trump`.

### Round 2 Decisions
- `America/American` without explicit Trump: neutral default.
- `Make America Great Again`:
  - if golf/sports context present -> `pro-Trump` + `blended`
  - otherwise -> `pro-Trump` + `politics/ideology`
- `GOAT/king` without explicit politics -> default frame `blended`.
- Sarcasm markers (`lol`, `lmao`, `sure`, `as if`, `smh`, `/s`) trigger sarcasm handling logic.

## 5) Quantitative Analysis Decisions

### Tests Implemented
- Cross-platform stance distribution: chi-square, standardized residuals, Cramer's V.
- Cross-platform frame distribution: chi-square, Cramer's V.
- Stance-by-frame association: chi-square, Cramer's V.
- Engagement blended vs non-blended: Mann-Whitney U + Cliff's delta.
- Engagement across stances: Kruskal-Wallis + pairwise Mann-Whitney (Bonferroni-corrected).

### Why Non-parametric Tests
- Engagement variables are highly skewed and zero-inflated.
- Non-parametric tests better reflect rank-based differences under skew.

## 6) Qualitative Excerpt Selection Decisions

Representative excerpts were appended in `P3_Analysis_Results.md` (Appendix C).

### Selection Method
- Selected within each `stance x frame` cell.
- Prioritized higher-engagement rows.
- Trimmed text for readability.
- Removed duplicate comments.
- Added cross-platform diversity when possible.

### Confidence Cleanup
- For exemplar quality, selection favored comments with clearer lexical alignment to assigned stance (especially pro/anti).
- If a cell had no comments, explicitly marked as `No comments in this category`.

## 7) Audit and Reproducibility Decisions

### Calibration Audit
- Added transition tables comparing previous coding pass to final calibrated pass:
  - stance transition matrix
  - frame transition matrix
- Reported counts and percentages of changed labels.

### Reproducibility
All outputs can be regenerated with:
- `run_b50_analysis.py` (coding + stats + results markdown)
- `generate_b50_figures.py` (figures 1-6 in PNG/SVG/PDF)

## 8) Limitations Acknowledged in Analysis

- Dictionary methods can miss implied meaning and complex irony.
- Some interpretation requires conversation-thread context unavailable in row-level comments.
- Platform metrics differ in structure (especially X view counts), requiring careful interpretation despite normalization.

## 9) Output Files Linked to These Decisions

- `B50_coded_comments.csv`
- `P3_Analysis_Results.md`
- `Figure_Captions.md`
- `Figure1_StanceByPlatform.*` through `Figure6_Integrated_Findings.*`
- `Session_Transcript.md`

---

This file documents how comments were selected, coded, and interpreted, and records the key analytical decisions used to produce the final B50 results package.
