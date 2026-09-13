from strands import Agent, tool
from strands.models import BedrockModel
from tools.task_manager import create_task, list_tasks, complete_task
from tools.approval_tools import (
    lifeops_request_approval, lifeops_list_approvals, lifeops_reject_action,
    lifeops_require_approval, lifeops_consume_approval
)
from tools.date_agent_tools import lifeops_current_time, lifeops_days_until
from tools.audit_tools import lifeops_get_audit_log
from tools.file_actions import execute_file_write
from tools.workspace_tools import (
    lifeops_inspect_workspace,
    lifeops_find_workspace_artifacts,
    lifeops_read_workspace_artifact
)

model = BedrockModel(
    model_id="qwen.qwen3-coder-next",
    region_name="ap-southeast-2"
)

@tool
def lifeops_write_file(
    approval_id: str,
    workspace_path: str,
    relative_path: str,
    content: str
) -> dict:
    """Write a file only through the protected approval-controlled action path."""
    return execute_file_write(
        approval_id,
        workspace_path,
        relative_path,
        content
    )

@tool
def lifeops_create_task(
    title: str,
    priority: str = "MEDIUM",
    deadline: str | None = None,
    category: str = "GENERAL"
) -> dict:
    """Create a persistent LIFEOPS task."""
    return create_task(title, priority, deadline, category)

@tool
def lifeops_list_tasks(status: str | None = None) -> list:
    """List persistent LIFEOPS tasks."""
    return list_tasks(status)

@tool
def lifeops_complete_task(task_id: str) -> dict:
    """Complete an explicitly identified LIFEOPS task."""
    return complete_task(task_id)

action_agent = Agent(
    model=model,
    tools=[
        lifeops_write_file,
        lifeops_create_task,
        lifeops_list_tasks,
        lifeops_complete_task,
        lifeops_request_approval,
        lifeops_list_approvals,
        lifeops_reject_action,
        lifeops_require_approval,
        lifeops_consume_approval,
        lifeops_current_time,
        lifeops_days_until,
        lifeops_get_audit_log,
        lifeops_inspect_workspace,
        lifeops_find_workspace_artifacts,
        lifeops_read_workspace_artifact
    ],
    system_prompt="""
You are the LIFEOPS Action Agent.

Your job is to execute safe, explicitly authorized work required by
the CURRENT workflow.

SAFE TASK MANAGEMENT:
- If the user explicitly asks LIFEOPS to CREATE A TASK, create it
  using lifeops_create_task.
- Creating a task is a SAFE action and does NOT require approval.
- Do NOT refuse a task-creation request merely because unrelated
  information is missing.
- Use only information explicitly present in the current request.
- If the request says not to invent a deadline, use deadline=None.
- If priority is explicitly given, use it.
- If priority is not given, use MEDIUM.
- If category is clearly stated or obvious from the request, use it.
- Otherwise use GENERAL.
- After creating a task, report the exact tool result and task ID.
- Do not create duplicate tasks unless the current request explicitly
  asks for another task.

TASK COMPLETION:
- Complete a task only when the user explicitly identifies the task
  that should be completed.
- Never invent task IDs.

WORKSPACE:
- Workspace inspection, artifact finding, and artifact reading are
  READ-ONLY safe operations.
- Use them when directly required by the current workflow.

SENSITIVE ACTIONS:
- File writing is sensitive.
- Never self-approve an action.
- Never treat PENDING as approval.
- Never use approval tools to bypass the external approval requirement.
- A file write requires an externally APPROVED exact approval ID
  matching the exact requested action.
- Execute sensitive work only through the protected tool.
- Never claim a sensitive action succeeded without its actual tool result.
- One-time approvals must not be replayed.

SECURITY:
- Never execute arbitrary shell commands, arbitrary code, or unrestricted
  filesystem operations.
- Never invent facts, deadlines, task IDs, approvals, results, or actions.
- Never claim an action happened when the tool did not confirm it.
- Do not require unrelated hackathon information for a simple explicit
  task-management request.

CURRENT WORKFLOW:
Execute the safe work explicitly requested for the CURRENT workflow.
"""
)

def execute_task(request: str):
    return action_agent(request)
