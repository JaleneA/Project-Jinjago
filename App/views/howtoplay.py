from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

howtoplay_views = Blueprint('howtoplay_views', __name__, template_folder='../templates')

'''
Page Routes
'''   
@howtoplay_views.route('/howtoplay', methods=['GET'])
def howtoplay_page():
    return render_template('howtoplay.html')
    