import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =========================
# Configuración de la App
# =========================
st.set_page_config(page_title="🎬 Recomendador de Películas", page_icon="🎥", layout="wide")
st.title("🎬 **Sistema de Recomendación de Películas**")
st.markdown("Explora películas similares según sus géneros usando el dataset **MovieLens**.")

# =========================
# Cargar dataset MovieLens
# =========================
@st.cache_data
def load_movies():
    return pd.read_csv("ml-latest-small/movies.csv")

movies = load_movies()

# =========================
# Sidebar
# =========================
st.sidebar.header("⚙️ Configuración")
num_recommendations = st.sidebar.slider("Cantidad de recomendaciones", 3, 10, 5)

# Obtener lista de géneros
all_genres = sorted(set(g for sublist in movies['genres'].str.split('|') for g in sublist))
selected_genre = st.sidebar.selectbox("Filtrar por género (opcional):", ["Todos"] + all_genres)

# =========================
# Modelo TF-IDF
# =========================
@st.cache_data
def build_similarity_matrix(movies):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

cosine_sim = build_similarity_matrix(movies)

# =========================
# Función de recomendación
# =========================
def get_recommendations(title, cosine_sim=cosine_sim, top_n=num_recommendations):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    recs = movies.iloc[movie_indices]
    if selected_genre != "Todos":
        recs = recs[recs['genres'].str.contains(selected_genre)]
    return recs

# =========================
# Interfaz Streamlit
# =========================
with st.container():
    st.subheader("🎥 Selecciona una película:")
    movie_list = movies['title'].values
    selected_movie = st.selectbox("", movie_list, index=0)

if st.button("🎯 Recomendar"):
    recommendations = get_recommendations(selected_movie)
    st.subheader(f"🔎 **Películas recomendadas:** (Top {num_recommendations})")

    if recommendations.empty:
        st.warning(f"No se encontraron películas en el género '{selected_genre}' para esta selección.")
    else:
        cols = st.columns(2)
        for idx, (_, row) in enumerate(recommendations.iterrows()):
            with cols[idx % 2]:
                st.markdown(
                    f"""
                    <div style="padding: 10px; border-radius: 10px; border: 1px solid #ccc; margin: 5px; background-color: #f9f9f9;">
                        <h4 style="margin:0;">🎬 {row['title']}</h4>
                        <p style="margin:0; color: gray;">Géneros: {row['genres']}</p>
                    </div>
                    """, unsafe_allow_html=True
                )
