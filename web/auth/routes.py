from flask import Flask,render_template, url_for,Blueprint
from web import get_logger,bcrypt,db
logger = get_logger(__name__)
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/register')
def register():
    return render_template('register.html')

