# streamlit run app.py
import streamlit as st
import pandas as pd

df = pd.read_csv("roommates_clean_for_tableau.csv")
match_df = pd.read_csv("roommate_top5_matches.csv")

st.title("Roommate Recommendations")
name = st.selectbox("Select your profile", sorted(df["Name"].dropna().unique()))
k = st.slider("Top-K", 1, 10, 5)

sub = match_df.query("me == @name").head(k)
st.write(sub[["candidate","score","reasons"]])