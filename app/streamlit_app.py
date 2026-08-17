import sys
from pathlib import Path

import streamlit as st
from pypdf import PdfReader

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.chunking import chunk_text
from src.quality_checks import validate_document
from src.vector_store import build_index, semantic_search

st.set_page_config(page_title="AI Document Intelligence", page_icon="📄", layout="wide")
st.title("Enterprise AI Document Intelligence Pipeline")
st.caption("Ingest PDFs or text files, validate quality, create embeddings, and search semantically.")


def uploaded_text(uploaded_file) -> str:
    if uploaded_file.name.lower().endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    return uploaded_file.getvalue().decode("utf-8", errors="ignore")


uploaded = st.file_uploader("Upload a PDF or text document", type=["pdf", "txt"])
if uploaded:
    text = uploaded_text(uploaded)
    validation = validate_document(text)
    st.subheader("Data-quality result")
    st.json(validation)

    if validation["is_valid"] and st.button("Build AI search index"):
        chunks = chunk_text(text)
        with st.spinner("Creating embeddings and storing vectors..."):
            total = build_index(chunks)
        st.session_state["index_ready"] = True
        st.success(f"Indexed {total} document chunks.")

if st.session_state.get("index_ready"):
    st.divider()
    st.subheader("Semantic search")
    query = st.text_input("Ask a question about the uploaded document")
    if query and st.button("Search"):
        for result in semantic_search(query):
            st.markdown(f"**Chunk {result['chunk_number']}** · distance: {result['distance']}")
            st.write(result["text"])
