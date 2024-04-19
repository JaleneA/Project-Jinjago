from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.database import db
from App.models import Game, User, UserGuess
from datetime import date

user_history_views = Blueprint('user_history_views', __name__, template_folder='../templates')

@user_history_views.route("/user_history/<user_id>", defaults={"game_id" : None}, methods=["GET"])
@user_history_views.route("/user_history/<user_id>/<game_id>", methods=["GET"])
def user_history(user_id, game_id):
    user = User.query.filter_by(id=user_id).first()
    
    if not user:
        return render_template("404.html", error=f"user with ID <{user_id}> does not exist")
    
    guesses = UserGuess.query.filter_by(user_id=user.id).all()
    game_ids = {guess.game_id for guess in guesses}
    games = Game.query.filter(Game.id.in_(game_ids)).all()
    
    user_games = [
        {
            "id" : game.id,
            "date" : game.creation_date,
            "answer" : "[REDACTED]" if date.today == game.creation_date else game.answer,
            "answer_length" : game.answer_length,
            "max_attempts" : game.max_attempts,
            "guesses" : [guess for guess in guesses if guess.game_id == game.id],
            "num_guesses" : sum(1 for guess in guesses if guess.game_id == game.id)
        }
        for game in games
    ]

    return render_template("user_history.html",
                        user=user,
                        user_games=user_games,
                        num_games = len(user_games))
