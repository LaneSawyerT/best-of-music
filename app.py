from bson import ObjectId
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
def get_artist():
    artists_combined = {}
    artists = mongo.db.artists.find()
    for artist in artists:
        artists_combined[artist["artist_name"]] = [] 
        albums = mongo.db.albums.find({"artist_id": artist["_id"]})
        for album in albums:
            artists_combined[artist["artist_name"]].append(album["album_name"])

    print(artists_combined)
    return render_template("index.html", artists=artists_combined)


@app.route("/get_album")
def get_album():
    album_combined = {}
    album = mongo.db.albums.find()
    for album in albums:
        album_combined[album["album_name"]] = []
        albums = mongo.db.albums.find({"rating_id": rating["_id"]}, {"review_id": review["_id"]})
        for album in albums:
            artists_combined[album["rating"]].append(album["rating"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Code by the developer.
    Registers the user and send data to db
    """
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
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Code by the developer.
    Log the user in and send checks information inserted to db
    """

    if request.method == "POST":
        # Checks to see if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Makes sure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Password do not match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile")
def profile():
    """
    Code by the developer.
    Grabs the username from db and displays their uploaded info
    """
    if session["user"]:
        index = 0
        ratings_combined = []
        ratings = mongo.db.ratings.find({"created_by": session["user"]})
        for rating in ratings:
            album = mongo.db.albums.find_one({"_id": ObjectId(rating["album_id"])})
            album_name = album["album_name"]
            artist = mongo.db.artists.find_one({"_id": ObjectId(album["artist_id"])})
            ratings_combined.append({album_name: {}})
            ratings_combined[index][album_name]["rating"] = rating["rating"]
            ratings_combined[index][album_name]["review"] = rating["review"]
            ratings_combined[index][album_name]["artist"] = artist["artist_name"]
            ratings_combined[index][album_name]["image_url"] = album["image_url"]
            ratings_combined[index][album_name]["rating_id"] = rating["_id"]
            index += 1

        print(ratings_combined)
        return render_template("profile.html", data=ratings_combined, username=session["user"])
    else:
        
        return render_template("index.html")


@app.route("/logout")
def logout():
    """
    Code by the developer.
    Removes user from session
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/upload", methods=["GET", "POST"])
def upload():
    """
    Code by the developer.
    Uploads an album and sends data to db
    """

    artists = mongo.db.artists.find().sort("artist_name", 1)
    if request.method == "POST":
        album = {
            "album_name": request.form.get("album_name"),
            "artist_id": request.form.get("artist_name"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.albums.insert_one(album)

        albums = mongo.db.albums.find_one(album)

        rating = {
            "rating": request.form.get("rating"),
            "album_id": albums["_id"],
            "review": request.form.get("review"),
            "created_by": session["user"]
        }
        mongo.db.ratings.insert_one(rating)

    return render_template("upload.html", artists=artists)


@app.route("/upload_artist", methods=["GET", "POST"])
def upload_artist():
    if request.method == "POST":
        # Checks to see if artist name exists in db
        existing_artist = mongo.db.artists.find_one(
            {"artist_name": request.form.get("artist_name")})

        if existing_artist:
            flash("Artist is already uploaded")
            return redirect(url_for("upload"))

        artist = {
            "artist_name": request.form.get("artist_name")
            }
        mongo.db.artists.insert_one(artist)

        # Put the new user into upload page
        flash("Artist Successfully added!")
        return redirect(url_for("upload_artist"))

    return render_template("upload_artist.html")


@app.route("/edit_rating/<rating_id>", methods=["GET", "POST"])
def edit_rating(rating_id):
    rating = mongo.db.ratings.find_one({"_id": ObjectId(rating_id)})
    if request.method == "POST":
        submit = {
            "rating": request.form.get("rating"),
            "review": request.form.get("review"),
        }
        mongo.db.ratings.update_one({"_id": ObjectId(rating_id)}, {'$set': submit})
        flash("Rating Successfully Updated")
        return render_template("profile.html")

    return render_template("edit_rating.html", rating=rating)


@app.route("/rankings")
def rankings():
    """
    Code by the developer.
    Compiles information input by all users and puts them ranked
    """
    album_combined = []
    albums = mongo.db.albums.find()

    index = 0

    for album in albums:
        album_combined.append({})
        album_combined[index][album["album_name"]] = {"rating": 0, "artist_name": "", "image_url": "", "number_of_ratings": 0, "album_id": ""}
        artist = mongo.db.artists.find_one({"_id": ObjectId(album["artist_id"])})
        album_combined[index][album["album_name"]]["artist_name"] = artist["artist_name"]
        album_combined[index][album["album_name"]]["image_url"] = album["image_url"]
        album_combined[index][album["album_name"]]["album_id"] = album["_id"]

        ratings = mongo.db.ratings.find({"album_id": album["_id"]})
        count = 0
        running_total = 0

        for rating in ratings:
            running_total += int(rating["rating"]) 
            count +=1

        average = running_total/count
        album_combined[index][album["album_name"]]["rating"] = average
        album_combined[index][album["album_name"]]["number_of_ratings"] = count
        index += 1


    page_num = int(request.args["page"]) if "page" in request.args else 1

    num_per_page = 6

    is_paginated = True if len(album_combined) > num_per_page else False

    if len(album_combined) % num_per_page == 0:
        num_pages = int(len(album_combined) / num_per_page)
    else:
        num_pages = int((len(album_combined) / num_per_page) + 1)

    if page_num > num_pages:
        page_num = 1

    start = (num_per_page * page_num) - num_per_page
    end = (num_per_page * page_num)

    recordset = album_combined[start:end]

    return render_template("rankings.html", is_paginated=is_paginated, active_page=page_num, data=recordset, num_pages=num_pages)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)