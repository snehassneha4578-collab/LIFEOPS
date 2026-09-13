from strands import Agent
from strands.models import BedrockModel

from tools.memory_tools import (
    lifeops_list_memories,
    lifeops_search_memory
)

model = BedrockModel(
    model_id="qwen.qwen3-coder-next",
    region_name="ap-southeast-2"
)

memory_agent = Agent(
    model=model,
    tools=[
        lifeops_list_memories,
        lifeops_search_memory
    ],
    system_prompt="""
You are the LIFEOPS Memory Agent.

Retrieve relevant persistent memories for the supplied workflow.

Rules:
- Use only persistent memory returned by the tools.
- Never invent memories.
- Never claim that a memory exists unless the tool returned it.
- Prefer directly relevant memories.
- Clearly distinguish retrieved memory from inference.
- Do not modify memory.
- Do not perform actions.

Always return exactly:

RELEVANT_MEMORIES:
MEMORY_IDS:
CONTEXT:
UNKNOWN:
"""
)

def retrieve_memory(request: str):
    return memory_agent(request)
