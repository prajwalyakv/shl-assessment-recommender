import streamlit as st
from recommender import recommend_assessments

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

st.title("SHL Assessment Recommendation Engine")
st.write(
    "Enter a job description or required skills to get recommended SHL assessments."
)

job_desc = st.text_area(
    "Job Description / Required Skills",
    placeholder="e.g. Data analyst with Python, SQL and analytical skills",
)

top_n = st.slider("Number of recommendations", 1, 5, 3)

if st.button("Recommend Assessments"):
    if job_desc.strip() == "":
        st.warning("Please enter a job description.")
    else:
        results = recommend_assessments(job_desc, top_n)

        st.subheader("Recommended Assessments")
        for _, row in results.iterrows():
            st.markdown(f"### {row['assessment_name']}")
            st.write(f"**Similarity Score:** {row['similarity_score']:.2f}")
            st.write(f"**Matched Skills:** {row['matched_skills']}")
