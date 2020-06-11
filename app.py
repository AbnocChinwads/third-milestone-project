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

mongo = PyMongo(app)

# Tasks


@app.route("/")  # Display main page with paginated list
@app.route("/get_creatures")
def get_creatures():
    return render_template("index.html",
                           creatures=mongo.db.creatures.find())


"""
Display more in depth information on creatures such as:
stats, vulnerabilities, skills, actions etc.
"""


@app.route("/<creature_id>")
def more_info(creature_id):
    creature = mongo.db.creatures
    creature.find({"_id": ObjectId(creature_id)},
                  {
        "creature_name": request.form.get("creature_name"),
        "challenge_rating": request.form.get("challenge_rating"),
        "creautre_type": request.form.get("creature_type"),
        "creature_size": request.form.get("creature_size"),
        "creature_ac": request.form.get("creature_ac"),
        "creautre_hp": request.form.get("creature_hp"),
        "creature_speed": request.form.get("creature_speed"),
        "creature_alignment": request.form.get("creature_alignment"),
        "legendary": request.form.get("legendary")
    })
    return render_template("moreinfo.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contactus")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")), debug=True)
