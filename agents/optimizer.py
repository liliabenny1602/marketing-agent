from langchain_ollama import ChatOllama
from tools.ads_api import update_budget

llm = ChatOllama(model="phi3", temperature=0)


def optimizer_agent(state):

    tracer = state.get("tracer")
    if tracer:
        tracer.node_start("Optimizer")

    metrics = state.get("metrics", {})
    strategy = state.get("strategy", "")

    prompt = f"""
You are a campaign optimizer.

Metrics:
{metrics}

Strategy:
{strategy}

Output JSON:
{{
 "action": "...",
 "percent": number
}}
"""

    decision = llm.invoke(prompt).content

    # deterministic rule layer
    if metrics.get("roas", 0) < 1.5:
        execution = update_budget(metrics.get("campaign", "Campaign"), 20)
    else:
        execution = "No change required"

    if tracer:
        tracer.node_end("Optimizer")

    return {
        "decision": decision,
        "execution": execution
    }