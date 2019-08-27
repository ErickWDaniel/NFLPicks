from datetime import datetime

from nflpicks import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    picks = db.relationship('Picks', backref='picker', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f'<Picker {self.username}>'

    def check_password(self, password):

        return check_password_hash(self.password_hash, password)

class Picks(db.Model):

    __tablename__ = 'picks'

    pickers = db.relationship(User)
    
    id = db.Column(db.Integer, primary_key=True)
    picker_id = db.Column(
        db.String(60), db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    round = db.Column(db.Integer, nullable=False)
    winner = db.Column(db.String(60),nullable=False)
    loser = db.Column(db.String(60), nullable=False)

    def __init__(self, picker_id, round, winner, loser):
        self.picker_id = picker_id
        self.round = round
        self.winner = winner
        self.loser = loser
        

    def __repr__(self):
        return f'Picker {self.picker}: Selected {self.winner}'



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
