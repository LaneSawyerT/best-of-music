import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_artist")
def get_artist():
    artists_combined = {}
    artists = mongo.db.artists.find()
    for artist in artists:
        artists_combined[artist["artist_name"]] = [] 
        albums = mongo.db.albums.find({"artist_id": artist["_id"]})
        for album in albums:
            artists_combined[artist["artist_name"]].append(album["album_name"])

    print(artists_combined)
    return render_template("upload.html", artists=artists_combined)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        
        if existing_email:
            flash("Email already used")
            return redirect(url_for("register"))

        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)