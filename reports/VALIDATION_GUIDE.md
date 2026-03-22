# Report Data Validation Guide

This document explains how data flows through the **MD→JSON→Typst→PDF** pipeline and what rules are enforced at each step.

---

## Pipeline Overview

```
GitHub Issues (raw)
      │
      ▼
generate_weekly_report.py
      │
      ├─► validate_report_data.py
      │      sanitize_for_typst()   ← escapes Typst special chars
      │      build_report_json()    ← creates intermediate JSON
      │      save_report_json()     ← writes reports/week-N-data.json
      │
      ├─► generate_ai_summary_for_week()
      │      Ollama → fallback to simple list
      │      sanitize_summary()     ← sanitizes + clamps bullets
      │      validate_ai_summary()  ← warns if rules broken
      │
      └─► Typst source (.typ) → PDF
```

---

## Sanitisation Rules (`sanitize_for_typst`)

The following substitutions are applied to **all** text inserted into Typst templates:

| Original | Replacement | Reason |
|----------|------------|--------|
| `\`      | `\\`       | Escape sequence prefix |
| `#`      | `\#`       | Typst function call marker |
| `$`      | `\$`       | Typst math mode |
| `_`      | `\_`       | Typst emphasis |
| `*`      | ` ` (space) | Typst strong emphasis |
| `[`      | `(`        | Typst content block start |
| `]`      | `)`        | Typst content block end |
| `<`      | `\<`       | Typst label/link |
| `>`      | `\>`       | Typst label/link |
| `@`      | `\@`       | Typst citation/reference |

> **Note:** Backslash is replaced first to avoid double-escaping.

---

## AI Summary Validation Rules

The `validate_ai_summary()` function enforces:

| Rule | Constraint |
|------|-----------|
| Number of bullets | 3–5 |
| Words per bullet | ≤ 15 |
| Total word count | ≤ 100 |
| Unescaped Typst chars | Not allowed (`#`, `$`, `_`, `[`, `]`, `@`, `<`, `>`) |

If the AI-generated summary fails validation, `sanitize_summary()` is applied automatically:
- Clamps to 5 bullets
- Truncates each bullet to 15 words
- Runs `sanitize_for_typst()` on each bullet

---

## Intermediate JSON Schema

Every report run saves a `reports/week-N-data.json` file with this structure:

```json
{
  "week": 3,
  "metadata": {
    "generated_at": "2026-03-22T10:00:00+00:00",
    "github_sha": "abc1234",
    "qwen_model": "qwen3.5:2b",
    "issues_count": 12
  },
  "summary": {
    "bullets": [
      "Implemented plotter firmware with multi-axis control",
      "Completed AI-generated concept visualisation pipeline"
    ]
  },
  "issues": [
    {
      "number": 101,
      "title": "Design plotter firmware architecture",
      "body": "Designed the core firmware for CNC plotter.",
      "status": "completed",
      "priority": "high",
      "assignee": "berlogabob"
    }
  ]
}
```

> JSON files are **excluded from git** (see `.gitignore`) but kept locally for debugging.

---

## Local Testing (Offline)

Run the test script to validate the pipeline without GitHub CLI or Ollama:

```bash
# Basic test (Week 3 by default)
python3 scripts/test_report_generation.py

# Custom week and output path
python3 scripts/test_report_generation.py --week 2 --output /tmp/test-report.typ

# Also compile to PDF (requires Typst installed)
python3 scripts/test_report_generation.py --compile
```

The script uses fixed test data that includes:
- Cyrillic strings (to validate UTF-8 handling)
- Issues with problematic characters (`#`, `*`, `[`, `]`, `$`)
- A raw AI summary with Typst special characters

---

## Fallback Chain

If AI generation fails at any step, the pipeline gracefully degrades:

```
1. Ollama (qwen3.5:2b, local)
   ↓ (if unavailable or empty response)
2. Qwen API (DashScope)
   ↓ (if API key missing or error)
3. OpenAI API (gpt-4o-mini)
   ↓ (if API key missing or error)
4. Simple sanitized issue list (always works)
```

---

## UTF-8 / Cyrillic Handling

- All file writes use `encoding="utf-8"` explicitly
- JSON is serialized with `ensure_ascii=False`
- GitHub Actions workflow sets `LANG=en_US.UTF-8` and `PYTHONIOENCODING=utf-8`
- Typst supports Unicode natively, so sanitized UTF-8 text renders correctly
