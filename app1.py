import os
import pickle
import gdown
import streamlit as st
import pandas as pd

# Download similarity.pkl automatically
if not os.path.exists("similarity.pkl"):
    gdown.download(
        "PASTE_YOUR_GOOGLE_DRIVE_DIRECT_LINK",
        "similarity.pkl",
        quiet=False
    )

# Download movies_dict.pkl automatically
if not os.path.exists("movies_dict.pkl"):
    gdown.download(
        "PASTE_YOUR_GOOGLE_DRIVE_DIRECT_LINK",
        "movies_dict.pkl",
        quiet=False
    )

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):
    recommended_movies = recommend(selected_movie_name)

    for i in recommended_movies:
        st.write(i)