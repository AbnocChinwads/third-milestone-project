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


@app.route("/")  # Display main page with paginated list
@app.route("/game_list")
def game_list():
    return render_template("index.html",
                           game_list=mongo.db.game_list.find())

# Read Function


@app.route("/moreinfo/<game_list_id>", methods=["GET"])
def more_info(game_list_id):
    the_game = mongo.db.game_list.find_one({"_id": ObjectId(game_list_id)})
    all_categories = mongo.db.game_list.find()
    return render_template("moreinfo.html",
                           game=the_game, categories=all_categories)


"""
Add in the CRUD architecture:

* Create


@app.route("add_game") # Add a dataset using the database keys
def add_game():
    ** Create form style page for data addition **
    mongo.db.game_list.create_one({
        "game_name": value,
        "game_genre": value,
        "game_pegi_rating": value,
        "game_image": value,
    })
    return redirect("index",
                    add modal/alert with message
                    'the game has been added')


@app.route("add_review") # Add a review
def add_review():
    mongo.db.game_list.review.create_one()
    return redirect("index",
                    add modal/alert with message
                    'your review has been added')

* Read - Added
* Update


@app.route("edit_review") # Edit a review
def edit_review():
    mongo.db.game_list.review.update_one()
    return redirect("index",
                    add modal/alert with message
                    'your review has been updated')

* Delete


@app.route("/delete_game/<game_list_id>")  # Delete a full dataset
def delete_game(game_list_id):
    mongo.db.game_list.remove_one({"_id": ObjectId(game_list_id)})
    return redirect(url_for("more_info"),
                    add modal/alert with message
                    'your review has been deleted')


@app.route("/delete_review")  # Delete a review
def delete_review():
    mongo.db.game_list.review.remove_one()
    return redirect(url_for("more_info"),
                    add modal/alert with message
                    'your review has been deleted')

use less aggressive function to delete a subset of data from a
document by using the key to find the value you wish to remove...
use similar method to update document.
"""

"""
TODO:
    * Create login system, and use database to store usernames and passwords
    * Allow only the deletion of information the logged in user has posted
"""


@app.route("/login")
def login():
    return render_template("login.html")


"""
Not 100% sure this is needed, but business convention requires
a means of contact as well as means of connection on social media
"""


@app.route("/contactus")  # Contact information page poss using an email API
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")), debug=True)
