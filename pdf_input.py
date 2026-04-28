"""
Read a PDF file from the command line and print its extracted text.

Usage:
    python pdf_input.py path/to/resume.pdf

Install one PDF reader package first if needed:
    pip install pypdf
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable


def load_pdf_reader():
    """Return an installed PDF reader class, or raise a helpful error."""
    try:
        from pypdf import PdfReader

        return PdfReader
    except ImportError:
        try:
            from PyPDF2 import PdfReader

            return PdfReader
        except ImportError as exc:
            raise RuntimeError(
                "No PDF reader is installed. Run: pip install pypdf"
            ) from exc


def extract_pdf_text(pdf_path: Path) -> str:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a .pdf file, got: {pdf_path.name}")

    PdfReader = load_pdf_reader()
    reader = PdfReader(str(pdf_path))
    page_text: Iterable[str] = (
        page.extract_text() or "" for page in reader.pages
    )
    return "\n\n".join(text.strip() for text in page_text if text.strip())


def main() -> None:
    parser = argparse.ArgumentParser(description="Take a PDF as input.")
    parser.add_argument("pdf", type=Path, help="Path to the PDF file")
    args = parser.parse_args()

    text = extract_pdf_text("resume.pdf")

    if not text:
        print("No readable text was found in this PDF.")
        return

    print(text)


if __name__ == "__main__":
    main()
