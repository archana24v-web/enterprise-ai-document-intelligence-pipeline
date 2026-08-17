import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.chunking import chunk_text
from src.quality_checks import validate_document

st.set_page_config(page_title="AI Document Intelligence", page_icon="📄")
st.title("AI Document Intelligence Pipeline")
st.caption("Upload text, validate data quality, and prepare document chunks for AI retrieval.")

uploaded = st.file_uploader("Upload a text file", type=["txt"])
if uploaded:
    text = uploaded.getvalue().decode("utf-8", errors="ignore")
    result = validate_document(text)
    st.json(result)
    if result["is_valid"]:
        chunks = chunk_text(text)
        st.success(f"Prepared {len(chunks)} chunks for embedding.")
        st.write(chunks[:3])
