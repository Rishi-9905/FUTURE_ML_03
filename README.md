# FUTURE_ML_03
📄 An NLP-driven candidate screening system that mathematically ranks unstructured resumes against Job Descriptions using TF-IDF and Cosine Similarity.
# 📄 Resume & Candidate Screening System

## Overview
This project is an automated NLP-driven resume screener built for **Future Interns Task 3**. It systematically reads unstructured strings in candidate resumes, extracts core competencies, and mathematically ranks applicants based on their semantic similarity to a target Job Description (JD). 

## Features
- **Data Synthesis Engine**: `resume_data_generator.py` synthetically generates a complete "Machine Learning Engineer" Job Description alongside 100 uniquely templated applicant profiles mapping to different tech archetypes (ML Experts, Frontend, Data Engineering, Generalists).
- **Intelligent Matching Logic**: `screening_pipeline.py` cleans text, explicitly tracks required keywords, and calculates **TF-IDF Cosine Similarity** to determine the absolute percentage match between each candidate string and the target JD string.
- **Automated KPI Extraction**: Dynamically ranks applicants and flags explicitly missing mandatory skills, outputting a business-ready tabular ledger (`ranked_candidates.csv`) and a visual Match Percentage Bar Chart (`candidate_ranking.png`).

## Usage
1. Run `python resume_data_generator.py` to compile the mock `job_description.txt` constraint and the `synthetic_resumes.csv` dataset.
2. Run `python screening_pipeline.py` to ingest the documents, map the TF-IDF feature vectors, compute mathematical similarity scoring, and output the final rankings and visual charts.
