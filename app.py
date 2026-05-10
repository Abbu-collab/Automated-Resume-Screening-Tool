import streamlit as st
import pandas as pd
import re

from PyPDF2 import PdfReader
from docx import Document

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening Tool",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.stButton>button {
    width: 100%;
    height: 3em;
    border-radius: 10px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📄 AI-Powered Resume Screening Tool")

st.write("""
Upload resumes and a job description to automatically
screen candidates using NLP and ATS logic.
""")

# ---------------------------------------------------
# CLEAN TEXT
# ---------------------------------------------------

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()

# ---------------------------------------------------
# PDF EXTRACTION
# ---------------------------------------------------

def extract_pdf_text(pdf_file):

    text = ""

    try:

        reader = PdfReader(pdf_file)

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted + " "

    except Exception as e:

        st.error(f"PDF Error: {e}")

    return text

# ---------------------------------------------------
# DOCX EXTRACTION
# ---------------------------------------------------

def extract_docx_text(docx_file):

    text = ""

    try:

        doc = Document(docx_file)

        for para in doc.paragraphs:

            text += para.text + " "

    except Exception as e:

        st.error(f"DOCX Error: {e}")

    return text

# ---------------------------------------------------
# SKILL EXTRACTION
# ---------------------------------------------------

def extract_skills(text, skills):

    matched = []

    for skill in skills:

        if skill in text:

            matched.append(skill)

    return matched

# ---------------------------------------------------
# SIMILARITY SCORE
# ---------------------------------------------------

def calculate_score(resume_text, jd_text):

    documents = [
        resume_text,
        jd_text
    ]

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    score = round(similarity * 100, 2)

    return score

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("📂 Upload Files")

# ---------------------------------------------------
# JOB DESCRIPTION INPUT
# ---------------------------------------------------

jd_option = st.sidebar.radio(
    "Job Description Input Method",
    [
        "Upload TXT File",
        "Manual Input"
    ]
)

job_description = ""

# ---------------------------------------------------
# TXT FILE INPUT
# ---------------------------------------------------

if jd_option == "Upload TXT File":

    jd_file = st.sidebar.file_uploader(
        "Upload Job Description TXT File",
        type=["txt"]
    )

    if jd_file:

        job_description = jd_file.read().decode("utf-8")

# ---------------------------------------------------
# MANUAL INPUT
# ---------------------------------------------------

else:

    job_description = st.sidebar.text_area(
        "Paste Job Description",
        height=250
    )

# ---------------------------------------------------
# REQUIRED SKILLS INPUT
# ---------------------------------------------------

skills_input = st.sidebar.text_area(
    "Required Skills (comma separated)",
    value="Python, SQL, Pandas, NumPy, Machine Learning, APIs, Git"
)

required_skills = [
    skill.strip().lower()
    for skill in skills_input.split(",")
]

# ---------------------------------------------------
# RESUME UPLOAD
# ---------------------------------------------------

uploaded_resumes = st.sidebar.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

# ---------------------------------------------------
# PROCESS BUTTON
# ---------------------------------------------------

process = st.sidebar.button(
    "🚀 Start Screening"
)

# ---------------------------------------------------
# MAIN PROCESS
# ---------------------------------------------------

if process:

    if not uploaded_resumes:

        st.warning("Please upload resumes.")

    elif not job_description:

        st.warning("Please provide job description.")

    else:

        cleaned_jd = clean_text(job_description)

        results = []

        # ---------------------------------------------------
        # PROCESS EACH RESUME
        # ---------------------------------------------------

        for uploaded_file in uploaded_resumes:

            file_name = uploaded_file.name

            st.subheader(f"📄 Processing: {file_name}")

            # ---------------------------------------------------
            # EXTRACT TEXT
            # ---------------------------------------------------

            if file_name.endswith(".pdf"):

                resume_text = extract_pdf_text(
                    uploaded_file
                )

            elif file_name.endswith(".docx"):

                resume_text = extract_docx_text(
                    uploaded_file
                )

            else:

                resume_text = ""

            # ---------------------------------------------------
            # CLEAN TEXT
            # ---------------------------------------------------

            cleaned_resume = clean_text(
                resume_text
            )

            # ---------------------------------------------------
            # SKILLS
            # ---------------------------------------------------

            matched_skills = extract_skills(
                cleaned_resume,
                required_skills
            )

            # ---------------------------------------------------
            # SCORE
            # ---------------------------------------------------

            score = calculate_score(
                cleaned_resume,
                cleaned_jd
            )

            # ---------------------------------------------------
            # SHORTLIST LOGIC
            # ---------------------------------------------------

            if score >= 20:

                decision = "Shortlisted"

            else:

                decision = "Rejected"

            # ---------------------------------------------------
            # STORE RESULTS
            # ---------------------------------------------------

            results.append({
                "Resume": file_name,
                "Score": score,
                "Matched Skills": ", ".join(matched_skills),
                "Total Skills Matched": len(matched_skills),
                "Decision": decision
            })

        # ---------------------------------------------------
        # CREATE DATAFRAME
        # ---------------------------------------------------

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Score",
            ascending=False
        )

        # ---------------------------------------------------
        # METRICS
        # ---------------------------------------------------

        total = len(df)

        shortlisted = len(
            df[df["Decision"] == "Shortlisted"]
        )

        rejected = len(
            df[df["Decision"] == "Rejected"]
        )

        average_score = round(
            df["Score"].mean(),
            2
        )

        highest_score = round(
            df["Score"].max(),
            2
        )

        # ---------------------------------------------------
        # DISPLAY METRICS
        # ---------------------------------------------------

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric(
            "📁 Total Resumes",
            total
        )

        col2.metric(
            "✅ Shortlisted",
            shortlisted
        )

        col3.metric(
            "❌ Rejected",
            rejected
        )

        col4.metric(
            "📊 Average Score",
            average_score
        )

        col5.metric(
            "🏆 Highest Score",
            highest_score
        )

        st.divider()

        # ---------------------------------------------------
        # MAIN TABLE
        # ---------------------------------------------------

        st.subheader("📋 Resume Screening Results")

        st.dataframe(
            df,
            use_container_width=True,
            height=500
        )

        # ---------------------------------------------------
        # SHORTLISTED TABLE
        # ---------------------------------------------------

        st.subheader("✅ Shortlisted Candidates")

        shortlisted_df = df[
            df["Decision"] == "Shortlisted"
        ]

        st.dataframe(
            shortlisted_df,
            use_container_width=True,
            height=250
        )

        # ---------------------------------------------------
        # REJECTED TABLE
        # ---------------------------------------------------

        st.subheader("❌ Rejected Candidates")

        rejected_df = df[
            df["Decision"] == "Rejected"
        ]

        st.dataframe(
            rejected_df,
            use_container_width=True,
            height=250
        )

        # ---------------------------------------------------
        # SCORE CHART
        # ---------------------------------------------------

        st.subheader("📈 Resume Scores")

        st.bar_chart(
            df.set_index("Resume")["Score"]
        )

        # ---------------------------------------------------
        # DOWNLOAD CSV
        # ---------------------------------------------------

        csv = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="📥 Download CSV Report",
            data=csv,
            file_name="resume_screening_report.csv",
            mime="text/csv"
        )

        st.success(
            "Screening Completed Successfully!"
        )

else:

    st.info("""
    Upload job description and resumes,
    then click 'Start Screening'
    """)