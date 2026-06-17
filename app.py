from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

movies = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

def recommend(movie_name):

    try:
        index = movies.index.get_loc(movie_name)

        distances = similarity[index]

        movie_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x:x[1]
        )[1:6]

        recommendations = []

        for i in movie_list:
            recommendations.append(
                movies.index[i[0]]
            )

        return recommendations

    except:
        return ["Movie Not Found"]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend_movie():

    movie = request.form['movie']

    recommendations = recommend(movie)

    return render_template(
        "index.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)