import streamlit as st
import pickle
import pandas as pd


def recommend(movie_title, cosine_sim, movie_list):
    idx = movie_list[movie_list['title_x'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]

    return movie_list['title_x'].iloc[movie_indices]


movie_list = pickle.load(open('movies_dict.pkl', 'rb'))
movie_list = pd.DataFrame(movie_list)

sim_matrix = pickle.load(open('similarity.pkl', 'rb'))


st.title('Choose your preferred method of connection')

# Corrected selectbox
selected_movie = st.selectbox(
    'How would you like to be connected?',
    movie_list['title_x'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie, sim_matrix, movie_list)
    for i in recommendations:
        st.write(i)
