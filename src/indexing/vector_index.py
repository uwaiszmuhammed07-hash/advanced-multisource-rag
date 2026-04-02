import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_vector_index(documents, collection_name="rag_collection"):
    client = chromadb.PersistentClient(path="storage/chroma_db")
    collection = client.get_or_create_collection(name=collection_name)

    ids = []
    texts = []
    metadatas = []

    for i, doc in enumerate(documents):
        ids.append(f"doc_{i}")
        texts.append(doc["text"])
        metadatas.append({
            "source": doc.get("source", "unknown"),
            "type": doc.get("type", "unknown")
        })

    embeddings = model.encode(texts).tolist()

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    return collection