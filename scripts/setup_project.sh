#!/bin/bash
# Quick Start: GitHub Project Setup
# This script sets up milestones, labels, and issues for Project II

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Repository
REPO="berlogabob/Project02"

echo ""
echo "========================================================"
echo "🚀 GitHub Project Quick Start - The Oracle That Wears Us"
echo "   Project II (MCCIA)"
echo "========================================================"
echo ""

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}❌ GitHub CLI (gh) not found!${NC}"
    echo ""
    echo "Install with Homebrew:"
    echo "   brew install gh"
    echo ""
    exit 1
fi

echo -e "${GREEN}✅${NC} GitHub CLI found: $(gh --version | head -n1)"

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo -e "${RED}❌ GitHub CLI not authenticated!${NC}"
    echo ""
    echo "Authenticate with:"
    echo "   gh auth login"
    echo ""
    exit 1
fi

echo -e "${GREEN}✅${NC} GitHub CLI authenticated"
echo -e "${BLUE}📦${NC} Repository: ${REPO}"
echo ""

# Menu
echo "========================================================"
echo "What would you like to create?"
echo "========================================================"
echo ""
echo "1) Milestones only (3 items)"
echo "2) Labels only (17 items)"
echo "3) Phase 1 Issues only (8 items)"
echo "4) Phase 2 Issues only (15 items)"
echo "5) Everything (Milestones + Labels + All Issues)"
echo "6) Cancel"
echo ""
echo -n "Select option [1-6]: "
read -r option

case $option in
    1)
        echo -e "${YELLOW}🎯 Creating Milestones...${NC}"
        echo ""
        
        gh milestone create "Milestone 1: Documentation" \
          --due-date 2026-02-16 \
          --description "Presentation: Feb 16, 2026 | Weight: 15%" \
          --repo $REPO || echo "⚠️  Milestone 1 already exists"
        
        gh milestone create "Milestone 2: Prototype" \
          --due-date 2026-04-12 \
          --description "Delivery: Apr 12 | Presentation: Apr 13 | Weight: 35%" \
          --repo $REPO || echo "⚠️  Milestone 2 already exists"
        
        gh milestone create "Milestone 3: Final Product" \
          --due-date 2026-05-29 \
          --description "Delivery: May 29 | Presentation: Jun 5 | Weight: 50%" \
          --repo $REPO || echo "⚠️  Milestone 3 already exists"
        
        echo -e "${GREEN}✅ Milestones created!${NC}"
        ;;
        
    2)
        echo -e "${YELLOW}🏷️  Creating Labels...${NC}"
        echo ""
        
        # Priority
        gh label create "priority: critical" --color "B60205" --description "Blocker issues" --repo $REPO || true
        gh label create "priority: high" --color "D93F0B" --description "Important for milestone" --repo $REPO || true
        gh label create "priority: medium" --color "F9D0C4" --description "Standard priority" --repo $REPO || true
        gh label create "priority: low" --color "0E8A16" --description "Nice to have" --repo $REPO || true
        
        # Units
        gh label create "unit: project-ii" --color "5319E7" --description "Project II coordination" --repo $REPO || true
        gh label create "unit: interface-design" --color "5319E7" --description "Interface Design (60%)" --repo $REPO || true
        gh label create "unit: generative-ai" --color "5319E7" --description "Generative AI (50%)" --repo $REPO || true
        gh label create "unit: deep-learning" --color "5319E7" --description "Applied Deep Learning (50%)" --repo $REPO || true
        gh label create "unit: emerging-tech" --color "5319E7" --description "Emerging Technologies (50%)" --repo $REPO || true
        
        # Types
        gh label create "type: research" --color "0075CA" --description "Research tasks" --repo $REPO || true
        gh label create "type: development" --color "0075CA" --description "Development work" --repo $REPO || true
        gh label create "type: design" --color "0075CA" --description "Design work" --repo $REPO || true
        gh label create "type: documentation" --color "0075CA" --description "Documentation" --repo $REPO || true
        gh label create "type: testing" --color "0075CA" --description "Testing and QA" --repo $REPO || true
        gh label create "type: assets" --color "0075CA" --description "Asset creation/integration" --repo $REPO || true
        
        # Milestones
        gh label create "milestone-1" --color "D4C5F9" --description "Documentation (Feb 16)" --repo $REPO || true
        gh label create "milestone-2" --color "D4C5F9" --description "Prototype (Apr 12/13)" --repo $REPO || true
        gh label create "milestone-3" --color "D4C5F9" --description "Final Product (May 29/Jun 5)" --repo $REPO || true
        
        echo -e "${GREEN}✅ Labels created!${NC}"
        ;;
        
    3)
        echo -e "${YELLOW}📋 Creating Phase 1 Issues...${NC}"
        echo ""
        echo "Running Python script for Phase 1 issues..."
        python3 scripts/create_github_items.py
        ;;
        
    4)
        echo -e "${YELLOW}📋 Creating Phase 2 Issues...${NC}"
        echo ""
        echo "Note: Phase 2 issues require milestones to be created first."
        echo -n "Create milestones first? (y/n): "
        read -r create_milestones
        
        if [ "$create_milestones" = "y" ]; then
            echo "Creating milestones..."
            gh milestone create "Milestone 1: Documentation" --due-date 2026-02-16 --description "Presentation: Feb 16, 2026 | Weight: 15%" --repo $REPO || true
            gh milestone create "Milestone 2: Prototype" --due-date 2026-04-12 --description "Delivery: Apr 12 | Presentation: Apr 13 | Weight: 35%" --repo $REPO || true
            gh milestone create "Milestone 3: Final Product" --due-date 2026-05-29 --description "Delivery: May 29 | Presentation: Jun 5 | Weight: 50%" --repo $REPO || true
        fi
        
        echo "Running Python script for Phase 2 issues..."
        python3 scripts/create_github_items.py
        ;;
        
    5)
        echo -e "${YELLOW}🚀 Creating Everything...${NC}"
        echo ""
        python3 scripts/create_github_items.py
        ;;
        
    6)
        echo -e "${RED}❌ Cancelled${NC}"
        exit 0
        ;;
        
    *)
        echo -e "${RED}❌ Invalid option${NC}"
        exit 1
        ;;
esac

echo ""
echo "========================================================"
echo -e "${GREEN}✅ Done!${NC}"
echo "========================================================"
echo ""
echo "📬 View your issues:"
echo "   https://github.com/$REPO/issues"
echo ""
echo "📊 Add to Project Board:"
echo "   https://github.com/users/berlogabob/projects/7"
echo ""
echo "💡 Next steps:"
echo "   1. Go to your Project board"
echo "   2. Click 'Add items'"
echo "   3. Select the issues you just created"
echo "   4. Start working!"
echo ""
