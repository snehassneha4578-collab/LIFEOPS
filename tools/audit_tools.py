from strands import tool
from tools.audit_log import get_audit_log


@tool
def lifeops_get_audit_log() -> list:
    """Return the persistent LIFEOPS audit history."""
    return get_audit_log()
