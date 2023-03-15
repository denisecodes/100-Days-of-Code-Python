from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.FLOAT, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Books).all()
    return render_template("index.html", books=all_books)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    with app.app_context():
        book_to_delete = Books.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        with app.app_context():
            db.create_all()
            record = Books(
                title=title,
                author=author,
                rating=rating
            )
            db.session.add(record)
            db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        with app.app_context():
            book_to_update = Books.query.get(book_id)
            book_to_update.rating = request.form["rating"]
            db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    return render_template("edit.html", book=book_selected)

if __name__ == "__main__":
    app.run(debug=True)