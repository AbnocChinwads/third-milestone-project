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
                           game_list=mongo.db.game_list.find())


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
# and displays relevant reviews
@app.route("/more-info/<game_list_id>")
def more_info(game_list_id):
    the_game = mongo.db.game_list.find_one({"_id": ObjectId(game_list_id)})
    all_categories = mongo.db.game_list.find()
    reviews = mongo.db.reviews.find({"game_id": ObjectId(game_list_id)})
    result = list(reviews)
    return render_template("moreinfo.html", game=the_game,
                           categories=all_categories, review=result)


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


# Delete a chosen game and it's reviews
@app.route("/delete-game/<game_list_id>")
def delete_game(game_list_id):
    mongo.db.game_list.delete_one({"_id": ObjectId(game_list_id)})
    mongo.db.reviews.delete_many({"game_id": ObjectId(game_list_id)})
    return redirect(url_for("game_list"))

# Reviews


# Display form to add review
@app.route("/add-review/<game_list_id>")
def add_review(game_list_id):
    the_game = mongo.db.game_list.find_one({"_id": ObjectId(game_list_id)})
    return render_template("addreview.html", game=the_game)


# Add the review
@app.route("/insert-review", methods=["POST"])
def insert_review():
    form_game_id = request.form.get("game_id")
    game_id = ObjectId(form_game_id)
    reviews = mongo.db.reviews
    reviews.insert_one({
        "game_id": game_id,
        "review": request.form.get("review")
    })
    return redirect(url_for("game_list"))


# Edit the current review
@app.route("/edit-review/<game_list_id>/<review_id>")
def edit_review(game_list_id, review_id):
    the_game = mongo.db.game_list.find_one({"_id": ObjectId(game_list_id)})
    the_review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("editreview.html", game=the_game,
                           reviews=the_review)


# Update the review
@app.route("/update-review/<review_id>", methods=["POST"])
def update_review(review_id):
    form_game_id = request.form.get("game_id")
    game_id = ObjectId(form_game_id)
    reviews = mongo.db.reviews
    reviews.update({"_id": ObjectId(review_id)},
                   {
        "game_id": game_id,
        "review": request.form.get("review")
    })
    return redirect(url_for("game_list"))


# Delete a chosen review
@app.route("/delete-review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    return redirect(url_for("game_list"))


"""
Add in the CRUD architecture:

* Create: Reviews - Added (Works, have to return to the main page)
* Read: Done
* Update: Reviews - Added (Works, have to return to the main page)
* Delete: Reviews - Added (Works, have to return to the main page)

TODO:

https://www.codementor.io/@arpitbhayani/fast-and-efficient-pagination-in-mongodb-9095flbqr

def idlimit(page_size, last_id=None):
    page_size = 2
    # Function returns `page_size` number of documents after last_id
    and the new last_id. #

    if last_id is None:
        # When it is first page
        cursor = mongo.db['game_list'].find().limit(page_size)
    else:
        cursor = mongo.db['game_list'].find(
                {'_id': {'$gt': last_id}}).limit(page_size)

    # Get the data
    data = [x for x in cursor]

    if not data:
        # No documents left
        return None, None

    # Since documents are naturally ordered with _id, last document will
    # have max id.
    last_id = data[-1]['_id']

    # Return data and last_id
    return data, last_id

TODO:
    * Create a function to delete a single key:value pair from a
    * dataset by selecting the value you wish to remove
"""

"""
TODO:
    * Create login system, and use database to store emails,
    * usernames and passwords
    * Allow only the deletion of reviews the logged in user has posted
"""
# Login system

"""
@app.route("/<username>")
def login():
    return render_template("index.html")
"""


@app.route("/contactus")  # Contact information page poss using an email API
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")), debug=True)
