import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)