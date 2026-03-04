#!/bin/bash
# Create Phase 1 Issues with correct milestone names

REPO="berlogabob/Project02"

echo "Creating Phase 1 Issues..."
echo ""

# Issue 1
gh issue create \
  --title "#1 - Research Emergent Technologies" \
  --body "Investigate and select one emergent technology as reference for the experience.

## Deliverables
- Research emergent technologies for digital fashion
- Select one technology as project reference
- Document findings

## Acceptance Criteria
- [ ] Technology selected and justified
- [ ] Documentation added to wiki
- [ ] Presented to team

## Related Units
- Emerging Technologies (50%)

---
*Phase 1: Research and Concept Development (Weeks 1-3)*" \
  --label "type: research" \
  --label "unit: emerging-tech" \
  --label "milestone-1" \
  --label "priority: high" \
  --milestone "1st milestone: Documentation" \
  --repo $REPO && echo "✅ Created: #1" || echo "⚠️  Failed: #1"

# Issue 2
gh issue create \
  --title "#2 - Visual & Audio Reference Board" \
  --body "Collect references for style, image, color, sound for the experience.

## Deliverables
- Create mood board
- Collect visual references (style, color, imagery)
- Collect audio references (sound design, music)

## Acceptance Criteria
- [ ] Mood board created
- [ ] References documented
- [ ] Style guide established

## Related Units
- Interface Design and Interaction (60%)

---
*Phase 1: Research and Concept Development (Weeks 1-3)*" \
  --label "type: research" \
  --label "type: design" \
  --label "milestone-1" \
  --milestone "1st milestone: Documentation" \
  --repo $REPO && echo "✅ Created: #2" || echo "⚠️  Failed: #2"

# Issue 3
gh issue create \
  --title "#3 - User Flow Definition" \
  --body "Map user journey: interactions, outcomes, experience flow.

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
- Interface Design and Interaction (60%)

---
*Phase 1: Research and Concept Development (Weeks 1-3)*" \
  --label "type: design" \
  --label "type: documentation" \
  --label "milestone-1" \
  --milestone "1st milestone: Documentation" \
  --repo $REPO && echo "✅ Created: #3" || echo "⚠️  Failed: #3"

# Issue 4
gh issue create \
  --title "#4 - Topic Selection & Theoretical Framework" \
  --body "Define project topic with critical and theoretical support.

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
- [ ] References compiled

---
*Phase 1: Research and Concept Development (Weeks 1-3)*" \
  --label "type: research" \
  --label "type: documentation" \
  --label "milestone-1" \
  --label "priority: critical" \
  --milestone "1st milestone: Documentation" \
  --repo $REPO && echo "✅ Created: #4" || echo "⚠️  Failed: #4"

# Issue 5
gh issue create \
  --title "#5 - Weekly Activity Plan Creation" \
  --body "Create weekly plan contextualized by each supporting unit.

## Deliverables
- 14-week activity plan
- Unit-by-unit breakdown
- Milestone alignment

## Acceptance Criteria
- [ ] Plan created in timeline.md
- [ ] All units represented
- [ ] Milestones integrated

---
*Phase 1: Research and Concept Development (Weeks 1-3)*" \
  --label "type: documentation" \
  --label "milestone-1" \
  --label "priority: high" \
  --milestone "1st milestone: Documentation" \
  --repo $REPO && echo "✅ Created: #5" || echo "⚠️  Failed: #5"

# Issue 6
gh issue create \
  --title "#6 - Related Projects Research" \
  --body "Document existing projects in digital fashion/emergent tech space.

## Deliverables
- Research 5-10 related projects
- Analyze approaches and technologies
- Document findings

## Acceptance Criteria
- [ ] Research document created
- [ ] Competitive analysis complete
- [ ] Insights documented

---
*Phase 1: Research and Concept Development (Weeks 1-3)*" \
  --label "type: research" \
  --label "type: documentation" \
  --label "milestone-1" \
  --milestone "1st milestone: Documentation" \
  --repo $REPO && echo "✅ Created: #6" || echo "⚠️  Failed: #6"

# Issue 7
gh issue create \
  --title "#7 - Hardware & Framework Selection" \
  --body "Select appropriate hardware and define integration strategy.

## Deliverables
- Hardware requirements document
- Framework evaluation
- Integration strategy

## Acceptance Criteria
- [ ] Hardware selected
- [ ] Frameworks evaluated
- [ ] Integration strategy documented

## Related Units
- Emerging Technologies (50%)

---
*Phase 1: Research and Concept Development (Weeks 1-3)*" \
  --label "unit: emerging-tech" \
  --label "type: research" \
  --label "milestone-1" \
  --label "priority: high" \
  --milestone "1st milestone: Documentation" \
  --repo $REPO && echo "✅ Created: #7" || echo "⚠️  Failed: #7"

# Issue 8
gh issue create \
  --title "#8 - Milestone 1 Presentation Preparation" \
  --body "Prepare slides and production dossier for Feb 16 presentation.

## Deliverables
- Presentation slides
- Production dossier/report
- Weekly activity plan
- Research documentation

## Acceptance Criteria
- [ ] Slides completed
- [ ] Dossier submitted to Canvas
- [ ] Presentation rehearsed

## Deadline
- **Presentation:** Feb 16, 2026
- **Delivery:** Feb 16, 2026, 23:59:59 GMT

---
*Phase 1: Research and Concept Development (Weeks 1-3)*" \
  --label "milestone-1" \
  --label "type: documentation" \
  --label "priority: critical" \
  --milestone "1st milestone: Documentation" \
  --repo $REPO && echo "✅ Created: #8" || echo "⚠️  Failed: #8"

echo ""
echo "========================================================"
echo "✅ Phase 1 Issues Creation Complete!"
echo "========================================================"
echo ""
echo "View issues: https://github.com/$REPO/issues"
echo ""
