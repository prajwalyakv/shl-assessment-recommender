import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_assessments(job_description, top_n=3):
    """
    Recommends top N SHL assessments based on job description
    and explains why they were selected.
    """

    df = pd.read_csv("data/shl_catalogue.csv")

    # Combine text fields
    df["combined_text"] = (
        df["description"].fillna("").astype(str)
        + " "
        + df["skills"].fillna("").astype(str)
    )

    # Vectorization
    vectorizer = TfidfVectorizer(stop_words="english")
    assessment_vectors = vectorizer.fit_transform(df["combined_text"])
    job_vector = vectorizer.transform([job_description])

    # Similarity
    similarity_scores = cosine_similarity(job_vector, assessment_vectors)[0]
    df["similarity_score"] = similarity_scores

    # Extract keywords
    job_tokens = set(job_description.lower().split())

    explanations = []
    for skills in df["skills"]:
        skill_tokens = set(skills.lower().split())
        matched = job_tokens.intersection(skill_tokens)
        explanations.append(", ".join(matched) if matched else "General relevance")

    df["matched_skills"] = explanations

    # Top recommendations
    recommendations = df.sort_values(
        by="similarity_score", ascending=False
    ).head(top_n)

    return recommendations[
        ["assessment_name", "similarity_score", "matched_skills"]
    ]
