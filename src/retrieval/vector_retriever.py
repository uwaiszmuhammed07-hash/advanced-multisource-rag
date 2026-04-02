def retrieve_top_k(collection, query, k=5):
    query_words = set(query.lower().split())
    scored_docs = []

    for doc in collection:
        text = doc["text"].lower()
        source_type = doc.get("type", "unknown")

        overlap = sum(1 for word in query_words if word in text)

        bonus = 0
        if source_type == "website":
            bonus += 3

        score = overlap + bonus

        if score > 0:
            scored_docs.append((score, doc))

    scored_docs.sort(key=lambda x: x[0], reverse=True)
    top_docs = [item[1] for item in scored_docs[:k]]

    return {
        "documents": [[doc["text"] for doc in top_docs]],
        "metadatas": [[
            {
                "source": doc.get("source", "unknown"),
                "type": doc.get("type", "unknown")
            }
            for doc in top_docs
        ]]
    }