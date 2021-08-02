from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

mysql = MySQL(cursorclass=DictCursor)
application = Flask(__name__)

__all__ = ['init_app','mysql','application']


def init_app():
    # Initialize the Core Application
    application.config.from_object('config.Config')

    # Initialize the Plugins
    mysql.init_app(application)

    with application.app_context():
        # Routing
        from home import home_routes
        from app.form import form_routes
        from app.contact import contact_routes
        from app.errors import errors_routes
        import app.api_routes

        # Register Blueprints
        app.register_blueprint(home_routes.home_bp)
        app.register_blueprint(form_routes.form_bp)
        app.register_blueprint(contact_routes.contact_bp)
        app.register_blueprint(errors_routes.errors_bp)

        return application
