# HireLens: AI-Powered Resume Screener

HireLens is a smart, Streamlit-based tool that analyzes multiple resumes against a job description and ranks candidates based on their fit — using NLP, TF-IDF, and cosine similarity.

## 🔍 Features
- Upload any number of PDF resumes
- Paste a job description
- Get instant match scores
- See extracted skills and experience from each resume
- Beautiful, interactive web UI (custom Streamlit theme)

## 🛠️ Tech Stack
- Python
- Streamlit
- spaCy
- scikit-learn
- PyMuPDF (for reading PDFs)

## ⚙️ Setup
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
