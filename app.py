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


def get_album_from_rating(rating_id):

    rating = mongo.db.ratings.find_one({"_id": ObjectId(rating_id)})
    album = mongo.db.albums.find_one({"_id": ObjectId(rating["album_id"])})
    artist = mongo.db.artists.find_one({"_id": ObjectId(album["artist_id"])})

    return {"album": album["album_name"], "artist": artist["artist_name"],
            "image": album["image_url"]}


def get_combined_data():
    """
    Code by the developer.
    Combines data to be displayable in other functions
    """

    album_combined = []
    albums = mongo.db.albums.find()

    index = 0

    for album in albums:
        album_combined.append({})
        album_combined[index]["album"] = {"album_name": album["album_name"],
                                          "rating": 0, "artist_name": "",
                                          "image_url": "", "number_of_ratings":
                                          0, "album_id": "", "reviews": []}
        artist = mongo.db.artists.find_one({"_id":
                                            ObjectId(album["artist_id"])})
        album_combined[index]["album"]["artist_name"] = artist["artist_name"]
        album_combined[index]["album"]["image_url"] = album["image_url"]
        album_combined[index]["album"]["album_id"] = album["_id"]

        ratings = mongo.db.ratings.find({"album_id": album["_id"]})
        count = 0
        running_total = 0
        for rating in ratings:
            score = int(rating["rating"])
            review = rating["review"]
            user = rating["created_by"]
            album_combined[index]["album"]["reviews"].append({
                "rating": score, "review": review, "user": user})
            running_total += score
            count += 1

        try:
            average = running_total/count
        except ZeroDivisionError:
            average = 0
        album_combined[index]["album"]["rating"] = average
        album_combined[index]["album"]["number_of_ratings"] = count

        if "user" in session:
            edited = mongo.db.ratings.count_documents({"album_id":
                                                      album["_id"],
                                                       "created_by":
                                                      session["user"]})
        else:
            edited = 1

        if edited > 0:
            album_combined[index]["album"]["already_edited"] = True
        else:
            album_combined[index]["album"]["already_edited"] = False

        index += 1

    return album_combined


@app.route("/")
def index():
    """
    Code by the developer.
    Used to show the top rated albums
    and most recent albums on the home page
    """
    album_combined = get_combined_data()
    latest_uploads = album_combined[-3:]

    album_combined.sort(key=lambda item: item["album"]["rating"], reverse=True)

    return render_template("index.html", artists=album_combined,
                           latest=latest_uploads)


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
            if check_password_hash(existing_user["password"],
               request.form.get("password")):
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
            print(rating["album_id"])
            album = mongo.db.albums.find_one({"_id":
                                             ObjectId(rating["album_id"])})
            album_name = album["album_name"]
            artist = mongo.db.artists.find_one({"_id":
                                                ObjectId(album["artist_id"])})
            ratings_combined.append({album_name: {}})
            ratings_combined[index][album_name]["rating"] = rating["rating"]
            ratings_combined[index][album_name]["review"] = rating["review"]
            ratings_combined[index][album_name]["artist"] = \
                artist["artist_name"]
            ratings_combined[index][album_name]["image_url"] = \
                album["image_url"]
            ratings_combined[index][album_name]["rating_id"] = \
                rating["_id"]
            index += 1

        print(ratings_combined)
        return render_template("profile.html", data=ratings_combined,
                               username=session["user"])
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
        if not request.form.get("artist_name"):
            flash("You must supply an artist name!")
            return render_template("upload.html", artists=artists)

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

        flash("Album Successfully Added!")
        return redirect(url_for("rankings"))

    return render_template("upload.html", artists=artists)


@app.route("/upload_artist", methods=["GET", "POST"])
def upload_artist():
    """
    Code by the developer.
    Checks to see if artist is uploaded
    And uploads artist if not
    """
    if request.method == "POST":
        if len(request.form.get("artist_name")) == 0:
            flash("Artist is required!")
            return redirect(url_for("upload"))

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

        # Indicated Artist has been added
        flash("Artist Successfully Added!")
        return redirect(url_for("upload"))

    return render_template("upload_artist.html")


@app.route("/edit_rating/<rating_id>", methods=["GET", "POST"])
def edit_rating(rating_id):
    """
    Code by the developer.
    Edits existing rating and updates it to send to db
    """
    rating = mongo.db.ratings.find_one({"_id": ObjectId(rating_id)})
    album_details = get_album_from_rating(rating_id)
    if request.method == "POST":
        # sends edited data to db
        submit = {
            "rating": request.form.get("rating"),
            "review": request.form.get("review"),
        }
        mongo.db.ratings.update_one({"_id": ObjectId(rating_id)},
                                    {'$set': submit})
        flash("Rating Successfully Updated")
        return redirect(url_for("profile"))
        return render_template("profile.html")

    return render_template("edit_rating.html", rating=rating,
                           album=album_details)


@app.route("/delete_rating/<rating_id>")
def delete_rating(rating_id):
    """
    Code from Code Institure.
    Deletes rating
    """
    mongo.db.ratings.delete_one({"_id": ObjectId(rating_id)})
    flash("Rating Successfully Deleted")
    return redirect(url_for("rankings"))


@app.route("/rankings", methods=["GET", "POST"])
def rankings():
    """
    Code by the developer/mentor Matt Rudge.
    Compiles information input by all users
    and puts them ranked in paginated rows
    """
    if request.method == "POST":
        # user can rate album if not previous rated
        submit = {
            "rating": request.form.get("rating"),
            "review": request.form.get("review"),
            "album_id": ObjectId(request.form.get("album_id")),
            "created_by": session["user"]
        }
        mongo.db.ratings.insert_one(submit)
        flash("Rating Successfully Added")

    album_combined = get_combined_data()
    album_combined.sort(key=lambda item: item["album"]["rating"], reverse=True)
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

    return render_template("rankings.html", is_paginated=is_paginated,
                           active_page=page_num, data=recordset,
                           num_pages=num_pages)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
