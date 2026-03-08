# GitHub Actions - Weekly Report with AI Summary

## Overview

This workflow generates weekly progress reports with AI-powered summaries using **Ollama + qwen3.5:latest**.

## Features

- ✅ **Automatic scheduling** - Runs every Sunday at 22:00 UTC
- ✅ **AI Summary** - Uses Ollama qwen3.5:latest for intelligent summaries
- ✅ **Auto-detect week** - Calculates current week from project start
- ✅ **Manual trigger** - Can run manually with custom week number
- ✅ **PDF output** - Commits PDF to repository + uploads as artifact

## Setup

### 1. Repository Permissions

Ensure workflow has write permissions:

```yaml
permissions:
  contents: write
```

### 2. GitHub Token

The workflow uses `GITHUB_TOKEN` secret (automatically provided).

### 3. First Run

The first run will take ~5 minutes as it:
1. Installs Ollama
2. Downloads qwen3.5:latest model (~4GB)
3. Generates report

Subsequent runs are faster (~2 minutes).

## Usage

### Automatic (Scheduled)

Runs every Sunday at 22:00 UTC.

### Manual Trigger

1. Go to **Actions** tab
2. Select **"Generate Weekly Report (Ollama)"**
3. Click **"Run workflow"**
4. Optionally enter week number
5. Click **"Run workflow"**

### Output

- **PDF:** `reports/week-X-report.pdf` (committed to repo)
- **Artifact:** Downloadable from workflow run (30 days)

## Customization

### Change Schedule

Edit cron expression in workflow:

```yaml
on:
  schedule:
    - cron: '0 22 * * 0'  # Sunday 22:00 UTC
```

### Change AI Model

Edit Ollama model in workflow:

```yaml
- name: Install Ollama
  run: |
    ollama pull qwen3.5:latest  # Change model here
```

### Change Project Start Date

Edit in `scripts/generate_weekly_report.py`:

```python
PROJECT_START_DATE = datetime(2026, 3, 2)  # Week 1 starts Monday, Mar 2, 2026
```

## Troubleshooting

### Workflow fails on Ollama step

- Check runner has enough disk space (model is ~4GB)
- Increase timeout if needed
- Try smaller model: `ollama pull qwen2.5:7b`

### AI summary is empty

- Check Ollama is running: `ollama list`
- Test model: `ollama run qwen3.5:latest "hello"`
- Fallback: Report shows issue list if AI fails

### PDF not committed

- Check `permissions: contents: write`
- Verify branch protection rules
- Check workflow run logs

## Cost

- **GitHub Actions:** Free for public repos, included minutes for private
- **Ollama:** Free, open-source
- **qwen3.5:latest:** Free model

**Total cost: $0** 🎉

## Example Output

See `reports/week-1-report.pdf` for example output.
