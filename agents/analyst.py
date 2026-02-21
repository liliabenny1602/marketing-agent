from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0
)

def analyst_agent(state):
    data = state["metrics"]

    prompt = f"""
    You are a marketing performance analyst.

    Metrics:
    {data}

    Answer:
    1. What's underperforming?
    2. Why?
    3. What should be optimized first?
    """

    result = llm.invoke(prompt).content

    return {"analysis": result}