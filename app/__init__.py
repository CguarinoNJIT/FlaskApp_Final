from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


mysql = MySQL(cursorclass = DictCursor)
app = Flask(__name__)

__all__ = ['init_app']

def init_app():

    #Initialize the Core Application
    app.config.from_object('config.Config')

    #Initialize the Plugins
    mysql.init_app(app)

    with app.app_context():
        #Routing
        from app.home import home_routes
        from app.form import form_routes
        from app.contact import contact_routes
        from app.errors import errors_routes
        import app.api_routes

        #Register Blueprints
        app.register_blueprint(home_routes.home_bp)
        app.register_blueprint(form_routes.form_bp)
        app.register_blueprint(contact_routes.contact_bp)
        app.register_blueprint(errors_routes.errors_bp)

        return app
