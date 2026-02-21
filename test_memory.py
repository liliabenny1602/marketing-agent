from memory.vector_store import build_store, similarity_search

texts = [
    "Urgency headlines improve CTR",
    "High CPC indicates poor targeting",
    "ROAS below 1.5 means campaign losing money"
]

build_store(texts)

print(similarity_search("How to improve click rate?"))