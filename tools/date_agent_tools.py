from strands import tool
from tools.date_tools import get_current_time, days_until


@tool
def lifeops_current_time() -> str:
    """Return the current UTC time for LIFEOPS."""
    return get_current_time()


@tool
def lifeops_days_until(deadline: str) -> dict:
    """Calculate remaining days and overdue status for a YYYY-MM-DD deadline."""
    return days_until(deadline)
