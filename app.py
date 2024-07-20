import streamlit as st
import pickle
import pandas as pd


def recommend(movie_title):
    # Find the index of the movie
    if movie_title not in movies_list:
        return []
    movie_index = movies_list.index(movie_title)

    # Get the list of distances and sort them
    distances = similarity[movie_index]
    list_of_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for movie in list_of_movies:
        movie_id = movie[0]
        # fetch poster from API

        recommended_movies.append(movies_list[movie_id])
    return recommended_movies


# Load the data
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].tolist()

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
