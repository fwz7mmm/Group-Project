from web import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    phone = db.Column(db.Integer)
    birth = db.Column(db.String(50))
    status = db.Column(db.Boolean)
    last_login = db.Column(db.DATE, nullable=False, default=datetime.now)

# Printing out which user is current
    def __repr__(self):
        return '<UserId {0}, email {1}, name {2}> last_login {3}'.format(self.id, self.email, self.name, self.last_login)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)