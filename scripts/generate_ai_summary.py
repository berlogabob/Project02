#!/usr/bin/env python3
"""
AI Summary Generator for Weekly Report
Fetches completed issues and generates a concise summary using LLM API
"""

import subprocess
import json
import os
from datetime import datetime, timedelta

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
    """Generate AI summary of completed work."""
    if not issues:
        return "No issues completed this week."
    
    issues_text = format_issues_for_prompt(issues)
    
    prompt = f"""You are a project reporting assistant. Analyze the completed GitHub issues and write a concise, professional summary of the work done this week.

**Requirements:**
- Write 3-5 bullet points maximum
- Focus on key achievements and progress
- Be specific about what was accomplished
- Use professional but clear language
- Keep it under 150 words
- Format as bullet points with - prefix

**Completed Issues:**
{issues_text}

**Write the summary:**"""

    # Try different API providers
    if api_provider == "openai":
        return call_openai_api(prompt)
    elif api_provider == "qwen":
        return call_qwen_api(prompt)
    elif api_provider == "ollama":
        return call_ollama_api(prompt)
    else:
        return f"[AI summary not available - {len(issues)} issues completed]"


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
    """Call local Ollama API for summary."""
    import urllib.request
    import urllib.error
    
    # Use qwen3.5:latest model
    data = json.dumps({
        "model": "qwen3.5:latest",
        "prompt": prompt,
        "stream": False
    }).encode("utf-8")
    
    try:
        req = urllib.request.Request(
            "http://localhost:11434/api/generate",
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode())
            return result.get("response", "").strip()
    except Exception as e:
        print(f"Ollama error: {e}")
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
        summary = "No issues completed this week."
    else:
        print(f"🤖 Generating AI summary using {args.api}...")
        summary = generate_ai_summary(issues, args.api)
        if not summary:
            # Fallback to simple list
            summary = f"**{len(issues)} issues completed:**\n" + "\n".join([f"- #{i['number']} {i['title']}" for i in issues[:10]])
    
    print(f"\n✅ Summary:\n{summary}")
    
    if args.output:
        with open(args.output, "w") as f:
            f.write(summary)
        print(f"\n💾 Saved to: {args.output}")
    
    return summary


if __name__ == "__main__":
    main()
