from flask_login import UserMixin
from mainapp.__init__ import db,app
from flask_login import LoginManager

log_man = LoginManager(app)
log_man.init_app(app)


@log_man.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    
    __tablename__='User'
     
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)