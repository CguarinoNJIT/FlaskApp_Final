#Flask Configurations:
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

MYSQL_DATABASE_HOST = 'db'
MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_PASSWORD = 'root'
MYSQL_DATABASE_PORT = 3306
MYSQL_DATABASE_DB = 'biostatsData'
SECRET_KEY = environ.get('SECRET_KEY')