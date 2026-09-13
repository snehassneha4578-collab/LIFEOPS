from tools.memory_store import save_memory, search_memories

def remember_workflow(request, result):
    return save_memory(
        "WORKFLOW",
        f"Request: {request}\nResult: {result}",
        "orchestrator"
    )

def recall_workflow(request):
    matches = search_memories(request)
    return {
        "query": request,
        "matches": matches,
        "count": len(matches)
    }
