#!/usr/bin/env python3
"""
Validation and Sanitization Module for Weekly Report Generation.

Provides:
  - sanitize_for_typst(): escapes characters that have special meaning in Typst
  - validate_ai_summary(): checks that a summary meets quality rules
  - build_report_json(): assembles the intermediate JSON representation
  - save_report_json(): persists the JSON to disk for debugging/traceability
"""

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Sanitisation
# ---------------------------------------------------------------------------

_TYPST_REPLACEMENTS = [
    ("\\", "\\\\"),   # must be first to avoid double-escaping
    ("#", "\\#"),
    ("$", "\\$"),
    ("_", "\\_"),
    ("*", " "),
    ("[", "("),
    ("]", ")"),
    ("<", "\\<"),
    (">", "\\>"),
    ("@", "\\@"),
]


def sanitize_for_typst(text: str) -> str:
    """Escape characters that have special meaning in Typst.

    The replacement order matters: backslash must be escaped first so that
    subsequent replacements do not double-escape already-escaped sequences.
    """
    if not text:
        return ""
    for char, escaped in _TYPST_REPLACEMENTS:
        text = text.replace(char, escaped)
    return text


# ---------------------------------------------------------------------------
# AI-summary validation
# ---------------------------------------------------------------------------

_TYPST_SPECIAL_RE = re.compile(r"(?<!\\)[#$_\[\]@<>]|\*")


def validate_ai_summary(summary: str) -> tuple[bool, list[str]]:
    """Validate an AI-generated summary against quality rules.

    Rules:
      - Must contain 3-5 bullet points (lines starting with '-')
      - Each bullet must be at most 15 words
      - No unescaped Typst special characters
      - Total word count must be ≤ 100

    Returns:
        (is_valid, list_of_error_messages)
    """
    errors: list[str] = []

    lines = [l.strip() for l in summary.strip().split("\n") if l.strip()]
    bullets = [l for l in lines if l.startswith("-")]

    if not (3 <= len(bullets) <= 5):
        errors.append(
            f"Expected 3-5 bullet points, got {len(bullets)}"
        )

    for i, bullet in enumerate(bullets, 1):
        word_count = len(bullet.split())
        if word_count > 15:
            errors.append(
                f"Bullet {i} has {word_count} words (max 15): {bullet[:60]}…"
            )

    total_words = len(summary.split())
    if total_words > 100:
        errors.append(f"Summary has {total_words} words (max 100)")

    if _TYPST_SPECIAL_RE.search(summary):
        errors.append("Summary contains unescaped Typst special characters")

    return (len(errors) == 0, errors)


def sanitize_summary(summary: str) -> str:
    """Sanitize an AI summary to make it safe for Typst."""
    lines = [l.strip() for l in summary.strip().split("\n") if l.strip()]
    bullets = [l for l in lines if l.startswith("-")]

    # Clamp to 5 bullets
    bullets = bullets[:5]

    sanitized = []
    for bullet in bullets:
        # Remove the leading dash, sanitize, then re-add the dash
        content = bullet.lstrip("-").strip()
        # Limit to first 15 words
        words = content.split()[:15]
        content = " ".join(words)
        content = sanitize_for_typst(content)
        sanitized.append(f"- {content}")

    return "\n".join(sanitized)


# ---------------------------------------------------------------------------
# JSON schema
# ---------------------------------------------------------------------------

def build_report_json(
    week_num: int,
    completed: list,
    incomplete: list,
    future: list,
    ai_summary: str,
    github_sha: Optional[str] = None,
    qwen_model: Optional[str] = None,
) -> dict:
    """Build the intermediate JSON representation of a weekly report.

    The schema is:
    {
      "week": <int>,
      "metadata": {
        "generated_at": <ISO8601>,
        "github_sha": <str|null>,
        "qwen_model": <str|null>,
        "issues_count": <int>
      },
      "summary": {
        "bullets": [<str>, ...]
      },
      "issues": [
        {
          "number": <int>,
          "title": <str sanitized>,
          "body": <str sanitized>,
          "status": "completed" | "in_progress" | "future",
          "priority": "high" | "medium" | "low",
          "assignee": <str>
        },
        ...
      ]
    }
    """

    def _extract_priority(issue: dict) -> str:
        for label in issue.get("labels", []):
            name = label.get("name", "").lower()
            if "critical" in name or "high" in name:
                return "high"
            if "medium" in name:
                return "medium"
        return "low"

    def _extract_assignee(issue: dict) -> str:
        assignees = issue.get("assignees", [])
        return ", ".join(a.get("login", "") for a in assignees)

    def _clean_body(body: str) -> str:
        if not body:
            return ""
        # Strip images, HTML tags, and raw URLs before sanitizing
        body = re.sub(r"!\[.*?\]\(.*?\)", "", body)
        body = re.sub(r"<[^>]+>", "", body)
        body = re.sub(r"https?://\S+", "", body)
        body = re.sub(r"\*\*Parent:\*\*\s*#\d+", "", body, flags=re.IGNORECASE)
        body = re.sub(r"Parent:\s*#\d+", "", body, flags=re.IGNORECASE)
        return body.strip()[:500]

    def _issue_entry(issue: dict, status: str) -> dict:
        return {
            "number": issue.get("number", 0),
            "title": sanitize_for_typst(str(issue.get("title", ""))[:200]),
            "body": sanitize_for_typst(_clean_body(issue.get("body", "") or "")),
            "status": status,
            "priority": _extract_priority(issue),
            "assignee": sanitize_for_typst(_extract_assignee(issue)),
        }

    issues_list = (
        [_issue_entry(i, "completed") for i in completed]
        + [_issue_entry(i, "in_progress") for i in incomplete]
        + [_issue_entry(i, "future") for i in future]
    )

    # Parse bullets from AI summary
    bullets = [
        l.strip().lstrip("-").strip()
        for l in ai_summary.strip().split("\n")
        if l.strip().startswith("-")
    ]

    return {
        "week": week_num,
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "github_sha": github_sha or os.environ.get("GITHUB_SHA"),
            "qwen_model": qwen_model,
            "issues_count": len(issues_list),
        },
        "summary": {
            "bullets": bullets,
        },
        "issues": issues_list,
    }


def save_report_json(report_data: dict, output_dir: str = "reports") -> str:
    """Persist the intermediate report JSON to disk.

    Returns:
        The path to the saved file.
    """
    week_num = report_data.get("week", "unknown")
    out_path = Path(output_dir) / f"week-{week_num}-data.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    return str(out_path)


# ---------------------------------------------------------------------------
# CLI helper (for manual debugging)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate and display a saved report JSON file"
    )
    parser.add_argument("file", help="Path to a week-N-data.json file")
    args = parser.parse_args()

    with open(args.file, encoding="utf-8") as f:
        data = json.load(f)

    bullets = data.get("summary", {}).get("bullets", [])
    summary_text = "\n".join(f"- {b}" for b in bullets)

    is_valid, errors = validate_ai_summary(summary_text)
    if is_valid:
        print("✅ Summary is valid")
    else:
        print("❌ Summary validation failed:")
        for err in errors:
            print(f"   • {err}")

    print(f"\n📊 Issues: {len(data.get('issues', []))}")
    print(f"📅 Generated at: {data.get('metadata', {}).get('generated_at')}")
