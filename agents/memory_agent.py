from memory.vector_store import similarity_search, mmr_search


def _choose_query(state):
    """
    Determines best retrieval query from available state.
    Priority order ensures robustness.
    """     

    if "analysis" in state and state["analysis"]:
        return state["analysis"]

    if "metrics" in state:
        return str(state["metrics"])

    return "marketing campaign performance optimization"


def memory_agent(state):
    """
    Retrieves relevant past campaign knowledge
    and injects it into agent reasoning state.
    """

    query = _choose_query(state)

    try:
        # try diversity-aware retrieval first
        memories = mmr_search(query, k=3)

        if not memories:
            memories = similarity_search(query, k=3)

    except Exception as e:
        memories = [f"[Memory retrieval failed: {str(e)}]"]

    return {
        "memories": memories,
        "memory_query": query,
        "memory_count": len(memories)
    }