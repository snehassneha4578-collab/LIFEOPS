# 🚀 LIFEOPS — Autonomous Personal Operations Agent

<div align="center">

## 🧠 Autonomous AI Operations Agent

**Plan → Research → Act → Verify → Recover → Remember → Report**

![LIFEOPS Architecture](docs/LIFEOPS_Architecture_Diagram.png)

**🏆 Agents for Humans Hackathon · Everyday Agents**

</div>

---

## 🌟 What is LIFEOPS?

LIFEOPS is an autonomous personal operations agent built with the **Strands Agents SDK** and **Amazon Bedrock**. It turns real-life objectives into planned, actionable, verifiable workflows.

## 💡 Why LIFEOPS?

Most AI assistants stop at generating an answer. LIFEOPS coordinates an objective through planning, research, controlled action, verification, recovery, memory, and reporting.

> 🧠 **AI output ≠ proof.**

## 🔥 Core Workflow

USER OBJECTIVE
↓
🧠 PLAN → 🎯 PRIORITIZE → 🔎 RESEARCH
↓
⚙️ ACT → 🛡️ HUMAN APPROVAL
↓
✅ VERIFY → 🔄 RECOVER → 🧠 REMEMBER
↓
📊 FINAL REPORT

## ⚡ Key Capabilities

| Capability | LIFEOPS |
|---|---|
| 🧠 Planning | Multi-agent planning and prioritization |
| 🔎 Research | Source-bound research + persistent evidence |
| ⚙️ Action | Controlled task and workspace actions |
| 🛡️ Safety | Human approval for sensitive actions |
| ✅ Verification | Evidence-based verification |
| 🔄 Recovery | Failure recovery workflow |
| 🧠 Memory | Persistent workflow memory |
| 📋 Reporting | Traceable final reports |

## 🛡️ Human-in-the-Loop Safety

Sensitive actions require an externally approved exact approval. LIFEOPS cannot self-approve or bypass the approval boundary. Protected execution consumes one-time approvals and records the result in the audit trail.

## 🔍 Verification

LIFEOPS verifies results using persistent task state, research evidence, audit records, deadline information, and memory evidence instead of simply trusting model output.

## 🧪 Regression Tests

**7/7 tests passing** ✅

- ✓ Approval execution and replay protection
- ✓ Blocked execution without approval
- ✓ Memory evidence integrity
- ✓ Report memory traceability
- ✓ Task creation persistence
- ✓ Verification memory traceability
- ✓ Workflow memory retrieval

## 🏗️ Architecture

![LIFEOPS Architecture](docs/LIFEOPS_Architecture_Diagram.png)

## 💻 Technology Stack

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![Strands](https://img.shields.io/badge/Strands-Agents%20SDK-orange)
![AWS](https://img.shields.io/badge/Amazon%20Bedrock-AWS-orange?logo=amazonaws&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-7%2F7-success)
![License](https://img.shields.io/badge/License-MIT-green)

- Python 3.14
- Strands Agents SDK
- Amazon Bedrock
- Qwen3-Coder-Next
- Persistent JSON state stores
- Git and GitHub

## 📁 Project Structure

LIFEOPS/
├── agents/   → Specialized AI agents
├── tools/    → Controlled tools and persistence
├── app/      → Workflow orchestration
├── data/     → Runtime state
├── reports/  → Generated reports
├── docs/     → Architecture documentation
└── tests/    → Regression tests

## 🚀 Run

python -m app.main

## 🧪 Test

python -m unittest discover -s tests -p "test_*.py" -v

## 🏆 Hackathon

**Agents for Humans Hackathon — Everyday Agents**

## 👩‍💻 Developer

**Sneha S** · Solo Developer

## 📜 License

MIT License — see [LICENSE](LICENSE).

<div align="center">

**🚀 Turn objectives into verified progress.**

</div>
