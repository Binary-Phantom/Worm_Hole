from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhocario.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'minhocario.db')
app.config['SECRET_KEY'] ='abcd'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from minhocario.admin import routes