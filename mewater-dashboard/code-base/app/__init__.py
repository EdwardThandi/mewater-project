import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# migrate = Migrate()
db = SQLAlchemy()
# csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # * app extensions / 'services'
    db.init_app(app)
    # migrate.init_app(app, db)
    # csrf.init_app(app)

    # * Import and Register blueprints
    from app.views import index_view
    from app.routes.dashboard.views import dashboard_view
    from app.routes.report.views import report_view

    app.register_blueprint(index_view)
    app.register_blueprint(dashboard_view)
    app.register_blueprint(report_view)

    from app import models


    return app
