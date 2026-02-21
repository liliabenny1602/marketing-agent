from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0
)

def copywriter_agent(state):
    strategy = state["strategy"]

    prompt = f"""
    You are an ad copywriter.

    Strategy:
    {strategy}

    Generate 3 ad variations.
    """

    result = llm.invoke(prompt).content

    return {"copy": result}