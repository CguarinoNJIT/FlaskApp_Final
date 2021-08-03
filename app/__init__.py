from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask_sqlalchemy import SQLAlchemy


mysql = MySQL(cursorclass = DictCursor)
app = Flask(__name__)
db = SQLAlchemy()
__all__ = ['init_app']

def init_app():

    #Initialize the Core Application
    app.config.from_object('config.Config')

    #Initialize the Plugins
    mysql.init_app(app)
    db.init_app(app)

    with app.app_context():
        #Routing
        import routes

        return app
