from strands import tool
from tools.evidence_store import list_evidence

@tool
def lifeops_get_research_evidence() -> list:
    """Return persistent LIFEOPS research evidence."""
    return list_evidence()
