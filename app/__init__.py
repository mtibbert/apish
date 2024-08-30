from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from config import Config
from app.extensions import db, api as api_ex

from app.routes.home.home_bp import home_bp
from app.routes.language.language_bp import language_bp


# Prefix for api routes
url_prefix = "/api/v1"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Create the API
    api_ext = Api(app, prefix=url_prefix)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.database.models import language

    # Register blueprints here
    app.register_blueprint(home_bp)                              # /

    # Set API Endpoints
    app.register_blueprint(language_bp, url_prefix=url_prefix)   # /language

    return app
