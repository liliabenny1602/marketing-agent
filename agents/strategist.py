from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3", temperature=0)


def strategist_agent(state):

    tracer = state.get("tracer")
    if tracer:
        tracer.node_start("Strategist")

    analysis = state.get("analysis", "")
    memories = state.get("memories", [])

    prompt = f"""
You are a senior marketing strategist.

Analysis:
{analysis}

Relevant Past Learnings:
{memories}

Produce a clear optimization strategy.
"""

    result = llm.invoke(prompt).content

    if tracer:
        tracer.node_end("Strategist")

    return {"strategy": result}