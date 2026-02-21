from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3", temperature=0)

def strategist_agent(state):
    analysis = state["analysis"]
    memories = state.get("memories", [])

    prompt = f"""
You are a senior marketing strategist.

Current Analysis:
{analysis}

Relevant Past Campaign Learnings:
{memories}

Using both, produce a precise optimization strategy.
"""

    result = llm.invoke(prompt).content

    return {"strategy": result}