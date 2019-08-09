from flask import Blueprint
from gamenight.players.models import Player
from flask import render_template

main = Blueprint('main', __name__)

@main.route("/")
def show_players():
    players = Player.query.all()
    return render_template('home.html', players=players)
