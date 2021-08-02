from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

__all__ = ['init_app','db_fun','get_flask_app']

def db_fun():
    db_var = MySQL(cursorclass=DictCursor)
    return db_var

def get_flask_app():
    application = Flask(__name__)
    return application

def init_app(application: Flask=get_flask_app(), db_var: MySQL=db_fun()):
    # Initialize the Core Application
    application.config.from_object('config.Config')

    # Initialize the Plugins
    db_var.init_app(application)

    with application.app_context():
        # Routing
        from home import home_routes
        from form import form_routes
        from contact import contact_routes
        from errors import errors_routes
        import api_routes

        # Register Blueprints
        application.register_blueprint(home_routes.home_bp)
        application.register_blueprint(form_routes.form_bp)
        application.register_blueprint(contact_routes.contact_bp)
        application.register_blueprint(errors_routes.errors_bp)
        application.register_blueprint(api_routes.api_bp)

        return application
