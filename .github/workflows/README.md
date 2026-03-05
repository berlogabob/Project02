# Daily Plans Generator - GitHub Action

**Pure YAML-only workflow - No Python required**

---

## Overview

This GitHub Action automatically generates daily plan PDFs for all team members based on their assigned GitHub issues. Each plan is a professionally styled 2-page document with:

- **Page 1:** Task overview, priority issues, all tasks
- **Page 2:** Planning notes, time blocks, blockers, end-of-day checklist

---

## Features

| Feature | Description |
|---------|-------------|
| ✅ **Zero Python** | Pure bash + gh CLI + Typst |
| ✅ **Separate Template** | `templates/daily-plan-template.typ` |
| ✅ **Daily Automation** | Runs at 00:00 UTC (02:00 Lisbon) |
| ✅ **Manual Trigger** | Run for specific team member |
| ✅ **Image Handling** | Replaces images with `[IMAGE_PLACEHOLDER]` |
| ✅ **Priority Sorting** | Critical/High issues first |
| ✅ **PDF Artifacts** | 14-day retention |

---

## Workflow Configuration

### Schedule
```yaml
0 0 * * *  # Daily at midnight UTC
```

### Team Members
- `naydino` - Nadine Allan
- `berlogabob` - Andrey Dyakov
- `electricianv001` - Dmitri Kazantsev

---

## File Structure

```
.github/workflows/
└── daily-plans.yml          # Main workflow

templates/
└── daily-plan-template.typ  # Typst template (edit styles here)

reports/daily-plans/
├── YYYYMMDD-daily-plan-naydino.typ
├── YYYYMMDD-daily-plan-naydino.pdf
├── YYYYMMDD-daily-plan-berlogabob.typ
├── YYYYMMDD-daily-plan-berlogabob.pdf
├── YYYYMMDD-daily-plan-electricianv001.typ
└── YYYYMMDD-daily-plan-electricianv001.pdf
```

---

## Manual Trigger

1. Go to **Actions** → **Daily Plans Generator**
2. Click **Run workflow**
3. Select team member (or leave empty for all)
4. Click **Run workflow**

---

## Template Customization

Edit `templates/daily-plan-template.typ` to modify:

- **Colors:** 4 chapter themes (blue, red, green, orange)
- **Fonts:** Noto Sans, 10pt
- **Layout:** A4, margins
- **Components:** `issue_card`, `report_header`, `section_title`, `page_footer`

### Theme Colors

```typst
#let chapter_themes = (
  "1": (blue theme - default),
  "2": (red theme),
  "3": (green theme),
  "4": (orange theme)
)
```

---

## Issue Label Priority

| Label | Priority | Card Color |
|-------|----------|------------|
| `priority: critical` | Highest | Red background |
| `priority: high` | High | Orange background |
| `priority: medium` | Medium | Green background |
| `priority: low` | Low | Gray background |

---

## Image Handling

Images in GitHub issues are replaced with:
```
[IMAGE_PLACEHOLDER: Original issue contained an image - check manually for weekly report inclusion]
```

This allows manual review for weekly reports where visual documentation may be needed.

---

## Troubleshooting

### Workflow Fails

1. Check **Actions** tab for error logs
2. Verify `gh` CLI authentication (auto with `GITHUB_TOKEN`)
3. Ensure Typst is installed (handled by action)

### No PDFs Generated

1. Check Typst compilation step in logs
2. Verify template file exists at `templates/daily-plan-template.typ`
3. Check for Typst syntax errors in generated `.typ` files

### Missing Issues

1. Verify issues are **open** and **assigned** to team member
2. Check issue labels for priority
3. Ensure workflow has `GITHUB_TOKEN` permissions

---

## Artifacts

Generated artifacts are available for **14 days**:

| Artifact | Contents |
|----------|----------|
| `daily-plans-pdf-YYYY-MM-DD` | All PDF files |
| `daily-plans-typ-YYYY-MM-DD` | All Typst source files |

Download from workflow run page or use:
```bash
gh run download --name=daily-plans-pdf-YYYY-MM-DD
```

---

## Local Testing

Test the workflow locally:

```bash
# Authenticate gh CLI
gh auth login

# Run workflow manually
gh workflow run daily-plans.yml

# Or run for specific member
gh workflow run daily-plans.yml -f member=berlogabob

# Check run status
gh run list --workflow=daily-plans.yml

# Download artifacts
gh run download
```

---

## Dependencies

| Tool | Version | Provided By |
|------|---------|-------------|
| gh CLI | latest | ubuntu-latest |
| Typst | 0.14.2+ | typst-community/setup-typst@v3 |
| jq | latest | ubuntu-latest |
| bash | 5.x | ubuntu-latest |

---

## Permissions Required

```yaml
permissions:
  contents: write   # Commit generated files
  actions: read     # Upload artifacts
```

---

## Related Workflows

| Workflow | Purpose |
|----------|---------|
| `daily-plans.yml` | Daily individual task plans |
| `weekly-report.yml` | Weekly consolidated report |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v3.0 | Mar 5, 2026 | YAML-only (no Python) |
| v2.0 | Mar 4, 2026 | Python script + template |
| v1.0 | Mar 3, 2026 | Initial workflow |

---

## Support

For issues or questions:
- Check `PROJECT_AUDIT.md` for comprehensive documentation
- Review workflow logs in **Actions** tab
- Contact team: @berlogabob

---

*Last updated: March 5, 2026*
