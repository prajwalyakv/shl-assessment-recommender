# **SHL ASSESSMENT RECOMMENDATION ENGINE**

---

## **PROJECT OVERVIEW**

This project implements an **Assessment Recommendation Engine** designed to automate the mapping of job requirements to candidate evaluations. By leveraging **Natural Language Processing (NLP)**, the system suggests the most relevant **SHL assessments** based on a job description or a specific skill set.

---

## **PROBLEM STATEMENT**

Recruiters often face challenges in identifying which specific assessments best measure the unique requirements of a new role. This tool addresses that gap by **semantically matching job descriptions with assessment metadata** to enable **data-driven hiring decisions**.

---

## **TECHNICAL APPROACH**

The solution follows a structured **NLP pipeline** to ensure both **accuracy and interpretability**:

### 1. Data Synthesis

A representative dataset of SHL assessment categories was created, including:

* Numerical Reasoning
* Coding Assessments
* Verbal Reasoning

### 2. Feature Engineering

Assessment descriptions and skill tags were consolidated into a **unified text corpus** for analysis.

### 3. Vectorization

**TF-IDF (Term Frequency–Inverse Document Frequency)** was used to transform text into high-dimensional numerical vectors.

### Similarity Scoring

**Cosine Similarity** was applied to compute the semantic distance between:

* Job description vectors
* Assessment catalogue vectors

---

## **TECHNICAL STACK**

| Component         | Technology   |
| ----------------- | ------------ |
| Language          | Python       |
| Data Manipulation | Pandas       |
| Machine Learning  | Scikit-learn |
| Web Interface     | Streamlit    |

---

## **PROJECT STRUCTURE**

```plaintext
shl-assessment-recommender/
├── data/
│   └── shl_catalogue.csv   # Synthetic assessment dataset
├── recommender.py          # Core ML logic and NLP pipeline
├── app.py                  # Streamlit UI and interaction layer
├── requirements.txt        # Environment dependencies
└── README.md               # Project documentation
```

---

## **INSTALLATION AND USAGE**

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Launch the Application

```bash
streamlit run app.py
```

---

## **KEY FEATURES**

* **Semantic Matching**
  Identifies relevance beyond simple keyword matching by understanding contextual similarity.

* **Ranked Recommendations**
  Outputs a prioritized list of assessments along with similarity scores.

* **Explainability**
  Displays matched skills to provide transparency on why specific assessments were selected.

* **Streamlined UI**
  A clean, professional interface designed for ease of use by recruitment teams.

---

## **FUTURE ROADMAP**

* **Advanced Embeddings**
  Integration of Sentence-BERT (SBERT) for deeper semantic understanding.

* **Experience Filtering**
  Logic to categorize assessments by seniority (e.g., Junior vs. Executive).

* **Feedback Integration**
  Implementation of a feedback loop to refine recommendation accuracy based on recruiter input.

---


