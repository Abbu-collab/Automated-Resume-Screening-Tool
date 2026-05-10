# 📄 Automated Resume Screening Tool

An AI/NLP-powered Resume Screening and ATS (Applicant Tracking System) simulation project developed using Python and Streamlit.

This project automatically:
- extracts resume text from PDF/DOCX
- compares resumes with job descriptions
- performs skill matching
- calculates ATS similarity scores
- ranks candidates
- shortlists/rejects resumes
- generates downloadable reports

---

# 🚀 Features

✅ Resume Upload (PDF & DOCX)  
✅ Multiple Resume Screening  
✅ Job Description Upload  
✅ Manual JD Input  
✅ Required Skills Matching  
✅ ATS Resume Scoring  
✅ TF-IDF + Cosine Similarity  
✅ Candidate Ranking  
✅ Shortlisted / Rejected Decision  
✅ CSV Report Download  
✅ Interactive Streamlit Dashboard  
✅ Large Excel-like Data Table  
✅ Resume Analytics & Charts  

---

# 🧠 Project Workflow

```text
Resume Upload
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Skill Extraction
      ↓
Job Description Matching
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity Scoring
      ↓
Resume Ranking
      ↓
Shortlist / Reject Decision
      ↓
CSV Report Generation
```

---

# 🏢 Industry Relevance

This project simulates how real ATS systems work in companies and HR teams.

Useful for:
- HR Tech
- Recruitment Automation
- NLP Projects
- Python Development
- Data Analytics
- AI-based Screening Systems

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Streamlit | Interactive Dashboard |
| Pandas | Data Handling |
| NumPy | Numerical Operations |
| Scikit-learn | TF-IDF & Cosine Similarity |
| PyPDF2 | PDF Text Extraction |
| python-docx | DOCX Text Extraction |
| Regex | Text Cleaning |

---

# 📂 Project Structure

```text
Automated-Resume-Screening-Tool/
│
├── resumes/
│   ├── sample_resume1.pdf
│   ├── sample_resume2.docx
│
├── data/
│   └── full_stack_developer_jd.txt
│
├── outputs/
│   └── resume_screening_report.csv
│
├── src/
│   ├── resume_parser.py
│   ├── scorer.py
│   ├── skill_matcher.py
│   ├── text_cleaner.py
│   └── report_generator.py
│
├── images/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

---

## 2️⃣ Open Project Folder

```bash
cd Automated-Resume-Screening-Tool
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

## Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

# 📤 How To Use

## Step 1
Upload Job Description:
- TXT file
OR
- Paste manually

---

## Step 2
Enter Required Skills:
Example:

```text
Python, SQL, React.js, APIs, Git
```

---

## Step 3
Upload Resumes:
- PDF
- DOCX

---

## Step 4
Click:

```text
Start Screening
```

---

# 📊 Output

The dashboard displays:

- Resume Name
- ATS Score
- Matched Skills
- Total Skills Matched
- Shortlisted / Rejected Status

---

# 📈 Dashboard Features

✅ Full Width Excel-like Table  
✅ Search & Filtering  
✅ Score Analytics  
✅ Resume Ranking  
✅ Charts & Metrics  
✅ CSV Export  

---

# 📷 Screenshots To Add

Add screenshots inside `images/` folder.

Suggested screenshots:
- Dashboard Home
- Resume Upload
- Job Description Upload
- Screening Results
- Shortlisted Candidates
- Rejected Candidates
- Charts & Analytics
- CSV Download

---

# 🧪 Example Job Description

```text
Looking for a Full Stack Developer with skills in:
HTML, CSS, JavaScript, React.js, Python,
Node.js, SQL, MongoDB, APIs, Git
```

---

# 🧠 ATS Logic Used

The system uses:
- TF-IDF Vectorization
- Cosine Similarity
- Skill Matching
- Keyword Analysis

to calculate resume-job similarity scores.

---

# 📋 Example Output

| Resume | Score | Decision |
|---|---|---|
| python_resume.pdf | 89.4 | Shortlisted |
| fullstack_resume.docx | 75.2 | Shortlisted |
| java_resume.pdf | 18.5 | Rejected |

---

# 🎯 Learning Outcomes

By building this project, you will learn:

- NLP Basics
- Resume Parsing
- ATS Systems
- TF-IDF
- Cosine Similarity
- Python Automation
- Streamlit Dashboard Development
- GitHub Project Management

---

# 🔮 Future Improvements

- AI Skill Prediction
- Semantic NLP Matching
- Resume Recommendation System
- Database Integration
- Recruiter Login System
- Authentication
- Cloud Deployment
- Resume Upload History

---

# 👨‍💻 Author

Shaik Abbu Bakar

B.Tech CSE Student  
Python Developer | AI/NLP Enthusiast | Full Stack Learner

---

# ⭐ GitHub Topics

```text
python
streamlit
nlp
resume-screening
ats
machine-learning
automation
tfidf
cosine-similarity
hr-tech
```

---

# 📚 Official Documentation

- Python: https://docs.python.org/3/
- Streamlit: https://docs.streamlit.io
- Scikit-learn: https://scikit-learn.org
- PyPDF2: https://pypdf2.readthedocs.io
- python-docx: https://python-docx.readthedocs.io
