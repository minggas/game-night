from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from gamenight.games.models import Game
from gamenight.players.models import Player
from gamenight.shared.models import db


games = Blueprint('games', __name__)


@games.route("/game/new_game", methods=['GET', 'POST'])
def new_game():
    if request.method == 'POST':
        player = Player.query.filter_by(id = 1).first()
        title = request.form.get('title')
        description = request.form.get('description')
        max_players = request.form.get('max_players')
        time = request.form.get('time')
        game = Game(id=10, title=title, description=description, time=time, max_players=max_players, owner=player)
        db.session.add(game)
        db.session.commit()
    return render_template('create_game.html')