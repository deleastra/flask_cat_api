from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

db = SQLAlchemy()


def create_app():
    app = APIFlask(__name__)

    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    migrate = Migrate(app, db)

    # importing the models to make sure they are known to Flask-Migrate
    from .cat import CatModel

    # any other registrations; blueprints, template utilities, commands

    return app