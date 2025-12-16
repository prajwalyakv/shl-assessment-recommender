SHL Assessment Recommendation Engine


OVERVIEW

This project implements a baseline Assessment Recommendation Engine that recommends relevant SHL assessments based on a given job description or required skill set. The system is designed to assist recruiters or hiring teams in selecting appropriate assessments aligned with job requirements.

PROBLEM STATEMENT

Given a job description, identify and recommend the most relevant SHL assessments by semantically matching job requirements with assessment descriptions and skill coverage.

APPROACH

Since SHL’s proprietary assessment catalogue is not publicly available, a representative synthetic dataset was created based on commonly used assessment categories (e.g., numerical reasoning, coding, data analysis).

The solution follows a baseline NLP approach:

Combine assessment descriptions and skills

Convert text into numerical vectors using TF-IDF

Compute similarity using Cosine Similarity

Rank assessments based on relevance scores

Provide explainability by highlighting matched skills

This approach is interpretable, scalable, and suitable as a strong baseline.

TECK STACK

Python

Pandas

Scikit-learn

Streamlit

PROJECT STRUCTURE
shl-assessment-recommender/
│
├── data/
│   └── shl_catalogue.csv
├── recommender.py
├── app.py
├── requirements.txt
└── README.md

HOW TO RUN

Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

FEATURES

Job-to-assessment semantic matching

Ranked recommendations

Explainable outputs (matched skills)

Simple, interactive UI

FUTURE IMPROVEMENTS

Use sentence embeddings (e.g., SBERT)

Support experience-level filtering

Integrate real SHL catalogue data

Add evaluation metrics and feedback loop