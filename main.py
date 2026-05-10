import os

from src.resume_parser import extract_resume_text
from src.text_cleaner import clean_text
from src.skill_matcher import extract_skills
from src.scorer import calculate_similarity
from src.report_generator import generate_report

# -----------------------------
# REQUIRED SKILLS
# -----------------------------

required_skills = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "machine learning",
    "apis",
    "git",
    "automation",
    "data analysis"
]

# -----------------------------
# LOAD JOB DESCRIPTION
# -----------------------------

with open("data/job_description.txt", "r", encoding="utf-8") as file:

    job_description = file.read()

job_description = clean_text(job_description)

# -----------------------------
# RESUME FOLDER
# -----------------------------

resume_folder = "resumes"

resume_results = []

# -----------------------------
# PROCESS EACH RESUME
# -----------------------------

for file_name in os.listdir(resume_folder):

    file_path = os.path.join(resume_folder, file_name)

    print(f"\nProcessing Resume: {file_name}")

    # Extract text
    resume_text = extract_resume_text(file_path)

    # Clean text
    cleaned_resume = clean_text(resume_text)

    # Extract skills
    matched_skills = extract_skills(
        cleaned_resume,
        required_skills
    )

    # Similarity score
    score = calculate_similarity(
        cleaned_resume,
        job_description
    )

    # Decision
    if score >= 20:
        decision = "Shortlisted"
    else:
        decision = "Rejected"

    # Store result
    resume_results.append({
        "Resume": file_name,
        "Score": score,
        "Matched Skills": ", ".join(matched_skills),
        "Decision": decision
    })

# -----------------------------
# GENERATE REPORT
# -----------------------------

output_file = "outputs/resume_screening_report.csv"

df = generate_report(
    resume_results,
    output_file
)

# -----------------------------
# DISPLAY RESULTS
# -----------------------------

print("\n========== SCREENING RESULTS ==========\n")

print(df)

print(f"\nCSV Report Saved: {output_file}")