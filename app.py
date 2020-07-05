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

# Games


@app.route("/")  # Display main page with paginated list
@app.route("/game-list")
def game_list():
    return render_template("index.html",
                           game_list=mongo.db.game_list.find().limit(5))


@app.route("/add-game")  # Display form page to add game
def add_game():
    return render_template("addgame.html")


# Add a new game
@app.route("/insert-game", methods=["POST"])
def insert_game():
    games = mongo.db.game_list
    games.insert_one(request.form.to_dict())
    return redirect(url_for("game_list"))


# Display more information on the selected game
@app.route("/more-info/<game_list_id>")
def more_info(game_list_id):  # gameID
    the_game = mongo.db.game_list.find_one({"_id": ObjectId(game_list_id)})
    all_categories = mongo.db.game_list.find()
    # reviews = mongo.db.reviews.find({"_id": ObjectId(gameID)})
    return render_template("moreinfo.html", game=the_game,
                           categories=all_categories)  # review=reviews


# Display form page to edit game
@app.route("/edit-game-information/<game_list_id>")
def edit_game(game_list_id):
    the_game = mongo.db.game_list.find_one({"_id": ObjectId(game_list_id)})
    return render_template("editgame.html", game=the_game)


# Edit the chosen game
@app.route("/update-game/<game_list_id>", methods=["POST"])
def update_game(game_list_id):
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


@app.route("/delete-game/<game_list_id>")  # Delete a chosen game
def delete_game(game_list_id, reviews_gameID):
    mongo.db.game_list.remove_one({"_id": ObjectId(game_list_id)})
    mongo.db.reviews.remove({"_id": ObjectId(reviews_gameID)})
    return redirect(url_for("game_list"))

# Reviews


# Add a review
@app.route("/add-review/<game_list_id>")
def add_review(game_list_id):
    the_game = mongo.db.game_list.find_one({"_id": ObjectId(game_list_id)})
    all_categories = mongo.db.game_list.find()
    review = mongo.db.reviews.find()
    return render_template("addreview.html", reviews=review,
                           game=the_game, categories=all_categories)


# Add a new game
@app.route("/insert-review", methods=["POST"])
def insert_review():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for("game_list"))


@app.route("/edit-review/<review_id>")  # Update the current review
def edit_review(review_id):
    the_review = mongo.db.review.find_one({"_id": ObjectId(review_id)})
    return render_template("editreview.html", review=the_review)


@app.route("/update-review/<review_id>", methods=["GET", "POST"])
def update_review(review_id):
    reviews = mongo.db.reviews
    reviews.update({"_id": ObjectId(review_id)},
                   {
        "review": request.form.get("review")
    })
    return redirect(url_for("more_info"))


"""
Add in the CRUD architecture:

* Create: Games - Added
          Reviews - Added (Returns 405 error)
* Read: Games - Added
        Reviews - Added
* Update: Games - Added
          Reviews - Added (Returns 405 error)
* Delete: Games - Added (Needs connecting to webpage)
          Reviews - Needs implementing


@app.route("/delete_review")  # Delete a review
def delete_review():
    mongo.db.review.remove_one()
    return redirect(url_for("more_info"))

TODO:
    Create a function to delete a single key: value pair from a
    dataset by selecting the value you wish to remove
"""

"""
TODO:
    * Create login system, and use database to store usernames and passwords
    * Allow only the deletion of information the logged in user has posted
"""
# Login system


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/contactus")  # Contact information page poss using an email API
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")), debug=True)
