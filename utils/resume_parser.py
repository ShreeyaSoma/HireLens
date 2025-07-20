import fitz  # PyMuPDF
import spacy
import re

nlp = spacy.load("en_core_web_sm")

# Basic tech keywords list (expand as needed)
SKILL_KEYWORDS = [
    "python", "java", "sql", "excel", "react", "node", "aws", "docker", "flask",
    "django", "javascript", "html", "css", "tableau", "mongodb", "git", "github",
    "tensorflow", "pandas", "numpy", "power bi", "keras", "matplotlib"
]

def parse_resume(pdf_file):
    text = ""
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
    except:
        text = ""

    doc_nlp = nlp(text)
    sentences = [sent.text.strip() for sent in doc_nlp.sents]

    # Extract skills (exact keyword match)
    found_skills = []
    text_lower = text.lower()
    for skill in SKILL_KEYWORDS:
        if skill in text_lower:
            found_skills.append(skill)

    # Extract experience lines
    experience = [s for s in sentences if re.search(r"\bexperience\b|\byears\b|\bworked\b", s.lower())]

    return {
        "text": text,
        "skills": list(set(found_skills)),
        "experience": experience
    }
