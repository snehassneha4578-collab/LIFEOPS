 # LIFEOPS — Autonomous Personal Operations Agent
## Overview
LIFEOPS is an autonomous personal operations agent built with the Strands Agents SDK. It turns real-life objectives into planned, actionable, verifiable workflows.
## Core Workflow
Understand objective → Plan → Prioritize → Research → Act → Verify → Recover → Remember → Report
## Problem
Everyday objectives require planning, research, actions, deadlines, verification, and follow-up. LIFEOPS coordinates these steps through specialized AI agents.
## Solution
LIFEOPS coordinates specialized agents for planning, research, safe actions, verification, recovery, memory, and reporting.
## Human-in-the-Loop Safety
Sensitive actions require an externally approved exact approval and protected execution. LIFEOPS never self-approves.
## Verification and Evidence
Research evidence, task state, approvals, audit records, and memory evidence are persisted and used to verify workflow results.
## Architecture
User → Orchestrator → Planner → Priority → Research → Action → Verification → Recovery → Memory → Report
## Technology Stack
Python | Strands Agents SDK | AWS Bedrock | Qwen3-Coder-Next | JSON | Git/GitHub
## Project Structure
agents/ — specialized agents | tools/ — controlled tools | app/ — orchestration | data/ — persistent state | reports/ — reports | tests/ — regression tests
## Installation
Use the project virtual environment and install dependencies from requirements.txt.
## Run
python -m app.main
## Testing
python -m unittest discover -s tests -p test_*.py
## Hackathon
Agents for Humans Hackathon — Everyday Agents
## Team
Sneha S — Solo Developer
## License
MIT License. See LICENSE.
## Status
Core autonomous workflow, controlled actions, approval safety, verification, evidence, recovery, memory, auditability and regression testing are implemented.
