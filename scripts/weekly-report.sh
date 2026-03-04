#!/bin/bash
# Weekly Report Quick Start Script
# Generates and compiles a weekly report

set -e  # Exit on error

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo ""
echo "========================================================"
echo "📊 Weekly Report Generator"
echo "   The Oracle That Wears Us"
echo "========================================================"
echo ""

# Check prerequisites
if ! command -v gh &> /dev/null; then
    echo -e "${RED}❌ GitHub CLI (gh) not found!${NC}"
    echo "Install with: brew install gh"
    exit 1
fi

if ! command -v typst &> /dev/null; then
    echo -e "${RED}❌ Typst not found!${NC}"
    echo "Install with: brew install typst"
    echo "Or download from: https://github.com/typst/typst/releases"
    exit 1
fi

echo -e "${GREEN}✅${NC} GitHub CLI found"
echo -e "${GREEN}✅${NC} Typst found"
echo ""

# Get week number
echo -n "Enter week number (e.g., 1, 2, 3): "
read -r week_num

if [ -z "$week_num" ]; then
    echo -e "${RED}❌ Week number is required${NC}"
    exit 1
fi

# Get milestone
echo ""
echo "Select milestone:"
echo "1) 1st milestone: Documentation"
echo "2) 2nd milestone: Prototype"
echo "3) 3rd milestone: Final Product"
echo -n "Choose [1-3]: "
read -r milestone_choice

case $milestone_choice in
    1)
        milestone="1st milestone: Documentation"
        ;;
    2)
        milestone="2nd milestone: Prototype"
        ;;
    3)
        milestone="3rd milestone: Final Product"
        ;;
    *)
        echo -e "${RED}❌ Invalid choice${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${YELLOW}📝 Generating Week ${week_num} report...${NC}"
echo -e "   Milestone: ${milestone}"
echo ""

# Generate Typst report
python3 scripts/generate_weekly_report.py \
    --week "$week_num" \
    --milestone "$milestone" \
    --output "reports/week-$(printf "%02d" $week_num)-report.typ"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to generate report${NC}"
    exit 1
fi

echo ""
echo -e "${YELLOW}📄 Compiling to PDF...${NC}"

# Compile to PDF
typst compile "reports/week-$(printf "%02d" $week_num)-report.typ" \
              "reports/week-$(printf "%02d" $week_num)-report.pdf"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to compile PDF${NC}"
    exit 1
fi

echo ""
echo "========================================================"
echo -e "${GREEN}✅ Success!${NC}"
echo "========================================================"
echo ""
echo "📁 Generated files:"
echo "   - reports/week-$(printf "%02d" $week_num)-report.typ"
echo "   - reports/week-$(printf "%02d" $week_num)-report.pdf"
echo ""
echo "👁️  Preview PDF:"
echo "   open reports/week-$(printf "%02d" $week_num)-report.pdf"
echo ""
echo "👁️  Preview Typst (live reload):"
echo "   typst preview reports/week-$(printf "%02d" $week_num)-report.typ"
echo ""
echo "📊 Commit to git:"
echo "   git add reports/week-$(printf "%02d" $week_num)-report.*"
echo "   git commit -m '📊 Add weekly report: Week ${week_num}'"
echo "   git push"
echo ""
