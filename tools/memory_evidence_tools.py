from strands import tool
from tools.memory_evidence import get_memory_evidence

@tool
def lifeops_get_memory_evidence() -> dict:
    """Return persistent memory evidence and integrity metadata."""
    return get_memory_evidence()
