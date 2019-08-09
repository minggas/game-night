from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import UserMixin
from config import Config
from gamenight.shared.models import db



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from gamenight.main.routes import main
    from gamenight.players.routes import players
    from gamenight.games.routes import games
    app.register_blueprint(main)
    app.register_blueprint(players)
    app.register_blueprint(games)
    with app.test_request_context():
        db.create_all()
   
    return app