from strands import tool

from tools.workflow_memory import (
    list_workflows,
    search_workflows
)


@tool
def lifeops_list_workflows() -> list:
    """Return saved LIFEOPS workflow history."""
    return list_workflows()


@tool
def lifeops_search_workflows(
    query: str,
    limit: int = 5
) -> list:
    """
    Search previously saved LIFEOPS workflows for relevant
    historical context.

    Returns only information already persisted in workflow history.
    """
    return search_workflows(query, limit)