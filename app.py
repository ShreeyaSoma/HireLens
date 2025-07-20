import streamlit as st
from utils.resume_parser import parse_resume
from utils.jd_matcher import match_resume_to_jd

# Page setup
st.set_page_config(page_title="HireLens - Resume Screener", layout="wide")

# Title and intro
st.title("📄 HireLens")
st.subheader("AI-Powered Resume Screening Tool")
st.markdown("Upload resumes and a job description to get AI-ranked matches using smart keyword matching.")

# Sidebar
st.sidebar.title("👩‍💻 About HireLens")
st.sidebar.markdown("""
HireLens is an AI-powered resume screening tool designed to simplify candidate evaluation through automated skill and experience matching.

**Key Features:**
- 🔍 Smart keyword-based matching  
- 📄 Multiple resume uploads  
- 📊 Ranked match scores  
- 🎯 Skill & experience extraction  

**Built With:**
- Python  
- Streamlit   
- NLP & Regex   

Developed by **Shreeya Soma** with the vision of making recruitment smarter and faster.
""")

# JD Input
st.header("📋 Job Description")
jd_text = st.text_area("Paste the job description here:", height=250)

# Resume Upload
st.header("📁 Upload Resumes")
uploaded_files = st.file_uploader("Upload one or more resume PDFs:", type=["pdf"], accept_multiple_files=True)

st.markdown("---")
analyze = st.button("🔍 Analyze Resumes")

if analyze:
    if not jd_text:
        st.warning("⚠️ Please paste a job description first.")
    elif not uploaded_files:
        st.warning("⚠️ Please upload at least one resume.")
    else:
        st.info("⏳ Analyzing resumes...")
        results = []

        for file in uploaded_files:
            resume_data = parse_resume(file)
            match_score = match_resume_to_jd(jd_text, resume_data["text"])
            match_percent = round(match_score * 100, 2)

            print(f"\n📄 Resume: {file.name}")
            print(f"✅ Match Score: {match_percent}%")
            print(f"📝 Resume Snippet: {resume_data['text'][:300]}")

            results.append((file.name, match_percent, resume_data))

        results.sort(key=lambda x: x[1], reverse=True)
        top_score = results[0][1]

        if top_score < 20:
            st.warning("⚠️ No strong matches found.")
            st.info("Try using a broader job description or clearer resumes.")
        else:
            st.success("✅ Analysis complete!")

        for name, score, data in results:
            st.subheader(f"📌 {name}")
            st.markdown(f"**Match Score:** `{score}%`")

            if score >= 75:
                st.success("🎯 Strong Match!")
            elif score >= 50:
                st.info("🟡 Moderate Match")
            else:
                st.warning("⚠️ Low Match")

            st.markdown("**Top Skills Found:** " + ", ".join(data["skills"][:10] or ["None found"]))
            st.markdown("**Experience Snippets:**")
            if data["experience"]:
                for exp in data["experience"]:
                    st.markdown(f"- {exp}")
            else:
                st.write("No experience details found.")

            st.markdown("---")
