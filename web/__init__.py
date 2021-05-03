from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import logging
from logging.config import fileConfig
import os

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()
fileConfig('conf/log-app.conf')


@login_manager.user_loader
def load_user(user_id):
    return None

def get_basedir():
    return os.path.abspath(os.path.dirname(__file__))

def get_logger(name):
    return logging.getLogger(name)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    login_manager.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    from web.auth.routes import auth
    from web.main.routes import main
    from web.user.routes import user
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(user)
    with app.app_context():
        db.create_all()
        return app
