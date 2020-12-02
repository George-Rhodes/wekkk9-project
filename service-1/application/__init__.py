from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)


app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY_DB'))
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:george_rhodes@db:3306/project"

from application import routes