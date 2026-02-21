from tools.ads_api import update_budget
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0
)

def optimizer_agent(state):
    metrics = state["metrics"]
    strategy = state["strategy"]

    prompt = f"""
    You are a campaign optimizer.

    Metrics: {metrics}
    Strategy: {strategy}

    Output JSON:
    {{
        "action": "...",
        "percent": number
    }}
    """

    decision = llm.invoke(prompt).content

    # rule safety layer
    if metrics["roas"] < 1.5:
        result = update_budget(metrics["campaign"], 20)
    else:
        result = "No change required"

    return {"decision": decision, "execution": result}