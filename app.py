import streamlit as st
import pickle
import pandas as pd
import requests

def getId(movie):
    movie_id = []
    
    for m in movie.values:
        movie_id_df = movie_list[movie_list['title_x'] == m]
        movie_id.append(movie_id_df['movie_id'].values[0])
    
    return movie_id

def getPoster(moviesIDs):
    api_key = "e79a40a1d81b18fd7fdec0f69c5704a7"
    base_url ='https://image.tmdb.org/t/p/w500'
    posters = []
    for id in moviesIDs:
        url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}"
        response = requests.get(url)
        data = response.json()
        posters.append(base_url + data['poster_path'])
    return posters

def recommend(movie_title, cosine_sim, movie_list):
    # Initialize idx for the selected movie
    idx = None
    for index, row in movie_list.iterrows():
        title = row['title_x']
        if title.lower() == movie_title.lower():  # Comparing without case sensitivity
            idx = index
            break  # We found the movie, exit the loop

    if idx is None:
        return []  # If the movie was not found, return an empty list

    simScore = []
    for index, cos_sim in enumerate(cosine_sim[idx]):
        simScore.append((index, cos_sim))
    
    # Sorting the similarity scores in descending order
    sorted_list = sorted(simScore, key=lambda x: x[1], reverse=True)
    sorted_list = [i[0] for i in sorted_list]
    
    # Selecting the top 5 most similar movies (excluding the movie itself)
    movie_indices = sorted_list[1:6]
    moviesIDs = getId(movie_list['title_x'].iloc[movie_indices])
    movie_posters = getPoster(moviesIDs)
    
    return movie_posters

# Load movie data and similarity matrix
movie_list = pickle.load(open('movies_dict.pkl', 'rb'))
movie_list = pd.DataFrame(movie_list)

sim_matrix = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie = st.selectbox(
    'Select a movie:',
    movie_list['title_x'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie, sim_matrix, movie_list)
    
    if recommendations:
        cols = st.columns(5)  # Adjust this number if you want more/less posters per row
        for i, poster in enumerate(recommendations):
            if i < len(cols):  # Make sure there are enough columns to display the images
                cols[i].image(poster)
    else:
        st.write("No recommendations found.")
