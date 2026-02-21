from langgraph.graph import StateGraph
from state import AgentState

from agents.analyst import analyst_agent
from agents.memory_agent import memory_agent
from agents.strategist import strategist_agent
from agents.copywriter import copywriter_agent
from agents.optimizer import optimizer_agent


def build_graph():

    graph = StateGraph(AgentState)

    # nodes
    graph.add_node("analyst", analyst_agent)
    graph.add_node("memory", memory_agent)
    graph.add_node("strategist", strategist_agent)
    graph.add_node("copywriter", copywriter_agent)
    graph.add_node("optimizer", optimizer_agent)

    # entry
    graph.set_entry_point("analyst")

    # sequential chain
    graph.add_edge("analyst", "memory")
    graph.add_edge("memory", "strategist")

    # parallel branches
    graph.add_edge("strategist", "copywriter")
    graph.add_edge("strategist", "optimizer")

    # finish when BOTH complete
    graph.set_finish_point("copywriter")
    graph.set_finish_point("optimizer")

    return graph.compile()