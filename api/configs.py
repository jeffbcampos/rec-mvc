import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = os.getenv("LINK_PG")
JWT_SECRET_KEY = os.getenv("JWT_KEY")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=5)
MAIL_SERVER = 'smtp.office365.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.getenv("MAIL")
MAIL_PASSWORD = os.getenv("PWD_MAIL")
