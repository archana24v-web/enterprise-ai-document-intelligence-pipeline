# Enterprise AI Document Intelligence Pipeline

A portfolio project that demonstrates an AI-ready data engineering workflow: document ingestion, quality validation, chunking, and a Streamlit interface for preparing content for retrieval-augmented generation (RAG).

## Features
- Document text quality checks
- Overlapping text chunking for embeddings
- Streamlit demo application
- Pytest unit tests
- GitHub Actions CI on every push and pull request

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Test
```bash
pytest -q
```

## Roadmap
- Add PDF ingestion
- Generate embeddings with Sentence Transformers
- Store vectors in ChromaDB
- Add semantic search and cited answers
- Containerize with Docker Compose
