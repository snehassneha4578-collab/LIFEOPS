<p align="center">
  <img src="assets/LIFEOPS_Hero_Banner.png" width="100%" alt="LIFEOPS â€” Autonomous Personal Operations Agent">
</p><h1 align="center">ðŸš€ LIFEOPS</h1><p align="center">
  <strong>Autonomous Personal Operations Agent</strong>
</p><p align="center">
  <strong>Plan â€¢ Research â€¢ Act â€¢ Approve â€¢ Verify â€¢ Recover â€¢ Remember â€¢ Report</strong>
</p><p align="center">
  <a href="https://github.com/snehassneha4578-collab/LIFEOPS">
    <img src="https://img.shields.io/badge/GitHub-LIFEOPS-181717?style=for-the-badge&logo=github">
  </a>
  <a href="https://agentsforhumans.devpost.com/">
    <img src="https://img.shields.io/badge/Agents%20for%20Humans-Hackathon-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white">
  </a>
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Strands%20Agents-SDK-232F3E?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>---

ðŸŒŸ Mission

LIFEOPS is an autonomous personal operations agent designed to transform a real-world objective into a structured, evidence-backed and safely executed workflow.

ðŸ§  Core Lifecycle

<p align="center">ðŸŽ¯ <strong>Objective</strong>
Â â†’Â 
ðŸ§  <strong>Plan</strong>
Â â†’Â 
ðŸ”Ž <strong>Research</strong>
Â â†’Â 
âš™ï¸ <strong>Act</strong>
Â â†’Â 
ðŸ›¡ï¸ <strong>Approve</strong>
Â â†’Â 
âœ… <strong>Verify</strong>
Â â†’Â 
ðŸ”„ <strong>Recover</strong>
Â â†’Â 
ðŸ§  <strong>Remember</strong>
Â â†’Â 
ðŸ“Š <strong>Report</strong>

</p>---

ðŸš€ What LIFEOPS Does

ðŸ§© Capability| ðŸ’¡ Description
ðŸ§  Planning| Converts real-world objectives into structured tasks
ðŸ”Ž Research| Researches information and preserves supporting evidence
âš™ï¸ Action| Executes controlled and policy-aware actions
ðŸ›¡ï¸ Approval| Requires human approval for sensitive operations
ðŸ” Safety| Blocks unauthorized or unsafe sensitive actions
âœ… Verification| Validates results using persistent evidence
ðŸ”„ Recovery| Handles workflow failures and recovery paths
ðŸ§  Memory| Preserves useful workflow history and evidence
ðŸ“Š Reporting| Produces a structured final readiness report

---
ðŸ–¥ï¸ Streamlit Dashboard

<p align="center">
  <img src="assets/LIFEOPS_Workflow.png" width="100%" alt="LIFEOPS Streamlit Workflow">
</p>LIFEOPS includes a visual Streamlit dashboard for running and monitoring the complete agent workflow.

â–¶ï¸ Run Locally

.\.venv\Scripts\python.exe -m streamlit run .\ui\dashboard.py

ðŸŒ Open Dashboard

After starting the application, open the following address in your browser:

http://localhost:8501

Â«âš ï¸ Note: "localhost:8501" is a local development address.
It works only on the computer where the LIFEOPS Streamlit application is running. It is not a public online link.Â»

ðŸš€ Live Demo

Â«ðŸ”— Live dashboard deployment: Coming SoonÂ»

Once LIFEOPS is deployed online, the public Streamlit URL will be added here.

ðŸ—ï¸ Architecture

<p align="center">
  <img src="docs/LIFEOPS_Architecture_Diagram.png" width="100%" alt="LIFEOPS Architecture Diagram">
</p><p align="center">
  <strong>
    Planner â†’ Research â†’ Action â†’ Approval â†’ Verification â†’ Recovery â†’ Memory â†’ Report
  </strong>
</p>ðŸ“˜ Architecture Documentation:
"docs/ARCHITECTURE.md" (docs/ARCHITECTURE.md)

---

ðŸ”„ LIFEOPS Workflow

<p align="center">
  <img src="assets/LIFEOPS_Workflow.png" width="100%" alt="LIFEOPS Workflow">
</p>Complete Workflow

ðŸŽ¯ Objective
â†“
ðŸ§  Plan
â†“
ðŸ“Œ Prioritize
â†“
ðŸ”Ž Research
â†“
âš™ï¸ Act
â†“
ðŸ›¡ï¸ Approval
â†“
âœ… Verify
â†“
ðŸ”„ Recover
â†“
ðŸ§  Remember
â†“
ðŸ“Š Report

---

ðŸ›¡ï¸ Safety & Human Approval

<p align="center">
  <img src="assets/LIFEOPS_Safety.png" width="100%" alt="LIFEOPS Safety Architecture">
</p>LIFEOPS is designed around safe autonomy, ensuring that autonomous execution does not bypass human control or verification.

ðŸ” Safety Principles

- âœ… Explicit approval for sensitive operations
- ðŸš« Unauthorized actions are blocked
- ðŸ” Approval replay is prevented
- ðŸ“ Sensitive operations are audited
- ðŸ“ Controlled file operations
- ðŸš« No unrestricted shell execution
- ðŸ‘¤ Human oversight for high-impact actions

Â«LIFEOPS does not treat autonomy as permission to perform everything. Safety and human control remain part of the workflow.Â»

---

ðŸ” Evidence-Based Verification

LIFEOPS separates action from verification.

An agent claiming that an operation was completed is not considered sufficient proof.

Verification can use:

- ðŸ“Œ Task state
- ðŸ“ Audit records
- ðŸ”Ž Research evidence
- ðŸ§  Memory evidence
- âš™ï¸ Action results
- ðŸ’¾ Persistent workflow state

Verification States

<p align="center">ðŸŸ¢ <strong>VERIFIED</strong>
Â Â â€¢Â Â 
ðŸŸ¡ <strong>UNVERIFIED</strong>
Â Â â€¢Â Â 
ðŸ”´ <strong>FAILED</strong>
Â Â â€¢Â Â 
â›” <strong>BLOCKED</strong>

</p>---

ðŸ“Š Readiness Report

<p align="center">
  <img src="assets/LIFEOPS_Readiness_Report.png" width="100%" alt="LIFEOPS Readiness Report">
</p>After the workflow completes, LIFEOPS generates a structured Readiness Report containing:

ðŸ“‹ Report Section| ðŸ”Ž Purpose
ðŸŽ¯ Objective| Original real-world goal
ðŸ“Š Status| Current workflow state
ðŸ“š Evidence| Supporting evidence collected
âœ… Verification| Verification results
âš ï¸ Issues| Problems or unresolved items
ðŸ”„ Recovery| Recovery actions taken
ðŸ§  Memory| Relevant workflow memory
ðŸš€ Next Steps| Recommended actions

---

ðŸ§° Technology Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Amazon%20Bedrock-AI-FF9900?style=flat-square&logo=amazonaws&logoColor=white">
  <img src="https://img.shields.io/badge/Strands%20Agents-Agent%20SDK-232F3E?style=flat-square">
  <img src="https://img.shields.io/badge/GitHub-Version%20Control-181717?style=flat-square&logo=github">
</p>ðŸ”§ Core Technologies

Python â€¢ Strands Agents SDK â€¢ Amazon Bedrock â€¢ Qwen â€¢ Streamlit â€¢ Git/GitHub â€¢ Evidence Store â€¢ Approval Manager â€¢ Audit Logging â€¢ Workflow Memory

---

ðŸ“¦ Installation

1ï¸âƒ£ Clone the Repository

git clone https://github.com/snehassneha4578-collab/LIFEOPS.git

2ï¸âƒ£ Enter the Project

cd LIFEOPS

3ï¸âƒ£ Create Virtual Environment

python -m venv .venv

4ï¸âƒ£ Install Dependencies

pip install -r requirements.txt

5ï¸âƒ£ Start LIFEOPS

.\.venv\Scripts\python.exe -m streamlit run .\ui\dashboard.py

---

ðŸ§ª Testing

LIFEOPS includes regression coverage for important safety, verification and memory components.

Test Coverage

- ðŸ›¡ï¸ Approval execution
- ðŸ” Approval replay protection
- ðŸš« Blocking sensitive actions without approval
- ðŸ§  Memory evidence integrity
- ðŸ“Š Report memory traceability
- ðŸ’¾ Task persistence
- âœ… Verification memory traceability
- ðŸ”Ž Workflow memory retrieval

---

ðŸŽ¥ Demo Video

Â«ðŸš§ Demo Video: Coming SoonÂ»

The final demonstration will showcase:

ðŸŽ¯ Real-world objective
â†’ ðŸ§  Planning
â†’ ðŸ”Ž Research
â†’ âš™ï¸ Controlled execution
â†’ ðŸ›¡ï¸ Human approval
â†’ âœ… Verification
â†’ ðŸ”„ Recovery
â†’ ðŸ§  Memory
â†’ ðŸ“Š Final readiness report

---

ðŸ† Hackathon

<p align="center">
  <strong>ðŸ¤– Agents for Humans Hackathon</strong>
</p><p align="center">
  <strong>Track: Everyday Agents</strong>
</p><p align="center">
  <a href="https://agentsforhumans.devpost.com/">
    <img src="https://img.shields.io/badge/Official%20Hackathon-Devpost-003E54?style=for-the-badge&logo=devpost">
  </a>
</p>---

ðŸ’» Repository

<p align="center">
  <a href="https://github.com/snehassneha4578-collab/LIFEOPS">
    <img src="https://img.shields.io/badge/VIEW%20SOURCE%20CODE-GitHub-181717?style=for-the-badge&logo=github">
  </a>
</p><p align="center">
  <strong>GitHub:</strong>
  <a href="https://github.com/snehassneha4578-collab/LIFEOPS">
    snehassneha4578-collab/LIFEOPS
  </a>
</p>---

ðŸ‘©â€ðŸ’» Developer

<p align="center"><strong>Sneha S</strong>

<br>ECE Student â€¢ AI/ML â€¢ Embedded Systems â€¢ VLSI

</p>---

ðŸ“œ License

This project is licensed under the MIT License.

---

<p align="center"><h2 align="center">ðŸš€ LIFEOPS</h2><p align="center">
  <strong>Autonomous operations with safety, evidence and verification.</strong>
</p><p align="center">
  ðŸŽ¯ Plan &nbsp;â€¢&nbsp;
  ðŸ”Ž Research &nbsp;â€¢&nbsp;
  âš™ï¸ Act &nbsp;â€¢&nbsp;
  ðŸ›¡ï¸ Approve &nbsp;â€¢&nbsp;
  âœ… Verify &nbsp;â€¢&nbsp;
  ðŸ”„ Recover &nbsp;â€¢&nbsp;
  ðŸ§  Remember &nbsp;â€¢&nbsp;
  ðŸ“Š Report
</p></p>
