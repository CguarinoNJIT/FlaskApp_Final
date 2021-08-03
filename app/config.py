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

#We could add other classes in this file so that we could have different configuration enviroments depending on what we are trying to do. Not nessesary for this project.
#EX:
# class ProdConfig(Config):
#     FLASK_ENV = 'production'
#     DEBUG = False
#     TESTING = False
#     DATABASE_URI = environ.get('PROD_DATABASE_URI')
#
#
# class DevConfig(Config):
#     FLASK_ENV = 'development'
#     DEBUG = True
#     TESTING = True
#     DATABASE_URI = environ.get('DEV_DATABASE_URI')