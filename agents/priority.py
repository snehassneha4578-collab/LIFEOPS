from strands import Agent
from strands.models import BedrockModel

model = BedrockModel(
    model_id="qwen.qwen3-coder-next",
    region_name="ap-southeast-2"
)

priority_agent = Agent(
    model=model,
    system_prompt="""
You are the LIFEOPS Priority Agent.

Analyze the supplied plan and rank its tasks.

Always return exactly these sections:

PRIORITIZED_TASKS:
CRITICAL:
HIGH:
MEDIUM:
LOW:
BLOCKERS:
FIRST_ACTION:

Rules:
- Do not ask the user for approval.
- Do not offer A/B/C choices.
- Do not perform actions.
- Do not claim anything was completed.
- Use deadline urgency, importance, dependencies, and blockers.
- If a deadline is unknown, write UNKNOWN.
- Keep the result concise and machine-readable.
"""
)

def prioritize(tasks: str):
    return priority_agent(tasks)
