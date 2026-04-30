# TGL Report Workflow: Code and Command Log

## Purpose

This file documents commands/code used during the outline and full-report construction workflow in this chat session.

It is intentionally separate from project analysis code that may have been run in earlier sessions.

## Important Context

- The report-writing workflow primarily used document reads, synthesis, and structured writing.
- No new Python or statistical computation script was executed in this session to regenerate dataset findings.
- Report values were sourced from existing project files already present in the workspace.

## Commands Executed in This Workflow

### 1) Word/line/character count check for full draft

**Environment:** PowerShell  
**Command:**

```powershell
(Get-Content "c:\Users\herna\OneDrive\Desktop\LSU\Graduate School\Social Issues\DATA&RESOURCES\DATA&RESOURCES\PROJECT2\TGL\TGL_Report_Full_Draft.md" -Raw | Measure-Object -Word -Line -Character) | Format-List
```

**Purpose:** Validate page-length feasibility under 12 pt, Times New Roman, double spacing.

**Observed output summary:**
- Lines: 234
- Words: 2678
- Characters: 20353

## Non-Shell Processing Steps (Tool-Driven, No Local Script)

The following actions were performed through editor tools rather than direct local scripts:
- File discovery (glob searches) across the `TGL` folder.
- File content reads from markdown/csv artifacts.
- Draft creation and updates via patch edits.
- Lint checks on edited markdown files.
- Literature discovery via web search.

These steps involved no executable analysis code in the local project environment beyond the single PowerShell count command above.

## Related Existing Code Artifacts (Already in Project Folder)

For prior analysis/visualization code and coding strings used in the broader project, see:
- `TGL_All_Code_Used.md`
- `TGL_keyword_search_codestrings.md`
- `TGL_keyword_search_iterations_and_verification.md`
- `TGL_keyword_dictionary_with_code_labels.csv`

## If You Need a "Run-Again" Script

If desired, a separate reproducibility script can be created to:
1. Load `TGL_VIDEO.xlsx` and `TGL_COMMENT.xlsx`,
2. Apply dictionary/code-label matching from CSV,
3. Recompute the reported counts used in the report,
4. Export a fresh results table for citation in the manuscript.
