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