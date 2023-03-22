from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    with app.app_context():
        cafes = db.session.query(Cafe).all()
        random_cafe = random.choice(cafes)
    # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    with app.app_context():
        cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def find_a_cafe():
    location = request.args.get('loc')
    with app.app_context():
        cafes = db.session.query(Cafe).all()
        all_cafes = []
        for cafe in cafes:
            if cafe.location == location:
                all_cafes.append(cafe.to_dict())
        if not all_cafes:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})
        else:
            return jsonify(cafe=all_cafes)



## HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_a_cafe():
    with app.app_context():
        new_cafe = Cafe(
             name=request.form.get("name"),
             map_url=request.form.get("map_url"),
             img_url=request.form.get("img_url"),
             location=request.form.get("loc"),
             has_sockets=bool(request.form.get("sockets")),
             has_toilet=bool(request.form.get("toilet")),
             has_wifi=bool(request.form.get("wifi")),
             can_take_calls=bool(request.form.get("calls")),
             seats=request.form.get("seats"),
             coffee_price=request.form.get("coffee_price"),
         )
        db.session.add(new_cafe)
        db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_coffee_price(cafe_id):
    with app.app_context():
        cafe_to_update = Cafe.query.get(cafe_id)
        try:
            cafe_to_update.coffee_price = request.args.get('new_price')
        except:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
        else:
            db.session.commit()
            return jsonify(success="Successfully updated the price.")


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key != "TopSecretyAPIKey":
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key.")
    else:
        with app.app_context():
            cafe_to_delete = Cafe.query.get(cafe_id)
            try:
                db.session.delete(cafe_to_delete)
            except:
                return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
            else:
                db.session.commit()
                return jsonify(success="Successfully deleted the cafe.")


if __name__ == '__main__':
    app.run(debug=True)
