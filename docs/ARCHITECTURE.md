# LIFEOPS Architecture

## Core Flow

User Objective ? Orchestrator ? Planner ? Priority ? Research ? Action ? Verification ? Recovery ? Final Readiness Report

## Agents

- Planner Agent — decomposes the user's objective into actionable tasks.
- Priority Agent — identifies urgency, importance, dependencies, and blockers.
- Research Agent — retrieves source-bound web evidence and stores evidence IDs.
- Action Agent — performs safe operations and manages tasks.
- Verification Agent — verifies results using persistent evidence.
- Recovery Agent — handles failures and supports workflow recovery.
- Report Agent — produces the final readiness report.

## Human-in-the-Loop Security

Sensitive actions require explicit human approval before execution. Approved actions pass through the secure action layer and are recorded in the audit log.

## Evidence and Verification

LIFEOPS does not treat an agent response as proof. Verification uses persistent task state, research evidence, audit records, deadlines, and memory evidence.

## Persistent State

Tasks, approvals, audit records, research evidence, workflow memory, and workflow history are persisted locally and protected from repository commits.
