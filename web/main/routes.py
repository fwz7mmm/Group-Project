from flask import Flask,render_template, url_for,Blueprint
from web import get_logger,bcrypt,db
from flask_sqlalchemy import SQLAlchemy
logger = get_logger(__name__)
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route("/home")
def home():
    return render_template("home.html")
    
    
