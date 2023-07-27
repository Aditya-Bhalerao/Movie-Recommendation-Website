import pandas as pd
import pickle
import requests
from decouple import config

# -------------------------------------------------------------------------------------

desc_df = pd.read_csv("static/description_db.csv")
desc_cosine_sim = pickle.load(open("static/description_cosine_sim.pkl", 'rb'))
desc_titles = desc_df['title']
desc_indices = pd.Series(desc_df.index, index=desc_df['title'])
def description_based_recommendations(title):
    idx = desc_indices[title]
    sim_scores = list(enumerate(desc_cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    id_name = desc_titles.iloc[movie_indices]
    movie_ids = []
    imdb_ids = []
    for movie_idx in id_name.index:
        movie_id = desc_df.iloc[movie_idx]['id']
        movie_ids.append(movie_id)
        imdb_id = desc_df.iloc[movie_idx]['imdb_id']
        imdb_ids.append(imdb_id)
    return movie_ids, imdb_ids

# -------------------------------------------------------------------------------------

data_df = pd.read_csv("static/data_db.csv")
data_cosine_sim = pickle.load(open("static/data_cosine_sim.pkl", 'rb'))
data_titles = data_df['title']
data_indices = pd.Series(data_df.index, index=data_df['title'])
def movie_data_based_recommendations(title):
    idx = data_indices[title]
    sim_scores = list(enumerate(data_cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    id_name = data_titles.iloc[movie_indices]
    movie_ids = []
    imdb_ids = []
    for movie_idx in id_name.index:
        movie_id = data_df.iloc[movie_idx]['id']
        movie_ids.append(movie_id)
        imdb_id = data_df.iloc[movie_idx]['imdb_id']
        imdb_ids.append(imdb_id)
    return movie_ids, imdb_ids

# -------------------------------------------------------------------------------------

API_KEY = config("API_KEY")

headers = {
    "accept": "application/json",
    "Authorization": API_KEY
}

# -------------------------------------------------------------------------------------

def get_poster_source(ids, imdb_ids):
    poster_srcs = []
    for movie in ids:
        url = f"https://api.themoviedb.org/3/movie/{movie}"
        poster_jpg = requests.get(url, headers=headers).json()['poster_path']
        poster_url = f"https://image.tmdb.org/t/p/original/{poster_jpg}"
        poster_srcs.append(poster_url)
    imdb_srcs = []
    for movie in imdb_ids:
        imdb_url = f"https://www.imdb.com/title/{movie}"
        imdb_srcs.append(imdb_url)
    return poster_srcs, imdb_srcs

# -------------------------------------------------------------------------------------