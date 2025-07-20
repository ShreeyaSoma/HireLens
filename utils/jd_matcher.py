import re

def extract_keywords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return set(words)

def match_resume_to_jd(jd_text, resume_text):
    jd_keywords = extract_keywords(jd_text)
    resume_keywords = extract_keywords(resume_text)

    if not jd_keywords or not resume_keywords:
        return 0.0

    match_count = len(jd_keywords.intersection(resume_keywords))
    total_keywords = len(jd_keywords)
    return match_count / total_keywords if total_keywords > 0 else 0.0
