from graphviz import Digraph
from workflows.campaign_graph import build_graph


def visualize():

    graph = build_graph()

    dot = Digraph(comment="Agent Workflow")
    dot.attr(rankdir="LR", size="8,5")

    # Extract nodes + edges from compiled graph
    internal = graph.get_graph()

    for node in internal.nodes:
        dot.node(node)

    for edge in internal.edges:
        dot.edge(edge[0], edge[1])

    dot.render("agent_workflow", format="png", cleanup=True)
    print("Graph saved as agent_workflow.png")


if __name__ == "__main__":
    visualize()