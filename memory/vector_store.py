import os
from typing import List

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# ---------- EMBEDDING MODEL ----------

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# ---------- BUILD STORE ----------

def build_store(texts: List[str], save_path: str = "faiss_index"):
    embeddings = get_embeddings()

    store = FAISS.from_texts(texts, embeddings)

    store.save_local(save_path)
    return store


# ---------- LOAD STORE ----------

def load_store(save_path: str = "faiss_index"):
    embeddings = get_embeddings()

    if not os.path.exists(save_path):
        raise FileNotFoundError("Vector store not found. Build it first.")

    return FAISS.load_local(
        save_path,
        embeddings,
        allow_dangerous_deserialization=True
    )


# ---------- RETRIEVAL ----------

def similarity_search(query: str, k: int = 3):
    store = load_store()
    docs = store.similarity_search(query, k=k)
    return [d.page_content for d in docs]


def mmr_search(query: str, k: int = 3):
    store = load_store()
    docs = store.max_marginal_relevance_search(query, k=k)
    return [d.page_content for d in docs]