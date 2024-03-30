# import boto3
import logging
from flask import Flask
from flask_migrate import Migrate
# from flask_login import LoginManager
# from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
# from flask.logging import default_handler
# from logging.handlers import RotatingFileHandler
# from app.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


migrate = Migrate()
db = SQLAlchemy()
# csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # * app extensions / 'services'
    db.init_app(app)
    migrate.init_app(app, db)
    # csrf.init_app(app)

    # * Flask-login
    # login_manager = LoginManager()
    # login_manager.login_view = 'ums_view.login'
    # login_manager.init_app(app)

    # * logging
    # app.logger.removeHandler(default_handler)
    # # Create a file handler object
    # size_in_kb = 20 * 1024
    # file_handler = RotatingFileHandler(
    #     'app/logs/logs.log', maxBytes=size_in_kb, backupCount=40)
    # # Set the logging level of the file handler object
    # file_handler.setLevel(logging.INFO)
    # # Create a file formatter object
    # file_formatter = logging.Formatter(
    #     '%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')
    # # Apply the file formatter object to the file handler object
    # file_handler.setFormatter(file_formatter)
    # # Add file handler object to the logger
    # app.logger.addHandler(file_handler)

    # * Import and Register blueprints
    from app.views import index_view
    from app.routes.dashboard.views import dashboard_view
    from app.routes.report.views import report_view

    app.register_blueprint(index_view)
    app.register_blueprint(dashboard_view)
    app.register_blueprint(report_view)

    from app import models

    # # ? user-loader -> Flask-login specific
    # from app.models import User

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))

    return app
