<p align="center">
<img src="assets/LIFEOPS_Hero_Banner.png" width="100%" alt="LIFEOPS">
</p>

<h1 align="center">LIFEOPS</h1>

<p align="center"><strong>Autonomous Personal Operations Agent</strong></p>

<p align="center">Plan Ã¢â‚¬Â¢ Research Ã¢â‚¬Â¢ Act Ã¢â‚¬Â¢ Approve Ã¢â‚¬Â¢ Verify Ã¢â‚¬Â¢ Recover Ã¢â‚¬Â¢ Remember Ã¢â‚¬Â¢ Report</p>

<p align="center">
<a href="https://github.com/snehassneha4578-collab/LIFEOPS"><img src="https://img.shields.io/badge/GitHub-LIFEOPS-181717?style=for-the-badge&logo=github"></a>
<a href="https://agentsforhumans.devpost.com/"><img src="https://img.shields.io/badge/Agents%20for%20Humans-Hackathon-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"></a>
<img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Strands%20Agents-SDK-232F3E?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

---

## Mission

LIFEOPS takes a real-world objective and turns it into a structured, evidence-backed workflow.

**Plan Ã¢â€ â€™ Research Ã¢â€ â€™ Act safely Ã¢â€ â€™ Verify Ã¢â€ â€™ Recover Ã¢â€ â€™ Remember Ã¢â€ â€™ Report**

## What LIFEOPS Does

| Capability | Description |
|---|---|
| Planning | Converts objectives into structured tasks |
| Research | Researches information and preserves evidence |
| Action | Executes controlled actions |
| Approval | Requires approval for sensitive operations |
| Safety | Blocks unauthorized sensitive actions |
| Verification | Checks persistent evidence |
| Recovery | Handles workflow problems |
| Memory | Preserves useful workflow history |
| Reporting | Produces a final readiness report |

---

# Streamlit Dashboard

<p align="center">
<img src="assets/LIFEOPS_Workflow.png" width="100%" alt="LIFEOPS Streamlit Workflow">
</p>

LIFEOPS includes a visual Streamlit dashboard for running and monitoring the complete agent workflow.

**Run locally:**

`.\.venv\Scripts\python.exe -m streamlit run .\ui\dashboard.py`

**Dashboard:** http://localhost:8501

---

# Architecture

<p align="center">
<img src="docs/LIFEOPS_Architecture_Diagram.png" width="100%" alt="LIFEOPS Architecture Diagram">
</p>

<p align="center"><strong>Planner Ã¢â€ â€™ Research Ã¢â€ â€™ Action Ã¢â€ â€™ Approval Ã¢â€ â€™ Verification Ã¢â€ â€™ Recovery Ã¢â€ â€™ Memory Ã¢â€ â€™ Report</strong></p>

**Architecture documentation:** [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

# LIFEOPS Workflow

<p align="center">
<img src="assets/LIFEOPS_Workflow.png" width="100%" alt="LIFEOPS Workflow">
</p>

**Objective Ã¢â€ â€™ Plan Ã¢â€ â€™ Prioritize Ã¢â€ â€™ Research Ã¢â€ â€™ Act Ã¢â€ â€™ Approval Ã¢â€ â€™ Verify Ã¢â€ â€™ Recover Ã¢â€ â€™ Remember Ã¢â€ â€™ Report**

---

# Safety & Human Approval

<p align="center">
<img src="assets/LIFEOPS_Safety.png" width="100%" alt="LIFEOPS Safety">
</p>

LIFEOPS is designed for safe autonomy.

- Explicit approval for sensitive operations
- Unauthorized actions are blocked
- Approval replay is prevented
- Sensitive operations are audited
- Controlled file operations
- No unrestricted shell execution

---

# Evidence-Based Verification

LIFEOPS separates action from verification.

An agent claiming that something was completed is not treated as sufficient proof.

Verification can use task state, audit records, research evidence, memory evidence, action results and persistent workflow state.

**VERIFIED Ã¢â‚¬Â¢ UNVERIFIED Ã¢â‚¬Â¢ FAILED Ã¢â‚¬Â¢ BLOCKED**

---

# Readiness Report

<p align="center">
<img src="assets/LIFEOPS_Readiness_Report.png" width="100%" alt="LIFEOPS Readiness Report">
</p>

After the workflow completes, LIFEOPS produces a structured readiness report containing status, evidence, verification results, issues and next steps.

---

# Technology Stack

<p align="center">
<img src="https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/Amazon%20Bedrock-AI-FF9900?style=flat-square&logo=amazonaws&logoColor=white">
<img src="https://img.shields.io/badge/Strands%20Agents-Agent%20SDK-232F3E?style=flat-square">
<img src="https://img.shields.io/badge/GitHub-Version%20Control-181717?style=flat-square&logo=github">
</p>

**Core:** Python Ã¢â‚¬Â¢ Strands Agents SDK Ã¢â‚¬Â¢ Amazon Bedrock Ã¢â‚¬Â¢ Qwen Ã¢â‚¬Â¢ Streamlit Ã¢â‚¬Â¢ Git/GitHub Ã¢â‚¬Â¢ Evidence Store Ã¢â‚¬Â¢ Approval Manager Ã¢â‚¬Â¢ Audit Logging Ã¢â‚¬Â¢ Workflow Memory

---

# Project Structure

```text
LIFEOPS/
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ agents/
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ planner.py
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ priority.py
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ research.py
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ action.py
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ verification.py
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ app/
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ orchestrator.py
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ tools/
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ ui/
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ dashboard.py
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ assets/
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ LIFEOPS_Hero_Banner.png
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ LIFEOPS_Logo.png
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ LIFEOPS_Workflow.png
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ LIFEOPS_Safety.png
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ LIFEOPS_Readiness_Report.png
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ docs/
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ ARCHITECTURE.md
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ LIFEOPS_Architecture_Diagram.png
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ tests/
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ README.md
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ LICENSE
Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ requirements.txt
```

---

# Installation

`git clone https://github.com/snehassneha4578-collab/LIFEOPS.git`

`cd LIFEOPS`

`python -m venv .venv`

`pip install -r requirements.txt`

**Start:**

`.\.venv\Scripts\python.exe -m streamlit run .\ui\dashboard.py`

---

# Testing

Core regression coverage includes:

- Approval execution and replay protection
- Blocking sensitive actions without approval
- Memory evidence integrity
- Report memory traceability
- Task persistence
- Verification memory traceability
- Workflow memory retrieval

---

# Demo Video

**Demo video: Coming soon**

The final demonstration will show the complete LIFEOPS workflow, safety controls, verification and Streamlit dashboard.

---

# Hackathon

**Agents for Humans Hackathon**

**Track: Everyday Agents**

Official event: https://agentsforhumans.devpost.com/

---

# Repository

<p align="center">
<a href="https://github.com/snehassneha4578-collab/LIFEOPS">
<img src="https://img.shields.io/badge/VIEW%20SOURCE%20CODE-GitHub-181717?style=for-the-badge&logo=github">
</a>
</p>

**GitHub:** https://github.com/snehassneha4578-collab/LIFEOPS

---

# Developer

**Sneha S**

ECE Student Ã¢â‚¬Â¢ AI/ML Ã¢â‚¬Â¢ Embedded Systems Ã¢â‚¬Â¢ VLSI

---

# License

MIT License

---

<p align="center"><strong>LIFEOPS</strong><br>Autonomous operations with safety, evidence and verification.</p>