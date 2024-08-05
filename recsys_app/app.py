import streamlit as st
import pickle
import pandas

from utils import fetch_poster, recommend, improved_recommendations


st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://getwallpapers.com/wallpaper/full/4/4/c/327072.jpg");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

#st.header('Movie Recommender System Using Machine Learning')
st.markdown("<h2 style='text-align: center;'>Movie Recommender System Using Machine Learning</h2>", unsafe_allow_html=True)
# загрузка файлов
with open('recsys_app/src/movies_df.pkl', 'rb') as f:
    movies = pickle.load(f)

with open('recsys_app/src/cosine_sim.pkl', 'rb') as f:
    similarity = pickle.load(f)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie,movies,similarity)
    num_cols = 5
    num_recommendations = 10

    col_list = st.columns(num_cols)

    for i in range(num_recommendations):
        col_index = i % num_cols
        with col_list[col_index]:
            st.image(recommended_movie_posters[i])
            st.text(recommended_movie_names[i])

if st.button('Show Improved Recommendations'):
    recommendations = improved_recommendations(selected_movie,movies,similarity)
    
    if recommendations is not None:
        recommended_movie_ids = recommendations['id'].tolist()
        recommended_movie_names = recommendations['title'].tolist()
        recommended_movie_posters = []
        
        for movie_id in recommended_movie_ids:
            recommended_movie_posters.append(fetch_poster(movie_id))

        num_recommendations = len(recommended_movie_ids)
        num_cols = 5
        
        # Расчет необходимого числа строк
        num_rows = (num_recommendations + num_cols - 1) // num_cols

        for row in range(num_rows):
            col_list = st.columns(num_cols)
            start_index = row * num_cols
            end_index = min((row + 1) * num_cols, num_recommendations)
            
            for i in range(start_index, end_index):
                with col_list[i - start_index]:
                    st.image(recommended_movie_posters[i])
                    st.text(recommended_movie_names[i])
