# Scripts Directory

Automation tools for GitHub Project management.

---

## 🚀 Quick Start

### Step 1: Install GitHub CLI

```bash
brew install gh
```

### Step 2: Authenticate

```bash
gh auth login
```

Follow the prompts to log in with your GitHub account.

### Step 3: Run the Setup

**Option A: Interactive Shell Script (Easiest)**
```bash
./scripts/setup_project.sh
```

**Option B: Python Script (Full control)**
```bash
python3 scripts/create_github_items.py
```

---

## 📁 Files

| File | Description |
|------|-------------|
| `setup_project.sh` | Interactive shell script with menu |
| `create_github_items.py` | Full Python automation script |
| `AUTOMATION_GUIDE.md` | Complete learning guide |

---

## 🎯 What Gets Created

### Milestones (3)
- Milestone 1: Documentation (Due: Feb 16, 2026)
- Milestone 2: Prototype (Due: Apr 12, 2026)
- Milestone 3: Final Product (Due: May 29, 2026)

### Labels (17)
- **Priority:** critical, high, medium, low
- **Units:** project-ii, interface-design, generative-ai, deep-learning, emerging-tech
- **Types:** research, development, design, documentation, testing, assets
- **Milestones:** milestone-1, milestone-2, milestone-3

### Issues (23)
- **Phase 1:** 8 issues (Research & Concept)
- **Phase 2:** 15 issues (Prototyping & Technical)

---

## 🛠️ Manual Commands

If you prefer to create items one by one:

```bash
# View existing milestones
gh milestone list

# View existing labels
gh label list

# View existing issues
gh issue list

# Create a milestone
gh milestone create "My Milestone" --due-date 2026-12-31

# Create a label
gh label create "my-label" --color "FF0000"

# Create an issue
gh issue create --title "My Issue" --body "Description"
```

---

## 📊 Add to Project Board

After creating issues, add them to your Project board:

1. Go to: https://github.com/users/berlogabob/projects/7
2. Click **Add items**
3. Search and select your issues
4. Click **Add to project**

Or use GitHub CLI (beta):
```bash
gh project item-add 7 --owner berlogabob --url https://github.com/berlogabob/Project02/issues/1
```

---

## 🔧 Troubleshooting

### "gh: command not found"
Install GitHub CLI: `brew install gh`

### "authentication required"
Run: `gh auth login`

### "milestone already exists"
The milestone was already created. This is fine - skip to the next item.

### "rate limit exceeded"
GitHub API has rate limits. Wait a few minutes and try again.

---

## 📚 Learn More

- [GitHub CLI Manual](https://cli.github.com/manual/)
- [GitHub Projects Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [Full Automation Guide](AUTOMATION_GUIDE.md)

---

## 🎓 Learning Path

1. **Beginner:** Use `setup_project.sh` (interactive menu)
2. **Intermediate:** Read `AUTOMATION_GUIDE.md` and understand the commands
3. **Advanced:** Modify `create_github_items.py` for custom needs
4. **Expert:** Use GitHub API directly with `curl` or Python `requests`

---

**Created for:** Project II - The Oracle That Wears Us (MCCIA Master's Program)  
**Semester:** 2025-2026 / 2nd Semester
