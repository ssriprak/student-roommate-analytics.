# 🏠 Student Roommate Analytics & Recommendation System

This project helps match students with potential roommates based on lifestyle preferences, food habits, smoking/alcohol preferences, campus location, and other attributes.  

It combines **data cleaning, analytics, and machine learning** to generate roommate recommendations, visualize insights with Tableau, and provide an interactive interface via Streamlit.  

---

## 📂 Project Structure
Student Roommate Analytics/
│── cleaned_names.csv               # Cleaned dataset (after initial preprocessing)
│── roommates_clean_for_tableau.csv # Processed dataset ready for Tableau/ML
│── roommate_top5_matches.csv       # Final match recommendations
│── notebooks/                      # Jupyter notebooks (EDA, cleaning, modeling)
│── app.py                          # Streamlit app for recommendations
│── README.md                       # Project documentation

---

## 🚀 Features
- **Data Cleaning & Preprocessing**
  - Standardized inconsistent entries (program names, food preferences, yes/no values).
  - Converted names into anonymized short form (e.g., `S Sripr`).
  - Removed duplicates and handled missing values.

- **Exploratory Data Analysis (EDA)**
  - Summary stats on demographics (age, gender, state, program).
  - Distribution of lifestyle preferences (smoking, alcohol, music, food).
  - Correlation analysis between attributes.

- **Recommendation System**
  - **Hard filters** (e.g., strict vegetarian ≠ non-vegetarian, non-smoker ≠ smoker).
  - **Cosine similarity** on weighted features (campus, housing, food, habits).
  - Generates **Top-K roommate matches** for each student with reasons.

- **Visualization**
  - Tableau dashboards showing demographics, preferences, and compatibility stats.

- **Streamlit App**
  - Simple interface to select a student and view top roommate matches.
  - Shows similarity score + reasons for each match.

---

## 🛠️ Tech Stack
- **Python**: pandas, numpy, scikit-learn  
- **Visualization**: Tableau, Streamlit  
- **Storage**: CSV (PostgreSQL/BigQuery optional)  
- **Other Tools**: Jupyter Notebook, GitHub  

---

## 📊 Example KPIs / Insights
- % of students preferring on-campus vs off-campus housing  
- Food preference distribution (Veg / Eggetarian / Non-veg)  
- % smokers, alcohol-friendly students  
- Most common ASU campus preferences  
- Average similarity score per student  

