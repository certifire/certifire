from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

import certifire.config as config

__author__ = "Githin Manesh <githinmanesh@gmail.com>"
__version__ = (1, 0, 0)
__licence__ = "Apache License V2.0"


def get_version():
    return ".".join(map(str, __version__))


def get_author():
    return __author__.split(" <")[0]


def get_author_email():
    return __author__.split(" <")[1][:-1]

app = Flask(__name__)

app.config['SECRET_KEY'] = config.CERTIFIRE_TOKEN_SECRET
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
auth = HTTPBasicAuth()
