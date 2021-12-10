from flask import render_template, redirect, request
from ..models.player import Player
from players_app import app

# localhost:5000/
@app.route("/")
def index():
    print("in index")

    return render_template("index.html", players = Player.get_all_players())

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():

    print("creating a player")
    # TODO: actually create a player

    return redirect("/")