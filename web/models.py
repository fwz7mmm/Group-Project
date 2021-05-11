from web import db ,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True,nullable=False)
    email = db.Column(db.String(128), unique=True,nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.Integer)
    birth = db.Column(db.String(128))
    status = db.Column(db.Boolean)
    user_type = db.Column(db.Integer)

# Printing out which user is current
    def __repr__(self):
        return '<UserId {0}, email {1}, name {2}> last_login {3}'.format(self.id, self.email, self.name, self.last_login)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Quiztype(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(64))
    topic = db.Column(db.String(64))

class Questions(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(256))
    choiceA = db.Column(db.String(128))
    choiceB = db.Column(db.String(128))
    choiceC = db.Column(db.String(128))
    choiceD = db.Column(db.String(128))
    answer = db.Column(db.String(128))
    quiztype_id = db.Column(db.Integer, db.ForeignKey('quiztype.id'), nullable=False)
    quiztype = db.relationship("Quiztype")

class Quizdata(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiztype_id = db.Column(db.Integer, db.ForeignKey('quiztype.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(128), nullable=False)
    user = db.relationship("User")
    quiztype = db.relationship("Quiztype")

