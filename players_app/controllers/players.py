from flask import render_template, redirect, request
from ..models.player import Player
from players_app import app

@app.route("/")
def index():
    print("in index")
    return render_template("index.html", players=Player.get_all())

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    Player.create(request.form)
    return redirect("/")