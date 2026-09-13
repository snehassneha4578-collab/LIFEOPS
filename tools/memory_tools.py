from strands import tool

from tools.memory_store import (
    save_memory,
    list_memories,
    search_memories
)

@tool
def lifeops_save_memory(
    memory_type: str,
    content: str,
    source: str = "workflow"
) -> dict:
    """Persist useful LIFEOPS workflow memory."""
    return save_memory(memory_type, content, source)

@tool
def lifeops_list_memories(
    memory_type: str = None
) -> list:
    """Return persistent LIFEOPS memories."""
    return list_memories(memory_type)

@tool
def lifeops_search_memory(
    query: str
) -> list:
    """Search persistent LIFEOPS memory."""
    return search_memories(query)
