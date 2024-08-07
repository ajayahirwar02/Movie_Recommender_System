import streamlit as st
import pickle
import pandas as pd

#set page configuration
st.set_page_config(
    page_title="Movie Recommender System" 
)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))


st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'How would you like to to be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    recommendation=recommend(selected_movie_name)

    for i in recommendation:
        st.write(i)

#design footer
st.markdown(
    """
    <style>
    .footer { 
        #link{
        text-decoration: none;
        }
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 14px;d
        box-shadow: 0px -1px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    <div class="footer">
        <p> <a id ="link" href = "https://www.linkedin.com/in/ajayahirwar02/">Developed by Ajay </a></p>
    </div>
    """,
    unsafe_allow_html=True
)
