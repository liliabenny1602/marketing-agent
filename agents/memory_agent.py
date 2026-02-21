from memory.vector_store import similarity_search, mmr_search


def _choose_query(state):

    if state.get("analysis"):
        return state["analysis"]

    if state.get("metrics"):
        return str(state["metrics"])

    return "marketing campaign optimization"


def memory_agent(state):

    tracer = state.get("tracer")
    if tracer:
        tracer.node_start("Memory")

    query = _choose_query(state)

    try:
        memories = mmr_search(query, k=3)
        if not memories:
            memories = similarity_search(query, k=3)
    except Exception as e:
        memories = [f"Memory retrieval error: {str(e)}"]

    if tracer:
        tracer.node_end("Memory")

    return {
        "memories": memories,
        "memory_query": query,
        "memory_count": len(memories)
    }