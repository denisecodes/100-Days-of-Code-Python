from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy import asc
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(app)


@app.route("/")
def home():
    all_movies = Movies.query.order_by(asc(Movies.rating)).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
        with app.app_context():
            db.session.commit()
    return render_template("index.html", movies=all_movies)


class ReviewForm(FlaskForm):
    rating = StringField('Your Rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.FLOAT)
    ranking = db.Column(db.Integer, unique=True)
    review = db.Column(db.String(250), unique=True)
    img_url = db.Column(db.String(250))

    def __repr__(self):
        return f'<Movie {self.title}>'


with app.app_context():
    db.create_all()

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = ReviewForm()
    movie_id = request.args.get("id")
    if form.validate_on_submit():
        with app.app_context():
            movie = Movies.query.get(movie_id)
            movie.rating = float(form.rating.data)
            movie.review = form.review.data
            db.session.commit()
        return redirect(url_for('home'))
    movie = Movies.query.get(movie_id)
    return render_template("edit.html", movie=movie, form=form)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    with app.app_context():
        movie_to_delete = Movies.query.get(movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        tmdb_url = "https://api.themoviedb.org/3/search/movie"
        api_key = os.environ.get("API_KEY")
        params = {
            "api_key": api_key,
            "query": movie_title
        }
        response = requests.get(url=tmdb_url, params=params)
        movie_data = response.json()['results']
        print(movie_data)
        return render_template("select.html", options=movie_data)
    return render_template("add.html", form=form)

@app.route("/find_movie")
def find_movie():
    movie_id = request.args.get("id")
    if movie_id:
        api_key = os.environ.get("API_KEY")
        tmdb_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            "api_key": api_key
        }
        response = requests.get(url=tmdb_url, params=params)
        data = response.json()
        title = data['title']
        img_url = f"https://image.tmdb.org/t/p/original{data['poster_path']}"
        year = data['release_date'].split("-")[0]
        description = data['overview']
        with app.app_context():
            db.create_all()
            movie = Movies(
                title=title,
                year=year,
                description=description,
                img_url=img_url
            )
            db.session.add(movie)
            db.session.commit()
            return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)