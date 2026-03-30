import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_skills(text, required_skills):
    text_lower = text.lower()
    found_skills = []
    missing_skills = []
    for skill in required_skills:
        # Simple string match allows us to flag missing skills
        if skill.lower() in text_lower:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)
    return found_skills, missing_skills

def main():
    # 1. Load Data
    try:
        with open('data/job_description.txt', 'r') as f:
            jd_text = f.read()
        resumes_df = pd.read_csv('data/synthetic_resumes.csv')
    except FileNotFoundError:
        print("Data files not found. Please run resume_data_generator.py first.")
        return

    # Defined core required skills from the JD
    required_skills = ["Python", "SQL", "Machine Learning", "Deep Learning", "NLP", "AWS", "Docker", "Git"]

    # 2. Text Preprocessing
    print("Cleaning text data and setting up TF-IDF...")
    resumes_df['Clean_Resume'] = resumes_df['Resume_Text'].apply(clean_text)
    clean_jd = clean_text(jd_text)

    # 3. Compute TF-IDF Cosine Similarity
    # Fit vectorizer on the combined vocabulary (JD + Resumes)
    corpus = [clean_jd] + resumes_df['Clean_Resume'].tolist()
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(corpus)
    
    # JD is at index 0, resumes are index 1 onward
    jd_vector = tfidf_matrix[0]
    resume_vectors = tfidf_matrix[1:]
    
    # Calculate similarity score
    similarity_scores = cosine_similarity(jd_vector, resume_vectors)[0]
    resumes_df['Match_Percentage'] = np.round(similarity_scores * 100, 2)

    # 4. Explicit Skill Gap Analysis
    print("Performing skill gap analysis...")
    found_col = []
    missing_col = []
    for text in resumes_df['Resume_Text']:
        f_skills, m_skills = extract_skills(text, required_skills)
        found_col.append(", ".join(f_skills))
        missing_col.append(", ".join(m_skills))
        
    resumes_df['Found_Skills'] = found_col
    resumes_df['Missing_Skills'] = missing_col

    # 5. Rank Candidates Based on Match Percentage
    ranked_df = resumes_df.sort_values(by='Match_Percentage', ascending=False).reset_index(drop=True)
    
    print("\n--- Top 10 Ranked Candidates ---")
    print(ranked_df[['Candidate_ID', 'Match_Percentage', 'Missing_Skills']].head(10))
    
    output_cols = ['Candidate_ID', 'Match_Percentage', 'Found_Skills', 'Missing_Skills', 'Resume_Text']
    ranked_df[output_cols].to_csv('ranked_candidates.csv', index=False)
    print("\nSaved full ranking report to 'ranked_candidates.csv'")

    # 6. Automate Visual Delivery
    plt.figure(figsize=(10, 6))
    top_15 = ranked_df.head(15)
    
    # Color-code based on whether they are missing core "Machine Learning"
    colors = ['green' if 'Machine Learning' not in ms else 'orange' for ms in top_15['Missing_Skills']]
    
    plt.bar(top_15['Candidate_ID'], top_15['Match_Percentage'], color=colors)
    plt.title('Top 15 Candidates by TF-IDF Similarity Score', fontsize=14)
    plt.xlabel('Candidate ID', fontsize=12)
    plt.ylabel('Match Percentage against JD (%)', fontsize=12)
    plt.xticks(rotation=45)
    
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='green', label='Has ML Skill'),
                       Patch(facecolor='orange', label='Missing core ML Skill')]
    plt.legend(handles=legend_elements)
    
    plt.tight_layout()
    plt.savefig('candidate_ranking.png', dpi=300)
    print("Saved candidate ranking graph to 'candidate_ranking.png'")

if __name__ == "__main__":
    main()
