import streamlit as st
import pickle
import pandas as pd
import requests

if "selected_movie_id" not in st.session_state:
    st.session_state.selected_movie_id = None

st.markdown("""
<style>
.movie-card img {
    transition: transform 0.3s ease;
    border-radius: 12px;
    cursor: pointer;
}

.movie-card img:hover {
    transform: scale(1.08);
    box-shadow: 0 10px 20px rgba(0,0,0,0.7);
}
</style>
""", unsafe_allow_html=True)

import requests


def fetch_movie_details(movie_id):
    url = ('https://api.themoviedb.org/3/movie/{}?api_key=fe6f328db97072dd87386a6b8127fc2d'.format(movie_id))

    responses = requests.get(url)
    Data = responses.json()

    # Poster
    poster_path = Data.get("poster_path")
    poster = (
        f"https://image.tmdb.org/t/p/w500{poster_path}"
        if poster_path else "https://via.placeholder.com/500x750"
    )

    # Genres (convert list → string)
    genres = ", ".join([g["name"] for g in Data.get("genres", [])])

    return {
        "title": Data.get("title"),
        "poster": poster,
        "rating": Data.get("vote_average"),
        "genres": genres,
        "overview": Data.get("overview"),
        "release_date": Data.get("release_date")
    }

def set_style():
    st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    .stButton>button {
        background-color: #E50914;
        color: white;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

set_style()


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=fe6f328db97072dd87386a6b8127fc2d'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movie_dict = pickle.load(open('Data/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

st.markdown("<h3 style='color:white;'>🎬 Find your next movie</h3>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    label="",
    options=movies['title'].values,
    placeholder="Search movies…"
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.markdown(f"""
            <div class="movie-card">
                <img src="{posters[i]}" width="100%">
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"<p style='text-align:center;color:white'>{names[i]}</p>", unsafe_allow_html=True)