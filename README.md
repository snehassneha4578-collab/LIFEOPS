# LIFEOPS — Autonomous Personal Operations Agent

LIFEOPS is an autonomous personal operations agent built with the Strands Agents SDK and Amazon Bedrock. It turns real-life objectives into planned, actionable, verifiable workflows.

## Why LIFEOPS
Most AI assistants stop at generating an answer. LIFEOPS coordinates an objective from planning through action, verification, evidence, recovery, memory, and a final readiness report.

## Core Workflow
Understand objective → Plan → Prioritize → Research → Act → Verify → Recover → Remember → Report

## Key Capabilities
- Multi-agent planning and prioritization
- Source-bound web research with persistent evidence
- Controlled task and workspace actions
- Human approval for sensitive actions
- Persistent verification and audit evidence
- Failure recovery
- Workflow memory and traceability
- Regression-tested safety controls

## Human-in-the-Loop Safety
Sensitive actions require an externally approved exact approval. LIFEOPS cannot self-approve or bypass the approval boundary. Protected execution consumes one-time approvals and records the result in the audit trail.

## Verification: AI Output ≠ Proof
LIFEOPS separates generated conclusions from actual evidence. Verification can use persistent task state, research evidence, audit records, deadline tools, and memory evidence instead of trusting model output alone.

## Architecture
![LIFEOPS Architecture](docs/LIFEOPS_Architecture_Diagram.png)

## Technology Stack
- Python 3.14
- Strands Agents SDK
- Amazon Bedrock
- Qwen3-Coder-Next
- Persistent JSON state stores
- Git and GitHub

## Project Structure
- agents/ — specialized AI agents
- tools/ — controlled tools and persistence
- app/ — workflow orchestration
- data/ — runtime state
- reports/ — generated reports
- docs/ — architecture documentation
- tests/ — regression tests

## Installation
Use the project virtual environment and install dependencies from requirements.txt.

## Run
python -m app.main

## Testing
python -m unittest discover -s tests -p "test_*.py" -v

## Hackathon
Built for the Agents for Humans Hackathon — Everyday Agents.

## Team
Sneha S — Solo Developer

## Demo
The final demonstration will show LIFEOPS preparing a real hackathon submission objective, researching official requirements, inspecting project artifacts, creating actionable work, respecting approval boundaries, verifying results, and producing a traceable readiness report.

## License
MIT License. See LICENSE.

## Status
Core autonomous workflow, controlled actions, approval safety, verification, evidence, recovery, memory, auditability, architecture documentation, and regression testing are implemented.
