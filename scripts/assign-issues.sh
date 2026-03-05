#!/bin/bash
# Quick Assign Issues to Team Members

echo "📋 Assigning issues to team members..."
echo ""

# Issue 1 - Research Emergent Technologies
echo "Assigning #1 to @naydino..."
gh issue edit 1 --add-assignee naydino --repo berlogabob/Project02

# Issue 2 - Visual & Audio Reference Board
echo "Assigning #2 to @berlogabob..."
gh issue edit 2 --add-assignee berlogabob --repo berlogabob/Project02

# Issue 3 - User Flow Definition
echo "Assigning #3 to @naydino..."
gh issue edit 3 --add-assignee naydino --repo berlogabob/Project02

# Issue 4 - Topic Selection
echo "Assigning #4 to @electricianv001..."
gh issue edit 4 --add-assignee electricianv001 --repo berlogabob/Project02

# Issue 5 - Hardware Selection
echo "Assigning #5 to @berlogabob..."
gh issue edit 5 --add-assignee berlogabob --repo berlogabob/Project02

# Issue 6 - Milestone 1 Prep (all team)
echo "Assigning #6 to all team..."
gh issue edit 6 --add-assignee naydino --add-assignee berlogabob --add-assignee electricianv001 --repo berlogabob/Project02

echo ""
echo "✅ All issues assigned!"
echo ""
echo "Now run daily plan workflow to see tasks in PDFs:"
echo "https://github.com/berlogabob/Project02/actions/workflows/daily-plans-v2.yml"
