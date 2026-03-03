**Project Explanatory Note**

<<EcoCholar: Interactive Generative Planner with Real-time Video Processing and Machine Learning>>

**Author:** Andrey Dyakov
**Date:** January 6, 2026

This Project involves a development of an interactive physical computing system based on converting the NEJMaster 2 Plus laser engraver (working area $252 \times 452$ mm, N40500 laser module) into a multifunctional XY-robotics press as the tool. The system enables basic machine interaction via the machine with a web camera: image capture, detection of gestures, poses, faces, and generation and modification of abstract patterns -- transmission of control commands in G-code format -- physical drawing with surface adaptation and support for continuous material feed.

The project is structured around three interconnected modules (eachs), each from an active rotary encoder, allowing them to output a unique feedback signal to the robot system. This modular approach facilitates systematic functionality buildup, risk minimization, and the ability to demonstrate intermediate results. The focus developments on accessible technologies (ESP32-compatible controllers, browser-based libraries pjs.js and mids.js, cross-platform development with Futter), making the project reproducible and suitable for educational purposes.

**Description of the Three Main Project Modules**

**Module 1: Hardware Component on psjs.js and mids.js**
The system focuses on basic step file (stepsize, speeds), firmware flashing and configuration of the basic real-time chip (stepsize, speeds).

**Development Stages:**
*   *Development:* A single-point printing head (servo mechanism for lifting/flattening, G-code testing).
*   *Module 2 Integration of a load sensor (FSR) or load cell with HX7197 adapter for curved surfaces*: The project is structured around three steps, which include a step follower robot as a 'returner' mechanism (servo, three positions: neutral - 36°, ±45°; lowering one of the columns).
*   *Module 3 – Combined module (two-cor> + load sensor), 7-10. Material mechanics system*: Variant A. Closed conveyor belt (infinite feed, infinite capacity, endless capability; 2-step/step servo motors; step/continuous scroll modes); Variant B: Roll belt (rinning mode; step/continuous speed modes; optional semi-automatic shelter or cutter integration).

**Development stages:**
*   *Module 1 Implementation:* 1. Implementation of a generator for simple geometric patterns with a single continuous line.
*   *Construction of a layer overlay system (combination material generation, bridging digital reality digitalization to printer controls command)*: Testing uses various points (ballpoints and capillary).