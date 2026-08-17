from pathlib import Path
from pypdf import PdfReader


def extract_pdf_text(path: str) -> str:
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def list_pdf_files(directory: str) -> list[Path]:
    return sorted(Path(directory).glob("*.pdf"))
