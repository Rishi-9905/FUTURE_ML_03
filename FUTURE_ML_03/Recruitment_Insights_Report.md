# Recruitment Insights: Automated Resume Screening Report

## How Resumes Are Scored

Our screening system uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to mathematically compare a candidate's unstructured resume text against the specific target Job Description (JD) for the Machine Learning Engineer role.
- **TF-IDF** translates text into a numerical matrix by giving highest mathematical importance to unique, highly-relevant keywords (e.g., "TensorFlow", "Kubernetes") rather than generic filler words (e.g., "the", "worked").
- **Cosine Similarity** then calculates the geometric angle between the Resume's word-vector and the Job Description's word-vector. A mathematically identical document yields a 100% score, whereas no shared words yield a 0%.

## Why Certain Candidates Rank Higher

In our test pool of 100 candidates, top applicants like **CAND-1000** and **CAND-1016** achieved the highest similarity scores (~36.5%). 
This is because their unstructured resume narratives contained dense semantic clusters of the context required by the JD. Their profiles naturally possessed strong "ML Expert" traits, utilizing critical tools like *Deep Learning*, *Python*, and *PyTorch*, explicitly mapping to the heaviest-weighted demands of the job posting.

Conversely, candidates with strong "Frontend Developer" or purely qualitative backgrounds scored lowest because their text focused heavily on *HTML*, *React*, and *CSS*—terms entirely absent and irrelevant to the ML Engineer criteria.

## Identifying What Skills Are Missing

While a matched percentage is useful for ranking a leaderboard, recruiters also require transparent evidence of *why* a candidate might fail a technical interview later on.
The NLP system actively parses and flags resumes against a strict requirement list. For example, in our top 10 outputs:
- **CAND-1000** ranked #1 overall due to dense ML phrasing, but the system explicitly flagged they are entirely missing: `SQL, NLP, Docker`.
- **CAND-1074** ranked reasonably well (#7), but the system caught that they are missing the absolute core pillars: `Python, Machine Learning, NLP`. 

A recruiter or hiring manager can view these missing-skill flags immediately and reject candidates without wasting 15 minutes manually reading the PDF.

## Final Deliverables Generated
- `candidate_ranking.png`: A bar chart tracking the top 15 candidates by total match score, color-coded orange if the candidate is completely missing the core "Machine Learning" text requirement despite having other ML-adjacent words.
- `ranked_candidates.csv`: The master spreadsheet allowing HR to instantly sort the 100 candidates by Match Percentage, or filter out anyone missing mandatory tools.
