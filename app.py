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
@app.route("/game-list")
def game_list():
    return render_template("index.html",
                           game_list=mongo.db.game_list.find())

# Create


@app.route("/add-game")  # Display form page to add game
def add_game():
    return render_template("addgame.html")


# Add a new dataset using the database keys
@app.route("/insert-game", methods=["POST"])
def insert_game():
    games = mongo.db.game_list
    games.insert_one(request.form.to_dict())
    return redirect(url_for("game_list"))

# Read


@app.route("/more-info/<game_list_id>")
def more_info(game_list_id):
    the_game = mongo.db.game_list.find_one({"_id": ObjectId(game_list_id)})
    all_categories = mongo.db.game_list.find()
    return render_template("moreinfo.html",
                           game=the_game, categories=all_categories)

# Update


# Edit a game on the database
@app.route("/edit-game-information/<game_list_id>")
def update_game(game_list_id):
    the_game = mongo.db.game_list.find_one({"_id": ObjectId(game_list_id)})
    return render_template("editgame.html", game=the_game)


@app.route("/update-game/<game_list_id>", methods=["POST"])
def update_task(game_list_id):
    games = mongo.db.game_list
    games.update({"_id": ObjectId(game_list_id)},
                 {
                    "game_name": request.form.get("game_name"),
                    "game_genre": request.form.get("game_genre"),
                    "game_pegi_rating": request.form.get("game_pegi_rating"),
                    "game_image": request.form.get("game_image"),
                    "fair_use": request.form.get("fair_use")
                 })
    return redirect(url_for("game_list"))


"""
Add in the CRUD architecture:

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
    return redirect(url_for("more_info"),
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
