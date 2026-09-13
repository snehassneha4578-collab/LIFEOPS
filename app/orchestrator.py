from app.workflow_state import WorkflowState
from agents.planner import create_plan
from agents.priority import prioritize
from agents.research import research_task
from agents.action import execute_task
from agents.verification import verify_result
from agents.report import generate_report
from agents.recovery import recover_workflow

from tools.workflow_memory import save_workflow
from tools.workflow_memory_agent import recall_workflow, remember_workflow
from tools.evidence_store import list_evidence
from concurrent.futures import ThreadPoolExecutor


def orchestrate(request: str):
    state = WorkflowState(request)

    official_hackathon_url = "https://agentsforhumans.devpost.com/"

    research_request = f"""
Research the official Agents for Humans Hackathon requirements.

OFFICIAL SOURCE:
{official_hackathon_url}

Use lifeops_research_url on this exact URL.
Do not ask the user for the URL because it is supplied by the workflow.

Verify only information supported by the retrieved official source.
Extract submission requirements, deadline, submission format, required
fields/materials, repository requirements, media/demo requirements,
team rules, licensing requirements, judging requirements, and other
directly stated submission constraints.

Also identify what information is not stated by the official source.
"""

    workspace_request = """
Inspect the current LIFEOPS workspace for submission-related artifacts.

Find and inspect relevant files such as README.md, LICENSE, .gitignore,
documentation, reports, tests, configuration files, project descriptions,
architecture materials, demo materials, and other submission artifacts.

Use read-only workspace tools only.
Do not modify files.
Return exact file paths and what each artifact contains.
"""

    try:
        plan_request = (
            f"Previous relevant LIFEOPS memory:\n"
            f"{recall_workflow(request)}\n\n"
            f"Current request:\n{request}"
        )

        existing_evidence = list_evidence()
        cached_research = [
            item for item in existing_evidence
            if isinstance(item, dict)
            and item.get("url") == official_hackathon_url
        ]

        if cached_research:
            state.research = (
                "CACHED OFFICIAL RESEARCH\n"
                f"Source: {official_hackathon_url}\n"
                f"Persistent evidence records available: {len(cached_research)}\n"
                "Existing stored evidence will be used for verification."
            )
            state.plan = create_plan(plan_request)
        else:
            with ThreadPoolExecutor(max_workers=2) as executor:
                plan_future = executor.submit(create_plan, plan_request)
                research_future = executor.submit(research_task, research_request)
                state.plan = plan_future.result()
                state.research = research_future.result()

        state.priorities = state.plan

        state.evidence = list_evidence()

        state.action = execute_task(
            workspace_request
            + f"""

Execute the safe, explicitly authorized work required for the
CURRENT LIFEOPS workflow.

Use the registered LIFEOPS tools when they are directly required.

Safe capabilities include:
- creating actionable tasks when required
- listing and inspecting tasks
- completing only explicitly identified tasks
- inspecting the workspace read-only
- finding relevant workspace artifacts
- reading relevant workspace artifacts

Sensitive actions:
- never self-approve
- never treat PENDING as approval
- require an externally APPROVED exact approval
- execute sensitive actions only through protected tools
- never claim success without actual tool confirmation

Never execute arbitrary code, shell commands, or unrestricted
filesystem operations.

Never invent tasks, IDs, deadlines, approvals, results, or actions.

CURRENT OBJECTIVE:
{request}

PLAN:
{state.plan}

PRIORITIES:
{state.priorities}

RESEARCH:
{state.research}
"""
        )

        action_text = str(state.action).upper()

        if any(marker in action_text for marker in ["FAILED", "BLOCKED"]):
            state.errors.append(str(state.action))
            state.recovery = recover_workflow(str(state.action))

        state.verification = verify_result(
            f"""
Verify the actual results of this LIFEOPS workflow.

Objective:
{request}

Plan:
{state.plan}

Action result:
{state.action}

Recovery result:
{state.recovery}

Persistent evidence:
{state.evidence}
"""
        )

        state.report = generate_report(
            f"""
Objective:
{request}

PLAN:
{state.plan}

PRIORITIES:
{state.priorities}

RESEARCH:
{state.research}

ACTION:
{state.action}

RECOVERY:
{state.recovery}

VERIFICATION:
{state.verification}

PERSISTENT EVIDENCE:
{state.evidence}
"""
        )

        remember_workflow(
            request,
            f"Verification:\n{state.verification}\n\n"
            f"Report:\n{state.report}"
        )

    except Exception as exc:
        state.errors.append(str(exc))

    save_workflow(state)
    return state
