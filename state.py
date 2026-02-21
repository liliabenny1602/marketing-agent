from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict, total=False):
    metrics: Dict[str, Any]
    analysis: str
    memories: List[str]
    memory_query: str
    memory_count: int
    strategy: str
    copy: str
    decision: str
    execution: str