# TGL Keyword Search: Iterations and Verification Methods

## Purpose
This document records the iterative process used to identify legitimacy-related keywords across:
- `TGL_VIDEO.xlsx`
- `TGL_COMMENT.xlsx`

It also documents how outputs were verified before finalizing keyword dictionaries.

## Research Alignment
The keyword extraction was aligned to the project RQ framing:
- Public acceptance, resistance, and ambivalence
- Whether TGL is perceived as "real golf"
- Technology-driven, entertainment-first framing
- Economic and social legitimacy

## Iteration Log

### Iteration 1: Scope and construct clarification
- Confirmed legitimacy framing should include both social and economic dimensions.
- Confirmed focus on whether fans view TGL as actual/real golf.
- Confirmed output style:
  - top 10 keywords
  - mixed single words + short phrases
  - normalized variants merged

### Iteration 2: Dataset profiling and field validation
- Loaded both spreadsheets and verified available text-bearing columns.
- Confirmed extraction fields:
  - `TGL_VIDEO.xlsx`: `title`, `description`, `summary`, `text` (+ contextual columns reviewed)
  - `TGL_COMMENT.xlsx`: `text`
- Verified non-empty text coverage before keyword extraction.

### Iteration 3: Initial lexical seeding
- Built seed families from RQ and plan language:
  - `real golf`, `not real`, `legitimacy`, `authenticity`, `gimmick`
  - `entertainment`, `future of golf`, `tradition`
  - `innovation/technology`, `commercialization`, `resistance`, `seriousness`
- Included phrase-level and single-token variants.

### Iteration 4: Normalization pass
- Applied:
  - lowercase normalization
  - punctuation cleanup
  - stopword filtering
  - variant merging (example: `legit`, `legitimate`, `legitimacy`)
- Removed generic high-frequency noise (URLs, platform artifacts, names not concept-linked).

### Iteration 5: Frequency ranking and conceptual filtering
- Computed candidate counts across combined corpora (video + comment text).
- Split checks by dataset to confirm terms appear in both contexts where expected.
- Filtered to terms that directly signal legitimacy rather than generic popularity words.

### Iteration 6: Concept-specific reruns
- Ran targeted reruns for:
  - Technology legitimacy
  - Commercialization
- Kept method consistent with prior normalization and ranking logic.

### Iteration 7: Dictionary build
- Generated consolidated coding dictionary with columns:
  - `concept`
  - `keyword`
  - `variants`
  - `polarity`
  - `rationale`
- Built second labeled version with:
  - `code_label` (`LEGIT_POS`, `LEGIT_NEG`, `LEGIT_AMB`)

## Verification Methods Used

### 1) Field-level verification
- Confirmed sheet names and columns before extraction.
- Confirmed selected text fields had non-empty coverage.

### 2) Method consistency checks
- Same normalization logic used across concept passes.
- Same merge strategy for variants used across runs.
- Same top-10 ranking style used for all concept outputs.

### 3) Relevance validation
- Retained terms only when tied to legitimacy interpretation in the RQ.
- Excluded high-frequency but non-legitimacy tokens.

### 4) Cross-source validation
- Compared appearance across video metadata text and comment text.
- Checked concept terms were not isolated to a single noisy source.

### 5) Output integrity checks
- Verified final table row counts after export.
- Exported to both `.xlsx` and `.csv` for reproducibility.
- Confirmed labeled file preserves all original rows with added `code_label`.

## Produced Outputs
- `TGL_keyword_dictionary.xlsx`
- `TGL_keyword_dictionary.csv`
- `TGL_keyword_dictionary_with_code_labels.xlsx`
- `TGL_keyword_dictionary_with_code_labels.csv`

## Notes
- Keyword extraction was concept-guided rather than purely unsupervised.
- This supports transparent coding for qualitative/thematic interpretation.
