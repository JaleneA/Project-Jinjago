from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.database import db
from App.models import Game, User, UserGuess
from datetime import datetime

user_history_views = Blueprint('user_history_views', __name__, template_folder='../templates')

@user_history_views.route("/user_history/<user_id>", defaults={"game_id" : None}, methods=["GET"])
@user_history_views.route("/user_history/<user_id>/<game_id>", methods=["GET"])
def user_history(user_id, game_id):
    user = User.query.filter_by(id=user_id).first()
    
    if not user:
        return render_template("404.html", error=f"user with ID <{user_id}> does not exist")
    
    game = Game.query.filter_by(id=user_id).first()

    user_games = None
    user_guesses = None
    
    user_games = UserGuess.query.filter_by(user_id=user.id).first()

    # Cannot select a game without first selecting a user
    if game:
        user_guesses = UserGuess.query.filter_by(user_id=user.id, game_id=game.id).first()

    return render_template("user_history.html",
                        user=user,
                        user_games=user_games,
                        user_guesses=user_guesses)
