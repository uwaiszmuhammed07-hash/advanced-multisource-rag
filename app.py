import os
import streamlit as st

from src.loaders.pdf_loader import load_pdf
from src.loaders.csv_loader import load_csv
from src.loaders.web_loader import load_web
from src.processing.cleaner import clean_text
from src.processing.chunker import chunk_text
from src.retrieval.vector_retriever import retrieve_top_k
from src.llm.response_generator import generate_answer

st.set_page_config(page_title="Multi-Source RAG", layout="wide")
st.title("Advanced Multi-Source RAG for Enterprise Knowledge Base")
st.write("Upload PDF / CSV or enter website URL, then ask questions.")

uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])
uploaded_csv = st.file_uploader("Upload CSV", type=["csv"])
website_url = st.text_input("Enter Website URL")
query = st.text_input("Ask your question")

documents = []

if uploaded_pdf:
    pdf_path = os.path.join("data/pdfs", uploaded_pdf.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.read())
    documents.extend(load_pdf(pdf_path))

if uploaded_csv:
    csv_path = os.path.join("data/csv", uploaded_csv.name)
    with open(csv_path, "wb") as f:
        f.write(uploaded_csv.read())
    documents.extend(load_csv(csv_path))

if website_url:
    try:
        documents.extend(load_web(website_url))
    except Exception as e:
        st.error(f"Website loading failed: {e}")

processed_docs = []
for doc in documents:
    cleaned = clean_text(doc["text"])
    chunks = chunk_text(cleaned, chunk_size=700, overlap=150)

    for chunk in chunks:
        processed_docs.append({
            "text": chunk,
            "source": doc["source"],
            "type": doc["type"]
        })

if processed_docs:
    if query:
        results = retrieve_top_k(processed_docs, query, k=5)

        docs = results["documents"][0]
        metas = results["metadatas"][0]

        if docs:
            answer = generate_answer(query, docs)

            st.subheader("Final Answer")
            st.write(answer)

            st.subheader("Retrieved Chunks")
            for i, (doc, meta) in enumerate(zip(docs, metas), start=1):
                st.markdown(f"### Result {i}")
                st.write(doc)
                st.caption(f"Source: {meta['source']} | Type: {meta['type']}")
        else:
            st.warning("No matching results found.")
else:
    st.info("Please upload a PDF/CSV or enter a website URL first.")