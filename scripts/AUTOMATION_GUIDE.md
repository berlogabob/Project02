# GitHub Project Automation Guide

This guide teaches you how to automate creating issues, milestones, and labels for Project II - "The Oracle That Wears Us".

---

## 📚 What You'll Learn

1. **GitHub CLI** (`gh`) - Command-line tool for GitHub
2. **GitHub API** - Direct HTTP requests
3. **Python Script** - Automated bulk creation
4. **GitHub Actions** - Scheduled automation (optional)

---

## 🔧 Setup: Install GitHub CLI

### macOS (Homebrew)
```bash
brew install gh
```

### Authenticate
```bash
gh auth login
```

Follow the prompts:
1. Select **GitHub.com**
2. Choose **HTTPS** or **SSH**
3. Select **Login with a web browser**
4. Copy the code, open the link, paste the code
5. Confirm authentication

### Verify
```bash
gh --version
gh repo view berlogabob/Project02
```

---

## 🎯 Method 1: GitHub CLI (Recommended for beginners)

### Create Milestones

```bash
# Navigate to your repo
cd /Users/berloga/Documents/GitHub/Project02

# Create Milestone 1
gh milestone create "Milestone 1: Documentation" \
  --due-date 2026-02-16 \
  --description "Presentation: Feb 16, 2026 | Weight: 15%" \
  --repo berlogabob/Project02

# Create Milestone 2
gh milestone create "Milestone 2: Prototype" \
  --due-date 2026-04-12 \
  --description "Delivery: Apr 12 | Presentation: Apr 13 | Weight: 35%" \
  --repo berlogabob/Project02

# Create Milestone 3
gh milestone create "Milestone 3: Final Product" \
  --due-date 2026-05-29 \
  --description "Delivery: May 29 | Presentation: Jun 5 | Weight: 50%" \
  --repo berlogabob/Project02
```

### Create Labels

```bash
# Priority labels
gh label create "priority: critical" --color "B60205" --description "Blocker issues"
gh label create "priority: high" --color "D93F0B" --description "Important for milestone"
gh label create "priority: medium" --color "F9D0C4" --description "Standard priority"
gh label create "priority: low" --color "0E8A16" --description "Nice to have"

# Unit labels
gh label create "unit: project-ii" --color "5319E7" --description "Project II coordination"
gh label create "unit: interface-design" --color "5319E7" --description "Interface Design (60%)"
gh label create "unit: generative-ai" --color "5319E7" --description "Generative AI (50%)"
gh label create "unit: deep-learning" --color "5319E7" --description "Applied Deep Learning (50%)"
gh label create "unit: emerging-tech" --color "5319E7" --description "Emerging Technologies (50%)"

# Type labels
gh label create "type: research" --color "0075CA" --description "Research tasks"
gh label create "type: development" --color "0075CA" --description "Development work"
gh label create "type: design" --color "0075CA" --description "Design work"
gh label create "type: documentation" --color "0075CA" --description "Documentation"
gh label create "type: testing" --color "0075CA" --description "Testing and QA"
gh label create "type: assets" --color "0075CA" --description "Asset creation/integration"

# Milestone labels
gh label create "milestone-1" --color "D4C5F9" --description "Documentation (Feb 16)"
gh label create "milestone-2" --color "D4C5F9" --description "Prototype (Apr 12/13)"
gh label create "milestone-3" --color "D4C5F9" --description "Final Product (May 29/Jun 5)"
```

### Create Issues (Phase 1)

```bash
# Issue #1
gh issue create \
  --title "#1 - Research Emergent Technologies" \
  --body "Investigate and select one emergent technology as reference for the experience.

**Deliverables:**
- Research emergent technologies for digital fashion
- Select one technology as project reference
- Document findings

**Labels:** \`type: research\` \`unit: emerging-tech\` \`milestone-1\` \`priority: high\`" \
  --label "type: research" \
  --label "unit: emerging-tech" \
  --label "milestone-1" \
  --label "priority: high" \
  --milestone "Milestone 1: Documentation" \
  --repo berlogabob/Project02

# Issue #2
gh issue create \
  --title "#2 - Visual & Audio Reference Board" \
  --body "Collect references for style, image, color, sound for the experience.

**Deliverables:**
- Create mood board
- Collect visual references (style, color, imagery)
- Collect audio references (sound design, music)

**Labels:** \`type: research\` \`type: design\` \`milestone-1\`" \
  --label "type: research" \
  --label "type: design" \
  --label "milestone-1" \
  --milestone "Milestone 1: Documentation" \
  --repo berlogabob/Project02

# Issue #3
gh issue create \
  --title "#3 - User Flow Definition" \
  --body "Map user journey: interactions, outcomes, experience flow.

**Deliverables:**
- Define user entry point
- Map interaction sequence
- Document expected outcomes
- Create user flow diagram

**Labels:** \`type: design\` \`type: documentation\` \`milestone-1\`" \
  --label "type: design" \
  --label "type: documentation" \
  --label "milestone-1" \
  --milestone "Milestone 1: Documentation" \
  --repo berlogabob/Project02
```

---

## 🐍 Method 2: Python Script (Bulk creation)

### Create the Script

Save this as `scripts/create_github_items.py`:

```python
#!/usr/bin/env python3
"""
GitHub Project Automation Script
Creates milestones, labels, and issues for Project II
"""

import subprocess
import json
from dataclasses import dataclass
from typing import List

# Configuration
REPO = "berlogabob/Project02"

@dataclass
class Milestone:
    title: str
    due_date: str
    description: str

@dataclass
class Label:
    name: str
    color: str
    description: str

@dataclass
class Issue:
    number: int
    title: str
    body: str
    labels: List[str]
    milestone: str

# Data from timeline.md
MILESTONES = [
    Milestone(
        title="Milestone 1: Documentation",
        due_date="2026-02-16",
        description="Presentation: Feb 16, 2026 | Weight: 15%"
    ),
    Milestone(
        title="Milestone 2: Prototype",
        due_date="2026-04-12",
        description="Delivery: Apr 12 | Presentation: Apr 13 | Weight: 35%"
    ),
    Milestone(
        title="Milestone 3: Final Product",
        due_date="2026-05-29",
        description="Delivery: May 29 | Presentation: Jun 5 | Weight: 50%"
    ),
]

LABELS = [
    # Priority
    Label("priority: critical", "B60205", "Blocker issues"),
    Label("priority: high", "D93F0B", "Important for milestone"),
    Label("priority: medium", "F9D0C4", "Standard priority"),
    Label("priority: low", "0E8A16", "Nice to have"),
    
    # Units
    Label("unit: project-ii", "5319E7", "Project II coordination"),
    Label("unit: interface-design", "5319E7", "Interface Design (60%)"),
    Label("unit: generative-ai", "5319E7", "Generative AI (50%)"),
    Label("unit: deep-learning", "5319E7", "Applied Deep Learning (50%)"),
    Label("unit: emerging-tech", "5319E7", "Emerging Technologies (50%)"),
    
    # Types
    Label("type: research", "0075CA", "Research tasks"),
    Label("type: development", "0075CA", "Development work"),
    Label("type: design", "0075CA", "Design work"),
    Label("type: documentation", "0075CA", "Documentation"),
    Label("type: testing", "0075CA", "Testing and QA"),
    Label("type: assets", "0075CA", "Asset creation/integration"),
    
    # Milestones
    Label("milestone-1", "D4C5F9", "Documentation (Feb 16)"),
    Label("milestone-2", "D4C5F9", "Prototype (Apr 12/13)"),
    Label("milestone-3", "D4C5F9", "Final Product (May 29/Jun 5)"),
]

PHASE_1_ISSUES = [
    Issue(
        number=1,
        title="Research Emergent Technologies",
        body="""Investigate and select one emergent technology as reference for the experience.

## Deliverables
- Research emergent technologies for digital fashion
- Select one technology as project reference
- Document findings

## Acceptance Criteria
- [ ] Technology selected and justified
- [ ] Documentation added to wiki
- [ ] Presented to team

## Related Units
- Emerging Technologies (50%)""",
        labels=["type: research", "unit: emerging-tech", "milestone-1", "priority: high"],
        milestone="Milestone 1: Documentation"
    ),
    Issue(
        number=2,
        title="Visual & Audio Reference Board",
        body="""Collect references for style, image, color, sound for the experience.

## Deliverables
- Create mood board
- Collect visual references (style, color, imagery)
- Collect audio references (sound design, music)

## Acceptance Criteria
- [ ] Mood board created
- [ ] References documented
- [ ] Style guide established

## Related Units
- Interface Design and Interaction (60%)""",
        labels=["type: research", "type: design", "milestone-1"],
        milestone="Milestone 1: Documentation"
    ),
    Issue(
        number=3,
        title="User Flow Definition",
        body="""Map user journey: interactions, outcomes, experience flow.

## Deliverables
- Define user entry point
- Map interaction sequence
- Document expected outcomes
- Create user flow diagram

## Acceptance Criteria
- [ ] User flow diagram created
- [ ] Interaction points documented
- [ ] Outcomes defined

## Related Units
- Interface Design and Interaction (60%)""",
        labels=["type: design", "type: documentation", "milestone-1"],
        milestone="Milestone 1: Documentation"
    ),
    Issue(
        number=4,
        title="Topic Selection & Theoretical Framework",
        body="""Define project topic with critical and theoretical support.

## Topics to Consider
- Identity
- Body
- Society
- Culture
- Wearables
- Industry 5.0
- Consumption

## Deliverables
- Selected topic with justification
- Theoretical framework document
- Critical references

## Acceptance Criteria
- [ ] Topic selected
- [ ] Theoretical support documented
- [ ] References compiled""",
        labels=["type: research", "type: documentation", "milestone-1", "priority: critical"],
        milestone="Milestone 1: Documentation"
    ),
    Issue(
        number=5,
        title="Weekly Activity Plan Creation",
        body="""Create weekly plan contextualized by each supporting unit.

## Deliverables
- 14-week activity plan
- Unit-by-unit breakdown
- Milestone alignment

## Acceptance Criteria
- [ ] Plan created in timeline.md
- [ ] All units represented
- [ ] Milestones integrated""",
        labels=["type: documentation", "milestone-1", "priority: high"],
        milestone="Milestone 1: Documentation"
    ),
    Issue(
        number=6,
        title="Related Projects Research",
        body="""Document existing projects in digital fashion/emergent tech space.

## Deliverables
- Research 5-10 related projects
- Analyze approaches and technologies
- Document findings

## Acceptance Criteria
- [ ] Research document created
- [ ] Competitive analysis complete
- [ ] Insights documented""",
        labels=["type: research", "type: documentation", "milestone-1"],
        milestone="Milestone 1: Documentation"
    ),
    Issue(
        number=7,
        title="Hardware & Framework Selection",
        body="""Select appropriate hardware and define integration strategy.

## Deliverables
- Hardware requirements document
- Framework evaluation
- Integration strategy

## Acceptance Criteria
- [ ] Hardware selected
- [ ] Frameworks evaluated
- [ ] Integration strategy documented

## Related Units
- Emerging Technologies (50%)""",
        labels=["unit: emerging-tech", "type: research", "milestone-1", "priority: high"],
        milestone="Milestone 1: Documentation"
    ),
    Issue(
        number=8,
        title="Milestone 1 Presentation Preparation",
        body="""Prepare slides and production dossier for Feb 16 presentation.

## Deliverables
- Presentation slides
- Production dossier/report
- Weekly activity plan
- Research documentation

## Acceptance Criteria
- [ ] Slides completed
- [ ] Dossier submitted
- [ ] Presentation rehearsed

## Deadline
- **Presentation:** Feb 16, 2026
- **Delivery:** Feb 16, 2026, 23:59:59 GMT""",
        labels=["milestone-1", "type: documentation", "priority: critical"],
        milestone="Milestone 1: Documentation"
    ),
]

def run_command(cmd: List[str]) -> str:
    """Run a shell command and return output"""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        return None
    return result.stdout.strip()

def create_milestones():
    """Create all milestones"""
    print("\n🎯 Creating Milestones...")
    for m in MILESTONES:
        cmd = [
            "gh", "milestone", "create", m.title,
            "--due-date", m.due_date,
            "--description", m.description,
            "--repo", REPO
        ]
        result = run_command(cmd)
        if result:
            print(f"✅ Created: {m.title}")
        else:
            print(f"⚠️  Already exists: {m.title}")

def create_labels():
    """Create all labels"""
    print("\n🏷️  Creating Labels...")
    for label in LABELS:
        cmd = [
            "gh", "label", "create", label.name,
            "--color", label.color,
            "--description", label.description,
            "--repo", REPO
        ]
        result = run_command(cmd)
        if result:
            print(f"✅ Created: {label.name}")
        else:
            print(f"⚠️  Already exists: {label.name}")

def create_issues(issues: List[Issue]):
    """Create issues"""
    print("\n📋 Creating Issues...")
    for issue in issues:
        labels_flat = ",".join(issue.labels)
        cmd = [
            "gh", "issue", "create",
            "--title", f"#{issue.number} - {issue.title}",
            "--body", issue.body,
            "--label", labels_flat,
            "--milestone", issue.milestone,
            "--repo", REPO
        ]
        result = run_command(cmd)
        if result:
            print(f"✅ Created: #{issue.number} - {issue.title}")
            # Extract issue URL from result
            if "https://" in result:
                print(f"   {result}")
        else:
            print(f"⚠️  Failed: #{issue.number} - {issue.title}")

def main():
    print("🚀 GitHub Project Automation")
    print("=" * 50)
    
    # Check if gh is installed
    result = run_command(["gh", "--version"])
    if not result:
        print("❌ GitHub CLI not found. Install with: brew install gh")
        return
    
    print(f"✅ GitHub CLI found: {result.split()[0]}")
    print(f"📦 Repository: {REPO}")
    
    # Confirm
    confirm = input("\nProceed with creation? (y/n): ")
    if confirm.lower() != 'y':
        print("Cancelled.")
        return
    
    # Create items
    create_milestones()
    create_labels()
    create_issues(PHASE_1_ISSUES)
    
    print("\n" + "=" * 50)
    print("✅ Done! Check your project at:")
    print(f"https://github.com/{REPO}/issues")
    print(f"https://github.com/users/berlogabob/projects/7")

if __name__ == "__main__":
    main()
```

### Make it Executable

```bash
# Create scripts directory
mkdir -p scripts

# Save the script
# (save the code above as scripts/create_github_items.py)

# Make executable
chmod +x scripts/create_github_items.py
```

### Run the Script

```bash
cd /Users/berloga/Documents/GitHub/Project02
python3 scripts/create_github_items.py
```

---

## 🌐 Method 3: GitHub API (Advanced)

### Using curl

```bash
# Set your token (create at: https://github.com/settings/tokens)
export GITHUB_TOKEN="your_token_here"

# Create a milestone
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/berlogabob/Project02/milestones \
  -d '{
    "title": "Milestone 1: Documentation",
    "due_on": "2026-02-16T23:59:59Z",
    "description": "Presentation: Feb 16, 2026 | Weight: 15%"
  }'

# Create a label
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/berlogabob/Project02/labels \
  -d '{
    "name": "priority: critical",
    "color": "B60205",
    "description": "Blocker issues"
  }'

# Create an issue
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/berlogabob/Project02/issues \
  -d '{
    "title": "#1 - Research Emergent Technologies",
    "body": "Investigate and select one emergent technology...",
    "labels": ["type: research", "milestone-1"],
    "milestone": 1
  }'
```

---

## 📊 Add Issues to Project Board

### Using GitHub CLI (Beta)

```bash
# Get your project ID
gh project view 7 --owner berlogabob --format json

# Add an issue to the project
gh project item-add 7 \
  --owner berlogabob \
  --url https://github.com/berlogabob/Project02/issues/1
```

### Manual Method

1. Go to: https://github.com/users/berlogabob/projects/7
2. Click **Add items**
3. Search for your issues
4. Select and add

---

## 🤖 Bonus: GitHub Actions (Scheduled Automation)

Create `.github/workflows/project-setup.yml`:

```yaml
name: Project Setup

on:
  workflow_dispatch:  # Manual trigger

jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup GitHub CLI
        run: |
          gh auth login --with-token <<< "${{ secrets.GITHUB_TOKEN }}"
      
      - name: Create Milestones
        run: |
          gh milestone create "Milestone 1: Documentation" --due-date 2026-02-16
          gh milestone create "Milestone 2: Prototype" --due-date 2026-04-12
          gh milestone create "Milestone 3: Final Product" --due-date 2026-05-29
```

---

## 📝 Quick Reference

| Task | Command |
|------|---------|
| View milestones | `gh milestone list` |
| View labels | `gh label list` |
| View issues | `gh issue list` |
| Create issue | `gh issue create --title "..." --body "..."` |
| Close issue | `gh issue close <number>` |
| Add to project | `gh project item-add <project-id>` |

---

## 🎓 Next Steps

1. **Install GitHub CLI**: `brew install gh`
2. **Authenticate**: `gh auth login`
3. **Run the Python script**: `python3 scripts/create_github_items.py`
4. **Add issues to Project board** (manual or via CLI)
5. **Start tracking progress!**

---

## 🔗 Resources

- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Your Project Board](https://github.com/users/berlogabob/projects/7)
- [Your Repository](https://github.com/berlogabob/Project02)
