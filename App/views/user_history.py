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
    game_ids = set()

    for i in guesses:
        if i.game_id not in game_ids:
            game_ids.add(i.game_id)

    games = Game.query.filter(Game.id.in_(game_ids)).all()
    user_games = []
    for i in games:
        curr_game = {
            "id" : i.id,
            "date" : i.creation_date,
            "answer" : "[REDACTED]" if date.today == i.creation_date else i.answer,
            "answer_length" : i.answer_length,
            "max_attempts" : i.max_attempts,
            "guesses" : [j for j in guesses if j.game_id == i.id]
        }
        curr_game["num_guesses"] = len(curr_game["guesses"])
        user_games.append(curr_game)

    return render_template("user_history.html",
                        user=user,
                        user_games=user_games,
                        num_games = len(user_games))
