# Issue Comments in Weekly Reports

## ✅ YES - Comments Are Now Included!

When team members add comments to issues, they will now **automatically appear in the weekly report**.

---

## How It Works

### Example Workflow

**Issue #1: Research Emergent Technologies**

1. **Monday**: Issue created and assigned to @naydino
2. **Wednesday**: @naydino adds comment with research findings:
   ```
   Found 3 promising technologies:
   - Leap Motion for hand tracking
   - TouchDesigner for real-time visuals
   - OSC for communication
   
   Next: Test integration with Unity
   ```
3. **Sunday night**: GitHub Action generates weekly report
4. **Monday morning**: Report shows:
   - ✅ Issue #1 in "Completed" or "In Progress" section
   - ✅ **Your research comment appears below the issue title**
   - ✅ Professor sees your progress!

---

## Report Output Example

### In the PDF Report:

```
#1 - Research Emergent Technologies                    [done]
  @naydino (2026-03-05): Found 3 promising technologies: Leap Motion for hand tracking...
  @berlogabob (2026-03-06): Great! I'll start Unity integration this weekend
```

---

## What Gets Included

### ✅ Included:
- All comments on issues (max 5 most recent per issue)
- Comment author (@username)
- Comment date
- Comment text (truncated to 150 chars if longer)

### ❌ Not Included:
- Issue description itself (shown separately)
- System-generated comments (bot activity)
- Very old comments (only from last week's activity)

---

## Best Practices

### 1. **Use Comments for Progress Updates**
```
@berlogabob: Plotter calibration complete!
- Tested with red pen on cotton fabric
- Speed: 50mm/s works best
- Pressure: 0.3 N optimal
```

### 2. **Add Research Findings**
```
@naydino: Research results:
- Algorithmic mediation: 3 key papers found
- Collective creation: Analyzed 5 installations
- Comparison table: See attached image
```

### 3. **Document Decisions**
```
@electricianv001: Decision made:
- Using UV-reactive fabric for hidden layers
- MVP will use single fabric piece (not modular)
- Rationale: Simpler for first demo
```

### 4. **Ask Questions (Tag Team)**
```
@dmitri-kazantsev: Question for team:
Should we prioritize speed or quality for MVP?
@naydino @berlogabob thoughts?
```

---

## Formatting

Comments in the report appear as:
- **Smaller font** (8pt)
- **Gray color** (distinguished from titles)
- **Indented** below issue title
- **Attributed** to author with date

Example Typst output:
```typst
#1 - Research Emergent Technologies
  \text(size: 8pt, fill: gray)[@naydino (2026-03-05): Found 3 promising...]
  \text(size: 8pt, fill: gray)[@berlogabob (2026-03-06): Great! I'll start...]
```

---

## Technical Details

### Script: `scripts/generate_weekly_report.py`

```python
# Fetches issues WITH comments
issues = run_gh_command([...], include_comments=True)

# Formats comments for report
comments = format_comments(issue)
# Output: ["@author (date): text", ...]
```

### Limits
- Max 5 comments per issue (most recent)
- Max 150 characters per comment (truncated with "...")
- Only shows comments from issues updated this week

---

## Example Comments That Help

### ✅ Good Comments:

**Research Results:**
```
Completed literature review on algorithmic mediation.
Key findings:
1. Interactive systems shift authorship dynamically
2. Collective creation requires clear input mapping
3. AI should augment, not replace, human creativity

Sources: 5 papers, 3 installations analyzed
```

**Technical Progress:**
```
TouchDesigner ↔ Unity OSC connection working!
- Sent "pattern_generated" event from TD to Unity
- Latency: ~15ms (acceptable)
- Next: Add parameter mapping
```

**Test Results:**
```
Plotter test results:
✅ Cotton fabric: Good line quality
❌ Silk fabric: Too slippery
⚠️  UV fabric: Needs higher pressure

Recommendation: Use cotton for MVP
```

### ❌ Not Helpful:
```
done
ok
test
```

---

## Benefits

### For Team:
- ✅ Automatic progress tracking
- ✅ Knowledge sharing
- ✅ Decision documentation
- ✅ No duplicate status meetings

### For Professor:
- ✅ Clear visibility of work
- ✅ See actual progress (not just checkboxes)
- ✅ Understand challenges
- ✅ Better demo discussions

### For You:
- ✅ Show your work automatically
- ✅ No separate status reports needed
- ✅ Comments = Report content
- ✅ Credit for your contributions

---

## Workflow Summary

```
┌─────────────────────────────────────────────────────┐
│ During Week                                         │
│ - Work on issue                                     │
│ - Add comment with progress/results                 │
│ - Tag team members if needed                        │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│ Sunday Night (Auto)                                 │
│ - GitHub Action fetches issues + comments           │
│ - Formats comments in report                        │
│ - Generates PDF                                     │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│ Monday Morning                                      │
│ - Professor sees your comments in report            │
│ - Live demo with context                            │
│ - Discussion based on actual progress               │
└─────────────────────────────────────────────────────┘
```

---

## Quick Tips

1. **Comment Early, Comment Often**
   - Daily updates = detailed report
   - Shows consistent progress

2. **Be Specific**
   - "Tested plotter with cotton" ✓
   - "Worked on stuff" ✗

3. **Tag Team for Visibility**
   - "@naydino @berlogabob check this out"
   - Gets their attention
   - Shows collaboration

4. **Include Numbers/Data**
   - "Latency: 15ms"
   - "5 papers reviewed"
   - "3 test runs completed"

5. **Add Images/Screenshots**
   - GitHub renders them in comments
   - Report shows text description
   - Professor can click to see full issue

---

## Summary

| Feature | Status |
|---------|--------|
| Comments in report | ✅ YES |
| Author attribution | ✅ @username |
| Date shown | ✅ YYYY-MM-DD |
| Truncation | ✅ 150 chars |
| Max per issue | ✅ 5 comments |
| Formatting | ✅ Small, gray, indented |

**Start commenting on issues - your progress will automatically appear in Monday's report!** 🎉

---

**Created for:** Project II - The Oracle That Wears Us  
**Feature added:** March 4, 2026
