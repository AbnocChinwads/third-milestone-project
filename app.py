import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "third_milestone_project"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

# Tasks


@app.route("/")  # Display main page with paginated list
@app.route("/game_list")
def game_list():
    return render_template("index.html",
                           game_list=mongo.db.game_list.find())


@app.route("/moreinfo/<game_list_id>")
def more_info(game_list_id):
    the_game = mongo.db.game_list.find_one({"_id": ObjectId(game_list_id)})
    all_categories = mongo.db.categories.find()
    return render_template("moreinfo.html",
                           game=the_game, categories=all_categories)


"""
Add in the CRUD architecture, and settle on what data to use for the database.
It has to be sensible, you can't keep jumping around like this between
ridiculous ideas. Pick some information that lends itself to being
created, read, updated, and deleted... not some high fancy idea
of reworking the Monster Manual or getting some kind of open source
writing project off the ground.


@app.route("create_data")
def create_data():
    mongo.db.create_one()
    return redirect("index",
                    add modal/alert with message 'your data has been added')

Use objectId to find the data they are looking for.
Maybe use a search element in the header for this.

@app.route("/get_data")
def get_data():
    request.form.get()
    return redirect("index")


@app.route("/delete_review/<review_id>")  # Delete a review from the database
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    return redirect(url_for("get_reviews"),
                    add modal/alert 'the entry has been deleted')

use less aggressive function to delete a subset of data from a
document by using the key to find the value you wish to remove...
use similar method to update document.
"""
# Create login system, and use database to store usernames and passwords


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/contactus")  # Contact information page poss using an email API
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")), debug=True)
