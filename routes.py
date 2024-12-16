from flask import render_template, request
from flask_login import login_user, logout_user, current_user, login_required

from models import User

#a function to avoid circular imports
def register_routes(app, db, bcrypt):
    @app.route('/', methods=['POST','GET'])
    def index():
        if current_user.is_authenticated:
            return str(current_user.username)
        else:
            return 'no user is logged in'
    @app.route('/login/<uid>')
    def login(uid):
        user= User.query.get(uid)
        login_user(user)
        return 'success'
    @app.route('/loginout/<uid>')
    def logout(uid):
        logout_user(uid)
        return 'success'