
import streamlit as st
import pickle
import pandas as pd
import numpy as np
from fuzzywuzzy import process

# Load datasets
movies_df = pd.read_csv("movies.csv").head(50000)

# Load trained models
def load_models():
    with open("tfidf_model.pkl", "rb") as f:
        tfidf, cosine_sim = pickle.load(f)
    with open("als_model.pkl", "rb") as f:
        als_model, movie_columns = pickle.load(f)
    return tfidf, cosine_sim, als_model, movie_columns

# Fuzzy Matching Function
def get_closest_match(title):
    best_match = process.extractOne(title, movies_df["title"].dropna())[0]
    return best_match

# Hybrid Recommendation Function
def hybrid_recommendation(movie_title, top_n=5):
    tfidf, cosine_sim, als_model, movie_columns = load_models()
    
    correct_movie = get_closest_match(movie_title)
    movie_idx = movies_df[movies_df["title"] == correct_movie].index[0]
    
    # Content-Based Recommendations
    content_scores = list(enumerate(cosine_sim[movie_idx]))
    content_scores = sorted(content_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    content_recommendations = [movies_df.iloc[i[0]]["title"] for i in content_scores]
    
    # Collaborative Filtering Recommendations (ALS)
    movie_id = movies_df.iloc[movie_idx]["id"]
    if movie_id in movie_columns:
        als_movie_idx = list(movie_columns).index(movie_id)
        scores = als_model.item_factors.dot(als_model.item_factors[als_movie_idx])
        colab_indices = np.argsort(scores)[::-1][1:top_n+1]
        collaborative_recommendations = [movies_df.iloc[i]["title"] for i in colab_indices]
    else:
        collaborative_recommendations = []
    
    hybrid_recommendations = list(dict.fromkeys(content_recommendations + collaborative_recommendations))[:top_n]
    
    return {
        "Corrected Movie Title": correct_movie,
        "Recommended Movies": hybrid_recommendations
    }

# Streamlit UI
st.title("Movie Recommendation System")
st.write("Enter a movie name to get recommendations.")

# User input
movie_name = st.text_input("Enter a movie name:")

# Button to get recommendations
if st.button("Get Recommendations"):
    if movie_name:
        results = hybrid_recommendation(movie_name)
        st.subheader("Recommended Movies:")
        for movie in results["Recommended Movies"]:
            st.write(f"- {movie}")
    else:
        st.warning("Please enter a valid movie name.")
