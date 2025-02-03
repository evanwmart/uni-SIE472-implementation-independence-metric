# Implementation Independence in Layered Architectures (IILA)

## Description

This project was developed under the **INSuRE (Information Security and Research) Program** in collaboration with the **National Security Agency (NSA)**. It provides a **metric-based approach** for assessing “implementation independence” across layered architectures—especially relevant to IoT and other security-critical systems. By examining common vulnerabilities and repeated technical underpinnings, the framework helps determine how likely it is that **one exploit** can compromise multiple layers in a system.

---

## Table of Contents

- [Description](#description)
- [Contents](#contents)
- [Features](#features)
- [Technology](#technology)
- [Lessons](#lessons)
- [Overview / Retrospective](#overview--retrospective)
- [Contributors](#contributors)
- [A Note on Academic Integrity](#a-note-on-academic-integrity)

---

## Contents

- **`main.py`**  
  Launches the Tkinter-based **GUI**, coordinates the metric calculation, and orchestrates file output (PDF/CSV).  

- **`guiFunctions.py`**  
  Encapsulates the **GUI building** logic—widgets, layout, color schemes, etc.  

- **`backendApis.py`**  
  Retrieves vulnerabilities from the **NVD CVE database**. Implements parsing, filtering, and date-based queries.  

- **`example.pdf`**  
  A sample PDF illustrating a sample output from the tool.

- **`__pycache__/`**  
  Auto-generated folder for Python bytecode.

**To Run the Tool**  
1. Clone this repo.  
2. (Optionally) create a Python virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   ```  
3. Install dependencies (if a requirements.txt is provided):  
   ```bash
   pip install -r requirements.txt
   ```  
4. Launch:  
   ```bash
   python main.py
   ```  
5. Within the GUI:  
   - **Add** layer names.  
   - **Select** hardware, software, security, network, and data management components per layer.  
   - **Generate** the results: a Uniqueness Score per component and an overall Diversity Score for the system.  
   - **Optionally** gather CVEs for specific keywords or date ranges and export a PDF summary.

---

## Features

1. **Layered Architecture Analysis**  
   - Flexible setup for labeling or categorizing components by layer (e.g., “Perception,” “Transport,” “Processing,” “Application”).  

2. **Uniqueness & Diversity Scores**  
   - Each component type is assigned a **Uniqueness Score** (0–1).  
   - The final **Diversity Score** aggregates these scores, indicating how robust or “independent” the overall design is.  

3. **CVE-Based Security Insights**  
   - Queries the NIST National Vulnerability Database (NVD) for relevant vulnerabilities based on chosen components or keywords.  

4. **PDF Report Generation**  
   - Allows offline review, distribution, or record-keeping of your analysis results.  

5. **Extensible**  
   - Though demonstrated on IoT-inspired examples, it can generalize to any multi-layered system—e.g., cryptographic solutions, firewall setups, or layered storage frameworks.

---

## Technology

- **Language**: Python 3.x  
- **GUI**: Tkinter  
- **Data Retrieval**: `requests` library for NVD API calls  
- **Report Generation**: `reportlab` library for PDF creation  
- **Environment**: Compatible with Linux, macOS, and Windows

---

## Lessons

- **Layer Complexity**: Defining a universal layered model is nontrivial. We use a four-layer scheme common in IoT contexts but remain flexible for expansions or reductions.  
- **Real-World Vulnerabilities**: Tying in live CVE data underscores how frequently repeated or shared libraries can unify exploit vectors across “diverse” products.  
- **Agile Approach**: Iterative updates and sponsor feedback (via NSA/INSuRE) guided the addition of features like PDF exports and dynamic scoring.  
- **Scalability**: The tool covers major component categories, but deeper or domain-specific expansions (e.g., specialized ICS hardware or HPC networking) remain feasible as future work.

---

## Overview / Retrospective

- **What Went Well**:  
  - Successful synergy of a user-friendly GUI with a flexible backend for scoring and live vulnerability lookups.  
  - Clear metric definitions for easy adoption across distinct layered systems.  

- **Challenges**:  
  - Defining “implementation independence” in a mathematically rigorous yet user-friendly manner required balancing detail with simplicity.  
  - Access to real device detail or proprietary firmware is limited; open-source or hypothetical data was essential for demonstration.

- **Future Directions**:  
  - Incorporate **machine learning** or pattern recognition to detect code-level overlaps and vulnerabilities.  
  - Expand on dynamic weighting based on exploit severity or real-time threat feeds.  
  - Evaluate deeper use-cases: large-scale distributed systems, multi-tenant cloud solutions, or specialized ICS/SCADA networks.

---

## Contributors

**Codebase Core Team**  
### Codebase Core Team
- [**Richardo Larez**](https://github.com/richardolarez) (Undergraduate in Software Engineering)  
- [**Glenn Sears**](https://github.com/gsears72) (Undergraduate in Software Engineering)  
- [**Evan Martin**](https://github.com/evanwmart) (Undergraduate in Software Engineering)    

**Full Project & Report**  
- Richardo Larez  
- Glenn Sears  
- Evan Martin  
- Alain Sandoval  
- Seth White  

*Completed under [SIE 472] as part of the INSuRE Program with sponsorship from the National Security Agency (NSA).*

---

## A Note on Academic Integrity

This repository is intended **for reference and learning purposes only**. If you are a student reviewing this work:

- **Do Not Copy** any part of this project into your own submissions.  
- **Do Not Submit** this code as your own for any class or assignment.  
- **Use Responsibly**: Feel free to learn from the structure, logic, and methodology. Then craft **original solutions** that reflect your personal effort and understanding.

Please uphold your institution’s honor code and academic integrity guidelines.
