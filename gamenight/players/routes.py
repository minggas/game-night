from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template
from gamenight.games.models import Game
from gamenight.players.models import Player
from gamenight.shared.models import db

players = Blueprint('players', __name__)

@players.route('/games/<int:player_id>')
def show_games_from_player(player_id):
    games = Game.query.filter_by(player_id = player_id).all()
    player = Player.query.filter_by(id = player_id).first()
    total = len(games) 
    print(total)   
    return render_template('games.html', games=games, player=player, total = total)

@players.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')        
        player = Player(id=10, name=name, email=email, password=password)
        db.session.add(player)
        db.session.commit()
        return redirect(url_for('main.show_players'))
    return render_template('account.html')