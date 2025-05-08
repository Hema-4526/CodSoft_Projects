import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Movie data
data = {
    'title': ['The Matrix', 'John Wick', 'Titanic', 'Avengers: Endgame'],
    'description': [
        'A hacker discovers reality is fake and fights for freedom.',
        'An assassin seeks revenge for his dog.',
        'A love story set on a doomed ship.',
        'Superheroes unite to save the universe.'
    ]
}

df = pd.DataFrame(data)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def recommend(title):
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:3]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Streamlit UI
st.title("🎬 Movie Recommendation System")

movie_list = df['title'].values
selected_movie = st.selectbox("Choose a movie you like:", movie_list)

if st.button("Recommend"):
    results = recommend(selected_movie)
    st.write("You might also like:")
    for m in results:
        st.write("✅", m)
