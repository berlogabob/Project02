# Project02

## Project II - Interactive Exhibition Timeline

**Mermaid Gantt Chart for README.md**  
**Semester:** 2025-2026 / 2nd Semester  
**Program:** Master's in Creative Computing and Artificial Intelligence (M-CCIA)

```mermaid
gantt
    title Project II Interactive Exhibition Timeline
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    excludes    weekends

    section Phase 1: Research & Concept
    Briefing Presentation                :done,    des1, 2026-02-02, 1d
    Group Formation                     :active,  des2, after des1, 2d
    Technology Research                 :         des3, after des2, 5d

    section Phase 2: Prototyping
    Moodboard & Concept Doc              :milestone,m1, 2026-02-16, 0d
    Sensor Integration Design           :         dev1, after m1, 7d
    AI Model Selection                  :         dev2, after dev1, 5d
    Visual Asset Production             :         dev3, after dev2, 7d
    Prototype Development               :crit,    dev4, after dev3, 10d

    section Phase 3: Refinement
    User Testing Iteration 1            :         dev5, after dev4, 3d
    Performance Optimization            :         dev6, after dev5, 5d
    Accessibility Review                :         dev7, after dev6, 3d
    Content Polish                      :         dev8, after dev7, 4d

    section Phase 4: Finalization
    Integration Testing                 :crit,    dev9, after dev8, 7d
    Final Production Dossier            :milestone,m2, 2026-05-29, 0d
    Exhibition Setup                    :         dev10, after m2, 5d
    Final Presentation                  :milestone,m3, 2026-06-05, 0d

    section Milestones
    Documentation (MCCA)                :milestone,M1, 2026-02-16, 0d
    Prototype (MCCA)                   :milestone,M2, 2025-04-13, 0d
    Final Product (MCCIA)              :milestone,M3, 2026-05-29, 0d
```

---

## Alternative Gantt Chart View

```mermaid
gantt
    title Project II - Simplified Timeline
    dateFormat  YYYY-MM-DD
    axisFormat  %d/%m

    section Phase 1
    Briefing & Formation                :done, p1, Feb 2-9

    section Phase 2 
    Technical Implementation            :active, p2, after p1
    Prototype Development               :crit, p3, after p2

    section Phase 3
    User Testing & Refinement           :p4, after p3

    section Phase 4
    Final Polish & Exhibition Setup     :crit, p5, after p4
```

---

## Timeline Summary

| Phase | Duration | Key Milestones |
|--------|-------|--------|
| **Phase 1: Research** | Feb 2-9 | Briefing, Team formation, Technology selection |
| **Phase 2: Prototyping** | Feb 9 - Mar 30 | Documentation (MCCA), Technical implementation |
| **Phase 3: Refinement** | Apr 1 - May 5 | User testing, Accessibility compliance |
| **Phase 4: Finalization** | May 6-29 | Integration testing, Final dossier, Exhibition setup |

---

## Critical Path Analysis

```
Critical Milestones (Red):
├── Documentation (MCCA): Feb 16 → 15% of grade
├── Prototype (MCCA): Apr/May 2026 → 35% of grade
└── Final Product (MCCIA): May 29 → 50% of grade

Dependencies:
    Research → Prototyping → Refinement → Exhibition Setup → Final Presentation
```

---

*Note: Date discrepancies in original brief require verification with course coordinator.
