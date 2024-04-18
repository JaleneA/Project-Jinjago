from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.database import db
from App.models import UserGuess
from datetime import datetime

player_history_views = Blueprint('player_history_views', __name__, template_folder='../templates')

@player_history_views.route("/history/<user_id>/<game_id>", methods=["GET"])
def player_history(user_id, game_id):
    return render_template("player_history.html")