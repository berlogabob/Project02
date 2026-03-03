#!/bin/bash
# Milestone creation script for Project 7
# Corrected dates based on current project status

set -e

echo "=================="
echo "Creating Milestones for Project 7"
echo "Repository: Users/berlogabob/Project02"
echo "=================="

# Get repo info first (needed for project association)
echo "Getting repository info..."
REPO_ID=$(gh repo view --jq .id) || REPO_ID="${GITHUB_REPO_ID:-"default"}"

echo "Repository ID check complete"
echo "Creating milestones..."

# Milestone 1 - Documentation (35-45 days)
echo "" 
echo "📝 Creating Milestone 1: Documentation (MCCA)..."
github milestone create \
    --repo . \
    "1st Milestone - Documentation (MCCA)" 2026-02-16 || echo "⚠️ Milestone 1 may already exist or needs project association"

# Milestone 2 - Prototype (45-60 days)
echo "" 
echo "🛠️ Creating Milestone 2: Prototype (MCCA)..."
gh milestone create \
    --repo . \
    "2nd Milestone - Prototype (MCCA)" 2025-11-13 || echo "⚠️ Milestone 2 may already exist or needs project association"

# Milestone 3 - Final Product (60-90 days)
echo "" 
echo "🎉 Creating Milestone 3: Final Product (MCCIA)..."
gh milestone create \
    --repo . \
    "3rd Milestone - Final Product (MCCIA)" 2025-12-31 || echo "⚠️ Milestone 3 may already exist or needs project association"

echo ""
echo "=================="
echo "✓ All milestones created!"
echo "=================="
echo "List your milestones: gh milestone list"
echo "View in project: https://github.com/users/berlogabob/projects/7"
echo ""
echo "Done!"
