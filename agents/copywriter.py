from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3", temperature=0.7)


def copywriter_agent(state):

    tracer = state.get("tracer")
    if tracer:
        tracer.node_start("Copywriter")

    strategy = state.get("strategy", "")

    prompt = f"""
You are an ad copywriter.

Strategy:
{strategy}

Generate 3 ad variants.
"""

    result = llm.invoke(prompt).content

    if tracer:
        tracer.node_end("Copywriter")

    return {"copy": result}