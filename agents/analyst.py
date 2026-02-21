from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3", temperature=0)


def analyst_agent(state):

    tracer = state.get("tracer")
    if tracer:
        tracer.node_start("Analyst")

    metrics = state.get("metrics", {})

    prompt = f"""
You are a marketing performance analyst.

Metrics:
{metrics}

Answer:
1. What's underperforming?
2. Why?
3. What should be optimized first?
"""

    result = llm.invoke(prompt).content

    if tracer:
        tracer.node_end("Analyst")

    return {"analysis": result}