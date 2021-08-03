from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)
mysql.init_app(app)
__all__ = ['init_app']

#Config
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'biostatsData'
app.config['SECRET_KEY'] = '79e39995d7d24c5f83f61f6c7089c2e3'
app.config["RECAPTCHA_PUBLIC_KEY"] = "iubhiukfgjbkhfvgkdfm"
app.config["RECAPTCHA_PARAMETERS"] = {"size": "100%"}

def init_app():

    #Initialize the Core Application
    app.config.from_object('config.Config')

    #Initialize the Plugins
    mysql.init_app(app)

    with app.app_context():
        #Routing
        import routes

        return app
