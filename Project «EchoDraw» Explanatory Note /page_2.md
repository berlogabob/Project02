```markdown
# Module 3: Cross-Platform Wrapper on Flutter

This module provides a unified user interface for all system components (web and mobile versions).

## Development stages

1.  Basic application with plinter connection and G-code file sending.
2.  Integration of pattern generators and on-demand G-code generation.
3.  Implementation of layer and blending system.
4.  Addition of camera processing and filters.
5.  Full integration (real-time mode, ML, camera control).

## Module Interconnections and Integration into a Unified System

The modules have pronounced interdependence, forming a hierarchical structure:

*   *Module 1 acts as the execution mechanism, receiving G-code via WiFi/Socket(native Fluid3C support).*
*   *Module 2 generates content and provides intelligent interaction, forming commands for Module 1.*
*   *Module 1 integrates with the layer, integrating Module 2 (embelling P5-js canvas) and providing convenient access to Module 1.*

**Integration occurred phased: first file transfer → real-time stream → full synchronization (camera — ML — pattern — plotter).** The resulting system is an interactive installation where digital reality transformation immediately materializes in a physical drawing.

## Methodology and Approaches to Problem Solving

Development follows an incremental principle: each stage ends with a working prototype. Hardware modifications use 3D printing and standard components. The software part relies on open libraries (p5.js, mjs/Fluid3.C). Testing includes calibrations (steps/levels, servo angles), pen type comparison, and material feed mode validation.

## Approximate Work Schedule
*(Calculation for 6–8 months at 6 modules per week load)*

*   **Month 1**: Stages 1-3 of Module 1.
*   **Month 2**: Full Module 2 (including ML), + updates of Module 1.
*   **Month 3**: Conveyor system of Module 1.
*   **Month 4**: 7–8: Full Module 3 + final integration and testing.

## Budget Estimate
*(Overall limit — 500 €)*

| | Cost (€) |
| :--- | :--- |
| **Basic hardware:** | 120–150 € |
| *Upgrades (FSR, two-colour module)*: | 80 € |
| *Conveyor system:* | 150–200 € |
| *Reserve (materials, delivery):* | 50 € |
| **Total:** | **400–480 €** |
```