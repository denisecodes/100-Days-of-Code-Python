from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

#Login manager
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        if User.query.filter_by(email=email).first():
            flash("You've already signed up with that email, log in instead!")
        else:
            hash_and_salted_password = generate_password_hash(
                request.form.get('password'),
                method='pbkdf2:sha256',
                salt_length=8
            )
            with app.app_context():
                db.create_all()
                new_user = User(
                    email=email,
                    password=hash_and_salted_password,
                    name=request.form.get('name')
                )
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('secrets', name=new_user.name))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        if User.query.filter_by(email=email).first():
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, request.form.get('password')):
                login_user(user)
                return redirect(url_for('secrets', name=user.name))
            else:
                flash("Password incorrect, please try again!")
        else:
            flash("The email does not exist, please try again!")
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    name = request.args.get("name")
    return render_template("secrets.html", name=name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home', logged_in=current_user.is_authenticated))


@app.route('/download', methods=['GET'])
@login_required
def download():
    return send_from_directory(directory='static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
