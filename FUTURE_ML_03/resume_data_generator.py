import pandas as pd
import numpy as np
import random
import os

os.makedirs('data', exist_ok=True)
np.random.seed(42)
random.seed(42)

def generate_job_description():
    jd = """
    We are looking for a Machine Learning Engineer to join our growing data team.
    
    Responsibilities:
    - Build and deploy scalable machine learning models to production.
    - Work with deep learning frameworks and natural language processing techniques.
    - Write clean, production-ready code in Python.
    - Query massive datasets using SQL to extract actionable insights.
    - Deploy models to AWS using Docker and Kubernetes.
    
    Required Skills:
    Python, SQL, Machine Learning, Deep Learning, NLP, AWS, Docker, Git.
    """
    with open('data/job_description.txt', 'w') as f:
        f.write(jd.strip())
    print("Generated data/job_description.txt")

def generate_candidate():
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Jamie", "Drew"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]
    
    # Core skills repository
    strong_ml_skills = ["Python", "Machine Learning", "Deep Learning", "NLP", "TensorFlow", "PyTorch"]
    data_eng_skills = ["SQL", "AWS", "Docker", "Kubernetes", "Spark", "Hadoop", "Airflow"]
    general_dev_skills = ["Git", "Java", "C++", "JavaScript", "HTML", "CSS", "React"]
    
    # Determine the candidate's "archetype"
    archetype = random.choice(["ML Expert", "Data Engineer", "Frontend Developer", "Generalist"])
    
    candidate_skills = []
    if archetype == "ML Expert":
        candidate_skills = random.sample(strong_ml_skills, k=4) + random.sample(data_eng_skills, k=1) + ["Python", "Git"]
    elif archetype == "Data Engineer":
        candidate_skills = random.sample(data_eng_skills, k=4) + random.sample(strong_ml_skills, k=1) + ["SQL", "Git"]
    elif archetype == "Frontend Developer":
        candidate_skills = random.sample(general_dev_skills, k=4) + ["JavaScript", "HTML"]
    else: # Generalist
        all_skills = strong_ml_skills + data_eng_skills + general_dev_skills
        candidate_skills = random.sample(all_skills, k=5)
        
    candidate_skills = list(set(candidate_skills))
    
    # Generate some experience text
    exp_templates = [
        f"Worked as a software developer using {candidate_skills[0]} and {candidate_skills[1]}.",
        f"Implemented a data pipeline utilizing {candidate_skills[0]} to improve efficiency.",
        f"Experienced professional highly skilled in {', '.join(candidate_skills[:3])}.",
        f"Deployed applications and models utilizing modern tools including {', '.join(candidate_skills)}."
    ]
    
    resume_text = f"Name: {random.choice(first_names)} {random.choice(last_names)}\n"
    resume_text += f"Summary: Dedicated professional with background in tech logistics.\n"
    resume_text += f"Experience: {random.choice(exp_templates)}\n"
    resume_text += f"Skills: {', '.join(candidate_skills)}\n"
    
    return resume_text, candidate_skills

def main():
    generate_job_description()
    
    data = []
    for i in range(100):
        text, true_skills = generate_candidate()
        data.append({
            "Candidate_ID": f"CAND-{i+1000}",
            "Resume_Text": text,
            "True_Skills": ", ".join(true_skills)
        })
        
    df = pd.DataFrame(data)
    df.to_csv('data/synthetic_resumes.csv', index=False)
    print("Generated data/synthetic_resumes.csv with 100 candidate profiles")

if __name__ == "__main__":
    main()
