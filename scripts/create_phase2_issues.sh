#!/bin/bash
# Create Phase 2 Issues with correct milestone names

REPO="berlogabob/Project02"

echo "Creating Phase 2 Issues..."
echo ""

# Issue 9
gh issue create \
  --title "#9 - Task Breakdown & Problem Identification" \
  --body "List all tasks required to complete a functional project; identify potential problems and necessities.

## Deliverables
- Complete task list
- Risk assessment
- Resource requirements

## Acceptance Criteria
- [ ] All tasks identified
- [ ] Risks documented
- [ ] Resources listed

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: documentation" \
  --label "milestone-2" \
  --label "priority: high" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #9" || echo "⚠️  Failed: #9"

# Issue 10
gh issue create \
  --title "#10 - Unity Project Setup" \
  --body "Initialize Unity project with proper structure and version control.

## Deliverables
- Unity project initialized
- Folder structure created
- Git configuration for Unity

## Acceptance Criteria
- [ ] Unity project created
- [ ] Standard folders organized
- [ ] .gitignore configured for Unity

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: development" \
  --label "milestone-2" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #10" || echo "⚠️  Failed: #10"

# Issue 11
gh issue create \
  --title "#11 - TouchDesigner Integration Setup" \
  --body "Configure TouchDesigner as core tool for real-time generative behaviours.

## Deliverables
- TouchDesigner project structure
- Unity-TouchDesigner communication
- Basic generative patch

## Acceptance Criteria
- [ ] TouchDesigner project created
- [ ] Communication with Unity established
- [ ] Basic patch functional

## Related Units
- Generative AI (50%)
- Applied Deep Learning (50%)

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: development" \
  --label "unit: generative-ai" \
  --label "unit: deep-learning" \
  --label "milestone-2" \
  --label "priority: high" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #11" || echo "⚠️  Failed: #11"

# Issue 12
gh issue create \
  --title "#12 - Generative AI Pipeline Development" \
  --body "Build prompt engineering pipelines for content generation and task execution.

## Deliverables
- Prompt templates
- Content generation pipeline
- Task execution workflow

## Acceptance Criteria
- [ ] Prompts engineered
- [ ] Pipeline functional
- [ ] Content generated

## Related Units
- Generative AI (50%)

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: development" \
  --label "unit: generative-ai" \
  --label "milestone-2" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #12" || echo "⚠️  Failed: #12"

# Issue 13
gh issue create \
  --title "#13 - Agentic AI Loop Implementation" \
  --body "Develop initial agentic workflow for autonomous task execution.

## Deliverables
- Agentic loop architecture
- Autonomous task execution
- Safety constraints

## Acceptance Criteria
- [ ] Agentic loop designed
- [ ] Autonomous execution working
- [ ] Safety checks implemented

## Related Units
- Generative AI (50%)

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: development" \
  --label "unit: generative-ai" \
  --label "milestone-2" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #13" || echo "⚠️  Failed: #13"

# Issue 14
gh issue create \
  --title "#14 - Deep Learning Model Selection & Dataset Prep" \
  --body "Choose model architecture and prepare training dataset.

## Deliverables
- Model selection document
- Dataset collected and prepared
- Training configuration

## Acceptance Criteria
- [ ] Model architecture selected (VAE/GAN/diffusion/embedding)
- [ ] Dataset prepared
- [ ] Training config defined

## Related Units
- Applied Deep Learning (50%)

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: development" \
  --label "unit: deep-learning" \
  --label "milestone-2" \
  --label "priority: high" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #14" || echo "⚠️  Failed: #14"

# Issue 15
gh issue create \
  --title "#15 - Model Training/Fine-tuning" \
  --body "Train or fine-tune selected model; document parameters and process.

## Deliverables
- Trained/fine-tuned model
- Training logs
- Parameter documentation

## Acceptance Criteria
- [ ] Model trained
- [ ] Results evaluated
- [ ] Process documented

## Related Units
- Applied Deep Learning (50%)

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: development" \
  --label "unit: deep-learning" \
  --label "milestone-2" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #15" || echo "⚠️  Failed: #15"

# Issue 16
gh issue create \
  --title "#16 - Latent Space Experiments" \
  --body "Experiment with latent space manipulation for creative outputs.

## Deliverables
- Latent space exploration
- Creative output samples
- Experiment documentation

## Acceptance Criteria
- [ ] Experiments conducted
- [ ] Creative outputs generated
- [ ] Results documented

## Related Units
- Applied Deep Learning (50%)

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: development" \
  --label "type: research" \
  --label "unit: deep-learning" \
  --label "milestone-2" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #16" || echo "⚠️  Failed: #16"

# Issue 17
gh issue create \
  --title "#17 - Sensor-Based Interaction Implementation" \
  --body "Implement body tracking, gesture recognition, or AR features.

## Deliverables
- Sensor integration
- Interaction mapping
- Testing documentation

## Acceptance Criteria
- [ ] Sensors integrated
- [ ] Interactions mapped
- [ ] Testing complete

## Related Units
- Emerging Technologies (50%)

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: development" \
  --label "unit: emerging-tech" \
  --label "milestone-2" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #17" || echo "⚠️  Failed: #17"

# Issue 18
gh issue create \
  --title "#18 - VR/AR Interaction Design" \
  --body "Design and implement VR/AR interactions (hand tracking, eye tracking, haptic feedback).

## Deliverables
- VR/AR interaction design
- Implementation
- Usability testing

## Acceptance Criteria
- [ ] Interactions designed
- [ ] Implementation complete
- [ ] Tested for usability

## Related Units
- Emerging Technologies (50%)
- Interface Design and Interaction (60%)

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: development" \
  --label "type: design" \
  --label "unit: emerging-tech" \
  --label "unit: interface-design" \
  --label "milestone-2" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #18" || echo "⚠️  Failed: #18"

# Issue 19
gh issue create \
  --title "#19 - Graphical Assets Integration" \
  --body "Integrate original or legally obtained graphical assets.

## Deliverables
- Graphical assets
- Asset documentation
- License verification

## Acceptance Criteria
- [ ] Assets integrated
- [ ] Sources documented
- [ ] Licenses verified

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: assets" \
  --label "type: design" \
  --label "milestone-2" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #19" || echo "⚠️  Failed: #19"

# Issue 20
gh issue create \
  --title "#20 - Audio Assets Integration" \
  --body "Integrate original or legally obtained audio assets.

## Deliverables
- Audio assets
- Asset documentation
- License verification

## Acceptance Criteria
- [ ] Audio integrated
- [ ] Sources documented
- [ ] Licenses verified

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: assets" \
  --label "type: design" \
  --label "milestone-2" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #20" || echo "⚠️  Failed: #20"

# Issue 21
gh issue create \
  --title "#21 - Core Functionality Prototype" \
  --body "Develop functional prototype demonstrating core features.

## Deliverables
- Functional prototype
- Core features working
- Demo video

## Acceptance Criteria
- [ ] Prototype functional
- [ ] Core features working
- [ ] Demo recorded

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "type: development" \
  --label "milestone-2" \
  --label "priority: critical" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #21" || echo "⚠️  Failed: #21"

# Issue 22
gh issue create \
  --title "#22 - Milestone 2 Documentation" \
  --body "Update production dossier with implementation reports from all units.

## Deliverables
- Updated production dossier
- Implementation reports:
  - Emerging Technologies: Sensor-based interactions
  - Applied Deep Learning: Model training/fine-tuning
  - Generative AI: Prompt engineering pipelines
- Activity plan execution record
- Workload distribution

## Deadline
- **Delivery:** Apr 12, 2026, 23:59:59 GMT
- **Presentation:** Apr 13, 2026

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "milestone-2" \
  --label "type: documentation" \
  --label "priority: critical" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #22" || echo "⚠️  Failed: #22"

# Issue 23
gh issue create \
  --title "#23 - Milestone 2 Presentation Preparation" \
  --body "Prepare slides for April 13 presentation.

## Deliverables
- Presentation slides
- Live demo preparation
- Rehearsal

## Deadline
- **Presentation:** Apr 13, 2026

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*" \
  --label "milestone-2" \
  --label "type: documentation" \
  --label "priority: critical" \
  --milestone "2nd milestone: Prototype" \
  --repo $REPO && echo "✅ Created: #23" || echo "⚠️  Failed: #23"

echo ""
echo "========================================================"
echo "✅ Phase 2 Issues Creation Complete!"
echo "========================================================"
echo ""
echo "View issues: https://github.com/$REPO/issues"
echo ""
