from langgraph.graph import StateGraph

from agents.analyst import analyst_agent
from agents.memory_agent import memory_agent
from agents.strategist import strategist_agent
from agents.copywriter import copywriter_agent
from agents.optimizer import optimizer_agent


def build_graph():

    graph = StateGraph(dict)

    graph.add_node("analyst", analyst_agent)
    graph.add_node("memory", memory_agent)
    graph.add_node("strategist", strategist_agent)
    graph.add_node("copywriter", copywriter_agent)
    graph.add_node("optimizer", optimizer_agent)

    graph.set_entry_point("analyst")

    graph.add_edge("analyst", "memory")
    graph.add_edge("memory", "strategist")
    graph.add_edge("strategist", "copywriter")
    graph.add_edge("strategist", "optimizer")

    graph.set_finish_point("optimizer")

    return graph.compile()