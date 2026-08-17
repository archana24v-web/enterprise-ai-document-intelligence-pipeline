# Enterprise AI Document Intelligence Pipeline

A production-style AI data engineering portfolio project that turns unstructured PDFs and text documents into a searchable knowledge base. It demonstrates ingestion, data-quality validation, chunking, vector embeddings, semantic retrieval, automated tests, and CI.

## Architecture

```text
PDF / TXT upload
      |
      v
Text extraction -> data-quality checks -> overlapping chunking
      |
      v
Sentence Transformer embeddings -> ChromaDB vector store
      |
      v
Streamlit semantic-search interface
```

## Features

- Upload PDF and TXT documents
- Extract and validate document text
- Chunk content with overlap for retrieval
- Generate embeddings using `all-MiniLM-L6-v2`
- Store vectors locally in ChromaDB
- Retrieve the most semantically relevant chunks for a question
- Run unit tests with Pytest on every push and pull request
- Run locally or in Docker

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

Open `http://localhost:8501`, upload a document, select **Build AI search index**, then ask a question. The first embedding run downloads the open-source model.

## Tests

```bash
pytest -q
```

## Docker

```bash
docker build -t ai-document-intelligence .
docker run -p 8501:8501 ai-document-intelligence
```

## Engineering practices

- Unit tests for chunking and document validation
- GitHub Actions CI workflow
- Modular ingestion, quality, chunking, and vector-store components
- No API key is required for the local semantic-search demo

## Roadmap

- Add source citations and answer generation with an LLM
- Add metadata filtering and document lineage
- Add Docker Compose and object storage
- Deploy the Streamlit application
