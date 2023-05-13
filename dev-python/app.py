# -*- coding: utf-8 -*-
from main.model.role import Role
from main.model.user import User
from flask import Flask
from flask_cors import CORS
import logging
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

config = app_config[app_active]


def create_app():
    config = app_config[app_active]
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #db = SQLAlchemy(config.APP)
   # migrate = Migrate(app, db)

   # db.init_app(app)

    # @app.shell_context_processor
    # def make_shell_context():
    #     return dict(db=db, User=User, Role=Role)
    CORS(app)

   

    @app.route("/")
    def index():
        logging.info('This is an info message')
        return "Flask inside Docker!!"

    return app
