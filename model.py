import pandas as pd
import pickle

from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

data = movies.merge(ratings,on='movieId')

movie_matrix = data.pivot_table(
    index='title',
    columns='userId',
    values='rating'
)

movie_matrix.fillna(0,inplace=True)

similarity = cosine_similarity(movie_matrix)

pickle.dump(
    movie_matrix,
    open('movies.pkl','wb')
)

pickle.dump(
    similarity,
    open('similarity.pkl','wb')
)

print("Model Saved Successfully")