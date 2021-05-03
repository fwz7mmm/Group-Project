from flask import Flask,render_template, url_for,Blueprint,request,redirect
from web import get_logger,bcrypt,db
from web.models import Questions,Quiztype

logger = get_logger(__name__)
main = Blueprint('main', __name__)
from flask_login import login_required
@main.route('/')
def index():
    return render_template('index.html')

@main.route("/home")
def home():
    return render_template("home.html")

@main.route("/content")
def content():
    return render_template("content.html")  

@main.route('/test', methods=['GET', 'POST'])
#@login_required
def test():
    if request.method == "POST":
        topic = request.form.get('topic')
        level = request.form.get('level')
        return redirect(url_for('main.quiz', topic=topic, level=level))

    return render_template("test.html")

@main.route('/quiz/<topic>,<level>', methods=['GET', 'POST'])
#@login_required
def quiz(topic, level):
    quiztype = Quiztype.query.filter_by(topic=topic,level=level).first()
    quizs  =Questions.query.filter_by(quiztype_id=quiztype.id).all()
    return render_template("quiz.html", quizs=quizs)