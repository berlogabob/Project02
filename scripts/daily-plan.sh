#!/bin/bash
# Daily Plan Quick Start Script
# Generates daily plans for all team members or specific member

set -e  # Exit on error

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo ""
echo "========================================================"
echo "📅 Daily Plan Generator"
echo "   The Oracle That Wears Us"
echo "========================================================"
echo ""

# Check prerequisites
if ! command -v typst &> /dev/null; then
    echo -e "${RED}❌ Typst not found!${NC}"
    echo "Install with: brew install typst"
    exit 1
fi

if ! command -v gh &> /dev/null; then
    echo -e "${RED}❌ GitHub CLI (gh) not found!${NC}"
    echo "Install with: brew install gh"
    exit 1
fi

echo -e "${GREEN}✅${NC} Typst found"
echo -e "${GREEN}✅${NC} GitHub CLI found"
echo ""

# Get generation mode
echo "Generate plans for:"
echo "1) All team members"
echo "2) Specific member"
echo -n "Choose [1-2]: "
read -r choice

case $choice in
    1)
        echo ""
        echo -e "${YELLOW}📋 Generating plans for all team members...${NC}"
        python3 scripts/generate_daily_plan.py --all-members --output-dir reports/daily-plans
        ;;
    2)
        echo ""
        echo "Select team member:"
        echo "1) Nadine Allan (@naydino)"
        echo "2) Andrey Dyakov (@berlogabob)"
        echo "3) Dmitri Kazantsev (@electricianv001)"
        echo -n "Choose [1-3]: "
        read -r member_choice
        
        case $member_choice in
            1)
                member="naydino"
                name="Nadine Allan"
                ;;
            2)
                member="berlogabob"
                name="Andrey Dyakov"
                ;;
            3)
                member="electricianv001"
                name="Dmitri Kazantsev"
                ;;
            *)
                echo -e "${RED}❌ Invalid choice${NC}"
                exit 1
                ;;
        esac
        
        echo ""
        echo -e "${YELLOW}📋 Generating plan for ${name}...${NC}"
        python3 scripts/generate_daily_plan.py \
            --member "$member" \
            --output "reports/daily-plan-${member}.typ"
        ;;
    *)
        echo -e "${RED}❌ Invalid choice${NC}"
        exit 1
        ;;
esac

echo ""
echo "========================================================"
echo -e "${GREEN}✅ Success!${NC}"
echo "========================================================"
echo ""
echo "📁 Generated files:"
if [ "$choice" = "1" ]; then
    ls -la reports/daily-plans/*.pdf 2>/dev/null || echo "   (check reports/daily-plans/)"
else
    echo "   - reports/daily-plan-${member}.typ"
    echo "   - reports/daily-plan-${member}.pdf"
fi
echo ""
echo "👁️  Preview PDF:"
if [ "$choice" = "1" ]; then
    echo "   open reports/daily-plans/daily-plan-*.pdf"
else
    echo "   open reports/daily-plan-${member}.pdf"
fi
echo ""
echo "📊 Commit to git:"
echo "   git add reports/daily-plans/"
echo "   git commit -m '📅 Add daily plans for $(date +%Y-%m-%d)'"
echo "   git push"
echo ""
