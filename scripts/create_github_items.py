#!/usr/bin/env python3
"""
GitHub Project Automation Script
Creates milestones, labels, and issues for Project II (The Oracle That Wears Us)

Usage:
    python3 create_github_items.py

Requirements:
    - GitHub CLI (gh) installed: brew install gh
    - Authenticated: gh auth login
"""

import subprocess
import sys
from dataclasses import dataclass
from typing import List

# Configuration
REPO = "berlogabob/Project02"


@dataclass
class Milestone:
    title: str
    due_date: str
    description: str


@dataclass
class Label:
    name: str
    color: str
    description: str


@dataclass
class Issue:
    number: int
    title: str
    body: str
    labels: List[str]
    milestone: str


# ============================================================================
# DATA DEFINITIONS
# ============================================================================

MILESTONES = [
    Milestone(
        title="Milestone 1: Documentation",
        due_date="2026-02-16",
        description="Presentation: Feb 16, 2026 | Weight: 15%",
    ),
    Milestone(
        title="Milestone 2: Prototype",
        due_date="2026-04-12",
        description="Delivery: Apr 12 | Presentation: Apr 13 | Weight: 35%",
    ),
    Milestone(
        title="Milestone 3: Final Product",
        due_date="2026-05-29",
        description="Delivery: May 29 | Presentation: Jun 5 | Weight: 50%",
    ),
]

LABELS = [
    # Priority
    Label("priority: critical", "B60205", "Blocker issues"),
    Label("priority: high", "D93F0B", "Important for milestone"),
    Label("priority: medium", "F9D0C4", "Standard priority"),
    Label("priority: low", "0E8A16", "Nice to have"),
    # Units
    Label("unit: project-ii", "5319E7", "Project II coordination"),
    Label("unit: interface-design", "5319E7", "Interface Design (60%)"),
    Label("unit: generative-ai", "5319E7", "Generative AI (50%)"),
    Label("unit: deep-learning", "5319E7", "Applied Deep Learning (50%)"),
    Label("unit: emerging-tech", "5319E7", "Emerging Technologies (50%)"),
    # Types
    Label("type: research", "0075CA", "Research tasks"),
    Label("type: development", "0075CA", "Development work"),
    Label("type: design", "0075CA", "Design work"),
    Label("type: documentation", "0075CA", "Documentation"),
    Label("type: testing", "0075CA", "Testing and QA"),
    Label("type: assets", "0075CA", "Asset creation/integration"),
    # Milestones
    Label("milestone-1", "D4C5F9", "Documentation (Feb 16)"),
    Label("milestone-2", "D4C5F9", "Prototype (Apr 12/13)"),
    Label("milestone-3", "D4C5F9", "Final Product (May 29/Jun 5)"),
]

PHASE_1_ISSUES = [
    Issue(
        number=1,
        title="Research Emergent Technologies",
        body="""Investigate and select one emergent technology as reference for the experience.

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
*Phase 1: Research and Concept Development (Weeks 1-3)*""",
        labels=[
            "type: research",
            "unit: emerging-tech",
            "milestone-1",
            "priority: high",
        ],
        milestone="Milestone 1: Documentation",
    ),
    Issue(
        number=2,
        title="Visual & Audio Reference Board",
        body="""Collect references for style, image, color, sound for the experience.

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
*Phase 1: Research and Concept Development (Weeks 1-3)*""",
        labels=["type: research", "type: design", "milestone-1"],
        milestone="Milestone 1: Documentation",
    ),
    Issue(
        number=3,
        title="User Flow Definition",
        body="""Map user journey: interactions, outcomes, experience flow.

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
*Phase 1: Research and Concept Development (Weeks 1-3)*""",
        labels=["type: design", "type: documentation", "milestone-1"],
        milestone="Milestone 1: Documentation",
    ),
    Issue(
        number=4,
        title="Topic Selection & Theoretical Framework",
        body="""Define project topic with critical and theoretical support.

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
*Phase 1: Research and Concept Development (Weeks 1-3)*""",
        labels=[
            "type: research",
            "type: documentation",
            "milestone-1",
            "priority: critical",
        ],
        milestone="Milestone 1: Documentation",
    ),
    Issue(
        number=5,
        title="Weekly Activity Plan Creation",
        body="""Create weekly plan contextualized by each supporting unit.

## Deliverables
- 14-week activity plan
- Unit-by-unit breakdown
- Milestone alignment

## Acceptance Criteria
- [ ] Plan created in timeline.md
- [ ] All units represented
- [ ] Milestones integrated

---
*Phase 1: Research and Concept Development (Weeks 1-3)*""",
        labels=["type: documentation", "milestone-1", "priority: high"],
        milestone="Milestone 1: Documentation",
    ),
    Issue(
        number=6,
        title="Related Projects Research",
        body="""Document existing projects in digital fashion/emergent tech space.

## Deliverables
- Research 5-10 related projects
- Analyze approaches and technologies
- Document findings

## Acceptance Criteria
- [ ] Research document created
- [ ] Competitive analysis complete
- [ ] Insights documented

---
*Phase 1: Research and Concept Development (Weeks 1-3)*""",
        labels=["type: research", "type: documentation", "milestone-1"],
        milestone="Milestone 1: Documentation",
    ),
    Issue(
        number=7,
        title="Hardware & Framework Selection",
        body="""Select appropriate hardware and define integration strategy.

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
*Phase 1: Research and Concept Development (Weeks 1-3)*""",
        labels=[
            "unit: emerging-tech",
            "type: research",
            "milestone-1",
            "priority: high",
        ],
        milestone="Milestone 1: Documentation",
    ),
    Issue(
        number=8,
        title="Milestone 1 Presentation Preparation",
        body="""Prepare slides and production dossier for Feb 16 presentation.

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
*Phase 1: Research and Concept Development (Weeks 1-3)*""",
        labels=["milestone-1", "type: documentation", "priority: critical"],
        milestone="Milestone 1: Documentation",
    ),
]

PHASE_2_ISSUES = [
    Issue(
        number=9,
        title="Task Breakdown & Problem Identification",
        body="""List all tasks required to complete a functional project; identify potential problems and necessities.

## Deliverables
- Complete task list
- Risk assessment
- Resource requirements

## Acceptance Criteria
- [ ] All tasks identified
- [ ] Risks documented
- [ ] Resources listed

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["type: documentation", "milestone-2", "priority: high"],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=10,
        title="Unity Project Setup",
        body="""Initialize Unity project with proper structure and version control.

## Deliverables
- Unity project initialized
- Folder structure created
- Git configuration for Unity

## Acceptance Criteria
- [ ] Unity project created
- [ ] Standard folders organized
- [ ] .gitignore configured for Unity

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["type: development", "milestone-2"],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=11,
        title="TouchDesigner Integration Setup",
        body="""Configure TouchDesigner as core tool for real-time generative behaviours.

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
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=[
            "type: development",
            "unit: generative-ai",
            "unit: deep-learning",
            "milestone-2",
            "priority: high",
        ],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=12,
        title="Generative AI Pipeline Development",
        body="""Build prompt engineering pipelines for content generation and task execution.

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
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["type: development", "unit: generative-ai", "milestone-2"],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=13,
        title="Agentic AI Loop Implementation",
        body="""Develop initial agentic workflow for autonomous task execution.

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
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["type: development", "unit: generative-ai", "milestone-2"],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=14,
        title="Deep Learning Model Selection & Dataset Prep",
        body="""Choose model architecture and prepare training dataset.

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
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=[
            "type: development",
            "unit: deep-learning",
            "milestone-2",
            "priority: high",
        ],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=15,
        title="Model Training/Fine-tuning",
        body="""Train or fine-tune selected model; document parameters and process.

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
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["type: development", "unit: deep-learning", "milestone-2"],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=16,
        title="Latent Space Experiments",
        body="""Experiment with latent space manipulation for creative outputs.

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
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=[
            "type: development",
            "type: research",
            "unit: deep-learning",
            "milestone-2",
        ],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=17,
        title="Sensor-Based Interaction Implementation",
        body="""Implement body tracking, gesture recognition, or AR features.

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
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["type: development", "unit: emerging-tech", "milestone-2"],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=18,
        title="VR/AR Interaction Design",
        body="""Design and implement VR/AR interactions (hand tracking, eye tracking, haptic feedback).

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
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=[
            "type: development",
            "type: design",
            "unit: emerging-tech",
            "unit: interface-design",
            "milestone-2",
        ],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=19,
        title="Graphical Assets Integration",
        body="""Integrate original or legally obtained graphical assets.

## Deliverables
- Graphical assets
- Asset documentation
- License verification

## Acceptance Criteria
- [ ] Assets integrated
- [ ] Sources documented
- [ ] Licenses verified

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["type: assets", "type: design", "milestone-2"],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=20,
        title="Audio Assets Integration",
        body="""Integrate original or legally obtained audio assets.

## Deliverables
- Audio assets
- Asset documentation
- License verification

## Acceptance Criteria
- [ ] Audio integrated
- [ ] Sources documented
- [ ] Licenses verified

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["type: assets", "type: design", "milestone-2"],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=21,
        title="Core Functionality Prototype",
        body="""Develop functional prototype demonstrating core features.

## Deliverables
- Functional prototype
- Core features working
- Demo video

## Acceptance Criteria
- [ ] Prototype functional
- [ ] Core features working
- [ ] Demo recorded

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["type: development", "milestone-2", "priority: critical"],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=22,
        title="Milestone 2 Documentation",
        body="""Update production dossier with implementation reports from all units.

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
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["milestone-2", "type: documentation", "priority: critical"],
        milestone="Milestone 2: Prototype",
    ),
    Issue(
        number=23,
        title="Milestone 2 Presentation Preparation",
        body="""Prepare slides for April 13 presentation.

## Deliverables
- Presentation slides
- Live demo preparation
- Rehearsal

## Deadline
- **Presentation:** Apr 13, 2026

---
*Phase 2: Prototyping and Technical Exploration (Weeks 3-7)*""",
        labels=["milestone-2", "type: documentation", "priority: critical"],
        milestone="Milestone 2: Prototype",
    ),
]

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================


def run_command(cmd: List[str], check: bool = False) -> tuple:
    """Run a shell command and return (success, output)"""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=check)
        return (result.returncode == 0, result.stdout.strip(), result.stderr.strip())
    except subprocess.CalledProcessError as e:
        return (False, "", str(e))


def check_gh_installed() -> bool:
    """Check if GitHub CLI is installed"""
    success, output, _ = run_command(["gh", "--version"])
    return success


def check_gh_authenticated() -> bool:
    """Check if GitHub CLI is authenticated"""
    success, _, _ = run_command(["gh", "auth", "status"])
    return success


def create_milestone(milestone: Milestone) -> bool:
    """Create a single milestone"""
    cmd = [
        "gh",
        "milestone",
        "create",
        milestone.title,
        "--due-date",
        milestone.due_date,
        "--description",
        milestone.description,
        "--repo",
        REPO,
    ]
    success, output, error = run_command(cmd)
    return success


def create_label(label: Label) -> bool:
    """Create a single label"""
    cmd = [
        "gh",
        "label",
        "create",
        label.name,
        "--color",
        label.color,
        "--description",
        label.description,
        "--repo",
        REPO,
    ]
    success, output, error = run_command(cmd)
    return success


def create_issue(issue: Issue) -> bool:
    """Create a single issue"""
    labels_flat = ",".join(issue.labels)
    cmd = [
        "gh",
        "issue",
        "create",
        "--title",
        f"#{issue.number} - {issue.title}",
        "--body",
        issue.body,
        "--label",
        labels_flat,
        "--milestone",
        issue.milestone,
        "--repo",
        REPO,
    ]
    success, output, error = run_command(cmd)
    return success


# ============================================================================
# MAIN FUNCTIONS
# ============================================================================


def create_milestones() -> int:
    """Create all milestones"""
    print("\n🎯 Creating Milestones...")
    print("=" * 60)

    created = 0
    for m in MILESTONES:
        success = create_milestone(m)
        if success:
            print(f"✅ Created: {m.title}")
            created += 1
        else:
            print(f"⚠️  Already exists or failed: {m.title}")

    print(f"\nMilestones created: {created}/{len(MILESTONES)}")
    return created


def create_labels() -> int:
    """Create all labels"""
    print("\n🏷️  Creating Labels...")
    print("=" * 60)

    created = 0
    for label in LABELS:
        success = create_label(label)
        if success:
            print(f"✅ Created: {label.name} (#{label.color})")
            created += 1
        else:
            print(f"⚠️  Already exists or failed: {label.name}")

    print(f"\nLabels created: {created}/{len(LABELS)}")
    return created


def create_issues(issues: List[Issue], phase_name: str) -> int:
    """Create issues for a phase"""
    print(f"\n📋 Creating {phase_name} Issues...")
    print("=" * 60)

    created = 0
    for issue in issues:
        success = create_issue(issue)
        if success:
            print(f"✅ Created: #{issue.number} - {issue.title}")
            created += 1
        else:
            print(f"⚠️  Already exists or failed: #{issue.number} - {issue.title}")

    print(f"\nIssues created: {created}/{len(issues)}")
    return created


def main():
    """Main function"""
    print("\n" + "=" * 60)
    print("🚀 GitHub Project Automation - The Oracle That Wears Us")
    print("   Project II (MCCIA)")
    print("=" * 60)

    # Check prerequisites
    print("\n📋 Checking prerequisites...")

    if not check_gh_installed():
        print("❌ GitHub CLI not found!")
        print("\nInstall with:")
        print("   brew install gh")
        sys.exit(1)

    print("✅ GitHub CLI installed")

    if not check_gh_authenticated():
        print("❌ GitHub CLI not authenticated!")
        print("\nAuthenticate with:")
        print("   gh auth login")
        sys.exit(1)

    print("✅ GitHub CLI authenticated")
    print(f"📦 Repository: {REPO}")

    # Confirm
    print("\n" + "=" * 60)
    print("This will create:")
    print(f"  - {len(MILESTONES)} milestones")
    print(f"  - {len(LABELS)} labels")
    print(f"  - {len(PHASE_1_ISSUES)} Phase 1 issues")
    print(f"  - {len(PHASE_2_ISSUES)} Phase 2 issues")
    print("=" * 60)

    confirm = input("\nProceed with creation? (y/n): ")
    if confirm.lower() != "y":
        print("\n❌ Cancelled by user.")
        sys.exit(0)

    # Create items
    total_created = 0

    total_created += create_milestones()
    total_created += create_labels()
    total_created += create_issues(PHASE_1_ISSUES, "Phase 1")
    total_created += create_issues(PHASE_2_ISSUES, "Phase 2")

    # Summary
    print("\n" + "=" * 60)
    print("✅ Setup Complete!")
    print("=" * 60)
    print(f"\nTotal items created: {total_created}")
    print("\n📬 Check your project at:")
    print(f"   https://github.com/{REPO}/issues")
    print(f"   https://github.com/users/berlogabob/projects/7")
    print("\n💡 Next steps:")
    print("   1. Add issues to your Project board")
    print("   2. Assign team members")
    print("   3. Start working on Phase 1!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
