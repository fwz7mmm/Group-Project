from flask import Flask,render_template, url_for,Blueprint
from web import get_logger,bcrypt,db
logger = get_logger(__name__)
main = Blueprint('main', __name__)
from flask_login import login_required
@main.route('/')
def index():
    return render_template('index.html')

@main.route("/home")
def home():
    return render_template("home.html")

@main.route("/test")
@login_required
def test():
    return render_template("test.html")

