# blue prints are imported 
# explicitly instead of using *
from .auth import auth_views
from .game import game_views
from .index import index_views
from .login import login_views
from .player_history import player_history_views
from .signup import signup_views
from .user import user_views


views = [
    auth_views,
    game_views,
    index_views,
    login_views,
    player_history_views,
    signup_views,
    user_views] 
# blueprints must be added to this list