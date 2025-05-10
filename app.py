import streamlit as st
import requests
from movielens_movie_recommendation_system import Recommender, movies

# TMDb API Key (replace 'YOUR_API_KEY' with your actual key)
TMDB_API_KEY = "ba9d41498b21993837617e5661413b5c"

def fetch_poster(movie_title):
    search_url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_title
    }
    response = requests.get(search_url, params=params)
    data = response.json()
    
    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w200{poster_path}"
    return None

# Initialize Recommender object
recommender = Recommender()

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("🎬 Movie Recommendation System")

# Movie selector
movie_titles = sorted(movies['title'].dropna().unique())
selected_movie = st.selectbox("Pick a movie you like:", movie_titles)

# Recommendation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("🎯 Recommend Based on Selected Movie"):
        recommendations = recommender.recommend_on_movie(selected_movie)
        st.subheader("Top Recommendations:")

        for i, title in enumerate(recommendations, 1):
            poster_url = fetch_poster(title)
            if poster_url:
                st.markdown(f"**{i}. {title}**")
                st.image(poster_url, width=120)
            else:
                st.write(f"{i}. {title} (No poster found)")