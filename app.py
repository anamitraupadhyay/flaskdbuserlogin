from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import bcrypt

db=SQLAlchemy()

#creates the app and returns it into an object
def create_app():
    app=Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./testdb.db'
    #the . signifies current directory i.e db will be created in current directory

    db.init_app(app) #initializes app

    #not importing yet we don't have stuff written out yet
    with app.app_context():
        from models import Person  # Import models to register them with SQLAlchemy
        db.create_all()  # This will create the tables if they don't exist

    #importing the routes like /index so on and in these routes we are going to import models(circular import would happen)
    #now after routes.py we import in the function
    from routes import register_routes
    register_routes(app,db)

    migrate= Migrate(app,db) #converts classes into db tables(orm)
    return app
#now summarizing the overview:
#routes import models, models import db from app and app import routes, if routes import not done in this function it will cause issues, now creating base template html