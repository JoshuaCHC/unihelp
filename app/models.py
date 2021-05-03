from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    marks = db.relationship('Marks', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)   

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        print(password, check_password_hash(self.password_hash,password))
        return check_password_hash(self.password_hash, password)


class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mod1 = db.Column(db.Float)
    mod2 = db.Column(db.Float)
    mod3 = db.Column(db.Float)
    avgMark = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<User {} got marks: 1: {} 2: {} 3: {}>'.format(self.user_id, mod1,mod2,mod3)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))