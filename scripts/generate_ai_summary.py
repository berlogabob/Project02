#!/usr/bin/env python3
"""
AI Summary Generator for Weekly Report
Fetches completed issues and generates a concise summary using LLM API
"""

import subprocess
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Allow importing from the same scripts/ directory when run directly
sys.path.insert(0, str(Path(__file__).parent))
try:
    from validate_report_data import validate_ai_summary, sanitize_summary
except ImportError:
    # Graceful fallback if the module is not yet present
    def validate_ai_summary(summary):
        return True, []

    def sanitize_summary(summary):
        return summary

REPO = "berlogabob/Project02"

def get_completed_issues(week_num: int) -> list:
    """Get completed issues for the given week."""
    # Calculate week date range
    project_start = datetime(2026, 3, 2)
    week_start = project_start + timedelta(weeks=(week_num - 1))
    week_end = week_start + timedelta(days=6)
    
    week_start_str = week_start.strftime("%Y-%m-%d")
    week_end_str = (week_end + timedelta(days=1)).strftime("%Y-%m-%d")
    
    result = subprocess.run(
        ["gh", "issue", "list", "--state", "closed",
         "--search", f"closed:>{week_start_str} closed:<{week_end_str}",
         "--limit", "100",
         "--json", "number,title,body,assignees,labels"],
        capture_output=True, text=True
    )
    
    try:
        issues = json.loads(result.stdout) if result.stdout else []
        # Filter only issues with week-N label
        week_issues = [i for i in issues if any(f"week-{week_num}" in lbl.get("name", "") for lbl in i.get("labels", []))]
        return week_issues
    except:
        return []


def format_issues_for_prompt(issues: list) -> str:
    """Format issues as text for LLM prompt."""
    formatted = []
    for issue in issues:
        num = issue.get("number", "?")
        title = issue.get("title", "")
        body = issue.get("body", "") or ""
        assignees = ", ".join([a.get("login", "") for a in issue.get("assignees", [])])
        labels = ", ".join([l.get("name", "") for l in issue.get("labels", [])])
        
        # Clean body - remove images, URLs, etc.
        import re
        body = re.sub(r'!\[.*?\]\(.*?\)', '', body)
        body = re.sub(r'https?://\S+', '', body)
        body = body.strip()[:500]  # Limit body length
        
        formatted.append(f"""
**Issue #{num}: {title}**
- Assignees: {assignees or "None"}
- Labels: {labels or "None"}
- Description: {body[:300]}...
""")
    
    return "\n".join(formatted)


def generate_ai_summary(issues: list, api_provider: str = "openai") -> str:
    """Generate AI summary of completed work.

    Tries the requested provider first, then falls back through the chain:
    ollama → qwen → openai → simple list.
    The returned string is always sanitized and validated before being returned.
    """
    if not issues:
        return "- No issues completed this week."

    issues_text = format_issues_for_prompt(issues)

    # Improved prompt for better summaries
    prompt = f"""You are a project reporting assistant. Analyze these completed GitHub issues and write a concise professional summary.

**Requirements:**
- Write exactly 3-5 bullet points
- Each bullet should be 1-2 sentences  
- Group related tasks together
- Focus on WHAT was accomplished, not just listing issues
- Use action verbs: Implemented, Completed, Developed, Created, etc.
- Keep it under 100 words total
- Format each bullet with - prefix
- Do NOT use hashtags, asterisks, brackets, or dollar signs in the text

**Completed Issues:**
{issues_text}

**Write the summary (3-5 bullets, no intro/outro):**"""

    # Build fallback chain based on requested provider
    _providers = {
        "openai": call_openai_api,
        "qwen": call_qwen_api,
        "ollama": call_ollama_api,
    }
    chain = [api_provider] + [p for p in ("ollama", "qwen", "openai") if p != api_provider]

    raw_summary = None
    for provider in chain:
        func = _providers.get(provider)
        if func is None:
            continue
        result = func(prompt)
        if result:
            raw_summary = result
            print(f"   ✅ Summary from provider: {provider}")
            break

    if not raw_summary:
        # Final fallback: plain list of issue titles
        raw_summary = "\n".join(
            [f"- #{i['number']} {i['title'][:60]}" for i in issues[:5]]
        )
        print("   ⚠️  Using simple fallback summary")

    # Sanitize and validate before returning
    sanitized = sanitize_summary(raw_summary)
    is_valid, errors = validate_ai_summary(sanitized)
    if not is_valid:
        print(f"   ⚠️  Summary validation warnings: {errors}")

    return sanitized


def call_openai_api(prompt: str) -> str:
    """Call OpenAI API for summary."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None
    
    import urllib.request
    import urllib.error
    
    data = json.dumps({
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200
    }).encode("utf-8")
    
    try:
        req = urllib.request.Request(
            "https://api.openai.com/v1/chat/completions",
            data=data,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode())
            return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return None


def call_qwen_api(prompt: str) -> str:
    """Call Qwen API (DashScope/Alibaba Cloud) for summary."""
    api_key = os.environ.get("DASHSCOPE_API_KEY") or os.environ.get("QWEN_API_KEY")
    if not api_key:
        return None
    
    import urllib.request
    import urllib.error
    
    data = json.dumps({
        "model": "qwen-plus",
        "input": {"messages": [{"role": "user", "content": prompt}]},
        "parameters": {"max_tokens": 200}
    }).encode("utf-8")
    
    try:
        req = urllib.request.Request(
            "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation",
            data=data,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode())
            content = result.get("output", {}).get("choices", [{}])[0].get("message", {}).get("content", "")
            return content.strip()
    except Exception as e:
        print(f"Qwen API error: {e}")
        return None


def call_ollama_api(prompt: str) -> str:
    """Call local Ollama API for summary.
    
    Note: Ollama can be slow locally. For GitHub Actions, use qwen3.5:2b.
    For local use, fallback to simple list is faster.
    """
    import subprocess
    
    # Try qwen3.5:0.8b (fastest) with short timeout
    try:
        result = subprocess.run(
            ['curl', '-s', '-m', '15', 'http://localhost:11434/api/generate',
             '-d', json.dumps({
                 'model': 'qwen3.5:0.8b',
                 'prompt': prompt[:500],  # Limit prompt length
                 'stream': False
             })],
            capture_output=True, text=True, timeout=20
        )
        
        if result.returncode == 0 and result.stdout:
            response_data = json.loads(result.stdout)
            response_text = response_data.get('response', '').strip()
            if response_text and len(response_text) > 20:
                # Extract bullet points
                lines = [l.strip() for l in response_text.split('\n') if l.strip().startswith('-')]
                if lines:
                    return '\n'.join(lines)
                return response_text
        return None
    except Exception as e:
        return None


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate AI summary for weekly report")
    parser.add_argument("--week", "-w", type=int, default=None, help="Week number (auto-detect if not provided)")
    parser.add_argument("--api", "-a", choices=["openai", "qwen", "ollama"], default="qwen", help="AI API provider")
    parser.add_argument("--output", "-o", type=str, default=None, help="Output file path")
    args = parser.parse_args()
    
    # Auto-detect week if not provided
    if args.week is None:
        from datetime import datetime
        project_start = datetime(2026, 3, 2)
        today = datetime.now()
        week_num = ((today - project_start).days // 7) + 1
    else:
        week_num = args.week
    
    print(f"📊 Fetching completed issues for Week {week_num}...")
    issues = get_completed_issues(week_num)
    print(f"   Found {len(issues)} completed issues")
    
    if not issues:
        summary = "- No issues completed this week."
    else:
        print(f"🤖 Generating AI summary using {args.api}...")
        summary = generate_ai_summary(issues, args.api)
        if not summary:
            # Fallback to simple list
            summary = "\n".join([f"- #{i['number']} {i['title'][:60]}" for i in issues[:5]])

    print(f"\n✅ Summary:\n{summary}")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"\n💾 Saved to: {args.output}")
    
    return summary


if __name__ == "__main__":
    main()
