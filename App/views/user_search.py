from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.database import db
from App.models import Game, User, UserGuess
from datetime import datetime

player_history_views = Blueprint('player_history_views', __name__, template_folder='../templates')

@player_history_views.route("/player_history/<user_id>", defaults={"game_id" : None}, methods=["GET"])
@player_history_views.route("/player_history/<user_id>/<game_id>", methods=["GET"])
def player_history(user_id, game_id):
    player = User.query.filter_by(id=user_id).first()
    
    if not player:
        return render_template("404.html", error=f"Player with ID <{user_id}> does not exist")
    
    game = Game.query.filter_by(id=user_id).first()

    player_games = None
    player_guesses = None
    
    player_games = UserGuess.query.filter_by(user_id=player.id).first()

    # Cannot select a game without first selecting a player
    if game:
        player_guesses = UserGuess.query.filter_by(user_id=player.id, game_id=game.id).first()

    return render_template("player_history.html",
                        player=player,
                        player_games=player_games,
                        player_guesses=player_guesses)
        

@player_history_views.route("/player_history_search/", methods=["GET"])
def player_history_search_action():
    pass