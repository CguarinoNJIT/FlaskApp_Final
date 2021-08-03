#Flask Configurations:
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

    MYSQL_DATABASE_HOST = 'db'
    TEMPLATES_FOLDER = 'templates'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'root'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_DB = 'biostatsData'
    SECRET_KEY = environ.get('SECRET_KEY')
    RECAPTCHA_PUBLIC_KEY = "iubhiukfgjbkhfvgkdfm"
    RECAPTCHA_PARAMETERS = {"size": "100%"}


    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = 'static'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')