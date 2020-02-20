from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt




app = Flask(__name__)
app.config['SECRET_KEY'] = 'ad66d90a56b675248acb31307cca3cc8017fc2ac'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///E:/webapp/test.db"
app.config['SQLAlCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
from mainapp import routes
from mainapp import catrout



