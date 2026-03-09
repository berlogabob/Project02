# GitHub Issues Hierarchy

## 🌲 Project Structure

### #57 Plotter (Hardware/FluidNC Project)
**11 Phase tasks → 72 individual tasks**

```
#57 Plotter
├── #61 📸 Machine Documentation Phase (Week 2)
│   ├── #72-77 Photo tasks (6)
├── #62 🔧 Hardware Disassembly Phase (Week 2)
│   ├── #78-92 Label/Disconnect tasks (15)
├── #63 ✅ System Verification Phase (Week 2)
│   ├── #93-100 Test tasks (8)
├── #64 📏 Measurement Phase (Week 2)
│   ├── #101-104 Measure tasks (4)
├── #65 📚 FluidNC Research Phase (Week 2)
│   ├── #105-108 Research tasks (4)
├── #66 ⚙️ FluidNC Configuration Phase (Week 2)
│   ├── #109-116 Config tasks (8)
├── #67 🔌 Board Installation Phase (Week 3)
│   ├── #117-123 Install tasks (7)
├── #68 🧪 Initial Testing Phase (Week 3)
│   ├── #124-127 Test tasks (4)
├── #69 📐 Calibration Phase (Week 3)
│   ├── #128-135 Calibration tasks (8)
├── #70 🎯 Fine Tuning Phase (Week 4)
│   ├── #136-142 Fine-tuning tasks (7)
└── #71 📊 Stabilization Phase (Week 4)
    ├── #143-147 Stabilization tasks (5)
```

---

### #58 Environmental Projection (Unity/TD Project)
**19 sub-issues (Milestone 2)**

```
#58 Environmental Projection Prototype (Unity)
├── #30  #9 - Task Breakdown & Problem Identification
├── #31  #10 - Unity Project Setup
├── #32  #11 - TouchDesigner Integration Setup
├── #33  #12 - Generative AI Pipeline Development
├── #34  #13 - Agentic AI Loop Implementation
├── #35  #14 - Deep Learning Model Selection & Dataset Prep
├── #36  #15 - Model Training/Fine-tuning
├── #37  #16 - Latent Space Experiments
├── #38  #17 - Sensor-Based Interaction Implementation
├── #39  #18 - VR/AR Interaction Design
├── #40  #19 - Graphical Assets Integration
├── #41  #20 - Audio Assets Integration
├── #42  #21 - Core Functionality Prototype
├── #43  #22 - Milestone 2 Documentation
├── #44  #23 - Milestone 2 Presentation Preparation
├── #48  Test and compare speech to text models inside of TD
├── #56  Oracle output based on user interaction
├── #148 System Architecture & Data Flow Definition
└── #149 Future Hardware / IoT Integration Strategy
```

---

## 📊 Statistics

| Project | Root Issue | Phase Tasks | Individual Tasks | Total |
|---------|-----------|-------------|------------------|-------|
| Plotter | #57 | 11 | 72 | 83 |
| Environmental Projection | #58 | 0 | 19 | 19 |
| **TOTAL** | | **11** | **91** | **102** |

---

## 🔧 Tools Used

- **Extension:** `gh sub-issue` (agbiotech/gh-sub-issue)
- **Installation:** `gh extension install agbiotech/gh-sub-issue`

---

## 📝 Commands

```bash
# View sub-issues
gh sub-issue list <parent-number>

# Link issues
gh sub-issue add <parent> --sub-issue-number <child>

# Remove link
gh sub-issue remove <parent> --sub-issue-number <child>
```

---

## ✅ Status

- ✅ All active Week 2-4 issues linked
- ✅ Week 1 completed issues remain historical (no linking needed)
- ✅ Two main project roots established
