from PyPDF2 import PdfReader
from docx import Document

# -----------------------------
# PDF TEXT EXTRACTION
# -----------------------------

def extract_pdf_text(pdf_path):

    text = ""

    try:
        reader = PdfReader(pdf_path)

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + " "

    except Exception as e:

        print(f"Error reading PDF file: {e}")

    return text


# -----------------------------
# DOCX TEXT EXTRACTION
# -----------------------------

def extract_docx_text(docx_path):

    text = ""

    try:
        doc = Document(docx_path)

        for para in doc.paragraphs:

            text += para.text + " "

    except Exception as e:

        print(f"Error reading DOCX file: {e}")

    return text


# -----------------------------
# RESUME TEXT EXTRACTION
# -----------------------------

def extract_resume_text(file_path):

    if file_path.endswith(".pdf"):

        return extract_pdf_text(file_path)

    elif file_path.endswith(".docx"):

        return extract_docx_text(file_path)

    else:

        return ""